"""
════════════════════════════════════════════════════════════════════════════════
WOORI LATAM AI PLATFORM V2 - INFOGRAPHIC FOR LATAM MANUFACTURING MANAGERS
Targeting: Pipe Production Managers in LATAM (Drawn Pipe / ERW Tube)
════════════════════════════════════════════════════════════════════════════════
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Kⁱ⁰⁷ Platform - Para Gerentes de Producción",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS for infographic style
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #0a1929 0%, #1e293b 100%);
    }
    
    .big-title {
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #60a5fa, #34d399);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 2rem 0;
    }
    
    .section-title {
        font-size: 2rem;
        font-weight: 800;
        color: #60a5fa;
        text-align: center;
        margin: 2rem 0 1rem 0;
        border-bottom: 3px solid #3b82f6;
        padding-bottom: 0.5rem;
    }
    
    .highlight-box {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.2), rgba(16, 185, 129, 0.2));
        border: 2px solid #3b82f6;
        border-radius: 1.5rem;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 10px 40px rgba(59, 130, 246, 0.3);
    }
    
    .problem-box {
        background: rgba(239, 68, 68, 0.1);
        border-left: 5px solid #ef4444;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 0.5rem;
    }
    
    .solution-box {
        background: rgba(16, 185, 129, 0.1);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 0.5rem;
    }
    
    .stat-big {
        font-size: 4rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stat-label {
        font-size: 1.2rem;
        color: #94a3b8;
        text-align: center;
        font-weight: 600;
    }
    
    .feature-card {
        background: rgba(30, 41, 59, 0.6);
        border: 2px solid rgba(59, 130, 246, 0.3);
        border-radius: 1rem;
        padding: 2.0rem;
        margin: 1rem 0;
        transition: all 0.3s;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(59, 130, 246, 0.4);
        border-color: #3b82f6;
    }
    
    .timeline-item {
        position: relative;
        padding-left: 2rem;
        padding-bottom: 2rem;
        border-left: 3px solid #3b82f6;
    }
    
    .timeline-item::before {
        content: '●';
        position: absolute;
        left: -0.65rem;
        color: #3b82f6;
        font-size: 1.5rem;
    }
            
    /* Metrics styling */
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.15), rgba(139, 92, 246, 0.15));
        border: 2px solid rgba(59, 130, 246, 0.4);
        border-radius: 1rem;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    div[data-testid="stMetric"]:hover {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.25), rgba(139, 92, 246, 0.25));
        transform: scale(1.05);
        box-shadow: 0 10px 30px rgba(59, 130, 246, 0.4);
    }
    
    div[data-testid="stMetric"] label {
        color: #94a3b8 !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #60a5fa !important;
        font-size: 3rem !important;
        font-weight: 900 !important;
    }        
</style>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# TITLE SECTION
# ════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div class="big-title">
    🏭 Su Día Cambiará Hoy
</div>
<h2 style="text-align:center;color:#93c5fd;font-weight:600;font-size:1.8rem;">
    De 2 Horas de Excel → 11 Minutos con IA
</h2>
<p style="text-align:center;color:#64748b;font-size:1.2rem;margin-bottom:3rem;">
    Para Gerentes de Producción de Tubería en LATAM
</p>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# SECTION 1: YOUR DAILY STRUGGLE
# ════════════════════════════════════════════════════════════════════════════

st.markdown('<div class="section-title">😓 Su Realidad Diaria</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="problem-box">
        <h3 style="color:#f87171;margin-top:0;">🕐 7:00 AM - Turno Nocturno</h3>
        <p style="color:#cbd5e1;font-size:1.1rem;line-height:1.8;">
        • Revisar reportes en papel del turno<br>
        • ¿Cuántos tubos defectuosos?<br>
        • ¿Por qué falló la soldadura otra vez?<br>
        • Llamar al operador: "¿Qué pasó?"
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="problem-box">
        <h3 style="color:#f87171;margin-top:0;">📊 9:00 AM - Excel</h3>
        <p style="color:#cbd5e1;font-size:1.1rem;line-height:1.8;">
        • Abrir 5 archivos Excel diferentes<br>
        • Copiar datos manualmente<br>
        • Calcular KPIs a mano<br>
        • ¿Este número está bien? 🤔
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="problem-box">
        <h3 style="color:#f87171;margin-top:0;">📞 11:00 AM - Jefe Llamando</h3>
        <p style="color:#cbd5e1;font-size:1.1rem;line-height:1.8;">
        • "¿Por qué bajó la producción?"<br>
        • "Necesito el reporte AHORA"<br>
        • Todavía calculando en Excel...<br>
        • Cliente quejándose de calidad
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="problem-box">
        <h3 style="color:#f87171;margin-top:0;">😰 2:00 PM - Auditoría</h3>
        <p style="color:#cbd5e1;font-size:1.1rem;line-height:1.8;">
        • "¿Dónde están los datos de ayer?"<br>
        • Buscar en cuadernos...<br>
        • ¿Cumplimos IATF 16949?<br>
        • Rezar que todo esté en orden 🙏
        </p>
    </div>
    """, unsafe_allow_html=True)

