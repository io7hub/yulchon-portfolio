"""
냉간인발 파이프 공정 공장운영 교육 시스템
Factory Operation Training System

Author: Claude
Version: 1.0
Date: 2024-12-29
"""

import streamlit as st
import os
import yaml
import json
import pandas as pd
from datetime import datetime
from pathlib import Path
import base64
from typing import List, Dict, Any
import plotly.graph_objects as go
import plotly.express as px

# LangChain imports
LANGCHAIN_AVAILABLE = False
LANGCHAIN_ERROR = None

try:
    from langchain_anthropic import ChatAnthropic
    from langchain_openai import ChatOpenAI
    
    # LangChain 버전에 따라 import 경로가 다름
    try:
        # v0.1.0+ (권장)
        from langchain_classic.memory import ConversationBufferMemory
        from langchain_classic.chains import LLMChain
        from langchain_core.prompts import PromptTemplate
        from langchain_core.output_parsers import StrOutputParser
    except ImportError:
        # Legacy import (v0.0.x)
        from langchain_classic.memory import ConversationBufferMemory
        from langchain_classic.chains import ConversationChain
        from langchain_classic.prompts import PromptTemplate
    
    LANGCHAIN_AVAILABLE = True
except ImportError as e:
    LANGCHAIN_ERROR = str(e)
    # 경고는 사이드바에서만 표시

# ============================================================================
# 페이지 설정
# ============================================================================

