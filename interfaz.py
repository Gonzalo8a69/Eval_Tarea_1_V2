import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

def aplicar_estilos():
    """Inyecta CSS global garantizando jerarquía visual, personalización de navegación y efectos de impacto."""
    css = """
    <style>
        /* --- FONDO PRINCIPAL --- */
        .stApp { background-color: #F3EFE6; }
        
        /* --- TIPOGRAFÍA GENERAL Y TÍTULOS --- */
        .texto-principal { font-size: 1.125rem !important; color: #333333; line-height: 1.6; text-align: justify; }
        h1 { color: #1A365D !important; font-size: 2.5rem !important; font-weight: bold; text-align: center; }
        h2, h3 { color: #1A365D !important; font-size: 1.75rem !important; text-align: center; margin-bottom: 0.5rem; }
        .metadato-home { color: #64748B !important; font-size: 1rem !important; text-transform: uppercase; text-align: center; display: block; margin-bottom: 2.5rem; }
        .metadato { color: #64748B !important; font-size: 0.875rem !important; text-transform: uppercase; }
        
        /* --- NAVEGACIÓN Y TABS --- */
        [data-testid="stSidebar"] .stRadio label p,
        [data-testid="stSidebar"] .stRadio label div {
            font-size: 1.5rem !important; font-weight: 600 !important; color: #1A365D !important; padding: 8px 0;
        }
        [data-testid="stTabs"] button[data-baseweb="tab"] p,
        [data-testid="stTabs"] button[data-baseweb="tab"] div,
        [data-testid="stTabs"] button[data-baseweb="tab"] span {
            font-size: 1.5rem !important; font-weight: bold !important; color: #1A365D !important;
        }
        
        /* --- TARJETAS RESULTADOS (NUEVO EFECTO LIFT & NEON) --- */
        .tarjeta-resultado {
            background-color: #FFFFFF; 
            padding: 20px; 
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
            border: 2px solid transparent;
            border-left: 6px solid #C5A880; 
            margin-bottom: 1rem; 
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        }
        .tarjeta-resultado:hover { 
            transform: translateY(-5px) scale(1.02); 
            border-color: #C5A880;
            box-shadow: 0 10px 20px rgba(197, 168, 128, 0.4);
        }
        .valor-destacado { font-size: 1.75rem !important; font-weight: bold; color: #1A365D; margin-top: 5px; }
        
        /* --- TARJETA INFO HOME --- */
        .tarjeta-info {
            background-color: #FFFFFF; padding: 35px; border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08); border-top: 6px solid #1A365D;
            margin: 0 auto; max-width: 850px;
        }
        
        /* --- BOTONES NATIVOS (PREPARACIÓN PARA EFECTO RIPPLE JS) --- */
        .stButton>button { 
            background-color: #1A365D; 
            color: #FFFFFF; 
            border: none; 
            border-radius: 5px; 
            width: 100%; 
            position: relative; /* Clave para contener la onda JS */
            overflow: hidden;   /* Oculta la onda fuera del botón */
            transition: background-color 0.3s ease, transform 0.1s ease; 
        }
        .stButton>button:hover { background-color: #0F2341; }
        .stButton>button:active { transform: scale(0.98); }
        
        /* Clase CSS inyectada por JS para el efecto Ripple */
        .efecto-ripple {
            position: absolute;
            background: rgba(255, 255, 255, 0.4);
            border-radius: 50%;
            transform: scale(0);
            animation: animacionRipple 0.6s linear;
            pointer-events: none; /* Ignora clics sobre la propia onda */
            width: 150px;
            height: 150px;
            margin-top: -75px;
            margin-left: -75px;
        }
        
        @keyframes animacionRipple {
            to { transform: scale(4); opacity: 0; }
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def renderizar_tarjeta(titulo, valor, unidad=""):
    """Renderiza una métrica individual."""
    html = f"""<div class="tarjeta-resultado">
                <div class="metadato">{titulo}</div>
                <div class="valor-destacado">{valor:,.2f} {unidad}</div>
              </div>"""
    st.markdown(html, unsafe_allow_html=True)

def renderizar_tarjeta_info(texto):
    """Renderiza el bloque descriptivo estructurado para el Home."""
    html = f"""<div class="tarjeta-info"><p class="texto-principal">{texto}</p></div>"""
    st.markdown(html, unsafe_allow_html=True)

def inyectar_js_animacion():
    """
    Inyecta el script JS encargado de las animaciones globales y del efecto 
    Ripple (Onda Expansiva) al hacer clic en los botones de cálculo.
    """
    js = """<script>
        document.addEventListener("DOMContentLoaded", function() {
            const doc = window.parent.document;
            
            // 1. Animación de entrada general (Fade In)
            const container = doc.querySelector('.stApp');
            if(container) {
                container.style.opacity = '0';
                container.style.transition = 'opacity 0.8s ease-in';
                setTimeout(() => { container.style.opacity = '1'; }, 50);
            }
            
            // 2. Lógica del Efecto Ripple en Botones
            function aplicarRippleBotones() {
                const botones = doc.querySelectorAll('.stButton > button');
                botones.forEach(btn => {
                    // Evitar listeners duplicados si Streamlit recarga la interfaz
                    btn.onclick = function(e) {
                        const rect = btn.getBoundingClientRect();
                        const x = e.clientX - rect.left;
                        const y = e.clientY - rect.top;
                        
                        const ripple = doc.createElement('span');
                        ripple.classList.add('efecto-ripple');
                        ripple.style.left = x + 'px';
                        ripple.style.top = y + 'px';
                        
                        btn.appendChild(ripple);
                        
                        // Limpiar el elemento del DOM tras la animación
                        setTimeout(() => { ripple.remove(); }, 600);
                    };
                });
            }
            
            // 3. MutationObserver para reaplicar el JS al cambiar de Tab
            const observer = new MutationObserver(() => {
                aplicarRippleBotones();
            });
            
            const appBody = doc.querySelector('.stApp') || doc.body;
            observer.observe(appBody, { childList: true, subtree: true });
            
            // Ejecución inicial
            setTimeout(aplicarRippleBotones, 500);
        });
    </script>"""
    components.html(js, height=0)

# --- COMPONENTES GRÁFICOS MODULARES ---

def mostrar_panel_ipr(qo, qb, qmax, pwf, q_arr, p_arr):
    """Construye el panel de resultados y gráficos para Producción."""
    c1, c2, c3 = st.columns(3)
    with c1: renderizar_tarjeta("Caudal Actual", qo, "STB/d")
    with c2: renderizar_tarjeta("Caudal a Burbuja", qb, "STB/d")
    with c3: renderizar_tarjeta("Caudal Máximo", qmax, "STB/d")
    
    _, col_graf, _ = st.columns([1, 3, 1])
    with col_graf:
        fig, ax = plt.subplots(figsize=(6, 3.5))
        fig.patch.set_facecolor('#F3EFE6') 
        ax.set_facecolor('#FFFFFF')
        ax.plot(q_arr, p_arr, color='#1A365D', linewidth=2.5, label='Curva IPR')
        ax.scatter(qo, pwf, color='#C5A880', s=120, zorder=5, label='Punto Operativo')
        ax.set_xlabel('Caudal (STB/d)', fontweight='bold', color='#1A365D')
        ax.set_ylabel('Pwf (psi)', fontweight='bold', color='#1A365D')
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.legend()
        st.pyplot(fig, use_container_width=True)

def mostrar_panel_perforacion(gh, ph, dp, tvd, pform):
    """Construye el panel de resultados y gráficos para Perforación."""
    c1, c2, c3 = st.columns(3)
    with c1: renderizar_tarjeta("Gradiente", gh, "psi/ft")
    with c2: renderizar_tarjeta("P. Hidrostática", ph, "psi")
    with c3: renderizar_tarjeta("Diferencial (\u0394P)", dp, "psi")
    
    _, col_graf, _ = st.columns([1, 1, 1])
    with col_graf:
        fig, ax = plt.subplots(figsize=(3.5, 5))
        fig.patch.set_facecolor('#F3EFE6')
        ax.set_facecolor('#FFFFFF')
        ax.plot([0, ph], [0, tvd], color='#1A365D', linewidth=2.5, label='P. Hidrostática')
        ax.scatter(pform, tvd, color='#C5A880', s=100, label='P. Formación')
        ax.invert_yaxis()
        ax.set_xlabel('Presión (psi)', fontweight='bold', color='#1A365D')
        ax.set_ylabel('Profundidad TVD (ft)', fontweight='bold', color='#1A365D')
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.legend()
        st.pyplot(fig, use_container_width=True)

def mostrar_panel_reservorios(hn, p_mmstb, r_mmstb):
    """Construye el panel de resultados y gráficos para Reservorios."""
    c1, c2, c3 = st.columns(3)
    with c1: renderizar_tarjeta("Espesor Neto", hn, "ft")
    with c2: renderizar_tarjeta("POES", p_mmstb, "MMSTB")
    with c3: renderizar_tarjeta("Reservas Rec.", r_mmstb, "MMSTB")
    
    _, col_graf, _ = st.columns([1, 2, 1])
    with col_graf:
        fig, ax = plt.subplots(figsize=(5, 3.5))
        fig.patch.set_facecolor('#F3EFE6')
        ax.set_facecolor('#FFFFFF')
        ax.bar(['POES Original', 'Recuperable'], [p_mmstb, r_mmstb], color=['#1A365D', '#C5A880'], width=0.6)
        ax.set_ylabel('Volumen (MMSTB)', fontweight='bold', color='#1A365D')
        st.pyplot(fig, use_container_width=True)