# Big impact stats
st.markdown("### 📉 El Costo de Este Sistema")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Tiempo Perdido", "2+ hrs", "análisis diario en Excel", delta_color="inverse")
with col2:
    st.metric("Errores", "30%", "en cálculo manual", delta_color="inverse")
with col3:
    st.metric("Decisiones Estratégicas", "0 hrs", "para mejoras", delta_color="inverse")

st.markdown("---")
# ════════════════════════════════════════════════════════════════════════════
# SECTION 2: THE SOLUTION
# ════════════════════════════════════════════════════════════════════════════

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<div class="section-title">✨ La Solución: Kⁱ⁰⁷ Platform</div>', unsafe_allow_html=True)

st.markdown("""
<div class="highlight-box">
    <h2 style="color:#60a5fa;text-align:center;font-size:2.5rem;margin:0;">
        🤖 IA + 📋 Normas = 💎 Decisiones Perfectas
    </h2>
    <p style="color:#e2e8f0;text-align:center;font-size:1.3rem;margin-top:1rem;">
        Inteligencia Artificial que ENTIENDE sus normas de manufactura
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="solution-box">
        <h3 style="color:#34d399;margin-top:0;">🕐 7:05 AM - 5 Minutos Después</h3>
        <p style="color:#cbd5e1;font-size:1.1rem;line-height:1.8;">
        ✅ Todos los datos del turno cargados<br>
        ✅ IA analizó automáticamente<br>
        ✅ Reporte completo listo<br>
        ✅ "Soldadura falló: temperatura -15°C"
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="solution-box">
        <h3 style="color:#34d399;margin-top:0;">📊 7:10 AM - Listo para Café</h3>
        <p style="color:#cbd5e1;font-size:1.1rem;line-height:1.8;">
        ✅ KPIs calculados (100% precisión)<br>
        ✅ Gráficas 3D generadas<br>
        ✅ Comparación IA vs Normas<br>
        ✅ Ya puede tomar su café ☕
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="solution-box">
        <h3 style="color:#34d399;margin-top:0;">📞 7:15 AM - Jefe Impresionado</h3>
        <p style="color:#cbd5e1;font-size:1.1rem;line-height:1.8;">
        ✅ Enviar reporte por WhatsApp (PDF)<br>
        ✅ "¡Excelente trabajo! 👏"<br>
        ✅ Cliente recibe datos en tiempo real<br>
        ✅ Usted es el héroe del día 🦸
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="solution-box">
        <h3 style="color:#34d399;margin-top:0;">😊 7:20 AM - Tiempo Libre</h3>
        <p style="color:#cbd5e1;font-size:1.1rem;line-height:1.8;">
        ✅ Auditoría preparada automáticamente<br>
        ✅ Todo cumple IATF 16949<br>
        ✅ Datos trazables 100%<br>
        ✅ Planear mejoras del proceso 🚀
        </p>
    </div>
    """, unsafe_allow_html=True)

# Impact comparison
st.markdown("### 🎯 El Impacto")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Análisis completo con IA", "11 min", "vs 2+ horas", delta_color="normal")
with col2:
    st.metric("Errores de cálculo", "0%", "vs 30%", delta_color="normal")
with col3:
    st.metric("Tiempo ahorrado para mejoras", "90%", "ahorrado", delta_color="normal")

st.markdown("---")

# ════════════════════════════════════════════════════════════════════════════
# SECTION 3: HOW IT WORKS
# ════════════════════════════════════════════════════════════════════════════

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<div class="section-title">⚙️ Cómo Funciona (Simple)</div>', unsafe_allow_html=True)