st.set_page_config(
    page_title="냉간인발 파이프 공정 공장운영 교육 시스템",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CSS 스타일
# ============================================================================

st.markdown("""
<style>
    /* 전역 폰트 설정 - Noto Sans KR */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap');
    
    * {
        font-family: 'Noto Sans KR', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    }
    
    /* 메인 컨테이너 */
    .main {
        padding: 2rem;
    }
    
    /* 헤더 스타일 */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2.5rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    .header-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .header-subtitle {
        font-size: 1.1rem;
        font-weight: 400;
        margin-top: 0.5rem;
        opacity: 0.95;
    }
    
    /* AI 답변 영역 스타일 개선 */
    .assistant-message {
        background: linear-gradient(to right, #f8f9fa 0%, #ffffff 100%);
        border-left: 5px solid #9c27b0;
        padding: 1.8rem;
        margin: 1.2rem 0;
        border-radius: 12px;
        line-height: 1.9;
        box-shadow: 0 4px 12px rgba(156, 39, 176, 0.1);
    }
    
    /* AI 답변 제목 체계 */
    .assistant-message h1 {
        color: #6a1b9a;
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #e1bee7;
    }
    
    .assistant-message h2 {
        color: #7b1fa2;
        font-size: 1.5rem;
        font-weight: 600;
        margin-top: 1.8rem;
        margin-bottom: 0.9rem;
        padding-bottom: 0.4rem;
        border-bottom: 2px solid #e1bee7;
    }
    
    .assistant-message h3 {
        color: #8e24aa;
        font-size: 1.3rem;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
    }
    
    .assistant-message h4 {
        color: #9c27b0;
        font-size: 1.1rem;
        font-weight: 500;
        margin-top: 1.2rem;
        margin-bottom: 0.6rem;
    }
    
    /* 단락 간격 */
    .assistant-message p {
        margin: 0.9rem 0;
        line-height: 1.9;
        color: #333;
    }
    
    /* 리스트 스타일 개선 */
    .assistant-message ul,
    .assistant-message ol {
        margin: 1rem 0;
        padding-left: 2rem;
    }
    
    .assistant-message li {
        margin: 0.6rem 0;
        line-height: 1.8;
    }
    
    /* 코드 블록 */
    .assistant-message pre {
        background: #2d2d2d;
        color: #f8f8f2;
        padding: 1.2rem;
        border-radius: 8px;
        margin: 1.2rem 0;
        overflow-x: auto;
        font-family: 'Consolas', 'Monaco', monospace !important;
        line-height: 1.6;
    }
    
    .assistant-message code {
        background: #f0f0f0;
        color: #d63384;
        padding: 0.2rem 0.5rem;
        border-radius: 4px;
        font-family: 'Consolas', 'Monaco', monospace !important;
        font-size: 0.9em;
    }
    
    .assistant-message pre code {
        background: transparent;
        color: #f8f8f2;
        padding: 0;
    }
    
    /* 표 스타일 */
    .assistant-message table {
        border-collapse: collapse;
        width: 100%;
        margin: 1.2rem 0;
        background: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .assistant-message th {
        background: linear-gradient(135deg, #9c27b0 0%, #7b1fa2 100%);
        color: white;
        padding: 0.9rem;
        font-weight: 600;
        text-align: left;
    }
    
    .assistant-message td {
        border: 1px solid #e0e0e0;
        padding: 0.8rem;
        color: #333;
    }
    
    .assistant-message tr:nth-child(even) {
        background: #f9f9f9;
    }
    
    .assistant-message tr:hover {
        background: #f5f5f5;
    }
    
    /* 인용문 */
    .assistant-message blockquote {
        border-left: 5px solid #9c27b0;
        padding-left: 1.2rem;
        margin: 1.2rem 0;
        color: #555;
        font-style: italic;
        background: #f9f9f9;
        padding: 1rem 1.2rem;
        border-radius: 0 8px 8px 0;
    }
    
    /* 구분선 */
    .assistant-message hr {
        border: none;
        border-top: 2px solid #e0e0e0;
        margin: 2rem 0;
    }
    
    /* 강조 */
    .assistant-message strong {
        color: #6a1b9a;
        font-weight: 600;
    }
    
    .assistant-message em {
        color: #7b1fa2;
    }
    
    /* 사용자 메시지 */
    .user-message {
        background: linear-gradient(to right, #e3f2fd 0%, #ffffff 100%);
        border-left: 5px solid #2196f3;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 12px;
        box-shadow: 0 3px 10px rgba(33, 150, 243, 0.1);
    }
    
    /* 카드 스타일 */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #667eea;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #666;
        margin-top: 0.5rem;
    }
    
    /* 채팅 메시지 */
    .chat-message {
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .user-message {
        background: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    
    .user-message strong {
        color: #1565c0;
    }
    
    .user-message .message-content {
        color: #263238;
        margin-top: 0.5rem;
        line-height: 1.6;
    }
    
    .assistant-message {
        background: #f3e5f5;
        border-left: 4px solid #9c27b0;
    }
    
    .assistant-message strong {
        color: #6a1b9a;
    }
    
    .assistant-message .message-content {
        color: #263238;
        margin-top: 0.5rem;
        line-height: 1.6;
        white-space: pre-wrap;
    }
    
    /* 버튼 스타일 */
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: 500;
    }
    
    /* 경고 박스 */
    .warning-box {
        background: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        color: #856404;
    }
    
    .warning-box strong {
        color: #856404;
    }
    
    .success-box {
        background: #d4edda;
        border-left: 4px solid #28a745;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        color: #155724;
    }
    
    .success-box strong {
        color: #155724;
    }
    
    .info-box {
        background: #d1ecf1;
        border-left: 4px solid #17a2b8;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        color: #0c5460;
    }
    
    .info-box strong {
        color: #0c5460;
    }
    
    /* 테이블 스타일 */
    .dataframe {
        font-size: 0.9rem;
    }
    
    /* 파일 업로더 */
    .uploadedFile {
        border: 2px dashed #667eea;
        border-radius: 10px;
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# 세션 상태 초기화
# ============================================================================

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'ontology_data' not in st.session_state:
    st.session_state.ontology_data = {}

if 'api_configured' not in st.session_state:
    st.session_state.api_configured = False

if 'current_model' not in st.session_state:
    st.session_state.current_model = None

if 'memory' not in st.session_state and LANGCHAIN_AVAILABLE:
    st.session_state.memory = ConversationBufferMemory(
        return_messages=True,
        memory_key="history"
    )

if 'uploaded_files_data' not in st.session_state:
    st.session_state.uploaded_files_data = []

# ============================================================================
# 유틸리티 함수
# ============================================================================

def load_env_file(env_file_path: str) -> Dict[str, str]:
    """
    .env 파일에서 API 키를 로드합니다.
    """
    env_vars = {}
    try:
        with open(env_file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    env_vars[key.strip()] = value.strip().strip('"').strip("'")
        return env_vars
    except Exception as e:
        st.error(f"❌ .env 파일 로드 실패: {str(e)}")
        return {}

def save_env_file(env_vars: Dict[str, str], env_file_path: str = ".env"):
    """
    API 키를 .env 파일로 저장합니다.
    """
    try:
        with open(env_file_path, 'w') as f:
            for key, value in env_vars.items():
                f.write(f"{key}={value}\n")
        return True
    except Exception as e:
        st.error(f"❌ .env 파일 저장 실패: {str(e)}")
        return False

def parse_ontology_file(file_content: bytes, file_name: str) -> Dict[str, Any]:
    """
    다양한 형식의 온톨로지 파일을 파싱합니다.
    지원 형식: YAML, JSON, CSV, TXT
    """
    file_extension = Path(file_name).suffix.lower()
    
    try:
        if file_extension in ['.yaml', '.yml']:
            return yaml.safe_load(file_content.decode('utf-8'))
        
        elif file_extension == '.json':
            return json.loads(file_content.decode('utf-8'))
        
        elif file_extension == '.csv':
            import io
            df = pd.read_csv(io.BytesIO(file_content))
            return df.to_dict(orient='records')
        
        elif file_extension == '.txt':
            text_content = file_content.decode('utf-8')
            # 간단한 key:value 파싱
            data = {}
            for line in text_content.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    data[key.strip()] = value.strip()
            return data
        
        else:
            st.warning(f"⚠️ 지원하지 않는 파일 형식: {file_extension}")
            return {"raw_content": file_content.decode('utf-8', errors='ignore')}
    
    except Exception as e:
        st.error(f"❌ 파일 파싱 실패 ({file_name}): {str(e)}")
        return {}

# ============================================================================
# RAG (Retrieval-Augmented Generation) Functions
# ============================================================================

def extract_keywords(text: str) -> List[str]:
    """텍스트에서 기술 키워드 추출"""
    keywords = []
    
    tech_terms = {
        'heat_treatment': ['열처리', '정규화', 'normalizing', '풀림', 'annealing'],
        'pickling': ['산세', 'pickling', '산'],
        'cold_drawing': ['냉간인발', 'cold drawing', '인발'],
        'inspection': ['검사', 'ECT', 'UT', '와전류', '초음파'],
        'quality': ['Cpk', 'SPC', 'AQL', '품질'],
        'material': ['탄소', 'carbon', 'ferrite', 'austenite'],
        'mechanical': ['경도', 'hardness', '인장', 'tensile'],
        'standard': ['KS', 'ASTM', 'DIN', 'ISO']
    }
    
    text_lower = text.lower()
    for category, terms in tech_terms.items():
        for term in terms:
            if term.lower() in text_lower:
                keywords.append(term)
    
    return list(set(keywords))


def search_dict_recursive(data: Dict, keywords: List[str], path: str = "") -> List[Dict]:
    """딕셔너리 재귀 검색"""
    matches = []
    
    if not isinstance(data, dict):
        return matches
    
    for key, value in data.items():
        current_path = f"{path}/{key}" if path else key
        key_str = str(key).lower()
        value_str = str(value).lower() if not isinstance(value, (dict, list)) else ""
        
        if any(kw.lower() in key_str or kw.lower() in value_str for kw in keywords):
            if not isinstance(value, (dict, list)):
                matches.append({
                    'path': current_path,
                    'value': str(value)[:200]
                })
        
        if isinstance(value, dict):
            matches.extend(search_dict_recursive(value, keywords, current_path))
    
    return matches


def create_ontology_context(user_question: str, ontology_data: Dict) -> str:
    """온톨로지 기반 컨텍스트 생성"""
    if not ontology_data:
        return ""
    
    keywords = extract_keywords(user_question)
    if not keywords:
        return ""
    
    all_matches = []
    for filename, data in ontology_data.items():
        if isinstance(data, dict):
            matches = search_dict_recursive(data, keywords)
            for match in matches:
                match['file'] = filename
            all_matches.extend(matches)
    
    if not all_matches:
        return ""
    
    context = "\n### 📚 온톨로지 관련 데이터\n\n"
    for match in all_matches[:8]:
        context += f"**{match['file']}** > `{match['path']}`: {match['value']}\n"
    
    return context


# ============================================================================
# AI 모델 초기화 및 관리
# ============================================================================

def initialize_llm(api_key: str, model_type: str, model_name: str = None):
    """
    LangChain LLM을 초기화합니다.
    
    Args:
        api_key: API 키
        model_type: 모델 타입 ("Claude (Anthropic)" 또는 "GPT-4o-mini (OpenAI)")
        model_name: 사용할 모델명 (Claude의 경우 필수)
    """
    if not LANGCHAIN_AVAILABLE:
        return None
    
    try:
        if model_type == "Claude (Anthropic)":
            # 모델명이 지정되지 않은 경우 가장 호환성 높은 버전 사용
            if not model_name:
                model_name = "claude-3-opus-20240229"
            
            llm = ChatAnthropic(
                anthropic_api_key=api_key,
                model_name=model_name,
                temperature=0.7,
                max_tokens=4096
            )
            
        elif model_type == "GPT-4o-mini (OpenAI)":
            llm = ChatOpenAI(
                openai_api_key=api_key,
                model_name="gpt-4o-mini",
                temperature=0.7,
                max_tokens=4096
            )
        else:
            st.error("❌ 지원하지 않는 모델 타입입니다.")
            return None
        
        return llm
    
    except Exception as e:
        st.error(f"❌ LLM 초기화 실패: {str(e)}")
        
        # 모델명 오류인 경우 추가 안내
        if "not_found_error" in str(e) or "404" in str(e):
            st.warning("""
            **모델을 찾을 수 없습니다.**
            
            가능한 원인:
            1. API 키에 해당 모델 접근 권한이 없음
            2. 모델이 아직 활성화되지 않음
            3. 계정에서 모델을 사용할 수 없음
            
            **해결 방법:**
            - 다른 모델 버전 선택 (예: claude-3-5-sonnet-20240620)
            - Anthropic Console에서 API 키 권한 확인
            - 새 API 키 발급
            
            **사용 가능한 Claude 모델:**
            - `claude-3-5-sonnet-20240620` (권장, 안정)
            - `claude-3-opus-20240229` (가장 강력)
            - `claude-3-sonnet-20240229` (균형)
            - `claude-3-haiku-20240307` (빠름)
            """)
        
        return None

def create_conversation_chain(llm, memory):
    """
    대화형 체인을 생성합니다.
    """
    template = """당신은 냉간인발 강관 제조 공정의 전문 AI 어시스턴트입니다.

**전문 분야:**
1. 냉간인발 이음매 없는 강관 제조공정 (Cold Drawn Seamless Steel Pipe Manufacturing)
2. IATF 16949, ISO 9001/14001 품질경영시스템
3. 비파괴검사 (NDT: ECT, UT)
4. 생산계획통제 (PPC)
5. 통계적 공정관리 (SPC, Cpk≥1.33)

**제조 공정 10단계:**
1. 입고검사 → 2. 열처리 → 3. 산세 → 4. 선단가공 → 5. 냉간인발 → 6. 교정 → 7. 절단 → 8. 검사(ECT/UT) → 9. 방청유 → 10. 출하검사

**보유 지식:**
- 설비: Heat Treatment Furnace, Pickling Line, Pointing & Swaging M/C, Draw Bench, Straightener, Cutting Machine, Anti-rust Oil Tank
- Fe-C 상태도: 탄소 0.15-0.25% 아공석강, A₃ 변태점 850-930°C, 정규화 880-920°C (A₃+30-50°C)
- 검사 기준: ISO 2859 (AQL), SPC 관리도, Cpk≥1.33, 전수검사 100%
- 소재 규격: KS D 3507/3562/3564, ASTM A53/A106/A179/A192/A210, DIN 2391/2393, EN 10305, JIS G3441/G3445
- 용접 규격: ASME Section IX, AWS D1.1, ISO 9606, KS B 0845
- 기계적 특성: 인장강도 370-470 MPa, 항복강도 ≥205 MPa, 연신율 ≥25%, 경도 120-180 HB
- 추적성: 15년 기록 보관, LOT 추적, 2D Barcode/QR Code
- 조직: Ferrite 85-90% + Pearlite 10-15%

**현재 시스템에 업로드된 온톨로지 데이터:**
{ontology_summary}

**주요 역할:**
1. 냉간인발 공정의 각 단계별 기술 지원 및 상세 설명
2. NDT 검사(ECT/UT) 절차 및 판정 기준 안내
3. 공정 최적화 및 품질 개선 방안 제시
4. Fe-C 상태도 기반 과학적 열처리 조건 설정
5. IATF 16949/ISO 요구사항 준수 확인
6. 온톨로지 데이터를 활용한 정확한 답변 제공

**답변 작성 규칙 (매우 중요):**

### 1. 구조화된 답변
- 답변은 명확한 구조로 작성하세요
- 제목은 3단계까지만 사용 (### 주제, #### 세부주제, 항목)
- 단락은 빈 줄로 명확히 구분하세요
- 한 단락은 3-5문장 이내로 작성하세요

### 2. 리스트 사용 규칙
- 3개 이상 항목만 리스트로 작성하세요
- 번호 리스트: 순서가 중요한 경우
- 글머리 리스트: 순서가 중요하지 않은 경우
- 들여쓰기는 일관성 있게 유지하세요
- 과도한 리스트 중첩을 피하세요

### 3. 표 사용
- 비교 데이터는 표로 작성하세요
- 헤더를 명확히 작성하세요
- 정렬을 일관성 있게 유지하세요

### 4. 코드 및 수식
- 공식은 백틱(`)으로 감싸세요
- 여러 줄 코드는 ```로 감싸세요
- 들여쓰기 4칸을 사용하세요

### 5. 강조 사용
- **중요**: 굵게 표시
- *참고*: 이탤릭 표시
- 과도한 강조는 피하세요

### 6. 구체적 데이터 제공
- 공정명: 정확한 영문명 사용
- 규격 번호: KS, ASTM, DIN, ISO, JIS 명시
- 수치: 단위와 함께 정확히 제공
- 온도: ±편차 포함
- 통계: Cpk, AQL 기준 명시

### 7. 답변 예시 구조
```
### 주제

#### 1. 개요
간단한 설명 (2-3문장)

#### 2. 세부 내용
**항목 1**: 설명
**항목 2**: 설명

#### 3. 구체적 기준
| 항목 | 기준 | 비고 |
|------|------|------|
| 값1 | 값2 | 값3 |

#### 4. 참고사항
- 중요 포인트 1
- 중요 포인트 2
```

이전 대화:
{history}

현재 질문: {input}

답변 (위의 규칙을 엄격히 준수하여 작성):"""

    try:
        # Modern LangChain (v0.1.0+)
        from langchain_core.prompts import PromptTemplate
        from langchain_core.runnables import RunnablePassthrough
        from langchain_core.output_parsers import StrOutputParser
        
        prompt = PromptTemplate(
            input_variables=["history", "input", "ontology_summary"],
            template=template
        )
        
        # Create chain using LCEL (LangChain Expression Language)
        chain = (
            {
                "history": lambda x: memory.load_memory_variables({})["history"],
                "input": RunnablePassthrough(),
                "ontology_summary": lambda x: x.get("ontology_summary", "")
            }
            | prompt
            | llm
            | StrOutputParser()
        )
        
        return chain
        
    except ImportError:
        # Legacy LangChain (v0.0.x)
        from langchain_classic.chains import ConversationChain
        from langchain_classic.prompts import PromptTemplate
        
        prompt = PromptTemplate(
            input_variables=["history", "input", "ontology_summary"],
            template=template
        )
        
        chain = ConversationChain(
            llm=llm,
            memory=memory,
            prompt=prompt,
            verbose=False
        )
        
        return chain

def generate_chat_history_html(chat_history: List[Dict]) -> str:
    """
    대화 이력을 HTML로 변환합니다.
    """
    if not chat_history:
        return ""
    
    entries = []
    for msg in chat_history:
        role_class = "user" if msg['role'] == 'user' else "assistant"
        role_text = "👤 사용자" if msg['role'] == 'user' else "🤖 AI 어시스턴트"
        timestamp = msg.get('timestamp', '')[:19].replace('T', ' ')
        content = msg['content'].replace('<', '&lt;').replace('>', '&gt;')  # HTML escape
        
        entry = f"""
                <div class="chat-entry">
                    <div class="chat-role {role_class}">
                        {role_text}
                        <span class="timestamp">{timestamp}</span>
                    </div>
                    <div class="chat-content">{content}</div>
                </div>"""
        entries.append(entry)
    
    chat_html = f"""
        <div class="section">
            <h2 class="section-title">💬 AI 대화 이력</h2>
            <div class="chat-history">
                <p class="chat-info">총 {len(chat_history)}개의 대화가 기록되었습니다.</p>
                {''.join(entries)}
            </div>
        </div>"""
    
    return chat_html


def generate_html_report(data: Dict[str, Any], chat_history: List[Dict] = None) -> str:
    """
    인사이트 보고서를 HTML 인포그래픽으로 생성합니다.
    
    Args:
        data: 보고서 데이터
        chat_history: AI 대화 이력 (옵션)
    """
    
    # Plotly 차트 생성
    figures = []
    
    # 1. 공정별 불량률 차트
    if 'process_defect_rate' in data:
        fig1 = go.Figure(data=[
            go.Bar(
                x=list(data['process_defect_rate'].keys()),
                y=list(data['process_defect_rate'].values()),
                marker_color='rgb(102, 126, 234)'
            )
        ])
        fig1.update_layout(
            title="공정별 불량률",
            xaxis_title="공정",
            yaxis_title="불량률 (%)",
            template="plotly_white"
        )
        figures.append(fig1.to_html(include_plotlyjs='cdn', div_id="chart1"))
    
    # 2. 온톨로지 구조 트리맵
    if 'ontology_structure' in data:
        df = pd.DataFrame(data['ontology_structure'])
        fig2 = px.treemap(
            df,
            path=['category', 'subcategory'],
            values='count',
            title="온톨로지 구조"
        )
        figures.append(fig2.to_html(include_plotlyjs='cdn', div_id="chart2"))
    
    # 3. KPI 게이지 차트
    if 'kpi_values' in data:
        fig3 = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=data['kpi_values'].get('current', 0),
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "수율 (%)"},
            delta={'reference': data['kpi_values'].get('target', 100)},
            gauge={
                'axis': {'range': [None, 100]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 80], 'color': "gray"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': data['kpi_values'].get('target', 100)
                }
            }
        ))
        figures.append(fig3.to_html(include_plotlyjs='cdn', div_id="chart3"))
    
    # HTML 템플릿
    html_template = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>냉간인발 파이프 공정 인사이트 보고서</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Noto Sans KR', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            padding: 3rem;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 3rem;
            padding-bottom: 2rem;
            border-bottom: 3px solid #667eea;
        }}
        
        .header h1 {{
            font-size: 2.5rem;
            color: #333;
            margin-bottom: 1rem;
        }}
        
        .header .subtitle {{
            font-size: 1.2rem;
            color: #666;
        }}
        
        .header .date {{
            font-size: 1rem;
            color: #999;
            margin-top: 0.5rem;
        }}
        
        .section {{
            margin: 2rem 0;
        }}
        
        .section-title {{
            font-size: 1.8rem;
            color: #667eea;
            margin-bottom: 1rem;
            padding-left: 1rem;
            border-left: 5px solid #667eea;
        }}
        
        .metrics {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }}
        
        .metric-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 15px;
            color: white;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}
        
        .metric-value {{
            font-size: 3rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }}
        
        .metric-label {{
            font-size: 1rem;
            opacity: 0.9;
        }}
        
        .chart-container {{
            margin: 2rem 0;
            background: #f8f9fa;
            padding: 2rem;
            border-radius: 15px;
        }}
        
        .insights {{
            background: #e3f2fd;
            padding: 2rem;
            border-radius: 15px;
            border-left: 5px solid #2196f3;
            margin: 2rem 0;
        }}
        
        .insights h3 {{
            color: #1976d2;
            margin-bottom: 1rem;
        }}
        
        .insights ul {{
            list-style-position: inside;
            line-height: 1.8;
        }}
        
        .footer {{
            text-align: center;
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 2px solid #e0e0e0;
            color: #999;
        }}
        
        .compliance-notice {{
            background: #fff9e6;
            border: 1px solid #ffeb3b;
            padding: 0.5rem;
            border-radius: 5px;
            margin-top: 1rem;
            font-size: 0.9rem;
            color: #856404;
        }}
        
        .chat-history {{
            background: #f8f9fa;
            padding: 2rem;
            border-radius: 15px;
            margin: 2rem 0;
        }}
        
        .chat-info {{
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 1.5rem;
            padding: 0.75rem;
            background: white;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }}
        
        .chat-entry {{
            background: white;
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }}
        
        .chat-role {{
            font-weight: bold;
            margin-bottom: 0.75rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #f0f0f0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .chat-role.user {{
            color: #2196f3;
        }}
        
        .chat-role.assistant {{
            color: #9c27b0;
        }}
        
        .timestamp {{
            font-size: 0.85rem;
            font-weight: normal;
            color: #999;
        }}
        
        .chat-content {{
            line-height: 1.8;
            color: #333;
            white-space: pre-wrap;
            word-wrap: break-word;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏭 냉간인발 파이프 공정 인사이트 보고서</h1>
            <div class="subtitle">Factory Operation Analytics Report</div>
            <div class="date">생성일: {datetime.now().strftime('%Y년 %m월 %d일 %H:%M')}</div>
        </div>
        
        <div class="section">
            <h2 class="section-title">📊 핵심 지표</h2>
            <div class="metrics">
                <div class="metric-card">
                    <div class="metric-value">{data.get('fpv', 'N/A')}%</div>
                    <div class="metric-label">직행률 (FPY)</div>
                </div>
                <div class="metric-card">
                    <div class="metric-value">{data.get('otd', 'N/A')}%</div>
                    <div class="metric-label">정시납기율 (OTD)</div>
                </div>
                <div class="metric-card">
                    <div class="metric-value">{data.get('wip_days', 'N/A')}일</div>
                    <div class="metric-label">WIP 재고일수</div>
                </div>
                <div class="metric-card">
                    <div class="metric-value">{data.get('defect_rate', 'N/A')}%</div>
                    <div class="metric-label">전체 불량률</div>
                </div>
            </div>
        </div>
        
        <div class="section">
            <h2 class="section-title">📈 데이터 시각화</h2>
            {''.join(figures)}
        </div>
        
        <div class="section">
            <h2 class="section-title">💡 주요 인사이트</h2>
            <div class="insights">
                <h3>발견된 개선 기회</h3>
                <ul>
                    {''.join([f'<li>{insight}</li>' for insight in data.get('insights', ['데이터 분석 중...'])])}
                </ul>
            </div>
        </div>
        
        <div class="section">
            <h2 class="section-title">🎯 권장 조치사항</h2>
            <div class="insights">
                <h3>즉시 실행 항목</h3>
                <ul>
                    {''.join([f'<li>{action}</li>' for action in data.get('actions', ['분석 결과 기반 권장사항 생성 중...'])])}
                </ul>
            </div>
        </div>
        
        {generate_chat_history_html(chat_history) if chat_history else ''}
        
        <div class="footer">
            <div style="border-top: 3px solid #667eea; padding-top: 2rem; margin-top: 3rem;">
                <h4 style="color: #667eea; margin: 0 0 1rem 0;">냉간인발 강관 제조 공정 교육 시스템</h4>
                <p style="margin: 0.5rem 0; color: #555;">
                    <strong>Cold Drawn Seamless Steel Pipe Manufacturing Training System</strong>
                </p>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; color: #777;">
                    데이터 기반 제조 공정 최적화 | AI 기반 품질관리 시스템
                </p>
                <p style="margin: 1rem 0 0.5rem 0; font-size: 0.9rem; color: #888;">
                    📊 IATF 16949 | ISO 9001:2015 | ISO 14001:2015 준수<br>
                    🔒 15년 기록 보관 | LOT 추적 시스템 | 2D Barcode/QR Code
                </p>
                <p style="margin: 1.5rem 0 0 0; font-size: 0.85rem; color: #999; border-top: 1px solid #e0e0e0; padding-top: 1rem;">
                    © 2024-2025 냉간인발 강관 제조 공정 교육 시스템. All rights reserved.<br>
                    본 시스템은 AI 기반 제조 공정 교육 및 품질관리를 위해 개발되었습니다.
                </p>
            </div>
        </div>
    </div>
</body>
</html>
"""
    
    return html_template

# ============================================================================
# 메인 애플리케이션
# ============================================================================

def main():
    
    # 헤더
    st.markdown("""
    <div class="header-container">
        <h1 class="header-title">🏭 냉간인발 강관 제조 공정 교육 시스템</h1>
        <p class="header-subtitle">Cold Drawn Seamless Steel Pipe Manufacturing Training System</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 사이드바: 설정
    with st.sidebar:
        st.header("⚙️ 시스템 설정")
        
        # Fe-C 상태도 보기
        st.subheader("🔬 Fe-C 상태도")
        with st.expander("📊 Fe-C 상태도 보기", expanded=False):
            st.markdown("""
            **철-탄소 상태도 (Iron-Carbon Phase Diagram)**
            
            냉간인발 강관의 열처리 및 기계적 특성 이해를 위한 필수 자료입니다.
            """)
            
            # Fe-C 상태도 설명
            st.markdown("""
            #### 주요 영역 및 온도
            
            **1. 순철 (Pure Iron)**
            - α-Fe (Ferrite): < 912°C (BCC)
            - γ-Fe (Austenite): 912-1394°C (FCC)
            - δ-Fe: 1394-1538°C (BCC)
            
            **2. 공석점 (Eutectoid Point)**
            - 온도: 727°C
            - 탄소 함량: 0.77% C
            - 조직: Pearlite (Ferrite + Cementite)
            
            **3. 강의 분류**
            - 아공석강 (Hypoeutectoid): < 0.77% C
              - 냉간인발 파이프 공정 소재: **0.15-0.25% C** ✓
            - 공석강 (Eutectoid): 0.77% C
            - 과공석강 (Hypereutectoid): 0.77-2.11% C
            
            **4. 주요 상변태 온도**
            ```
            A₃ 변태점 (0.15-0.25% C):
              - 시작: ~850-880°C
              - 완료: ~910-930°C
            
            A₁ 변태점 (공석온도):
              - 727°C (일정)
            ```
            
            #### 열처리 온도 범위
            
            **정규화 (Normalizing)**
            - 온도: 880-920°C (A₃ + 30-50°C)
            - 목적: 결정립 미세화, 균질화
            - 냉각: 공랭 (Air Cooling)
            
            **풀림 (Annealing)**
            - 온도: 650-700°C (A₁ 이하)
            - 목적: 응력 제거, 연화
            - 냉각: 노냉 (Furnace Cooling)
            
            **응력제거 (Stress Relieving)**
            - 온도: 580-620°C
            - 목적: 잔류응력 제거
            - 냉각: 공랭
            
            #### 탄소 함량별 특성
            
            | C % | 경도(HB) | 인장강도(MPa) | 연신율(%) | 용도 |
            |-----|----------|---------------|-----------|------|
            | 0.10 | 100-120 | 320-400 | 30-35 | 배관 |
            | **0.20** | **120-150** | **370-470** | **25-30** | **냉간인발 소재** |
            | 0.30 | 150-180 | 470-570 | 20-25 | 구조용 |
            | 0.40 | 180-220 | 570-670 | 15-20 | 기계부품 |
            
            #### 미세조직
            
            **냉간인발 파이프 공정 소재 (0.15-0.25% C):**
            - 주조직: **Ferrite (α-Fe)**
            - 부조직: Pearlite (소량)
            - 비율: Ferrite 80-90%, Pearlite 10-20%
            
            **특성:**
            - ✅ 우수한 연성 (≥25% 연신율)
            - ✅ 적절한 강도 (370-470 MPa)
            - ✅ 우수한 가공성
            - ✅ 우수한 용접성
            
            ---
            
            **📚 참고 표준:**
            - KS D 0204: 철강의 현미경 조직 시험 방법
            - ASTM E112: 결정립도 측정
            - JIS G 0551: 강의 결정립도 시험 방법
            """)
            
            # 간단한 ASCII 상태도
            st.code("""
Fe-C 상태도 (단순화)
Temperature (°C)
1600 |                    L (Liquid)
     |            .-----------------.
1400 |        .--'                   `--. δ+L
     |    .--'                           `--.
1200 | δ                                    `-.
     |                γ (Austenite)            `-. L+γ
1000 |                                            `-.
     |                                               γ+Fe₃C
 800 | α+γ        A₃                                  |
     |----.-------`------------------------.----------|
 727 | α  |    Pearlite (α+Fe₃C)           | γ+Fe₃C   | A₁
     |----|--------------------------------|----------|
 600 |    |                                |          |
     | α (Ferrite)                         | α+Fe₃C   |
     |                                     |          |
   0 +-----+-------------------+----------+----------+
     0   0.022              0.77%C      2.11%      6.67%
                        (Eutectoid)  (Eutectic)  (Fe₃C)
     
냉간인발 파이프 공정 소재: 0.15-0.25% C (아공석강 영역)
            """, language="text")
            
            st.info("💡 **Tip**: 열처리 온도 설정 시 A₃ 변태점(850-930°C)을 기준으로 합니다.")
        
        st.divider()
        
        # LangChain 설치 확인
        if not LANGCHAIN_AVAILABLE:
            st.error("⚠️ LangChain 미설치")
            with st.expander("📦 설치 방법 보기"):
                st.markdown("""
                **LangChain 설치가 필요합니다:**
                
                ```bash
                # 핵심 패키지
                pip install langchain
                pip install langchain-core
                pip install langchain-community
                
                # AI 모델 연동
                pip install langchain-anthropic
                pip install langchain-openai
                ```
                
                또는 한번에:
                
                ```bash
                pip install -r requirements.txt
                ```
                
                설치 후 앱을 재시작하세요.
                
                ---
                
                **버전 확인:**
                ```bash
                pip list | grep langchain
                ```
                
                **예상 출력:**
                - langchain >= 0.1.0
                - langchain-core >= 0.1.0
                - langchain-community >= 0.0.20
                """)
        else:
            st.success("✅ LangChain 설치됨")
        
        st.divider()
        
        # 1. API 설정
        st.subheader("1️⃣ API 설정")
        
        model_type = st.selectbox(
            "AI 모델 선택",
            ["Claude (Anthropic)", "GPT-4o-mini (OpenAI)"],
            help="사용할 AI 모델을 선택하세요"
        )
        
        # Claude 모델 세부 선택
        if model_type == "Claude (Anthropic)":
            claude_model = st.selectbox(
                "Claude 모델 버전",
                [
                    "claude-3-5-sonnet-20241022",
                    "claude-3-5-sonnet-20240620",
                    "claude-3-opus-20240229",
                    "claude-3-sonnet-20240229",
                    "claude-3-haiku-20240307"
                ],
                index=2,  # 기본값: claude-3-opus-20240229 (가장 호환성 높음)
                help="모델 버전을 선택하세요. 404 오류 시 claude-3-opus-20240229 또는 claude-3-haiku-20240307을 선택하세요."
            )
        else:
            claude_model = None
        
        # API 키 입력 방식 선택
        api_input_method = st.radio(
            "API 키 입력 방식",
            ["직접 입력", ".env 파일 업로드"],
            help="API 키를 입력하는 방식을 선택하세요"
        )
        
        if api_input_method == "직접 입력":
            if model_type == "Claude (Anthropic)":
                api_key = st.text_input(
                    "Anthropic API Key",
                    type="password",
                    help="ANTHROPIC_API_KEY를 입력하세요"
                )
            else:
                api_key = st.text_input(
                    "OpenAI API Key",
                    type="password",
                    help="OPENAI_API_KEY를 입력하세요"
                )
            
            if st.button("🔐 API 키 저장 (.env)"):
                env_key = "ANTHROPIC_API_KEY" if model_type == "Claude (Anthropic)" else "OPENAI_API_KEY"
                if save_env_file({env_key: api_key}):
                    st.success("✅ API 키가 .env 파일로 저장되었습니다!")
        
        else:  # .env 파일 업로드
            env_file = st.file_uploader(
                ".env 파일 업로드",
                type=['env', 'txt'],
                help="API 키가 포함된 .env 파일을 업로드하세요"
            )
            
            if env_file:
                env_content = env_file.read()
                # 임시 파일로 저장
                with open(".env", "wb") as f:
                    f.write(env_content)
                
                env_vars = load_env_file(".env")
                
                if model_type == "Claude (Anthropic)":
                    api_key = env_vars.get("ANTHROPIC_API_KEY", "")
                else:
                    api_key = env_vars.get("OPENAI_API_KEY", "")
                
                if api_key:
                    st.success("✅ .env 파일에서 API 키를 로드했습니다!")
                else:
                    st.error("❌ .env 파일에 해당 API 키가 없습니다.")
                    api_key = ""
            else:
                api_key = ""
        
        # API 설정 확인 버튼
        if st.button("🔌 연결 테스트", use_container_width=True):
            if api_key:
                with st.spinner("연결 테스트 중..."):
                    llm = initialize_llm(api_key, model_type, claude_model)
                    if llm:
                        st.session_state.current_model = llm
                        st.session_state.api_configured = True
                        
                        # 선택된 모델 정보 표시
                        if model_type == "Claude (Anthropic)":
                            st.success(f"✅ {model_type} 연결 성공!\n\n모델: `{claude_model}`")
                        else:
                            st.success(f"✅ {model_type} 연결 성공!")
                    else:
                        st.error("❌ 연결 실패. API 키와 모델을 확인하세요.")
            else:
                st.warning("⚠️ API 키를 입력하세요.")
        
        st.divider()
        
        # 2. 온톨로지 업로드
        st.subheader("2️⃣ 온톨로지 업로드")
        
        uploaded_files = st.file_uploader(
            "온톨로지 파일 업로드",
            type=['yaml', 'yml', 'json', 'csv', 'txt'],
            accept_multiple_files=True,
            help="YAML, JSON, CSV, TXT 형식 지원"
        )
        
        if uploaded_files:
            st.info(f"📁 {len(uploaded_files)}개 파일 업로드됨")
            
            if st.button("📥 파일 파싱", use_container_width=True):
                with st.spinner("파일 파싱 중..."):
                    parsed_data = []
                    for uploaded_file in uploaded_files:
                        file_content = uploaded_file.read()
                        data = parse_ontology_file(file_content, uploaded_file.name)
                        if data:
                            parsed_data.append({
                                'filename': uploaded_file.name,
                                'data': data
                            })
                    
                    st.session_state.uploaded_files_data = parsed_data
                    st.session_state.ontology_data = {
                        item['filename']: item['data'] 
                        for item in parsed_data
                    }
                    st.success(f"✅ {len(parsed_data)}개 파일 파싱 완료!")
        
        st.divider()
        
        # 3. 시스템 상태
        st.subheader("3️⃣ 시스템 상태")
        
        status_col1, status_col2 = st.columns(2)
        
        with status_col1:
            if st.session_state.api_configured:
                st.success("🟢 API 연결됨")
            else:
                st.error("🔴 API 미연결")
        
        with status_col2:
            if st.session_state.ontology_data:
                st.success(f"🟢 온톨로지 {len(st.session_state.ontology_data)}개")
            else:
                st.warning("🟡 온톨로지 없음")
        
        if st.button("🔄 초기화", use_container_width=True):
            st.session_state.clear()
            st.rerun()
    
    # 메인 콘텐츠: 탭
    tab1, tab_fec, tab2, tab3, tab4 = st.tabs([
        "💬 AI 대화",
        "🔬 Fe-C 상태도",
        "📚 운영 매뉴얼",
        "📊 온톨로지 뷰어",
        "📈 인사이트 보고서"
    ])
    
    # ========================================================================
    # 탭 1: AI 대화
    # ========================================================================
    
    with tab1:
        st.header("💬 AI 어시스턴트와 대화")
        
        if not st.session_state.api_configured:
            st.markdown("""
            <div class="warning-box">
                ⚠️ <strong>API 설정이 필요합니다</strong><br>
                왼쪽 사이드바에서 API 키를 설정하고 연결 테스트를 진행하세요.
            </div>
            """, unsafe_allow_html=True)
        else:
            # 온톨로지 요약
            ontology_summary = ""
            if st.session_state.ontology_data:
                ontology_summary = "업로드된 온톨로지:\n"
                for filename, data in st.session_state.ontology_data.items():
                    ontology_summary += f"- {filename}: {len(data)} 항목\n"
            else:
                ontology_summary = "업로드된 온톨로지가 없습니다."
            
            # 대화 이력 표시
            chat_container = st.container()
            
            with chat_container:
                for message in st.session_state.chat_history:
                    if message['role'] == 'user':
                        st.markdown(f"""
                        <div class="chat-message user-message">
                            <strong>👤 사용자</strong>
                            <div class="message-content">{message['content']}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class="chat-message assistant-message">
                            <strong>🤖 AI 어시스턴트</strong>
                            <div class="message-content">{message['content']}</div>
                        </div>
                        """, unsafe_allow_html=True)
            
            # 입력 폼
            with st.form(key="chat_form", clear_on_submit=True):
                user_input = st.text_area(
                    "질문을 입력하세요",
                    placeholder="예: 냉간인발 공정에서 표면 결함이 발생했을 때 조치 방법은?",
                    height=100
                )
                
                col1, col2 = st.columns([4, 1])
                with col1:
                    submit_button = st.form_submit_button("📤 전송", use_container_width=True)
                with col2:
                    clear_button = st.form_submit_button("🗑️ 초기화", use_container_width=True)
            
            if submit_button and user_input:
                # 사용자 메시지 추가
                st.session_state.chat_history.append({
                    'role': 'user',
                    'content': user_input,
                    'timestamp': datetime.now().isoformat()
                })
                
                # AI 응답 생성 (RAG 통합)
                with st.spinner("🔍 온톨로지 검색 중..."):
                    # 온톨로지 컨텍스트 생성
                    ontology_context = create_ontology_context(
                        user_input, 
                        st.session_state.ontology_data
                    )
                
                with st.spinner("🤖 AI가 답변 생성 중..."):
                    try:
                        if LANGCHAIN_AVAILABLE and st.session_state.current_model:
                            chain = create_conversation_chain(
                                st.session_state.current_model,
                                st.session_state.memory
                            )
                            
                            # RAG: 온톨로지 컨텍스트를 입력에 추가
                            enhanced_input = user_input
                            if ontology_context:
                                enhanced_input = f"{user_input}\n\n{ontology_context}"
                            
                            # Modern LangChain (LCEL) 방식
                            try:
                                response = chain.invoke({
                                    "input": enhanced_input,
                                    "ontology_summary": ontology_summary
                                })
                                
                                # Memory에는 원본 질문 저장
                                st.session_state.memory.save_context(
                                    {"input": user_input},
                                    {"output": response}
                                )
                                
                            except AttributeError:
                                # Legacy LangChain 방식 (predict)
                                response = chain.predict(
                                    input=user_input,
                                    ontology_summary=ontology_summary
                                )
                            
                            # AI 메시지 추가
                            st.session_state.chat_history.append({
                                'role': 'assistant',
                                'content': response,
                                'timestamp': datetime.now().isoformat()
                            })
                            
                            st.rerun()
                        else:
                            st.error("❌ LangChain이 설치되지 않았거나 모델이 초기화되지 않았습니다.")
                    except Exception as e:
                        st.error(f"❌ 오류 발생: {str(e)}")
                        # 상세 오류 정보 (디버그용)
                        with st.expander("🔍 상세 오류 정보"):
                            st.code(f"오류 타입: {type(e).__name__}\n오류 메시지: {str(e)}")
            
            if clear_button:
                st.session_state.chat_history = []
                if LANGCHAIN_AVAILABLE:
                    st.session_state.memory.clear()
                st.rerun()
            
            # 대화 내역 저장
            if st.session_state.chat_history:
                st.divider()
                
                st.markdown("### 💾 대화 내역 관리")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    if st.button("📥 JSON 저장", use_container_width=True):
                        chat_json = json.dumps(
                            st.session_state.chat_history,
                            ensure_ascii=False,
                            indent=2
                        )
                        st.download_button(
                            "⬇️ JSON 다운로드",
                            chat_json,
                            file_name=f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                            mime="application/json",
                            use_container_width=True
                        )
                
                with col2:
                    if st.button("📥 YAML 저장", use_container_width=True):
                        import yaml
                        chat_yaml = yaml.dump(
                            st.session_state.chat_history,
                            allow_unicode=True,
                            default_flow_style=False,
                            sort_keys=False
                        )
                        st.download_button(
                            "⬇️ YAML 다운로드",
                            chat_yaml,
                            file_name=f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.yaml",
                            mime="text/yaml",
                            use_container_width=True
                        )
                
                with col3:
                    if st.button("📥 TXT 저장", use_container_width=True):
                        chat_text = ""
                        for msg in st.session_state.chat_history:
                            role = "사용자" if msg['role'] == 'user' else "AI"
                            timestamp = msg.get('timestamp', '')
                            chat_text += f"[{timestamp}] {role}: {msg['content']}\n\n"
                        
                        st.download_button(
                            "⬇️ TXT 다운로드",
                            chat_text,
                            file_name=f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                
                st.divider()
                
                # 주제별 자동 보고서 생성
                st.markdown("### 📊 주제별 보고서 자동 생성")
                
                st.info("""
                💡 **자동 주제 분석**: AI 대화 내용을 자동으로 분석하여 주제별로 정리된 보고서를 생성합니다.
                - 공정별 질문/답변 분류
                - 주요 인사이트 추출
                - 기술 데이터 정리
                - 개선 제안 요약
                """)
                
                if st.button("🤖 AI 기반 주제별 보고서 생성", use_container_width=True, type="primary"):
                    if st.session_state.api_configured and st.session_state.current_model:
                        with st.spinner("대화 내용을 분석하고 주제별로 정리 중..."):
                            try:
                                # 대화 내용 요약
                                conversation_text = "\n\n".join([
                                    f"{'사용자' if msg['role'] == 'user' else 'AI'}: {msg['content']}"
                                    for msg in st.session_state.chat_history
                                ])
                                
                                # AI에게 주제별 정리 요청
                                summary_prompt = f"""다음은 냉간인발 강관 제조 공정에 대한 대화 내용입니다.
이 대화를 주제별로 분석하고 정리하여 교육 보고서를 작성해주세요.

대화 내용:
{conversation_text}

다음 형식으로 정리해주세요:

# 대화 주제별 분석 보고서

## 1. 대화 요약
- 총 대화 수: 
- 주요 주제:
- 다룬 공정 단계:

## 2. 공정별 질문/답변 분류
### 열처리 (Heat Treatment)
### 산세 (Pickling)
### 냉간인발 (Cold Drawing)
### 검사 (Inspection)
### 기타

## 3. 주요 기술 데이터
- 온도 범위:
- 재료 규격:
- 품질 기준:
- 기계적 특성:

## 4. 핵심 인사이트
(대화에서 발견된 중요한 기술적 인사이트)

## 5. 개선 제안 사항
(대화 내용 기반 공정 개선 아이디어)

## 6. 추가 학습 필요 영역
(더 깊이 공부해야 할 주제)

각 섹션을 구체적으로 작성해주세요."""

                                response = st.session_state.current_model.invoke(summary_prompt)
                                
                                # 텍스트 추출
                                if hasattr(response, 'content'):
                                    report_content = response.content
                                else:
                                    report_content = str(response)
                                
                                # 보고서 표시
                                st.success("✅ 주제별 보고서 생성 완료!")
                                
                                st.markdown("---")
                                st.markdown(report_content)
                                st.markdown("---")
                                
                                # 보고서 다운로드
                                col1, col2 = st.columns(2)
                                
                                with col1:
                                    st.download_button(
                                        "📥 보고서 다운로드 (Markdown)",
                                        report_content,
                                        file_name=f"topic_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                                        mime="text/markdown",
                                        use_container_width=True
                                    )
                                
                                with col2:
                                    # HTML 보고서 생성
                                    # 줄바꿈을 HTML br 태그로 변환
                                    report_html_content = report_content.replace('\n', '<br>')
                                    current_time = datetime.now().strftime('%Y년 %m월 %d일 %H:%M')
                                    
                                    html_report = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>주제별 분석 보고서</title>
    <style>
        body {{ font-family: 'Noto Sans KR', sans-serif; max-width: 900px; margin: 40px auto; padding: 20px; line-height: 1.8; }}
        h1 {{ color: #667eea; border-bottom: 3px solid #667eea; padding-bottom: 10px; }}
        h2 {{ color: #764ba2; margin-top: 30px; border-left: 5px solid #764ba2; padding-left: 10px; }}
        h3 {{ color: #555; }}
        pre {{ background: #f5f5f5; padding: 15px; border-radius: 5px; overflow-x: auto; }}
        code {{ background: #f0f0f0; padding: 2px 6px; border-radius: 3px; }}
        ul, ol {{ margin-left: 20px; }}
        .footer {{ margin-top: 50px; padding-top: 20px; border-top: 2px solid #e0e0e0; text-align: center; color: #999; }}
    </style>
</head>
<body>
    <h1>🏭 냉간인발 강관 제조 공정 - 주제별 분석 보고서</h1>
    <p><strong>생성일:</strong> {current_time}</p>
    <hr>
    {report_html_content}
    <div class="footer">
        <div style="border-top: 3px solid #667eea; padding-top: 2rem; margin-top: 3rem;">
            <h4 style="color: #667eea; margin: 0 0 1rem 0;">냉간인발 강관 제조 공정 교육 시스템</h4>
            <p style="margin: 0.5rem 0; color: #555; font-weight: 600;">
                Cold Drawn Seamless Steel Pipe Manufacturing Training System
            </p>
            <p style="margin: 0.8rem 0; font-size: 0.9rem; color: #777;">
                데이터 기반 제조 공정 최적화 | AI 기반 품질관리 시스템
            </p>
            <p style="margin: 1rem 0; font-size: 0.9rem; color: #888;">
                📊 IATF 16949 | ISO 9001:2015 | ISO 14001:2015<br>
                🔒 15년 기록 보관 | LOT 추적 | 2D Barcode/QR Code
            </p>
            <p style="margin: 1.5rem 0 0 0; font-size: 0.85rem; color: #999; border-top: 1px solid #e0e0e0; padding-top: 1rem;">
                © 2024-2025 냉간인발 강관 제조 공정 교육 시스템. All rights reserved.<br>
                본 보고서는 AI가 자동 생성한 분석 결과입니다.
            </p>
        </div>
    </div>
</body>
</html>"""
                                    st.download_button(
                                        "📥 보고서 다운로드 (HTML)",
                                        html_report,
                                        file_name=f"topic_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html",
                                        mime="text/html",
                                        use_container_width=True
                                    )
                            
                            except Exception as e:
                                st.error(f"❌ 보고서 생성 실패: {str(e)}")
                    else:
                        st.warning("⚠️ AI 모델이 연결되지 않았습니다. 먼저 사이드바에서 API를 설정하세요.")
    
    # ========================================================================
    # Fe-C 상태도 탭
    # ========================================================================
    
    with tab_fec:
        st.header("🔬 Fe-C 상태도 - 철강 제조의 바이블")
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2rem; border-radius: 15px; color: white; margin-bottom: 2rem;'>
            <h2 style='color: white; margin: 0;'>Iron-Carbon Phase Diagram</h2>
            <p style='margin: 0.5rem 0 0 0; font-size: 1.1rem;'>
                모든 열처리 공정의 과학적 근거이자, 품질 문제 해결의 핵심 도구
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # 서브탭 구성
        fec_subtabs = st.tabs([
            "📊 상태도 & 이론",
            "🌡️ 온도 계산기",
            "⚗️ 조직 & 특성 예측",
            "🔥 열처리 가이드",
            "📈 인터랙티브 차트"
        ])
        
        # 서브탭 1: 상태도 & 이론
        with fec_subtabs[0]:
            st.subheader("📊 Fe-C 상태도")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.code("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                        Fe-C 상태도 (Iron-Carbon Phase Diagram)              ║
╚═══════════════════════════════════════════════════════════════════════════╝

Temperature (°C)
    
1600│                            L (Liquid - 액체)
    │                     ┌─────────────────────────┐
1538│                 .───┘                          └───.  
    │             .───'                                  '───.
1495│         .───'                                          '───. δ+L
    │     .───'                                                  '───.
1400│ .───'                                                          '───.
    │'                                                                   '───.
1394│ δ-Fe (BCC)                                                             '───.
    │                                                                            └───.
1200│                                                                                 '─. L+γ
    │                                                                                   └──.
1148│                                                                                      └─.
    │              γ (Austenite - FCC, 오스테나이트)                                         └───.
1000│                                                                                           '──.
    │                                                                                              └─.Fe₃C+L
 912│ ┌───────────.  A₄                                                                              │
    │ │            ╲                                                                                 │
 800│ │    α+γ      ╲                                                                                │
    │ │              ╲    A₃ (850-930°C for 0.15-0.25%C) ◄── 냉간인발 소재                           │
    │ │               ╲                                                                              │
 727│ │  ┌─────────────┴────────────────────────────────────────────────────────.                   │ A₁
    │ │  │                                                                        ╲                  │
    │ │  │              Pearlite (α-Ferrite + Fe₃C)                               ╲                 │
 600│ │  │                                                                          ╲                │
    │ │  │                                                                           ╲     α+Fe₃C    │
 400│ │  │   α-Fe (Ferrite - BCC, 페라이트)                                           ╲              │
    │ │  │                                                                             ╲             │
 200│ │  │                                                                              ╲            │
    │ │  │                                                                               ╲           │
   0├─┴──┴────────────────────────────────────────────────────────────────────────────────┴──────────┤
    0  0.022              0.77%                    2.11%                    4.3%                 6.67%
                      (Eutectoid)              (Eutectic)                                     (Fe₃C)
                        공석점                      공정점                                    시멘타이트

════════════════════════════════════════════════════════════════════════════

[범례]
  α (Alpha):   Ferrite - 체심입방(BCC), 탄소 고용도 낮음 (<0.022%)
  γ (Gamma):   Austenite - 면심입방(FCC), 탄소 고용도 높음 (최대 2.11%)
  δ (Delta):   고온 Ferrite - 체심입방(BCC)
  Fe₃C:        Cementite (시멘타이트) - 매우 단단, 취성

[주요 변태점]
  A₁ = 727°C    (공석온도, Eutectoid)
  A₃ = 850-930°C (탄소량에 따라 변화)
  A₄ = 1394°C   (γ → δ 변태)

[냉간인발 소재 (0.15-0.25% C)]
  위치: 아공석강 영역 (Hypoeutectoid)
  조직: α-Ferrite (80-90%) + Pearlite (10-20%)
  특성: 우수한 가공성, 적절한 강도, 우수한 용접성
                """, language="text")
            
            with col2:
                st.markdown("""
                ### 🎯 핵심 포인트
                
                **상온 조직 (0.20% C)**
                - Ferrite: 85-90%
                - Pearlite: 10-15%
                
                **기계적 특성**
                - 경도: 120-150 HB
                - 인장강도: 370-470 MPa
                - 연신율: 25-30%
                
                **열처리 온도**
                - A₃: ~870°C
                - 정규화: 900°C
                - 풀림: 650-700°C
                
                **장점**
                - ✅ 냉간가공 용이
                - ✅ 용접 우수
                - ✅ 연성 높음
                - ✅ 경제적
                """)
            
            st.divider()
            
            # 상세 이론
            st.markdown("""
            ### 📚 Fe-C 상태도 상세 이론
            
            #### 1. 철의 동소체 (Allotropes of Iron)
            
            철은 온도에 따라 결정 구조가 변하는 **동소체**를 가집니다:
            
            | 온도 범위 | 상 | 결정구조 | 탄소 고용도 | 특성 |
            |----------|---|----------|------------|------|
            | < 912°C | α-Fe | BCC (체심입방) | < 0.022% | 자성, 연함 |
            | 912-1394°C | γ-Fe | FCC (면심입방) | 최대 2.11% | 비자성, 변형 용이 |
            | 1394-1538°C | δ-Fe | BCC (체심입방) | < 0.09% | 고온 |
            | > 1538°C | Liquid | - | 완전 고용 | 액체 |
            
            **왜 중요한가?**
            - 열처리는 이 상변태를 이용합니다
            - γ-Fe는 탄소를 많이 녹일 수 있어 열처리 핵심
            - α-Fe로 냉각 시 조직이 결정됩니다
            
            #### 2. 주요 변태점
            
            **A₁ (727°C) - 공석온도**
            ```
            γ (0.77% C) → α (0.022% C) + Fe₃C (6.67% C)
                       ↓
                    Pearlite
            ```
            - 모든 강종에서 일정
            - Pearlite(펄라이트) 생성
            - 층상 구조: Ferrite + Cementite
            
            **A₃ - 탄소에 따라 변화**
            ```
            탄소량     A₃ 온도
            0.10%  →  ~900°C
            0.20%  →  ~870°C
            0.30%  →  ~840°C
            0.77%  →  727°C (A₁과 만남)
            ```
            - 탄소 증가 → A₃ 하강
            - 열처리 온도 설정 기준
            
            #### 3. 강의 분류
            
            **아공석강 (< 0.77% C)** ← 냉간인발 소재
            - 주조직: Ferrite
            - 부조직: Pearlite
            - 탄소↑ → Pearlite↑ → 강도↑, 연성↓
            
            **공석강 (0.77% C)**
            - 전체 조직: 100% Pearlite
            - 강도와 경도 높음
            - 레일, 와이어 로프
            
            **과공석강 (0.77-2.11% C)**
            - Pearlite + 초석 Cementite
            - 매우 단단, 취성
            - 공구강, 베어링강
            
            #### 4. 냉간인발 소재 (0.15-0.25% C)
            
            **상온 조직 계산**
            ```
            탄소 0.20% C 기준:
            
            Pearlite 비율 = 0.20 / 0.77 × 100% = 26%
            Ferrite 비율 = 74%
            
            실제로는:
            - Ferrite: 85-90%
            - Pearlite: 10-15%
            (공석점 이하 탄소 일부는 Ferrite에 고용)
            ```
            
            **왜 이 성분인가?**
            - 강도: Pearlite가 제공
            - 연성: Ferrite가 제공
            - 가공성: Ferrite 다량 → 냉간인발 가능
            - 용접성: 탄소 낮아 우수
            - 경제성: 특수 합금 불필요
            """)
        
        # 서브탭 2: 온도 계산기
        with fec_subtabs[1]:
            st.subheader("🌡️ 열처리 온도 계산기")
            
            st.info("💡 탄소 함량을 입력하면 Fe-C 상태도 기반으로 최적 열처리 온도를 자동 계산합니다.")
            
            col1, col2 = st.columns(2)
            
            with col1:
                carbon_pct = st.slider(
                    "탄소 함량 (%)",
                    min_value=0.10,
                    max_value=0.50,
                    value=0.20,
                    step=0.01,
                    help="소재의 탄소 함량을 입력하세요"
                )
                
                heat_treatment_type = st.selectbox(
                    "열처리 종류",
                    ["정규화 (Normalizing)", "완전 풀림 (Full Annealing)", "응력제거 (Stress Relieving)"]
                )
            
            with col2:
                # A₃ 온도 계산 (근사식)
                A3_temp = 910 - 203 * carbon_pct**0.5
                
                st.metric("A₃ 변태점", f"{A3_temp:.0f}°C")
                st.metric("A₁ 공석온도", "727°C", delta="일정")
                
                # 조직 예측
                pearlite_pct = (carbon_pct / 0.77) * 100
                ferrite_pct = 100 - pearlite_pct
                
                st.metric("예상 Ferrite", f"{ferrite_pct:.0f}%")
                st.metric("예상 Pearlite", f"{pearlite_pct:.0f}%")
            
            st.divider()
            
            # 열처리 조건 계산
            st.markdown("### 📋 권장 열처리 조건")
            
            if "정규화" in heat_treatment_type:
                target_temp = A3_temp + 40
                holding_time = "30-60분 (두께에 따라)"
                cooling = "공랭 (Air Cooling)"
                purpose = "결정립 미세화, 조직 균질화"
                
            elif "완전 풀림" in heat_treatment_type:
                target_temp = A3_temp + 25
                holding_time = "1-2시간"
                cooling = "노냉 (Furnace Cooling, ~50°C/h)"
                purpose = "연화, 가공성 향상"
                
            else:  # 응력제거
                target_temp = 600
                holding_time = "1-2시간"
                cooling = "공랭 (Air Cooling)"
                purpose = "잔류응력 제거 (조직 변화 없음)"
            
            result_df = pd.DataFrame({
                '항목': ['목표 온도', '온도 범위', '유지 시간', '냉각 방법', '목적'],
                '값': [
                    f"{target_temp:.0f}°C",
                    f"{target_temp-10:.0f} ~ {target_temp+10:.0f}°C (±10°C)",
                    holding_time,
                    cooling,
                    purpose
                ]
            })
            
            st.dataframe(result_df, use_container_width=True, hide_index=True)
            
            st.success(f"""
            ✅ **계산 결과 요약**
            
            - 탄소 함량: {carbon_pct}%
            - A₃ 변태점: {A3_temp:.0f}°C
            - **권장 온도: {target_temp:.0f}°C**
            - 유지 시간: {holding_time}
            - 냉각: {cooling}
            """)
            
            # 온도 설정 체크리스트
            st.markdown("### ✅ 온도 설정 체크리스트")
            
            checklist = {
                "1. 밀시트에서 탄소 함량 확인": False,
                "2. A₃ 온도 계산": False,
                "3. 열처리 종류에 따른 온도 여유 추가": False,
                "4. 온도 편차 ±5°C 이내 설정": False,
                "5. 유지 시간 확인 (두께 기준)": False,
                "6. 냉각 방법 준비": False,
                "7. 온도 기록계 작동 확인": False
            }
            
            for item in checklist:
                st.checkbox(item, key=f"check_{item}")
        
        # 서브탭 3: 조직 & 특성 예측
        with fec_subtabs[2]:
            st.subheader("⚗️ 조직 구성 및 기계적 특성 예측")
            
            carbon_input = st.number_input(
                "탄소 함량 (%) 입력",
                min_value=0.10,
                max_value=1.00,
                value=0.20,
                step=0.01
            )
            
            # 조직 비율 계산
            if carbon_input <= 0.77:
                pearlite = (carbon_input / 0.77) * 100
                ferrite = 100 - pearlite
                cementite = 0
                classification = "아공석강 (Hypoeutectoid Steel)"
            elif carbon_input == 0.77:
                pearlite = 100
                ferrite = 0
                cementite = 0
                classification = "공석강 (Eutectoid Steel)"
            else:
                pearlite = ((2.11 - carbon_input) / (2.11 - 0.77)) * 100
                ferrite = 0
                cementite = 100 - pearlite
                classification = "과공석강 (Hypereutectoid Steel)"
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"### 📊 조직 구성")
                st.markdown(f"**분류:** {classification}")
                
                # 파이 차트
                import plotly.graph_objects as go
                
                labels = []
                values = []
                colors = []
                
                if ferrite > 0:
                    labels.append('Ferrite')
                    values.append(ferrite)
                    colors.append('#90caf9')
                
                if pearlite > 0:
                    labels.append('Pearlite')
                    values.append(pearlite)
                    colors.append('#ce93d8')
                
                if cementite > 0:
                    labels.append('Cementite')
                    values.append(cementite)
                    colors.append('#ffab91')
                
                fig_pie = go.Figure(data=[go.Pie(
                    labels=labels,
                    values=values,
                    marker=dict(colors=colors),
                    textinfo='label+percent',
                    textfont_size=14
                )])
                
                fig_pie.update_layout(
                    title=f"조직 구성 (탄소 {carbon_input}%)",
                    height=400
                )
                
                st.plotly_chart(fig_pie, use_container_width=True)
            
            with col2:
                st.markdown("### 📈 예상 기계적 특성")
                
                # 기계적 특성 예측 (경험식)
                tensile_strength = 320 + (carbon_input * 600)
                hardness = 100 + (carbon_input * 200)
                elongation = 35 - (carbon_input * 30)
                
                metrics_df = pd.DataFrame({
                    '특성': ['인장강도', '경도', '연신율'],
                    '예측값': [
                        f"{tensile_strength:.0f} MPa",
                        f"{hardness:.0f} HB",
                        f"{elongation:.0f} %"
                    ],
                    '냉간인발 기준': [
                        "370-470 MPa",
                        "120-180 HB",
                        "≥ 25%"
                    ],
                    '판정': [
                        "✅" if 370 <= tensile_strength <= 470 else "⚠️",
                        "✅" if 120 <= hardness <= 180 else "⚠️",
                        "✅" if elongation >= 25 else "⚠️"
                    ]
                })
                
                st.dataframe(metrics_df, use_container_width=True, hide_index=True)
                
                st.markdown("### 🎯 적합성 평가")
                
                if 0.15 <= carbon_input <= 0.25:
                    st.success(f"""
                    ✅ **냉간인발 소재로 적합**
                    
                    - 탄소 함량: {carbon_input}% (범위 내)
                    - 가공성: 우수
                    - 강도: 적절
                    - 용접성: 우수
                    """)
                elif carbon_input < 0.15:
                    st.warning(f"""
                    ⚠️ **강도 부족 우려**
                    
                    - 탄소 함량: {carbon_input}% (낮음)
                    - 연성은 우수하나 강도 부족
                    - 용도: 일반 배관용
                    """)
                else:
                    st.warning(f"""
                    ⚠️ **가공성 저하 우려**
                    
                    - 탄소 함량: {carbon_input}% (높음)
                    - 강도는 높으나 냉간가공 어려움
                    - 균열 위험 증가
                    """)
        
        # 서브탭 4: 열처리 가이드
        with fec_subtabs[3]:
            st.subheader("🔥 공정별 열처리 가이드")
            
            heat_guide_tabs = st.tabs(["정규화", "풀림", "담금질", "뜨임", "문제해결"])
            
            with heat_guide_tabs[0]:
                st.markdown("""
                ## 정규화 (Normalizing)
                
                ### 🎯 목적
                - 결정립 미세화
                - 조직 균질화
                - 기계적 성질 개선
                - 내부 응력 제거
                
                ### 📋 표준 절차
                
                **1단계: 가열**
                ```
                온도: A₃ + 30-50°C (880-920°C for 0.15-0.25%C)
                승온 속도: 100-200°C/h
                균열 방지: 예열 필요 시 600°C까지 서서히
                ```
                
                **2단계: 유지**
                ```
                시간: 30-60분 (기본)
                계산식: 1mm 두께당 1분
                예시: 20mm 두께 → 20분 + 여유 10분 = 30분
                온도 편차: ±5°C 이내
                ```
                
                **3단계: 냉각**
                ```
                방법: 공랭 (Still Air)
                속도: 자연 냉각 (~10°C/min)
                주의: 바람 직접 노출 금지
                종료: 상온까지
                ```
                
                ### ✅ 품질 기준
                - 경도: 120-150 HB
                - 조직: 미세 Ferrite + Pearlite
                - 결정립도: ASTM 6-8
                
                ### ⚠️ 주의사항
                - A₃ 이하 가열 시 불완전 변태
                - 과가열 시 결정립 조대화
                - 급냉 시 잔류 응력 발생
                """)
            
            with heat_guide_tabs[1]:
                st.markdown("""
                ## 풀림 (Annealing)
                
                ### 종류별 가이드
                
                #### 1. 완전 풀림 (Full Annealing)
                ```
                온도: A₃ + 20-30°C (870-900°C)
                유지: 1-2시간
                냉각: 노냉 (50°C/h)
                목적: 최대 연화
                ```
                
                #### 2. 구상화 풀림 (Spheroidizing)
                ```
                온도: A₁ 직하 (720°C)
                유지: 10-20시간
                냉각: 노냉
                결과: Cementite 구형화
                용도: 냉간가공 전처리
                ```
                
                #### 3. 응력제거 풀림 (Stress Relief)
                ```
                온도: 580-620°C (A₁ 이하)
                유지: 1-2시간
                냉각: 공랭
                특징: 조직 변화 없음
                ```
                
                ### 📊 냉각 속도 비교
                
                | 냉각 방법 | 속도 | 경도 | 조직 |
                |----------|------|------|------|
                | 노냉 | ~50°C/h | 낮음 | 조대 Pearlite |
                | 공랭 | ~600°C/h | 중간 | 미세 Pearlite |
                | 수냉 | ~5000°C/h | 높음 | Martensite |
                """)
            
            with heat_guide_tabs[2]:
                st.markdown("""
                ## 담금질 (Quenching)
                
                ### ⚠️ 냉간인발 소재에는 일반적으로 불필요
                
                탄소 0.15-0.25%는 담금질 효과가 제한적이며,
                주로 특수 요구사항이 있을 때만 실시합니다.
                
                ### 절차 (참고용)
                ```
                1. 가열: A₃ + 30-50°C
                2. 유지: 30-60분
                3. 급냉: 수냉 or 유냉
                4. 결과: Martensite (매우 단단, 취함)
                5. 필수: 뜨임 처리 병행
                ```
                
                ### 냉각 매체
                - 수냉: 가장 급냉, 균열 위험
                - 유냉: 중간, 변형 적음
                - 공랭: 완만, 경화 불충분
                
                ### 위험성
                - 균열 (Quenching Crack)
                - 변형
                - 잔류 응력
                - 취성 증가
                """)
            
            with heat_guide_tabs[3]:
                st.markdown("""
                ## 뜨임 (Tempering)
                
                ### 목적
                - 담금질 후 인성 회복
                - 잔류 응력 제거
                - 경도 조절
                
                ### 온도별 효과
                
                | 온도 범위 | 명칭 | 경도 | 인성 | 용도 |
                |----------|------|------|------|------|
                | 150-250°C | 저온 뜨임 | HRC 58-62 | 낮음 | 공구 |
                | 350-450°C | 중온 뜨임 | HRC 40-50 | 중간 | 스프링 |
                | 550-650°C | 고온 뜨임 | HRC 25-35 | 높음 | 축, 기어 |
                
                ### ⚠️ 뜨임 취성
                ```
                피해야 할 온도 구간:
                - 250-350°C: 저온 뜨임 취성
                - 500-600°C: 고온 뜨임 취성
                
                대책:
                - 해당 구간 빠르게 통과
                - 또는 급냉
                ```
                """)
            
            with heat_guide_tabs[4]:
                st.markdown("""
                ## 🔧 열처리 문제 해결
                
                ### 문제 1: 경도 목표치 미달
                
                **증상:** 120 HB 이하
                
                **원인 분석:**
                - A₃ 이하 가열 → Fe-C 상태도: 불완전 오스테나이트화
                - 유지 시간 부족 → 변태 미완료
                - 냉각 속도 과다 → 예상과 다른 조직
                
                **해결책:**
                ```
                1. 온도 상승: A₃ + 40°C로 재설정
                2. 유지 시간 연장: 50% 증가
                3. 온도 균일성 확인: 로내 편차 측정
                4. 재열처리 실시
                ```
                
                ### 문제 2: 경도 과다
                
                **증상:** 180 HB 초과
                
                **원인:**
                - 과가열 → Pearlite 증가
                - 급냉 → Bainite 생성
                
                **해결책:**
                ```
                1. 온도 하강: A₃ + 30°C로 조정
                2. 냉각 속도 감소: 서냉 적용
                3. 완전 풀림 적용: 연화
                ```
                
                ### 문제 3: 조직 불균일
                
                **증상:** 부위별 경도 편차 ≥ 15 HB
                
                **Fe-C 해석:**
                - 온도 편차 → 부분적 변태
                - 일부는 α+γ 영역, 일부는 γ 영역
                
                **해결책:**
                ```
                1. 로내 온도 분포 점검
                2. 장입 방법 개선
                3. 유지 시간 연장
                4. 순환 팬 작동 확인
                ```
                
                ### 문제 4: 표면 탈탄
                
                **증상:** 표면 경도 현저히 낮음
                
                **Fe-C 해석:**
                - 표면 탄소 손실 → Ferrite 증가
                - 내부는 정상 조직 유지
                
                **해결책:**
                ```
                1. 보호 분위기 사용: N₂, Ar
                2. 가열 시간 단축
                3. 탈탄층 연삭 제거
                4. 침탄 처리 (필요 시)
                ```
                
                ### 문제 5: 변형 과다
                
                **원인:**
                - 급냉 → 열응력
                - 변태 → 변태 응력
                - 고온 유지 → 크리프
                
                **대책:**
                ```
                1. 지그 사용: 형상 구속
                2. 서냉 적용: 응력 감소
                3. 예열/후열: 온도 구배 완화
                4. 형상 보정: 교정 공정 추가
                ```
                """)
        
        # 서브탭 5: 인터랙티브 차트
        with fec_subtabs[4]:
            st.subheader("📈 인터랙티브 Fe-C 상태도")
            
            st.info("💡 탄소 함량을 조정하면 해당 위치의 조직과 특성이 실시간으로 표시됩니다.")
            
            # Plotly로 인터랙티브 상태도 생성
            import plotly.graph_objects as go
            
            # 탄소 범위
            carbon_range = [0, 0.022, 0.77, 2.11, 4.3, 6.67]
            
            # A₃선 (근사)
            c_a3 = [c for c in range(0, 78, 1)]
            t_a3 = [910 - 203 * (c/100)**0.5 for c in c_a3]
            
            fig_interactive = go.Figure()
            
            # A₃선
            fig_interactive.add_trace(go.Scatter(
                x=[c/100 for c in c_a3],
                y=t_a3,
                mode='lines',
                name='A₃ 선',
                line=dict(color='red', width=3)
            ))
            
            # A₁선 (수평)
            fig_interactive.add_trace(go.Scatter(
                x=[0, 2.11],
                y=[727, 727],
                mode='lines',
                name='A₁ 선 (727°C)',
                line=dict(color='blue', width=3, dash='dash')
            ))
            
            # 영역 표시
            fig_interactive.add_annotation(
                x=0.2, y=600,
                text="α (Ferrite)",
                showarrow=False,
                font=dict(size=16, color='blue')
            )
            
            fig_interactive.add_annotation(
                x=0.4, y=1000,
                text="γ (Austenite)",
                showarrow=False,
                font=dict(size=16, color='green')
            )
            
            # 냉간인발 소재 범위 표시
            fig_interactive.add_vrect(
                x0=0.15, x1=0.25,
                fillcolor="yellow", opacity=0.2,
                annotation_text="냉간인발<br>소재 범위",
                annotation_position="top left"
            )
            
            fig_interactive.update_layout(
                title="Fe-C 상태도 (단순화)",
                xaxis_title="탄소 함량 (%)",
                yaxis_title="온도 (°C)",
                height=600,
                hovermode='x unified',
                xaxis=dict(range=[0, 1.2]),
                yaxis=dict(range=[0, 1600])
            )
            
            st.plotly_chart(fig_interactive, use_container_width=True)
            
            # 슬라이더로 탄소 함량 선택
            selected_carbon = st.slider(
                "탄소 함량 선택 (%)",
                0.0, 1.0, 0.20, 0.01,
                key="interactive_carbon"
            )
            
            # 선택한 위치의 정보 표시
            selected_a3 = 910 - 203 * selected_carbon**0.5
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("선택한 탄소", f"{selected_carbon}%")
                st.metric("A₃ 온도", f"{selected_a3:.0f}°C")
            
            with col2:
                if selected_carbon < 0.77:
                    classification = "아공석강"
                    color = "blue"
                elif selected_carbon == 0.77:
                    classification = "공석강"
                    color = "green"
                else:
                    classification = "과공석강"
                    color = "red"
                
                st.metric("강의 분류", classification)
                st.metric("정규화 온도", f"{selected_a3 + 40:.0f}°C")
            
            with col3:
                pearlite_pct = min((selected_carbon / 0.77) * 100, 100)
                hardness_est = 100 + (selected_carbon * 200)
                
                st.metric("Pearlite 비율", f"{pearlite_pct:.0f}%")
                st.metric("예상 경도", f"{hardness_est:.0f} HB")
    
    # ========================================================================
    # 탭 2: 운영 매뉴얼
    # ========================================================================
    
    with tab2:
        st.header("📚 냉간인발 공정 운영 매뉴얼")
        st.markdown("**공정 순서대로 체계적으로 정리된 기술 매뉴얼** (⭐ = 우선순위 주제)")
        
        manual_section = st.selectbox(
            "공정 단계 선택",
            [
                "📋 전체 공정 개요",
                "1️⃣ 입고검사 (Incoming Inspection)",
                "2️⃣ 열처리 (Heat Treatment) ⭐",
                "3️⃣ 산세 (Pickling)",
                "4️⃣ 선단가공 (Pointing & Swaging)",
                "5️⃣ 냉간인발 (Cold Drawing) ⭐",
                "6️⃣ 교정 (Straightening)",
                "7️⃣ 절단 (Cutting)",
                "8️⃣ 검사 - ECT/UT (Inspection) ⭐",
                "9️⃣ 방청유 (Anti-rust Oil)",
                "🔟 출하검사 (Final Inspection)",
                "➕ 품질관리 (Quality Control)",
                "➕ 설비관리 (Equipment Management)"
            ]
        )
        
        if "전체 공정" in manual_section:
            st.subheader("📋 냉간인발 강관 제조 전체 공정")
            
            st.markdown("""
            ### 공정 흐름도
            
            ```
            1. 입고검사
                ↓
            2. 열처리 (Normalizing) ⭐
                ↓
            3. 산세 (Pickling)
                ↓
            4. 선단가공 (Pointing & Swaging)
                ↓
            5. 냉간인발 (Cold Drawing) ⭐
                ↓
            6. 교정 (Straightening)
                ↓
            7. 절단 (Cutting)
                ↓
            8. 검사 (ECT/UT) ⭐
                ↓
            9. 방청유 (Anti-rust Oil)
                ↓
            10. 출하검사 (Final Inspection)
            ```
            
            ### 주요 공정 설명
            
            | 공정 | 목적 | 주요 설비 | 품질 기준 |
            |------|------|-----------|----------|
            | 입고검사 | 소재 검증 | 측정 장비 | 밀시트 확인 |
            | 열처리 | 조직 개선 | Heat Treatment Furnace | 경도 120-150 HB |
            | 산세 | 스케일 제거 | Pickling Line | 표면 청결 |
            | 선단가공 | 인발 준비 | Pointing M/C | 각도 15-30° |
            | 냉간인발 | 치수 가공 | Draw Bench | Cpk ≥ 1.33 |
            | 교정 | 진직도 확보 | Straightener | ≤ 1mm/m |
            | 절단 | 길이 가공 | Cutting M/C | ±0.5mm |
            | 검사 | 결함 검출 | ECT/UT | AQL 기준 |
            | 방청유 | 부식 방지 | Oil Tank | 피막 형성 |
            | 출하검사 | 최종 확인 | 측정 장비 | 100% 검사 |
            """)
        
        elif "Fe-C" in manual_section or "입고검사" in manual_section:
            st.subheader("🔄 냉간인발 공정 운영 루프")
            
            st.markdown("""
            ### 폐루프 운영 구조
            
            ```
            [1단계] 조건 설정
                ├─ 인발속도 (m/min)
                ├─ 감량율 (%)
                ├─ 윤활제 (종류/농도)
                └─ 다이스 (치수/마모상태)
                      ↓
            [2단계] 인발 작업
                ├─ 실시간 모니터링
                ├─ 하중/장력 확인
                └─ 표면 육안검사
                      ↓
            [3단계] 검사 실시
                ├─ ECT (와전류탐상)
                └─ UT (초음파탐상)
                      ↓
            [4단계] 결함 판정
                ├─ 표면 결함 → [5A]
                ├─ 내부 결함 → [5B]
                └─ 치수 불량 → [5C]
                      ↓
            [5단계] 조치 실행
                ├─ [5A] 표면 결함 → 연삭 → 재검사
                ├─ [5B] 내부 결함 → 즉시 스크랩
                └─ [5C] 치수 불량 → 다이스 교체 → 재작업
                      ↓
            [6단계] 표준조건 업데이트
                ├─ 이상 발생 시 → 표준조건 수정
                ├─ 정상 범위 내 → 조건 유지
                └─ 개선 효과 → 신규 표준으로 등록
            ```
            """)
            
            # 공정 조건 테이블
            st.subheader("📊 공정 조건 표준")
            
            process_data = {
                '항목': ['인발속도', '감량율', '윤활제 농도', '다이스 수명', '인발 하중'],
                '정상 범위': ['15-20 m/min', '18-22%', '5-8%', '<5,000 m', '80-120 kN'],
                '주의 범위': ['12-15 or 20-22', '16-18% or 22-25%', '4-5% or 8-10%', '5,000-6,000 m', '70-80 or 120-140'],
                '조치 범위': ['<12 or >22', '<16% or >25%', '<4% or >10%', '>6,000 m', '<70 or >140'],
                '조치 내용': ['속도 재조정', '다이스 교체', '농도 조정', '즉시 교체', '원인 분석']
            }
            
            df_process = pd.DataFrame(process_data)
            st.dataframe(df_process, use_container_width=True)
            
            # 체크리스트
            st.subheader("✅ 일일 운영 체크리스트")
            
            with st.expander("작업 전 점검"):
                col1, col2 = st.columns(2)
                with col1:
                    st.checkbox("모재 품질 확인")
                    st.checkbox("다이스 상태 확인")
                    st.checkbox("윤활제 농도 측정")
                with col2:
                    st.checkbox("인발기 정렬 확인")
                    st.checkbox("ECT/UT 장비 캘리브레이션")
            
            with st.expander("작업 중 점검"):
                col1, col2 = st.columns(2)
                with col1:
                    st.number_input("매시간 인발속도 (m/min)", min_value=0.0, max_value=30.0, value=18.0)
                    st.number_input("매시간 인발 하중 (kN)", min_value=0.0, max_value=200.0, value=100.0)
                with col2:
                    st.checkbox("3시간마다 윤활제 농도 확인")
                    st.text_area("이상 발생 기록", placeholder="시간/증상/조치")
        
        elif "NDT" in manual_section:
            st.subheader("🔬 NDT 검사 운영 매뉴얼")
            
            st.markdown("""
            ### 6주 학습 로드맵
            
            NDT 검사원을 위한 체계적인 교육 프로그램입니다.
            """)
            
            # 주차별 진도
            week = st.slider("학습 주차 선택", 1, 6, 1)
            
            week_content = {
                1: {
                    'title': 'Week 1: 기초 이론 및 안전',
                    'goals': ['NDT 개념 이해', '안전 교육 완료'],
                    'theory_hours': 16,
                    'practice_hours': 8,
                    'evaluation': '필기시험 70점 이상'
                },
                2: {
                    'title': 'Week 2: ECT 기초',
                    'goals': ['프로브 조작', '표면 결함 검출'],
                    'theory_hours': 12,
                    'practice_hours': 12,
                    'evaluation': '인공결함 검출률 90% 이상'
                },
                3: {
                    'title': 'Week 3: UT 기초',
                    'goals': ['커플런트 사용', '내부 결함 검출'],
                    'theory_hours': 12,
                    'practice_hours': 12,
                    'evaluation': '인공결함 검출률 85% 이상'
                },
                4: {
                    'title': 'Week 4: 판정 및 리포트',
                    'goals': ['합/불 판정', '보고서 작성'],
                    'theory_hours': 8,
                    'practice_hours': 16,
                    'evaluation': '판정 정확도 95% 이상'
                },
                5: {
                    'title': 'Week 5: 재검 및 격리',
                    'goals': ['재검사 루프', '불량품 관리'],
                    'theory_hours': 8,
                    'practice_hours': 16,
                    'evaluation': 'Lot 추적 오류 0건'
                },
                6: {
                    'title': 'Week 6: 종합 평가',
                    'goals': ['독립 운영 능력 검증'],
                    'theory_hours': 0,
                    'practice_hours': 20,
                    'evaluation': '실기시험 95점 이상'
                }
            }
            
            content = week_content[week]
            
            st.markdown(f"### {content['title']}")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("이론 학습", f"{content['theory_hours']}시간")
            with col2:
                st.metric("실습 학습", f"{content['practice_hours']}시간")
            with col3:
                st.metric("총 학습 시간", f"{content['theory_hours'] + content['practice_hours']}시간")
            
            st.markdown("#### 학습 목표")
            for goal in content['goals']:
                st.write(f"- {goal}")
            
            st.markdown(f"#### 평가 기준")
            st.info(content['evaluation'])
            
            # 체크리스트
            st.markdown("#### 진도 체크리스트")
            
            progress = st.progress(0)
            
            checklist_items = [
                "이론 학습 완료",
                "실습 학습 완료",
                "과제 제출",
                "평가 통과"
            ]
            
            checked_count = 0
            for item in checklist_items:
                if st.checkbox(item, key=f"week{week}_{item}"):
                    checked_count += 1
            
            progress.progress(checked_count / len(checklist_items))
            
            if checked_count == len(checklist_items):
                st.success(f"✅ Week {week} 완료!")
        
        else:  # PPC
            st.subheader("📊 생산계획통제(PPC) 전략")
            
            st.markdown("""
            ### 실시간 생산 현황 모니터링
            
            현장 데이터를 입력하여 즉시 실행 가능한 운영 지침을 확인하세요.
            """)
            
            # WIP 관리
            st.markdown("#### 📦 WIP (재공품) 관리")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                wip_days = st.number_input("WIP 일수 (현재)", min_value=0.0, max_value=30.0, value=7.5, step=0.5)
            
            with col2:
                wip_target = st.number_input("WIP 일수 (목표)", min_value=0.0, max_value=30.0, value=5.0, step=0.5)
            
            with col3:
                wip_reduction = ((wip_days - wip_target) / wip_days * 100) if wip_days > 0 else 0
                st.metric("목표 감축률", f"{wip_reduction:.1f}%", delta=f"{wip_target - wip_days:.1f}일")
            
            # 공정별 WIP
            st.markdown("##### 공정별 재고 현황")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                heat_wip = st.number_input("열처리 대기 (톤)", min_value=0.0, max_value=20.0, value=6.5)
                heat_limit = st.number_input("열처리 상한 (톤)", min_value=0.0, max_value=20.0, value=7.0)
                
                if heat_wip >= heat_limit:
                    st.error("🔴 초과: 입고 일시 중단 필요")
                elif heat_wip >= heat_limit * 0.8:
                    st.warning("🟡 주의: 열처리 우선 투입")
                else:
                    st.success("🟢 정상")
            
            with col2:
                draw_wip = st.number_input("인발 대기 (톤)", min_value=0.0, max_value=10.0, value=3.2)
                draw_limit = st.number_input("인발 상한 (톤)", min_value=0.0, max_value=10.0, value=4.0)
                
                if draw_wip >= draw_limit:
                    st.error("🔴 초과: 열처리 속도 조절")
                elif draw_wip >= draw_limit * 0.8:
                    st.warning("🟡 주의: 인발 잔업 검토")
                else:
                    st.success("🟢 정상")
            
            with col3:
                inspect_wip = st.number_input("검사 대기 (개)", min_value=0, max_value=1000, value=450)
                inspect_limit = st.number_input("검사 상한 (개)", min_value=0, max_value=1000, value=500)
                
                if inspect_wip >= inspect_limit:
                    st.error("🔴 초과: 생산 일시 중단")
                elif inspect_wip >= inspect_limit * 0.8:
                    st.warning("🟡 주의: 검사 인원 증원")
                else:
                    st.success("🟢 정상")
            
            st.divider()
            
            # 납기 관리
            st.markdown("#### 📅 납기 관리")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                otd_current = st.number_input("현재 OTD (%)", min_value=0, max_value=100, value=78)
            
            with col2:
                otd_target = st.number_input("목표 OTD (%)", min_value=0, max_value=100, value=95)
            
            with col3:
                avg_lt = st.number_input("평균 리드타임 (일)", min_value=0, max_value=60, value=14)
            
            with col4:
                delay_count = st.number_input("지연 건수 (월)", min_value=0, max_value=100, value=12)
            
            # OTD 게이지 차트
            fig_otd = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=otd_current,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "정시납기율 (OTD)"},
                delta={'reference': otd_target},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [0, 70], 'color': "lightgray"},
                        {'range': [70, 90], 'color': "gray"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': otd_target
                    }
                }
            ))
            
            st.plotly_chart(fig_otd, use_container_width=True)
            
            # 개선 계획
            if otd_current < otd_target:
                gap = otd_target - otd_current
                st.markdown("##### 🎯 OTD 개선 계획")
                
                phases = [
                    {'phase': '1단계', 'weeks': '1-2주', 'target': otd_current + gap * 0.25, 'actions': '긴급 주문 처리'},
                    {'phase': '2단계', 'weeks': '3-6주', 'target': otd_current + gap * 0.5, 'actions': '생산계획 표준화'},
                    {'phase': '3단계', 'weeks': '7-10주', 'target': otd_current + gap * 0.75, 'actions': '안전재고 정책'},
                    {'phase': '4단계', 'weeks': '11-12주', 'target': otd_target, 'actions': '실시간 모니터링'}
                ]
                
                df_phases = pd.DataFrame(phases)
                st.dataframe(df_phases, use_container_width=True)
    
    # ========================================================================
    # 탭 3: 온톨로지 뷰어
    # ========================================================================
    
    with tab3:
        st.header("📊 온톨로지 데이터 뷰어")
        
        if not st.session_state.ontology_data:
            st.markdown("""
            <div class="info-box">
                ℹ️ <strong>온톨로지 파일을 업로드하세요</strong><br>
                왼쪽 사이드바에서 YAML, JSON, CSV, TXT 파일을 업로드할 수 있습니다.
            </div>
            """, unsafe_allow_html=True)
        else:
            # 파일 선택
            selected_file = st.selectbox(
                "파일 선택",
                list(st.session_state.ontology_data.keys())
            )
            
            if selected_file:
                data = st.session_state.ontology_data[selected_file]
                
                # 데이터 타입 확인
                st.markdown(f"**파일:** `{selected_file}`")
                st.markdown(f"**데이터 타입:** `{type(data).__name__}`")
                
                # 시각화 옵션
                view_mode = st.radio(
                    "표시 방식",
                    ["JSON 뷰어", "테이블 뷰어", "트리 뷰어"],
                    horizontal=True
                )
                
                if view_mode == "JSON 뷰어":
                    st.json(data)
                
                elif view_mode == "테이블 뷰어":
                    if isinstance(data, list):
                        df = pd.DataFrame(data)
                        st.dataframe(df, use_container_width=True)
                        
                        # 통계
                        st.markdown("#### 📊 데이터 통계")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("총 레코드 수", len(df))
                        with col2:
                            st.metric("컬럼 수", len(df.columns))
                        with col3:
                            st.metric("메모리 사용량", f"{df.memory_usage(deep=True).sum() / 1024:.1f} KB")
                    
                    elif isinstance(data, dict):
                        df = pd.DataFrame([data]).T
                        df.columns = ['값']
                        st.dataframe(df, use_container_width=True)
                    
                    else:
                        st.write(data)
                
                else:  # 트리 뷰어
                    st.markdown("#### 🌳 데이터 구조")
                    
                    def render_tree(data, indent=0):
                        if isinstance(data, dict):
                            for key, value in data.items():
                                if isinstance(value, (dict, list)):
                                    st.markdown(f"{'&nbsp;' * indent * 4}📁 **{key}**", unsafe_allow_html=True)
                                    render_tree(value, indent + 1)
                                else:
                                    st.markdown(f"{'&nbsp;' * indent * 4}📄 {key}: `{value}`", unsafe_allow_html=True)
                        elif isinstance(data, list):
                            for i, item in enumerate(data):
                                if isinstance(item, (dict, list)):
                                    st.markdown(f"{'&nbsp;' * indent * 4}📁 **[{i}]**", unsafe_allow_html=True)
                                    render_tree(item, indent + 1)
                                else:
                                    st.markdown(f"{'&nbsp;' * indent * 4}📄 [{i}]: `{item}`", unsafe_allow_html=True)
                    
                    render_tree(data)
                
                # 다운로드 옵션
                st.divider()
                
                col1, col2 = st.columns(2)
                
                with col1:
                    json_str = json.dumps(data, ensure_ascii=False, indent=2)
                    st.download_button(
                        "📥 JSON으로 다운로드",
                        json_str,
                        file_name=f"{Path(selected_file).stem}.json",
                        mime="application/json",
                        use_container_width=True
                    )
                
                with col2:
                    if isinstance(data, list):
                        df = pd.DataFrame(data)
                        csv = df.to_csv(index=False).encode('utf-8-sig')
                        st.download_button(
                            "📥 CSV로 다운로드",
                            csv,
                            file_name=f"{Path(selected_file).stem}.csv",
                            mime="text/csv",
                            use_container_width=True
                        )
    
    # ========================================================================
    # 탭 4: 인사이트 보고서
    # ========================================================================
    
    with tab4:
        st.header("📈 인사이트 보고서 생성")
        
        st.markdown("""
        업로드된 온톨로지 데이터와 AI 대화 이력을 기반으로 HTML 인포그래픽 보고서를 자동 생성합니다.
        
        **📋 보고서 포함 내용:**
        - 핵심 KPI (FPY, OTD, WIP, 불량률)
        - 데이터 시각화 (차트)
        - 주요 인사이트
        - 권장 조치사항
        - **AI 대화 이력** (옵션)
        - **IATF 16949/ISO 9001/14001 준수 선언**
        """)
        
        # 보고서 옵션
        st.markdown("#### 📊 보고서 옵션")
        
        col1, col2 = st.columns(2)
        
        with col1:
            include_chat = st.checkbox(
                "💬 AI 대화 이력 포함",
                value=True,
                help="보고서에 AI 대화 내용을 포함합니다 (교육 피드백용)"
            )
            
            if include_chat:
                chat_count = len(st.session_state.chat_history)
                if chat_count > 0:
                    st.info(f"📝 {chat_count}개의 대화가 포함됩니다")
                else:
                    st.warning("⚠️ 대화 이력이 없습니다")
        
        with col2:
            include_ontology_summary = st.checkbox(
                "📚 온톨로지 요약 포함",
                value=True,
                help="업로드된 온톨로지 데이터의 요약을 포함합니다"
            )
            
            if include_ontology_summary:
                ontology_count = len(st.session_state.ontology_data)
                if ontology_count > 0:
                    st.info(f"📁 {ontology_count}개의 온톨로지 파일")
                else:
                    st.warning("⚠️ 온톨로지 데이터가 없습니다")
        
        st.divider()
        
        # 보고서 설정
        with st.form("report_form"):
            st.subheader("📋 보고서 기본 정보")
            
            col1, col2 = st.columns(2)
            
            with col1:
                report_title = st.text_input("보고서 제목", value="냉간인발 파이프 공정 인사이트 보고서")
                fpv_value = st.number_input("직행률 (FPY) %", min_value=0, max_value=100, value=93)
                otd_value = st.number_input("정시납기율 (OTD) %", min_value=0, max_value=100, value=78)
            
            with col2:
                report_subtitle = st.text_input("부제", value="Factory Operation Analytics Report")
                wip_value = st.number_input("WIP 재고일수", min_value=0.0, max_value=30.0, value=7.5, step=0.5)
                defect_value = st.number_input("전체 불량률 %", min_value=0.0, max_value=20.0, value=5.2, step=0.1)
            
            insights_text = st.text_area(
                "주요 인사이트 (한 줄씩)",
                value="열처리 공정 병목 현상 관찰\n재작업률 5% 초과로 원인 분석 필요\nNDT 검사 정확도 향상 필요",
                height=100
            )
            
            actions_text = st.text_area(
                "권장 조치사항 (한 줄씩)",
                value="열처리 설비 증설 검토 (예산: 확인 필요)\n재작업 루프 표준화 및 교육 실시\nNDT 검사원 추가 교육 프로그램 운영",
                height=100
            )
            
            generate_button = st.form_submit_button("🚀 보고서 생성", use_container_width=True)
        
        if generate_button:
            with st.spinner("보고서 생성 중..."):
                # 데이터 준비
                report_data = {
                    'fpv': fpv_value,
                    'otd': otd_value,
                    'wip_days': wip_value,
                    'defect_rate': defect_value,
                    'insights': [line.strip() for line in insights_text.split('\n') if line.strip()],
                    'actions': [line.strip() for line in actions_text.split('\n') if line.strip()]
                }
                
                # 온톨로지 요약 추가
                if include_ontology_summary and st.session_state.ontology_data:
                    ontology_summary = []
                    for filename, data in st.session_state.ontology_data.items():
                        if isinstance(data, dict):
                            ontology_summary.append(f"{filename}: {len(data)} 항목")
                        elif isinstance(data, list):
                            ontology_summary.append(f"{filename}: {len(data)} 레코드")
                    report_data['ontology_summary'] = ontology_summary
                
                # 샘플 차트 데이터
                if st.session_state.ontology_data:
                    # 온톨로지 기반 차트 데이터
                    report_data['process_defect_rate'] = {
                        'Heat Treatment': 2.1,
                        'Pickling': 1.8,
                        'Cold Drawing': 4.5,
                        'Straightening': 3.2,
                        'Cutting': 1.5,
                        'Inspection': 2.3
                    }
                    
                    report_data['ontology_structure'] = [
                        {'category': '공정', 'subcategory': '열처리', 'count': 15},
                        {'category': '공정', 'subcategory': '인발', 'count': 25},
                        {'category': '검사', 'subcategory': 'ECT', 'count': 12},
                        {'category': '검사', 'subcategory': 'UT', 'count': 10},
                        {'category': '불량', 'subcategory': '표면', 'count': 18},
                        {'category': '불량', 'subcategory': '내부', 'count': 8}
                    ]
                
                report_data['kpi_values'] = {
                    'current': fpv_value,
                    'target': 98
                }
                
                # AI 대화 이력 추가
                chat_history_to_include = None
                if include_chat and st.session_state.chat_history:
                    chat_history_to_include = st.session_state.chat_history
                
                # HTML 생성
                html_report = generate_html_report(report_data, chat_history_to_include)
                
                # 저장
                report_filename = f"insight_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
                
                with open(report_filename, 'w', encoding='utf-8') as f:
                    f.write(html_report)
                
                st.success("✅ 보고서 생성 완료!")
                
                # 통계 표시
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("생성 시간", datetime.now().strftime('%H:%M:%S'))
                with col2:
                    st.metric("대화 포함", "예" if chat_history_to_include else "아니오")
                with col3:
                    st.metric("온톨로지", f"{len(st.session_state.ontology_data)}개")
                
                # 미리보기
                st.markdown("### 📄 보고서 미리보기")
                
                with st.expander("HTML 미리보기 (축소)", expanded=False):
                    st.components.v1.html(html_report, height=600, scrolling=True)
                
                # 다운로드
                st.download_button(
                    "📥 HTML 보고서 다운로드",
                    html_report,
                    file_name=report_filename,
                    mime="text/html",
                    use_container_width=True
                )

# ============================================================================
# 실행
# ============================================================================

if __name__ == "__main__":
    main()