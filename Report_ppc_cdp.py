"""
════════════════════════════════════════════════════════════════════════════════
Kⁱ⁰⁷ MANUFACTURING INTELLIGENCE PLATFORM V2
FINAL EXECUTIVE PRESENTATION - ULTIMATE DESIGN
════════════════════════════════════════════════════════════════════════════════
Target: Korean Parent Company Executives
Focus: Visual Excellence + Technical Depth + ROI Impact
════════════════════════════════════════════════════════════════════════════════
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from PIL import Image

# Page config
st.set_page_config(
    page_title="Kⁱ⁰⁷ 경영 전략 보고서",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ultimate Professional CSS
st.markdown("""
<style>
    /* Main background */
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* 🚀 1. 폰트 적용 */
    body {
            font-family: 'Noto Sans KR', 'Inter', sans-serif;
            background-color: var(--color-light-gray);
            line-height: 1.6;
        }        

    /* Executive Title with animation */
    .executive-title {
        font-family: 'Noto Sans KR', sans-serif !important;     
        font-size: 4rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #60a5fa, #3b82f6, #1e40af);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 3rem 0 1rem 0;
        letter-spacing: -2px;
        animation: slideDown 1s ease-out;
    }
    
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-50px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Section headers with icon */
    .section-header {
        font-family: 'Noto Sans KR', sans-serif !important;      
        font-size: 2.5rem;
        font-weight: 900;
        color: #3b82f6;
        text-align: center;
        margin: 4rem 0 2rem 0;
        padding: 1.5rem;
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(30, 64, 175, 0.1));
        border-radius: 1.5rem;
        border: 3px solid #3b82f6;
        box-shadow: 0 10px 40px rgba(59, 130, 246, 0.3);
        position: relative;
    }
    
    .section-header::before {
        content: '';
        position: absolute;
        top: -3px;
        left: -3px;
        right: -3px;
        bottom: -3px;
        background: linear-gradient(135deg, #3b82f6, #1e40af);
        border-radius: 1.5rem;
        z-index: -1;
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .section-header:hover::before {
        opacity: 0.5;
    }
    
    /* Premium tech cards */
    .tech-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.95), rgba(15, 23, 42, 0.98));
        border: 3px solid transparent;
        background-clip: padding-box;
        border-radius: 2rem;
        padding: 3rem;
        margin: 2rem 0;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .tech-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        border-radius: 2rem;
        padding: 3px;
        background: linear-gradient(135deg, #3b82f6, #8b5cf6, #ec4899);
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        opacity: 0;
        transition: opacity 0.5s;
    }
    
    .tech-card:hover::before {
        opacity: 1;
    }
    
    .tech-card:hover {
        transform: translateY(-15px) scale(1.02);
        box-shadow: 0 30px 80px rgba(59, 130, 246, 0.6);
    }
    
    /* Glowing effect */
    .tech-card::after {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(59, 130, 246, 0.15) 0%, transparent 70%);
        opacity: 0;
        transition: opacity 0.5s;
    }
    
    .tech-card:hover::after {
        opacity: 1;
    }
    
    /* ROI highlight - premium gold theme */
    .roi-highlight {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.25), rgba(5, 150, 105, 0.35));
        border: 4px solid #10b981;
        border-radius: 2rem;
        padding: 3rem;
        margin: 3rem 0;
        box-shadow: 0 20px 60px rgba(16, 185, 129, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    .roi-highlight::before {
        content: '💎';
        position: absolute;
        font-size: 15rem;
        opacity: 0.05;
        right: -3rem;
        top: -3rem;
        transform: rotate(15deg);
    }
    
    /* Tech spec boxes */
    .tech-spec {
        background: rgba(15, 23, 42, 0.8);
        border: 2px solid rgba(59, 130, 246, 0.4);
        border-left: 5px solid #3b82f6;
        border-radius: 1rem;
        padding: 2rem;
        margin: 1.5rem 0;
        font-family: 'Consolas', 'Monaco', monospace;
        box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.3);
    }
    
    /* Metrics - ultra premium */
    .metric-ultra {
        font-family: 'Noto Sans KR', sans-serif !important;    
        font-size: 4.5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #3b82f6, #8b5cf6, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1;
        text-shadow: 0 0 40px rgba(59, 130, 246, 0.5);
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }
    
    .metric-roi-ultra {
        font-size: 6rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #10b981, #059669, #047857);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1;
        text-shadow: 0 0 40px rgba(16, 185, 129, 0.5);
    }
    
    .metric-label-ultra {
        font-size: 1.3rem;
        color: #94a3b8;
        text-align: center;
        font-weight: 700;
        margin-top: 1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    /* Strategic insight boxes */
    .strategic-insight {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.25), rgba(168, 85, 247, 0.3));
        border: 3px solid #8b5cf6;
        border-radius: 2rem;
        padding: 3rem;
        margin: 3rem 0;
        box-shadow: 0 20px 60px rgba(139, 92, 246, 0.4);
        position: relative;
    }
    
    .strategic-insight::before {
        content: '🎯';
        position: absolute;
        font-size: 12rem;
        opacity: 0.05;
        right: -2rem;
        bottom: -2rem;
    }
    
    /* Architecture box with grid background */
    .architecture-box {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.15), rgba(139, 92, 246, 0.15));
        border: 3px solid #3b82f6;
        border-radius: 2rem;
        padding: 3rem;
        margin: 2rem 0;
        position: relative;
        overflow: hidden;
    }
    
    .architecture-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: 
            linear-gradient(rgba(59, 130, 246, 0.1) 1px, transparent 1px),
            linear-gradient(90deg, rgba(59, 130, 246, 0.1) 1px, transparent 1px);
        background-size: 50px 50px;
        opacity: 0.3;
    }
    
    /* Problem/Solution boxes - enhanced */
    .problem-box {
        background: rgba(239, 68, 68, 0.15);
        border-left: 6px solid #ef4444;
        border-radius: 1rem;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(239, 68, 68, 0.2);
        transition: all 0.3s;
    }
    
    .problem-box:hover {
        transform: translateX(10px);
        box-shadow: 0 15px 40px rgba(239, 68, 68, 0.3);
    }
    
    .solution-box {
        background: rgba(16, 185, 129, 0.15);
        border-left: 6px solid #10b981;
        border-radius: 1rem;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(16, 185, 129, 0.2);
        transition: all 0.3s;
    }
    
    .solution-box:hover {
        transform: translateX(10px);
        box-shadow: 0 15px 40px rgba(16, 185, 129, 0.3);
    }
    
    /* Comparison table - professional */
    .comparison-table-container {
        background: rgba(15, 23, 42, 0.6);
        border-radius: 1.5rem;
        padding: 2rem;
        margin: 2rem 0;
        border: 2px solid rgba(59, 130, 246, 0.3);
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.5);
    }
    
    /* Timeline styling */
    .timeline-container {
        position: relative;
        padding: 2rem;
    }
    
    .timeline-item {
        position: relative;
        padding-left: 3rem;
        padding-bottom: 3rem;
        border-left: 4px solid #3b82f6;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -1rem;
        width: 2rem;
        height: 2rem;
        border-radius: 50%;
        background: linear-gradient(135deg, #3b82f6, #1e40af);
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.8);
    }
    
    /* CTA Button styling */
    .cta-button {
        background: linear-gradient(135deg, #10b981, #059669);
        color: white;
        padding: 1.5rem 3rem;
        border-radius: 1rem;
        font-size: 1.5rem;
        font-weight: 700;
        text-align: center;
        margin: 2rem auto;
        display: inline-block;
        box-shadow: 0 10px 30px rgba(16, 185, 129, 0.5);
        transition: all 0.3s;
        border: none;
        cursor: pointer;
    }
    
    .cta-button:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(16, 185, 129, 0.7);
    }
    
    /* Divider with gradient */
    .gradient-divider {
        height: 3px;
        background: linear-gradient(90deg, 
            transparent, 
            #3b82f6, 
            #8b5cf6, 
            #ec4899, 
            transparent);
        margin: 3rem 0;
        border-radius: 10px;
    }
    
    /* Image container */
    .image-container {
        border-radius: 1.5rem;
        overflow: hidden;
        border: 3px solid rgba(59, 130, 246, 0.3);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
        margin: 2rem 0;
        transition: all 0.3s;
    }
    
    .image-container:hover {
        transform: scale(1.02);
        box-shadow: 0 25px 70px rgba(59, 130, 246, 0.4);
        border-color: #3b82f6;
    }