# Timeline
st.markdown("""
<div class="timeline-item">
    <h3 style="color:#60a5fa;">1️⃣ Paso 1: Ingresa Datos (2 minutos)</h3>
    <p style="color:#cbd5e1;font-size:1.1rem;">
    Igual que Excel, pero más fácil:<br>
    • Cantidad producida: 1,000 metros<br>
    • Velocidad: 45 m/min<br>
    • Defectos: 5 tubos<br>
    • KPIs de calidad: OD, soldadura, rectitud
    </p>
</div>

<div class="timeline-item">
    <h3 style="color:#60a5fa;">2️⃣ Paso 2: IA Analiza (3 segundos)</h3>
    <p style="color:#cbd5e1;font-size:1.1rem;">
    🤖 <strong>Claude/GPT</strong> analiza tendencias y patrones<br>
    📋 <strong>Sistema de Normas</strong> verifica cumplimiento IATF<br>
    🔍 <strong>Comparación Profunda</strong>: ¿IA y Normas coinciden?
    </p>
</div>

<div class="timeline-item">
    <h3 style="color:#60a5fa;">3️⃣ Paso 3: Ve Resultados (3 minutos)</h3>
    <p style="color:#cbd5e1;font-size:1.1rem;">
    📊 Gráficas 3D del proceso<br>
    📈 Dashboards con 7+ tipos de charts<br>
    ⚠️ Alertas de problemas automáticas<br>
    💡 Recomendaciones específicas
    </p>
</div>

<div class="timeline-item">
    <h3 style="color:#60a5fa;">4️⃣ Paso 4: Exporta (2 minutos)</h3>
    <p style="color:#cbd5e1;font-size:1.1rem;">
    📄 PDF para jefe<br>
    📊 Excel para cliente<br>
    📝 Word para auditoría<br>
    🌐 HTML para compartir en web
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;padding:2rem;background:rgba(16,185,129,0.1);
            border-radius:1rem;border:2px solid #10b981;margin-top:2rem;">
    <h2 style="color:#34d399;font-size:2.5rem;margin:0;">
        ⏱️ Total: 11 Minutos
    </h2>
    <p style="color:#6ee7b7;font-size:1.3rem;margin-top:1rem;">
        vs 2+ Horas en Excel
    </p>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# SECTION 4: FEATURES FOR PIPE MANAGERS
# ════════════════════════════════════════════════════════════════════════════

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<div class="section-title">🎯 Diseñado Para Usted</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3 style="color:#60a5fa;text-align:left;">🏭 Proceso ERW/Drawn</h3>
        <p style="color:#cbd5e1;text-align:left;">
        ✅ Uncoiler → Welding → Sizing<br>
        ✅ 12 etapas del proceso<br>
        ✅ KPIs específicos de tubería<br>
        ✅ Control de soldadura crítico<br><br><br>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3 style="color:#60a5fa;text-align:left;">📋 Normas IATF</h3>
        <p style="color:#cbd5e1;text-align:left;">
        ✅ IATF 16949 integrado<br>
        ✅ ASTM A513, JIS G3445<br>
        ✅ Trazabilidad 100%<br>
        ✅ Listo para auditoría
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3 style="color:#60a5fa; text-align:left;">📊 KPIs Clave</h3>
        <p style="color:#cbd5e1;text-align:left;">
        ✅ Velocidad de producción<br>
        ✅ Tasa de defectos<br>
        ✅ Calidad de soldadura<br>
        ✅ Precisión dimensional (OD)<br>
        ✅ Rectitud del tubo<br>
        ✅ Acabado superficial
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3 style="color:#60a5fa;text-align:left;">🌐 Multi-idioma</h3>
        <p style="color:#cbd5e1;text-align:left;">
        ✅ Español (su idioma)<br>
        ✅ English (cliente USA)<br>
        ✅ Korean (casa matriz)<br>
        ✅ Cambiar con 1 click
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3 style="color:#60a5fa;text-align:left;">🤖 Doble IA</h3>
        <p style="color:#cbd5e1;text-align:left;">
        ✅ Claude (Anthropic)<br>
        ✅ GPT (OpenAI)<br>
        ✅ Comparar ambos<br>
        ✅ Mejor decisión siempre<br><br><br>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3 style="color:#60a5fa;text-align:left;">📱 Fácil de Usar</h3>
        <p style="color:#cbd5e1;text-align:left;">
        ✅ Interfaz simple<br>
        ✅ Como WhatsApp Web<br>
        ✅ No necesita capacitación<br>
        ✅ Funciona en teléfono
        </p>
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# SECTION 5: REAL BENEFITS
# ════════════════════════════════════════════════════════════════════════════

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<div class="section-title">💰 Beneficios Reales Para Usted</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h3 style="color:#60a5fa;">👤 Para Usted Personalmente</h3>
        <p style="color:#e2e8f0;font-size:1.1rem;line-height:2;">
        ✅ <strong>Más respeto</strong>: Reportes profesionales<br>
        ✅ <strong>Menos estrés</strong>: Sin errores de Excel<br>
        ✅ <strong>Terminar temprano</strong>: 90% tiempo ahorrado<br>
        ✅ <strong>Mejor salario</strong>: Resultados medibles<br>
        ✅ <strong>Reconocimiento</strong>: "¿Cómo lo hiciste?"
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h3 style="color:#60a5fa;">🏭 Para Su Planta</h3>
        <p style="color:#e2e8f0;font-size:1.1rem;line-height:2;">
        ✅ <strong>Menos defectos</strong>: Detectar problemas antes<br>
        ✅ <strong>Más producción</strong>: Optimización continua<br>
        ✅ <strong>Clientes felices</strong>: Calidad consistente<br>
        ✅ <strong>Auditorías fáciles</strong>: Todo documentado<br>
        ✅ <strong>Ahorros</strong>: ROI inmediato
        </p>
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# SECTION 6: TESTIMONIAL / CASE STUDY
# ════════════════════════════════════════════════════════════════════════════

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<div class="section-title">💬 Caso Real: Woori México</div>', unsafe_allow_html=True)
st.markdown("""
<div style="background:rgba(59,130,246,0.1);border:2px solid #3b82f6;
            border-radius:1.5rem;padding:3rem;margin:2rem 0;">
    <div style="text-align:center;">
        <p style="color:#60a5fa;font-size:2.5rem;margin:0;">🏭</p>
        <h3 style="color:#e2e8f0;font-size:1.5rem;">
            Woori México, S.A. de C.V.
        </h3>
        <p style="color:#94a3b8;">
            Parque Industrial SUMAR I, Calera, Zacatecas
        </p>
    </div>
    """, unsafe_allow_html=True)            

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h3 style="color:#60a5fa;">📊 Antes del Sistema:</h3>
        <p style="color:#e2e8f0;font-size:1.1rem;line-height:2;">
        • <strong>2 horas diarias</strong> en Excel<br>
        • <strong>Errores frecuentes</strong> en KPIs<br>
        • <strong>Reportes tardíos</strong> para cliente<br>
        • <strong>Estrés</strong> en auditorías<br>
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h3 style="color:#60a5fa;">✅ Después del Sistema:</h3>
        <p style="color:#e2e8f0;font-size:1.1rem;line-height:2;">
        • <strong>11 minutos</strong> de análisis<br>
        • <strong>0% errores</strong> de cálculo<br>
        • <strong>Reportes</strong> en tiempo real<br>
        • <strong>Auditorías</strong> con confianza<br>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# SECTION 7: CALL TO ACTION
# ════════════════════════════════════════════════════════════════════════════

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<div class="section-title">🚀 Comience Hoy</div>', unsafe_allow_html=True)
st.markdown("""
<div style="background:rgba(59,130,246,0.1);border:2px solid #3b82f6;
            border-radius:1.5rem;padding:3rem;margin:2rem 0;">
    <div style="text-align:center;">
        <p style="color:#60a5fa;font-size:2.5rem;margin:0;">🎁</p>
        <h3 style="color:#e2e8f0;font-size:1.5rem;">
            Prueba GRATIS por 30 Días 
        </h3>
        <p style="color:#94a3b8;">
            Sin tarjeta de crédito. Sin compromiso. Sin riesgo.
        </p>
    </div>
    """, unsafe_allow_html=True)            

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h3 style="color:#60a5fa;">✅ Qué Incluye:</h3>
        <p style="color:#e2e8f0;font-size:1.1rem;line-height:2;">
        • <strong>Instalación en 1 día</strong><br>
        • <strong>Capacitación incluida</strong> (2 horas)<br>
        • <strong>Soporte en español </strong> 24/7<br>
        • <strong>Actualización automática</strong><br>
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h3 style="color:#60a5fa;">📧 Contacto:</h3>
        <p style="color:#e2e8f0;font-size:1.1rem;line-height:2;">
        • <strong>Email:</strong> <a href="mailto:io7hub@naver.com">io7hub@naver.com</a><br>
        • <strong>Web: </strong> <a href="https://io7hub-projects-info-projects-main-jqmujm.streamlit.app/">https://io7hub-projects-info-projects-main-jqmujm.streamlit.app/</a><br>
        • <strong>WhatsApp </strong> +82 10 2610 5194<br><br>
        </p>
    </div>
    """, unsafe_allow_html=True)

