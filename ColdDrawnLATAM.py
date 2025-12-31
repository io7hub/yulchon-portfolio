"""
════════════════════════════════════════════════════════════════════════════════
Kⁱ⁰⁷ AI+ONTOLOGY PPC_COLD DRAWN TUBE_LAUNCHER
════════════════════════════════════════════════════════════════════════════════
"""

import streamlit as st
import subprocess
import time
import webbrowser
import socket
import os

# Page config
st.set_page_config(
    page_title="Kⁱ⁰⁷ AI+ONTOLOGY PPC_COLD DRAWN TUBE_LAUNCHER",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Session state
if 'show_commands' not in st.session_state:
    st.session_state.show_commands = {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# STUNNING CSS - Professional & Beautiful
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

st.markdown("""
<style>
    /* Main background with gradient */
    .main {
        background: linear-gradient(135deg, #0a1929 0%, #1e293b 50%, #0f172a 100%);
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom header styling */
    h1 {
        background: linear-gradient(135deg, #60a5fa, #a78bfa, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        text-align: center;
        margin-bottom: 0.5rem !important;
        text-shadow: 0 0 40px rgba(96, 165, 250, 0.3);
    }
    
    /* Subheader */
    .main h2 {
        color: #93c5fd;
        font-weight: 700;
        font-size: 1.8rem !important;
        margin-top: 0.5rem !important;
    }
    
    h3 {
        color: #60a5fa;
        font-weight: 700;
    }
    
    /* Phase cards - Beautiful gradient boxes */
    div[data-testid="column"] > div {
        background: linear-gradient(135deg, 
            rgba(30, 41, 59, 0.95) 0%, 
            rgba(15, 23, 42, 0.95) 50%,
            rgba(30, 41, 59, 0.95) 100%);
        border: 2px solid transparent;
        border-radius: 1.5rem;
        padding: 2rem;
        position: relative;
        overflow: hidden;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
    }
    
    /* Animated gradient border */
    div[data-testid="column"] > div::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        border-radius: 1.5rem;
        padding: 2px;
        background: linear-gradient(135deg, #3b82f6, #8b5cf6, #ec4899, #3b82f6);
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        opacity: 0;
        transition: opacity 0.5s;
        background-size: 200% 200%;
        animation: gradientShift 3s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    div[data-testid="column"] > div:hover::before {
        opacity: 1;
    }
    
    div[data-testid="column"] > div:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 25px 60px rgba(59, 130, 246, 0.5);
    }
    
    /* Glow effect on hover */
    div[data-testid="column"] > div::after {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(59, 130, 246, 0.1) 0%, transparent 70%);
        opacity: 0;
        transition: opacity 0.5s;
    }
    
    div[data-testid="column"] > div:hover::after {
        opacity: 1;
    }
    
    /* Metrics - Beautiful stat boxes */
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(139, 92, 246, 0.1));
        border: 1px solid rgba(59, 130, 246, 0.3);
        border-radius: 1rem;
        padding: 1rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    div[data-testid="stMetric"]:hover {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.2), rgba(139, 92, 246, 0.2));
        border-color: #3b82f6;
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.3);
    }
    
    div[data-testid="stMetric"] label {
        color: #94a3b8 !important;
        font-size: 0.75rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #60a5fa !important;
        font-size: 2rem !important;
        font-weight: 900 !important;
    }
    
    /* Buttons - Gorgeous gradient buttons */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #2563eb 0%, #3b82f6 50%, #60a5fa 100%);
        color: white;
        border: none;
        border-radius: 1rem;
        padding: 0.875rem 1rem;
        font-weight: 700;
        font-size: 1.1rem;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 20px rgba(37, 99, 235, 0.4);
        position: relative;
        overflow: hidden;
        justify-content: center;    
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton > button:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #1e40af 0%, #2563eb 50%, #3b82f6 100%);
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(37, 99, 235, 0.6);
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    /* Code blocks - Terminal style */
    .stCodeBlock {
        border-radius: 0.75rem;
        border: 2px solid rgba(16, 185, 129, 0.4);
        background: rgba(15, 23, 42, 0.95) !important;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.2);
    }
    
    code {
        color: #6ee7b7 !important;
        font-family: 'Monaco', 'Menlo', monospace !important;
    }
    
    /* Captions - Feature items */
    .stMarkdown p {
        color: #cbd5e1;
        line-height: 1.8;
    }
    
    /* Success/Info boxes */
    .stSuccess, .stInfo {
        border-radius: 1rem;
        border-left: 4px solid;
        background: rgba(30, 41, 59, 0.5);
    }
    
    .stSuccess {
        border-left-color: #10b981;
        background: rgba(16, 185, 129, 0.1);
    }
    
    .stInfo {
        border-left-color: #3b82f6;
        background: rgba(59, 130, 246, 0.1);
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        border-right: 1px solid rgba(59, 130, 246, 0.2);
    }
    
    section[data-testid="stSidebar"] h3 {
        color: #60a5fa;
        font-size: 1.1rem;
        font-weight: 700;
        margin-top: 1rem;
    }
    
    /* Horizontal rules */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(59, 130, 246, 0.5), 
            transparent);
        margin: 2rem 0;
    }
    
    /* Phase emoji - Large and glowing */
    .phase-emoji {
        font-size: 4rem;
        text-align: center;
        margin: 1rem 0;
        filter: drop-shadow(0 0 20px rgba(96, 165, 250, 0.5));
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* Feature bullets - Styled */
    .feature-bullet {
        color: #cbd5e1;
        padding: 0.5rem 0;
        padding-left: 1.5rem;
        position: relative;
        font-size: 0.9rem;
        transition: all 0.3s ease;
    }
    
    .feature-bullet::before {
        content: '▸';
        position: absolute;
        left: 0;
        color: #3b82f6;
        font-weight: bold;
        font-size: 1.2rem;
    }
    
    .feature-bullet:hover {
        color: #e2e8f0;
        padding-left: 2rem;
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(15, 23, 42, 0.5);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #2563eb, #7c3aed);
    }
</style>
""", unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HEADER - Stunning gradient title
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

st.title("⚙️ Kⁱ⁰⁷ AI+ONTOLOGY PPC_COLD DRAWN TUBE")
st.markdown("<h2 style='text-align:center;color:#93c5fd;font-weight:600;'>Manufacturing Intelligence System</h2>", unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SIDEBAR - Enhanced
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

with st.sidebar:
    st.markdown("### 🎯 Quick Navigation")
    st.info("""
    **How to Use:**
    1. Select a phase from the main area
    2. Click 🚀 Launch button
    3. Copy terminal command
    4. Run in your terminal
    """)
    
    st.markdown("---")
    st.markdown("### 📊 System Status")
    st.success("✅ All Phases Ready")
    st.info("🔵 Modular Active")
    
    st.markdown("---")
    st.markdown("### 📈 Quick Stats")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Phases", "4", delta="Complete")
        st.metric("Lines", "5,083", delta="Ready")
    with col2:
        st.metric("Features", "100%", delta="Preserved")
        st.metric("Formats", "7", delta="Export")
    
    st.markdown("---")
    st.markdown("### 🏭 Contact")
    st.caption("**Kⁱ⁰⁷ Data-driven VX Strategist**")
    st.caption("📧 io7hub@naver.com")
    st.caption("🌐 https://io7hub-projects-info-projects-main-jqmujm.streamlit.app/")
    st.caption("📍 Corea del Sur")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MAIN CONTENT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

st.markdown("---")
st.markdown("## 🚀 Select Phase to Launch")
st.caption("Choose any phase to start working with the intelligent manufacturing system")


# Phase data
phases = [
    {
        'num': 1,
        'emoji': '🔧',
        'title': 'Foundation',
        'description': 'Ontology-driven architecture with process selection & data input',
        'lines': 906,
        'features_count': 6,
        'file': 'WOORIV2_Phase1_Fixed.py',
        'features': [
            'YA listo!'
        ]
    },
    {
        'num': 2,
        'emoji': '🧠',
        'title': 'Intelligence - THE CORE',
        'description': 'AI + Ontology hybrid intelligence with deep comparison analysis',
        'lines': 1457,
        'features_count': 6,
        'file': 'WOORIV2_Phase2_Complete.py',
        'features': [
            'YA listo!'
        ]
    },
    {
        'num': 3,
        'emoji': '📊',
        'title': 'Visualization',
        'description': 'Advanced visualizations with Graphviz engines and simulator',
        'lines': 1349,
        'features_count': 6,
        'file': 'WOORIV2_Phase3_Visualization.py',
        'features': [
            'YA listo!'
        ]
    },
    {
        'num': 4,
        'emoji': '📄',
        'title': 'Reports & Export',
        'description': 'Professional reporting with 7 export formats for any workflow',
        'lines': 1371,
        'features_count': 7,
        'file': 'WOORIV2_Phase4_Reports.py',
        'features': [
            'YA listo!'
        ]
    }
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PHASE CARDS - 2x2 Grid with Beautiful Styling
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Row 1
col1, col2 = st.columns(2, gap="large")

with col1:
    phase = phases[0]
    st.markdown(f"<div class='phase-emoji'>{phase['emoji']}</div>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center;color:#e2e8f0;'>Phase {phase['num']}: {phase['title']}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;color:#10b981;'>{phase['description']}</p>", unsafe_allow_html=True)
    cola, colb, colc = st.columns([1.3, 1.7, 1])
    with colb: 
        if st.button(f"🚀 Launch Phase {phase['num']}", key=f"launch_{phase['num']}", type="primary"):
            st.session_state.show_commands[phase['num']] = True  
    if st.session_state.show_commands.get(phase['num'], False):
        st.code(f"streamlit run {phase['file']}", language="bash")
        if st.button("✓ Got it", key=f"close_{phase['num']}"):
            st.session_state.show_commands[phase['num']] = False
            st.rerun()
st.markdown("<br>", unsafe_allow_html=True)

with col2:
    phase = phases[1]
    st.markdown(f"<div class='phase-emoji'>{phase['emoji']}</div>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center;color:#e2e8f0;'>Phase {phase['num']}: {phase['title']}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;color:#10b981;'>{phase['description']}</p>", unsafe_allow_html=True) 
    cola, colb, colc = st.columns([1.3, 1.7, 1])
    with colb: 
        if st.button(f"🚀 Launch Phase {phase['num']}", key=f"launch_{phase['num']}", type="primary"):
            st.session_state.show_commands[phase['num']] = True    
    if st.session_state.show_commands.get(phase['num'], False):
        st.code(f"streamlit run {phase['file']}", language="bash")
        if st.button("✓ Got it", key=f"close_{phase['num']}"):
            st.session_state.show_commands[phase['num']] = False
            st.rerun()
st.markdown("<br>", unsafe_allow_html=True)


# Row 2
col1, col2 = st.columns(2, gap="large")

with col1:
    phase = phases[2]
    st.markdown(f"<div class='phase-emoji'>{phase['emoji']}</div>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center;color:#e2e8f0;'>Phase {phase['num']}: {phase['title']}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;color:#10b981;'>{phase['description']}</p>", unsafe_allow_html=True) 
    cola, colb, colc = st.columns([1.3, 1.7, 1])
    with colb: 
        if st.button(f"🚀 Launch Phase {phase['num']}", key=f"launch_{phase['num']}", type="primary"):
            st.session_state.show_commands[phase['num']] = True   
    if st.session_state.show_commands.get(phase['num'], False):
        st.code(f"streamlit run {phase['file']}", language="bash")
        if st.button("✓ Got it", key=f"close_{phase['num']}"):
            st.session_state.show_commands[phase['num']] = False
            st.rerun()
st.markdown("<br>", unsafe_allow_html=True)

with col2:
    phase = phases[3]
    st.markdown(f"<div class='phase-emoji'>{phase['emoji']}</div>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center;color:#e2e8f0;'>Phase {phase['num']}: {phase['title']}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;color:#10b981;'>{phase['description']}</p>", unsafe_allow_html=True) 
    cola, colb, colc = st.columns([1.3, 1.7, 1])
    with colb: 
        if st.button(f"🚀 Launch Phase {phase['num']}", key=f"launch_{phase['num']}", type="primary"):
            st.session_state.show_commands[phase['num']] = True    
    if st.session_state.show_commands.get(phase['num'], False):
        st.code(f"streamlit run {phase['file']}", language="bash")
        if st.button("✓ Got it", key=f"close_{phase['num']}"):
            st.session_state.show_commands[phase['num']] = False
            st.rerun()
st.markdown("<br>", unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FOOTER - Elegant
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; margin-top: 20px; padding: 15px;'>
    <p style="font-size: 1rem;">데이터 기반 가치 전환 전략<br>
    📧 <a href='mailto:io7hub@naver.com' style='text-decoration: none;'>io7hub@naver.com</a> | <a href='https://io7hub-projects-info-projects-main-jqmujm.streamlit.app/' style='text-decoration: none;'>🌐 https://io7hub-projects-info-projects-main-jqmujm.streamlit.app/</a></br>
    This work is based on my personal field analysis of data-driven value transformation strategies.<br>
            © 2024-2025 Data-driven VX Strategist | powered by Kⁱ⁰⁷<br></p>   
</div>
""", unsafe_allow_html=True)