</style>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# TITLE SECTION - ULTRA PREMIUM
# ════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div class="executive-title">
    🏢 LATAM 현지 자회사 경쟁력 강화 전략
</div>
<h2 style="text-align:center;color:#60a5fa;font-weight:800;font-size:2.2rem;margin-bottom:0.5rem;">
    Kⁱ⁰⁷ Manufacturing Intelligence Platform V2
</h2>
<h3 style="text-align:center;color:#94a3b8;font-weight:700;font-size:1.5rem;margin-bottom:1rem;">
    AI + Ontology + LangChain + Graphviz + 3D Simulator
</h3>
<p style="text-align:center;color:#64748b;font-size:1.2rem;margin-bottom:1rem;">
    기술적 우수성과 투자수익률의 완벽한 조화
</p>
<p style="text-align:center;color:#6ee7b7;font-size:1.1rem;font-weight:600;margin-bottom:3rem;">
    Trust Through Transparency | 신뢰할 수 있는 하이브리드 인텔리전스
</p>
""", unsafe_allow_html=True)

# Hero metrics - Ultra premium display
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style="text-align:center;padding:1.5rem;background:linear-gradient(135deg,rgba(16,185,129,0.2),rgba(5,150,105,0.3));
                border-radius:1.5rem;border:3px solid #10b981;box-shadow:0 15px 40px rgba(16,185,129,0.4);">
        <div class="metric-ultra">400%</div>
        <div class="metric-label-ultra">연간 ROI</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align:center;padding:1.5rem;background:linear-gradient(135deg,rgba(59,130,246,0.2),rgba(30,64,175,0.3));
                border-radius:1.5rem;border:3px solid #3b82f6;box-shadow:0 15px 50px rgba(59,130,246,0.4);">
        <div class="metric-ultra">90%</div>
        <div class="metric-label-ultra">분석시간 절감</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="text-align:center;padding:1.5rem;background:linear-gradient(135deg,rgba(139,92,246,0.2),rgba(124,58,237,0.3));
                border-radius:1.5rem;border:3px solid #8b5cf6;box-shadow:0 15px 50px rgba(139,92,246,0.4);">
        <div class="metric-ultra">100%</div>
        <div class="metric-label-ultra">데이터 정확도</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="text-align:center;padding:1.5rem;background:linear-gradient(135deg,rgba(236,72,153,0.2),rgba(219,39,119,0.3));
                border-radius:1.5rem;border:3px solid #ec4899;box-shadow:0 15px 50px rgba(236,72,153,0.4);">
        <div class="metric-ultra">5.7배</div>
        <div class="metric-label-ultra">의사결정 속도</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# SECTION 1: THE CHALLENGE
# ════════════════════════════════════════════════════════════════════════════

st.markdown('<div class="section-header">📊 LATAM 자회사의 현실적 과제</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="problem-box">
        <h2 style="color:#f87171;margin-top:0;font-size:2rem;font-weight:800;">
            🚨 현재 상황 (As-Is)
        </h2>
        <div style="margin-top:2rem;">
            <h3 style="color:#fca5a5;font-size:1.3rem;font-weight:700;">
                ⏰ 데이터 분석 병목
            </h3>
            <ul style="color:#e2e8f0;font-size:1.1rem;line-height:2;margin-top:1rem;">
                <li>일일 <strong style="color:#ef4444;">2+ 시간</strong> 수작업 Excel 분석</li>
                <li>현지 관리자의 <strong style="color:#ef4444;">30% 계산 오류율</strong></li>
                <li>본사 보고 <strong style="color:#ef4444;">24-48시간 지연</strong></li>
            </ul>
        </div>
        <div style="margin-top:2rem;">
            <h3 style="color:#fca5a5;font-size:1.3rem;font-weight:700;">
                ⚠️ 품질 관리 한계
            </h3>
            <ul style="color:#e2e8f0;font-size:1.1rem;line-height:2;margin-top:1rem;">
                <li>IATF 16949 준수 검증 <strong style="color:#ef4444;">수동 확인</strong></li>
                <li>불량 원인 분석 <strong style="color:#ef4444;">평균 3일 소요</strong></li>
                <li>예방적 조치 <strong style="color:#ef4444;">불가능</strong></li>
            </ul>
        </div>
        <div style="margin-top:2rem;">
            <h3 style="color:#fca5a5;font-size:1.3rem;font-weight:700;">
                📉 의사결정 지연
            </h3>
            <ul style="color:#e2e8f0;font-size:1.1rem;line-height:2;margin-top:1rem;">
                <li>평균 <strong style="color:#ef4444;">5-7일</strong> 의사결정 시간</li>
                <li>기회비용 <strong style="color:#ef4444;">연간 $180K+</strong> (1개 공장)</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="solution-box">
        <h2 style="color:#34d399;margin-top:0;font-size:2rem;font-weight:800;">
            ✅ 플랫폼 효과 (To-Be)
        </h2>
        <div style="margin-top:2rem;">
            <h3 style="color:#6ee7b7;font-size:1.3rem;font-weight:700;">
                ⚡ 실시간 인텔리전스
            </h3>
            <ul style="color:#e2e8f0;font-size:1.1rem;line-height:2;margin-top:1rem;">
                <li><strong style="color:#10b981;">11분</strong> 자동 분석 (vs 2+ 시간)</li>
                <li><strong style="color:#10b981;">0%</strong> 계산 오류 (AI + Ontology 검증)</li>
                <li><strong style="color:#10b981;">즉시</strong> 본사 대시보드 공유</li>
            </ul>
        </div>
        <div style="margin-top:2rem;">
            <h3 style="color:#6ee7b7;font-size:1.3rem;font-weight:700;">
                🎯 예측적 품질 관리
            </h3>
            <ul style="color:#e2e8f0;font-size:1.1rem;line-height:2;margin-top:1rem;">
                <li>IATF 16949 <strong style="color:#10b981;">100% 자동 검증</strong></li>
                <li>불량 원인 <strong style="color:#10b981;">3초</strong> 내 식별</li>
                <li>AI 기반 <strong style="color:#10b981;">예방 조치 제안</strong></li>
            </ul>
        </div>
        <div style="margin-top:2rem;">
            <h3 style="color:#6ee7b7;font-size:1.3rem;font-weight:700;">
                🚀 가속화된 의사결정
            </h3>
            <ul style="color:#e2e8f0;font-size:1.1rem;line-height:2;margin-top:1rem;">
                <li>평균 <strong style="color:#10b981;">1-2시간</strong> 의사결정</li>
                <li>기회비용 회수 <strong style="color:#10b981;">$180K+ 연간</strong></li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Impact visualization
st.markdown("<br><br>", unsafe_allow_html=True)

fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=('작업 시간 비교 (시간/일)', '의사결정 속도 (일)'),
    specs=[[{"type": "bar"}, {"type": "bar"}]]
)

fig.add_trace(
    go.Bar(
        x=['현재 방식', 'Kⁱ⁰⁷'],
        y=[2.5, 0.18],
        marker=dict(
            color=['#ef4444', '#10b981'],
            line=dict(color='white', width=2)
        ),
        text=['2.5시간', '11분'],
        textposition='auto',
        textfont=dict(size=14, color='white'),
        name='분석 시간'
    ),
    row=1, col=1
)

fig.add_trace(
    go.Bar(
        x=['현재 방식', 'Kⁱ⁰⁷'],
        y=[6, 0.08],
        marker=dict(
            color=['#ef4444', '#10b981'],
            line=dict(color='white', width=2)
        ),
        text=['5-7일', '1-2시간'],
        textposition='auto',
        textfont=dict(size=14, color='white'),
        name='의사결정'
    ),
    row=1, col=2
)

fig.update_layout(
    height=450,
    template='plotly_dark',
    showlegend=False,
    font=dict(size=13, color='white')
)

st.plotly_chart(fig, use_container_width=True)

st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# SECTION 2: COMPETITIVE ADVANTAGE - WITH UPLOADED IMAGE
# ════════════════════════════════════════════════════════════════════════════

st.markdown('<div class="section-header">🏆 경쟁사 대비 압도적 차별화</div>', unsafe_allow_html=True)

st.markdown("""
<div class="architecture-box">
    <h3 style="color:#60a5fa;text-align:center;font-size:2rem;font-weight:800;margin-bottom:2rem;">
        12가지 핵심 기능 비교 분석
    </h3>
    <p style="color:#e2e8f0;text-align:center;font-size:1.2rem;margin-bottom:3rem;">
        일반 MES, 범용 BI 도구, ChatGPT/Claude vs <strong style="color:#10b981;">Kⁱ⁰⁷ Platform</strong>
    </p>