# Add some charts for visual appeal
st.markdown('<div class="section-title">📊 Impacto Visual</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Before/After comparison
    fig = go.Figure()
    
    categories = ['Tiempo de<br>Análisis', 'Precisión', 'Estrés del<br>Gerente', 'Satisfacción<br>del Cliente']
    
    fig.add_trace(go.Scatterpolar(
        r=[120, 70, 90, 60],  # Before (minutes for time, % for others)
        theta=categories,
        fill='toself',
        name='Antes (Excel)',
        line_color='#ef4444'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=[11, 100, 20, 95],  # After
        theta=categories,
        fill='toself',
        name='Después (Kⁱ⁰⁷)',
        line_color='#10b981'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 120]
            )
        ),
        showlegend=True,
        title="Antes vs Después",
        template="plotly_dark",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Time savings
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=['Excel Manual', 'Kⁱ⁰⁷ Platform'],
        y=[120, 11],
        marker_color=['#ef4444', '#10b981'],
        text=['2+ horas', '11 minutos'],
        textposition='auto'
    ))
    
    fig.update_layout(
        title="Tiempo de Análisis Diario (minutos)",
        yaxis_title="Minutos",
        template="plotly_dark",
        height=400,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)

# ROI calculation
st.markdown("<br>", unsafe_allow_html=True)