</div>
""", unsafe_allow_html=True)

# Display uploaded comparison table
st.markdown('<div class="image-container">', unsafe_allow_html=True)
try:
    comparison_img = Image.open('/mnt/user-data/uploads/1766919966963_image.png')
    st.image(comparison_img, use_column_width=True, caption="경쟁사 대비 기능 비교 분석")
except Exception as e:
    # Fallback: show text-based comparison if image fails
#    st.warning("⚠️ 비교표 이미지를 불러올 수 없습니다. 텍스트 버전을 표시합니다.")
    st.markdown("""
    <table style="width:100%;border-collapse:collapse;margin:2rem 0;">
        <thead>
            <tr style="background:#1e40af;">
                <th style="padding:1rem;border:1px solid #3b82f6;color:white;">기능</th>
                <th style="padding:1rem;border:1px solid #3b82f6;color:white;">일반 MES</th>
                <th style="padding:1rem;border:1px solid #3b82f6;color:white;">범용 BI 도구</th>
                <th style="padding:1rem;border:1px solid #3b82f6;color:white;">ChatGPT/Claude</th>
                <th style="padding:1rem;border:1px solid #10b981;color:white;background:#10b981;">Kⁱ⁰⁷ Platform</th>
            </tr>
        </thead>
        <tbody style="color:#cbd5e1;">
            <tr>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);">AI 분석</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">✅</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">⚠️</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">✅</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;background:rgba(16,185,129,0.1);">✅</td>
            </tr>
            <tr>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);">도메인 특성 별 규칙/데이터구조 기반 검증</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">✅</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;background:rgba(16,185,129,0.1);">✅</td>
            </tr>
            <tr>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);">AI+ Rule Engine 하이브리드</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;background:rgba(16,185,129,0.1);">✅</td>
            </tr>
            <tr>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);">이중 AI 검증</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;background:rgba(16,185,129,0.1);">✅</td>
            </tr>
            <tr>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);">정량적 신뢰도 점수</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;background:rgba(16,185,129,0.1);">✅</td>
            </tr>
            <tr>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);">3D 시각화</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">✅</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;background:rgba(16,185,129,0.1);">✅</td>
            </tr>
            <tr>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);">다중 Graphviz 엔진</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;background:rgba(16,185,129,0.1);">✅</td>
            </tr>
            <tr>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);">맞춤형Export 포맷</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">⚠️</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">✅</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;background:rgba(16,185,129,0.1);">✅</td>
            </tr>
            <tr>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);">한/영/스 언어 지원</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">⚠️</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">✅</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">✅</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;background:rgba(16,185,129,0.1);">✅</td>
            </tr>
            <tr>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);">LangChain 통합</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;background:rgba(16,185,129,0.1);">✅</td>
            </tr>
            <tr>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);">온톨로지 엔진</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;background:rgba(16,185,129,0.1);">✅</td>
            </tr>
            <tr>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);">제조 도메인 특화</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">⚠️</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;">❌</td>
                <td style="padding:0.8rem;border:1px solid rgba(59,130,246,0.3);text-align:center;background:rgba(16,185,129,0.1);">✅</td>
            </tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Key differentiators - Premium cards
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
    <div class="tech-card" style="height:100%;">
        <div style="text-align:center;font-size:4rem;margin-bottom:1.5rem;">🎯</div>
        <h3 style="color:#3b82f6;text-align:center;font-size:1.6rem;font-weight:800;">
            핵심 차별점 1
        </h3>
        <h4 style="color:#60a5fa;text-align:center;margin-top:1.5rem;font-size:1.4rem;font-weight:700;">
            Trust Through Transparency
        </h4>
        <p style="color:#cbd5e1;text-align:center;font-size:1.1rem;line-height:2;margin-top:1.5rem;">
            AI의 "Black Box" 문제 완전 해결<br>
            <br>
            <strong style="color:#3b82f6;">AI 추천</strong><br>
            <strong style="color:#8b5cf6;">규칙 검증</strong><br>
            <strong style="color:#ec4899;">Deep Comparison</strong><br>
            <br>
            모든 결론에 <strong style="color:#10b981;">근거 제시</strong><br>
            의사결정 책임 <strong style="color:#10b981;">명확화</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="tech-card" style="height:100%;">
        <div style="text-align:center;font-size:4rem;margin-bottom:1.5rem;">🏭</div>
        <h3 style="color:#8b5cf6;text-align:center;font-size:1.6rem;font-weight:800;">
            핵심 차별점 2
        </h3>
        <h4 style="color:#a78bfa;text-align:center;margin-top:1.5rem;font-size:1.4rem;font-weight:700;">
            Deep Manufacturing Specialization
        </h4>
        <p style="color:#cbd5e1;text-align:center;font-size:1.1rem;line-height:2;margin-top:1.5rem;">
            범용 AI가 아닌
            <strong style="color:#8b5cf6;">제조업 특화 AI</strong><br>
            <br>
            ERW/Drawn Pipe 전문<br>
            IATF 16949 완전 내재화<br>
            12단계 공정 깊은 이해<br>
            <br>
            일반 ChatGPT 대비<br>
            <strong style="color:#a78bfa;">10배 높은 정확도</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="tech-card" style="height:100%;">
        <div style="text-align:center;font-size:4rem;margin-bottom:1.5rem;">✨</div>
        <h3 style="color:#10b981;text-align:center;font-size:1.6rem;font-weight:800;">
            핵심 차별점 3
        </h3>
        <h4 style="color:#34d399;text-align:center;margin-top:1.5rem;font-size:1.4rem;font-weight:700;">
            Complete End-to-End Solution
        </h4>
        <p style="color:#cbd5e1;text-align:center;font-size:1.1rem;line-height:2;margin-top:1.5rem;">
            데이터 입력부터 
            보고서 생성까지<br>
            <br>
            <strong style="color:#10b981;">All-in-One</strong><br>
            추가 도구 불필요<br>
            시스템 통합 비용 제로<br>
            <br>
            즉시 생산성 향상<br>
            <strong style="color:#34d399;">Day 1 ROI</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# SECTION 3: 5 CORE TECHNOLOGIES (Condensed but impactful)
# ════════════════════════════════════════════════════════════════════════════

st.markdown('<div class="section-header">🏗️ 5대 핵심 기술 아키텍처</div>', unsafe_allow_html=True)

st.markdown("""
<div class="architecture-box">
    <h2 style="color:#60a5fa;text-align:center;font-size:2.5rem;font-weight:900;margin-bottom:2rem;">
        Trust Through Transparency
    </h2>
    <h3 style="color:#e2e8f0;text-align:center;font-size:1.5rem;line-height:2;">
        AI + Ontology Hybrid Intelligence
    </h3>
    <p style="color:#94a3b8;text-align:center;font-size:1.2rem;margin-top:1.5rem;">
        단순한 AI 추천이 아닌, <strong style="color:#3b82f6;">규칙 기반 검증</strong>과 
        <strong style="color:#8b5cf6;">패턴 학습</strong>의 완벽한 조화
    </p>
</div>
""", unsafe_allow_html=True)

# Technology overview grid
tech_grid = [
    {
        'icon': '🤖',
        'name': 'Dual AI Engine',
        'tech': 'Claude Sonnet 4 + GPT-4',
        'value': '251 lines Deep Comparison',
        'color': '#3b82f6'
    },
    {
        'icon': '📋',
        'name': 'Manufactur-Ontology',
        'tech': 'YAML-based Rule Engine 2.0',
        'value': '106 lines Validation Logic',
        'color': '#8b5cf6'
    },
    {
        'icon': '🔗',
        'name': 'LangChain Agent',
        'tech': 'Multi-Agent Orchestration',
        'value': 'Full Automation Workflow',
        'color': '#06b6d4'
    },
    {
        'icon': '📐',
        'name': 'Graphviz Engines',
        'tech': 'dot/neato/fdp/sfdp/circo',
        'value': 'Process Visualization',
        'color': '#10b981'
    },
    {
        'icon': '🎮',
        'name': '3D Simulator',
        'tech': 'Plotly Interactive 3D',
        'value': '5-Dimension Data Viz',
        'color': '#ec4899'
    }
]