fig = go.Figure()

fig.add_trace(go.Waterfall(
    name="ROI",
    orientation="v",
    measure=["relative", "relative", "relative", "total"],
    x=["Tiempo Ahorrado<br>(2hrs/día)", "Menos Errores<br>(0% vs 30%)", "Mejor Calidad<br>(Clientes)", "ROI Total"],
    textposition="auto",
    text=["+$500/mes", "+$300/mes", "+$800/mes", "$1,600/mes"],
    y=[500, 300, 800, 0],
    connector={"line": {"color": "rgb(63, 63, 63)"}},
    decreasing={"marker": {"color": "#ef4444"}},
    increasing={"marker": {"color": "#10b981"}},
    totals={"marker": {"color": "#3b82f6"}}
))

fig.update_layout(
    title="Retorno de Inversión Mensual (USD)",
    template="plotly_dark",
    height=400,
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<div style="text-align:center;padding:2rem;background:rgba(16,185,129,0.1);
            border-radius:1rem;margin-top:2rem;">
    <h3 style="color:#34d399;font-size:1.8rem;">
        💰 Inversión: $X/mes | Ahorro: $1,600/mes
    </h3>
    <p style="color:#6ee7b7;font-size:1.2rem;">
        ROI Positivo desde el Día 1
    </p>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# FOOTER
# ════════════════════════════════════════════════════════════════════════════
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
col1, col2, col3 = st.columns([0.5, 3, 0.5])

with col2:
    st.markdown("""
    <div style="text-align:center;padding:2rem;">
        <h2 style="background:linear-gradient(135deg,#60a5fa,#34d399);
                   -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                   font-size:2rem;">
            ⚙️<strong>Kⁱ⁰⁷</strong> Manufacturing Intelligence
        </h2>
        <p style="color:#64748b;font-size:1rem;margin-top:1rem;">
            Desde 2023 Transformando LATAM Manufacturing con IA
        </p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: #64748b; margin-top: 20px; padding: 15px;'>
    <p style="font-size: 1rem;">데이터 기반 가치 전환 전략<br>
    © 2025 Data-driven VX Strategist | powered by Kⁱ⁰⁷  | 📧 io7hub@naver.com</p>
</div>
""", unsafe_allow_html=True)