cols = st.columns(5)
for idx, tech in enumerate(tech_grid):
    with cols[idx]:
        st.markdown(f"""
        <div style="text-align:center;padding:0.6rem;background:rgba(30,41,59,0.8);
                    border:2px solid {tech['color']};border-radius:1.5rem;height:100%;
                    box-shadow:0 10px 30px rgba(0,0,0,0.3);">
            <div style="font-size:3rem;margin-bottom:1rem;">{tech['icon']}</div>
            <h4 style="color:{tech['color']};font-size:1.1rem;font-weight:700;margin-bottom:0.5rem;">
                {tech['name']}
            </h4>
            <p style="color:#cbd5e1;font-size:0.9rem;margin:0.5rem 0;">
                {tech['tech']}
            </p>
            <p style="color:#94a3b8;font-size:0.85rem;margin-top:0.5rem;">
                <strong style="color:{tech['color']};">{tech['value']}</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)

# Technology flow diagram
st.markdown("<br><br>", unsafe_allow_html=True)

fig = go.Figure(data=[go.Sankey(
    node = dict(
        pad = 20,
        thickness = 25,
        line = dict(color = "white", width = 1),
        label = [
            "생산 데이터 입력",
            "Graphviz\n공정 시각화",
            "Dual AI Analysis\n(Claude + GPT)",
            "Ontology\nRule Engine",
            "LangChain\n오케스트레이션",
            "Deep Comparison\n(AI vs Rules)",
            "3D Simulator\n인터랙티브",
            "최종 보고서\n(맞춤형포맷)"
        ],
        color = ["#64748b", "#10b981", "#3b82f6", "#8b5cf6", "#06b6d4", "#ec4899", "#f59e0b", "#34d399"]
    ),
    link = dict(
        source = [0, 0, 1, 2, 3, 4, 4, 5, 5],
        target = [1, 4, 4, 4, 4, 5, 6, 6, 7],
        value = [100, 100, 80, 100, 100, 100, 50, 100, 100],
        color = ["rgba(59,130,246,0.3)"] * 9
    )
)])

fig.update_layout(
    title={
        'text': "데이터 입력부터 최종 보고서까지의 완전 자동화 흐름",
        'font': {'size': 18, 'color': '#60a5fa'}
    },
    font_size=13,
    template="plotly_dark",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# SECTION 4: ROI ANALYSIS - PREMIUM
# ════════════════════════════════════════════════════════════════════════════

st.markdown('<div class="section-header">💰 투자수익률 (ROI) 상세 분석</div>', unsafe_allow_html=True)

st.markdown("""
<div class="roi-highlight">
    <h2 style="font-family: 'Noto Sans KR', 'Inter', sans-serif;color:#10b981;text-align:center;font-size:3rem;margin:0;font-weight:900;">
        연간 ROI: 400% | 회수 기간: 3개월
    </h2>
    <p style="color:#6ee7b7;text-align:center;font-size:1.5rem;margin-top:1.5rem;font-weight:600;">
        단일 공장 기준 (월 생산량: 1,000톤 파이프)
    </p>
</div>
""", unsafe_allow_html=True)

# ROI calculation
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="tech-card">
        <h3 style="color:#ef4444;text-align:center;font-size:1.8rem;font-weight:800;">📉 투자 비용</h3>
        <table style="width:100%;color:#cbd5e1;margin-top:2rem;font-size:1.1rem;">
            <tr style="border-bottom:2px solid rgba(59,130,246,0.3);">
                <td style="padding:1rem;"><strong>항목</strong></td>
                <td style="padding:1rem;text-align:right;"><strong>금액 (연간)</strong></td>
            </tr>
            <tr style="border-bottom:1px solid rgba(59,130,246,0.2);">
                <td style="padding:1rem;">초기 구축<br><span style="color:#0f172a;">·</span></td>
                <td style="padding:1rem;text-align:right;color:#f87171;font-weight:700;">$3,000</td>
            </tr>
            <tr style="border-bottom:1px solid rgba(59,130,246,0.2);">
                <td style="padding:1rem;">AI API 비용<br><span style="color:#0f172a;">·</span></td>
                <td style="padding:1rem;text-align:right;color:#f87171;font-weight:700;">$2,400</td>
            </tr>
            <tr style="border-bottom:1px solid rgba(59,130,246,0.2);">
                <td style="padding:1rem;">유지보수/업데이트<br><span style="color:#0f172a;">·</span></td>
                <td style="padding:1rem;text-align:right;color:#f87171;font-weight:700;">$1,200</td>
            </tr>
            <tr style="border-bottom:1px solid rgba(59,130,246,0.2);">
                <td style="padding:1rem;">교육/지원<br><span style="color:#0f172a;">·</span></td>
                <td style="padding:1rem;text-align:right;color:#f87171;font-weight:700;">$800</td>
            </tr>
            <tr style="background:rgba(239,68,68,0.15);">
                <td style="padding:1.2rem;"><strong style="font-size:1.2rem;">총 투자</strong></td>
                <td style="padding:1.2rem;text-align:right;color:#ef4444;font-size:1.5rem;font-weight:900;">
                    $7,400
                </td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="tech-card">
        <h3 style="color:#10b981;text-align:center;font-size:1.8rem;font-weight:800;">📈 연간 효익</h3>
        <table style="width:100%;color:#cbd5e1;margin-top:2rem;font-size:1.1rem;">
            <tr style="border-bottom:2px solid rgba(59,130,246,0.3);">
                <td style="padding:1rem;"><strong>항목</strong></td>
                <td style="padding:1rem;text-align:right;"><strong>금액 (연간)</strong></td>
            </tr>
            <tr style="border-bottom:1px solid rgba(59,130,246,0.2);">
                <td style="padding:1rem;">분석 시간 절감<br><small style="color:#94a3b8;">(2hrs → 11min)</small></td>
                <td style="padding:1rem;text-align:right;color:#34d399;font-weight:700;">$8,400</td>
            </tr>
            <tr style="border-bottom:1px solid rgba(59,130,246,0.2);">
                <td style="padding:1rem;">불량률 감소<br><small style="color:#94a3b8;">(5% → 2%)</small></td>
                <td style="padding:1rem;text-align:right;color:#34d399;font-weight:700;">$12,000</td>
            </tr>
            <tr style="border-bottom:1px solid rgba(59,130,246,0.2);">
                <td style="padding:1rem;">의사결정 가속<br><small style="color:#94a3b8;">(기회비용)</small></td>
                <td style="padding:1rem;text-align:right;color:#34d399;font-weight:700;">$6,000</td>
            </tr>
            <tr style="border-bottom:1px solid rgba(59,130,246,0.2);">
                <td style="padding:1rem;">감사 대응 효율<br><small style="color:#94a3b8;">(95% 절감)</small></td>
                <td style="padding:1rem;text-align:right;color:#34d399;font-weight:700;">$3,600</td>
            </tr>
            <tr style="background:rgba(16,185,129,0.15);">
                <td style="padding:1.2rem;"><strong style="font-size:1.2rem;">총 효익</strong></td>
                <td style="padding:1.2rem;text-align:right;color:#10b981;font-size:1.5rem;font-weight:900;">
                    $30,000
                </td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ROI Summary
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="text-align:center;padding:3rem;background:linear-gradient(135deg,rgba(59,130,246,0.2),rgba(30,64,175,0.3));
                border:3px solid #3b82f6;border-radius:1.5rem;box-shadow:0 20px 60px rgba(59,130,246,0.5);">
        <div style="font-size:4rem;font-weight:900;color:#3b82f6;">
            $22,600
        </div>
        <div style="color:#93c5fd;font-size:1.3rem;margin-top:1rem;font-weight:700;">
            연간 순이익
        </div>
        <div style="color:#64748b;font-size:1rem;margin-top:0.5rem;">
            ($30,000 - $7,400)
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align:center;padding:3rem;background:linear-gradient(135deg,rgba(16,185,129,0.2),rgba(5,150,105,0.3));
                border:3px solid #10b981;border-radius:1.5rem;box-shadow:0 20px 60px rgba(16,185,129,0.5);">
        <div style="font-size:4rem;font-weight:900;color:#10b981;">
            400%
        </div>
        <div style="color:#6ee7b7;font-size:1.3rem;margin-top:1rem;font-weight:700;">
            ROI
        </div>
        <div style="color:#64748b;font-size:1rem;margin-top:0.5rem;">
            ($22,600 / $7,400 × 100%)
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="text-align:center;padding:3rem;background:linear-gradient(135deg,rgba(139,92,246,0.2),rgba(124,58,237,0.3));
                border:3px solid #8b5cf6;border-radius:1.5rem;box-shadow:0 20px 60px rgba(139,92,246,0.5);">
        <div style="font-size:4rem;font-weight:900;color:#8b5cf6;">
            3개월
        </div>
        <div style="color:#c4b5fd;font-size:1.3rem;margin-top:1rem;font-weight:700;">
            회수 기간
        </div>
        <div style="color:#64748b;font-size:1rem;margin-top:0.5rem;">
            (Payback Period)
        </div>
    </div>
    """, unsafe_allow_html=True)

# Waterfall chart
st.markdown("<br><br>", unsafe_allow_html=True)

fig = go.Figure(go.Waterfall(
    name = "ROI",
    orientation = "v",
    measure = ["relative", "relative", "relative", "relative", "relative", "total"],
    x = [
        "초기 투자",
        "시간 절감",
        "불량 감소",
        "의사결정",
        "감사 효율",
        "<b>순이익</b>"
    ],
    textposition = "outside",
    text = ["-$7,400", "+$8,400", "+$12,000", "+$6,000", "+$3,600", "$22,600"],
    y = [-7400, 8400, 12000, 6000, 3600, 0],
    connector = {"line":{"color":"rgb(63, 63, 63)", "width": 3}},
    decreasing = {"marker":{"color":"#ef4444", "line":{"color":"white", "width":2}}},
    increasing = {"marker":{"color":"#10b981", "line":{"color":"white", "width":2}}},
    totals = {"marker":{"color":"#3b82f6", "line":{"color":"#1e40af", "width":4}}}
))

fig.update_layout(
    title={
        'text': "연간 ROI 워터폴 분석 (단일 공장 기준)",
        'font': {'size': 20, 'color': '#60a5fa'}
    },
    template="plotly_dark",
    height=550,
    showlegend=False,
    font=dict(size=14)
)

st.plotly_chart(fig, use_container_width=True)

# Multi-plant scaling
st.markdown("""
<div class="strategic-insight">
    <h2 style="color:#a78bfa;font-size:2.2rem;text-align:center;margin-top:0;font-weight:900;">
        🏭 멀티 플랜트 스케일링 효과
    </h2>
    <p style="color:#e2e8f0;text-align:center;font-size:1.3rem;margin:1.5rem 0;">
        LATAM 3개 자회사 동시 운영 시 시너지
    </p>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;margin-top:3rem;">
        <div style="text-align:center;padding:2rem;background:rgba(139,92,246,0.1);
                    border-radius:1rem;border:2px solid #8b5cf6;">
            <div style="font-size:3.5rem;font-weight:900;color:#8b5cf6;">3배</div>
            <div style="color:#c4b5fd;margin-top:1rem;font-size:1.2rem;font-weight:600;">총 절감액</div>
            <div style="color:#94a3b8;font-size:1.1rem;margin-top:0.5rem;">$67,800/년</div>
        </div>
        <div style="text-align:center;padding:2rem;background:rgba(139,92,246,0.1);
                    border-radius:1rem;border:2px solid #8b5cf6;">
            <div style="font-size:3.5rem;font-weight:900;color:#8b5cf6;">15%</div>
            <div style="color:#c4b5fd;margin-top:1rem;font-size:1.2rem;font-weight:600;">단가 할인</div>
            <div style="color:#94a3b8;font-size:1.1rem;margin-top:0.5rem;">볼륨 라이센스</div>
        </div>
        <div style="text-align:center;padding:2rem;background:rgba(139,92,246,0.1);
                    border-radius:1rem;border:2px solid #8b5cf6;">
            <div style="font-size:3.5rem;font-weight:900;color:#8b5cf6;">1주</div>
            <div style="color:#c4b5fd;margin-top:1rem;font-size:1.2rem;font-weight:600;">배포 시간</div>
            <div style="color:#94a3b8;font-size:1.1rem;margin-top:0.5rem;">공장당 (2차부터)</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# SECTION 5: STRATEGIC ROADMAP
# ════════════════════════════════════════════════════════════════════════════

st.markdown('<div class="section-header">🎯 전략적 실행 로드맵</div>', unsafe_allow_html=True)

st.markdown("""
<div class="strategic-insight">
    <h2 style="color:#60a5fa;font-size:2.2rem;margin-top:0;text-align:center;font-weight:900;">
        📋 단계별 도입 계획 (3-6-12개월)
    </h2>
</div>
""", unsafe_allow_html=True)

# Timeline
phases_roadmap = [
    {
        'phase': 'Phase 1: Pilot',
        'duration': '1-3개월',
        'target': 'Yulchon México',
        'goals': ['단일 공장 PoC', 'ROI 400% 검증', '성공 사례 문서화'],
        'result': '월 $1,900 절감 실증',
        'color': '#10b981'
    },
    {
        'phase': 'Phase 2: Scale',
        'duration': '4-6개월',
        'target': 'LATAM 3개 공장',
        'goals': ['멕시코/브라질/콜롬비아', '통합 대시보드', 'Best Practice 표준화'],
        'result': '연 $67,800 절감',
        'color': '#3b82f6'
    },
    {
        'phase': 'Phase 3: Expand',
        'duration': '7-12개월',
        'target': 'Tier 2 협력사 50개',
        'goals': ['Supply Chain 최적화', 'Regional Hub', 'SaaS 모델 검토'],
        'result': '시장 점유율 15% 상승',
        'color': '#8b5cf6'
    }
]

for phase_info in phases_roadmap:
    st.markdown(f"""
    <div class="solution-box">
        <h3 style="color:{phase_info['color']};margin-top:0;font-size:1.8rem;font-weight:800;">
            ✅ {phase_info['phase']} ({phase_info['duration']})
        </h3>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-top:2rem;">
            <div>
                <h4 style="color:#6ee7b7;font-size:1.3rem;font-weight:700;">🎯 타겟</h4>
                <p style="color:#e2e8f0;font-size:1.2rem;margin-top:1rem;">
                    <strong style="color:{phase_info['color']};">{phase_info['target']}</strong>
                </p>
                <h4 style="color:#6ee7b7;font-size:1.3rem;font-weight:700;margin-top:2rem;">📋 주요 목표</h4>
                <ul style="color:#cbd5e1;font-size:1.1rem;line-height:2;margin-top:1rem;">
    """, unsafe_allow_html=True)
    
    for goal in phase_info['goals']:
        st.markdown(f"<li>{goal}</li>", unsafe_allow_html=True)
    
    st.markdown(f"""
                </ul>
            </div>
            <div>
                <div style="padding:2rem;background:rgba(16,185,129,0.1);
                            border-radius:1rem;border-left:5px solid #10b981;">
                    <h4 style="color:#34d399;font-size:1.3rem;font-weight:800;margin:0;">
                        💎 예상 결과
                    </h4>
                    <p style="color:#e2e8f0;font-size:1.3rem;margin-top:1.5rem;font-weight:600;">
                        {phase_info['result']}
                    </p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Timeline Gantt
st.markdown("<br><br>", unsafe_allow_html=True)

fig = go.Figure()

fig.add_trace(go.Bar(
    y=['Phase 3: Expand', 'Phase 2: Scale', 'Phase 1: Pilot'],
    x=[6, 3, 3],
    orientation='h',
    marker=dict(
        color=['#8b5cf6', '#3b82f6', '#10b981'],
        line=dict(color='white', width=2)
    ),
    text=['6개월', '3개월', '3개월'],
    textposition='inside',
    textfont=dict(size=16, color='white'),
    name=''
))

fig.update_layout(
    title={
        'text': '12개월 배포 타임라인',
        'font': {'size': 20, 'color': '#60a5fa'}
    },
    xaxis_title='개월',
    yaxis_title='',
    template='plotly_dark',
    height=350,
    showlegend=False,
    font=dict(size=14)
)

st.plotly_chart(fig, use_container_width=True)

st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# FINAL CTA
# ════════════════════════════════════════════════════════════════════════════

st.markdown('<div class="section-header">🚀 즉시 실행 계획</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
    <div class="tech-card">
        <h3 style="color:#60a5fa;text-align:center;font-size:1.8rem;font-weight:800;">Week 1</h3>
        <h4 style="color:#93c5fd;text-align:center;margin-top:1.5rem;font-size:1.3rem;">
            기술 검토 및 승인
        </h4>
        <ul style="color:#cbd5e1;font-size:1.1rem;line-height:2;margin-top:2rem;">
            <li>CTO/본부장 데모 세션</li>
            <li>기술 스펙 상세 검토</li>
            <li>보안/규정 준수 확인</li>
            <li>예산 승인 ($7,400)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="tech-card">
        <h3 style="color:#8b5cf6;text-align:center;font-size:1.8rem;font-weight:800;">Week 2-3</h3>
        <h4 style="color:#c4b5fd;text-align:center;margin-top:1.5rem;font-size:1.3rem;">
            Pilot 구축 및 가동
        </h4>
        <ul style="color:#cbd5e1;font-size:1.1rem;line-height:2;margin-top:2rem;">
            <li>Yulchon México 선정</li>
            <li>시스템 설치 (1일)</li>
            <li>관리자 교육 (2시간)</li>
            <li>First Run (11분 분석)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="tech-card">
        <h3 style="color:#10b981;text-align:center;font-size:1.8rem;font-weight:800;">Month 2-3</h3>
        <h4 style="color:#6ee7b7;text-align:center;margin-top:1.5rem;font-size:1.3rem;">
            성과 측정 및 확대
        </h4>
        <ul style="color:#cbd5e1;font-size:1.1rem;line-height:2;margin-top:2rem;">
            <li>90일 데이터 수집</li>
            <li>ROI 검증 (400%)</li>
            <li>확대 의사결정</li>
            <li>Phase 2 착수</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Final CTA
st.markdown("""
<div class="roi-highlight" style="text-align:center;padding:4rem;margin-top:3rem;">
    <h2 style="font-family: 'Noto Sans KR', 'Inter', sans-serif;color:#10b981;font-size:3rem;margin:0;font-weight:900;">
        💎 LATAM 제조업 경쟁력을 다음 단계로
    </h2>
    <p style="color:#e2e8f0;font-size:1.5rem;margin:2rem 0;line-height:2;">
        AI + Ontology 하이브리드 인텔리전스로<br>
        <strong style="color:#34d399;">본사와 현지의 완벽한 동기화</strong>를 실현하십시오
    </p>
    <div style="margin-top:3rem;padding:3rem;background:rgba(59,130,246,0.15);
                border-radius:1.5rem;border:3px solid #3b82f6;">
        <h3 style="color:#60a5fa;font-size:2.2rem;margin:0;font-weight:900;">
            📧 Contact
        </h3>
        <p style="color:#93c5fd;font-size:1.5rem;margin-top:1.5rem;font-weight:600;">
            <a href="mailto:io7hub@naver.com" style="text-decoration: none;">io7hub@naver.com</a>
        </p>
        <p style="color:#93c5fd;font-size:1.3rem;margin-top:1rem;">
            🌐 <a href="https://io7hub-projects-info-projects-main-jqmujm.streamlit.app/" style="text-decoration: none;">https://io7hub-projects-info-projects-main-jqmujm.streamlit.app/</a> | 📱 Demo 요청 즉시 가능
        </p>
    </div>
</div>
""", unsafe_allow_html=True)



st.markdown("---")

# Summary metrics footer
st.markdown("### 📊 Executive Summary - Final Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("연간 ROI", "400%", "+250% vs 업계평균")
with col2:
    st.metric("회수 기간", "3개월", "-9개월 vs 일반")
with col3:
    st.metric("시간 절감", "90%", "2시간 → 11분")
with col4:
    st.metric("의사결정", "5.7배", "7일 → 1-2시간")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.5, 3, 0.5])

with col2:
    st.markdown("""
    <div style="text-align:center;padding:3rem;">
        <h2 style="background:linear-gradient(135deg,#60a5fa,#8b5cf6,#34d399);
                   -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                   font-size:2rem;margin-bottom:1.5rem;font-weight:700;">
            ⚙️ Kⁱ⁰⁷ Manufacturing Intelligence
        </h2>
        <p style="color:#93c5fd;font-size:1.2rem;font-weight:700;margin-top:1rem;">
            Trust Through Transparency
        </p>
        <p style="color:#64748b;font-size:1.1rem;margin-top:1.5rem;">
            © 2025 Data-driven VX Strategist | powered by Kⁱ⁰⁷
        </p>
    </div>
    """, unsafe_allow_html=True)