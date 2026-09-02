import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

def aplicar_estilos():
    """Inyecta CSS global con la nueva paleta Lila Cálido y mantiene los efectos de impacto visual."""
    css = """
    <style>
        /* --- FONDO PRINCIPAL --- */
        .stApp { background-color: #F4EFF5; } /* Lila pastel suave */
        
        /* --- TIPOGRAFÍA GENERAL Y TÍTULOS --- */
        .texto-principal { font-size: 1.125rem !important; color: #333333; line-height: 1.6; text-align: justify; }
        h1 { color: #4A3554 !important; font-size: 2.5rem !important; font-weight: bold; text-align: center; }
        h2, h3 { color: #4A3554 !important; font-size: 1.75rem !important; text-align: center; margin-bottom: 0.5rem; }
        .metadato-home { color: #756A7B !important; font-size: 1rem !important; text-transform: uppercase; text-align: center; display: block; margin-bottom: 2.5rem; }
        .metadato { color: #756A7B !important; font-size: 0.875rem !important; text-transform: uppercase; }
        
        /* --- NAVEGACIÓN Y TABS --- */
        [data-testid="stSidebar"] .stRadio label p,
        [data-testid="stSidebar"] .stRadio label div {
            font-size: 1.5rem !important; font-weight: 600 !important; color: #4A3554 !important; padding: 8px 0;
        }
        [data-testid="stTabs"] button[data-baseweb="tab"] p,
        [data-testid="stTabs"] button[data-baseweb="tab"] div,
        [data-testid="stTabs"] button[data-baseweb="tab"] span {
            font-size: 1.5rem !important; font-weight: bold !important; color: #4A3554 !important;
        }
        
        /* --- TARJETAS RESULTADOS (LIFT & NEON CÁLIDO) --- */
        .tarjeta-resultado {
            background-color: #FFFFFF; 
            padding: 20px; 
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.04); 
            border: 2px solid transparent;
            border-left: 6px solid #D29B7F; /* Acento terracota/durazno */
            margin-bottom: 1rem; 
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        }
        .tarjeta-resultado:hover { 
            transform: translateY(-5px) scale(1.02); 
            border-color: #D29B7F;
            box-shadow: 0 10px 20px rgba(210, 155, 127, 0.35); /* Resplandor cálido */
        }
        .valor-destacado { font-size: 1.75rem !important; font-weight: bold; color: #4A3554; margin-top: 5px; }
        
        /* --- TARJETA INFO HOME --- */
        .tarjeta-info {
            background-color: #FFFFFF; padding: 35px; border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.06); border-top: 6px solid #4A3554;
            margin: 0 auto; max-width: 850px;
        }
        
        /* --- BOTONES NATIVOS (EFECTO RIPPLE JS) --- */
        .stButton>button { 
            background-color: #4A3554; /* Ciruela oscuro */
            color: #FFFFFF; 
            border: none; 
            border-radius: 5px; 
            width: 100%; 
            position: relative; 
            overflow: hidden;   
            transition: background-color 0.3s ease, transform 0.1s ease; 
        }
        .stButton>button:hover { background-color: #35253D; } /* Más oscuro al hover */
        .stButton>button:active { transform: scale(0.98); }
        
        /* Clase CSS para el efecto Ripple en JS */
        .efecto-ripple {
            position: absolute;
            background: rgba(255, 255, 255, 0.5);
            border-radius: 50%;
            transform: scale(0);
            animation: animacionRipple 0.6s linear;
            pointer-events: none; 
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
    """Inyecta el script JS encargado de las animaciones globales y del efecto Ripple."""
    js = """<script>
        document.addEventListener("DOMContentLoaded", function() {
            const doc = window.parent.document;
            
            // Animación de entrada general
            const container = doc.querySelector('.stApp');
            if(container) {
                container.style.opacity = '0';
                container.style.transition = 'opacity 0.8s ease-in';
                setTimeout(() => { container.style.opacity = '1'; }, 50);
            }
            
            // Lógica del Efecto Ripple en Botones
            function aplicarRippleBotones() {
                const botones = doc.querySelectorAll('.stButton > button');
                botones.forEach(btn => {
                    btn.onclick = function(e) {
                        const rect = btn.getBoundingClientRect();
                        const x = e.clientX - rect.left;
                        const y = e.clientY - rect.top;
                        
                        const ripple = doc.createElement('span');
                        ripple.classList.add('efecto-ripple');
                        ripple.style.left = x + 'px';
                        ripple.style.top = y + 'px';
                        
                        btn.appendChild(ripple);
                        setTimeout(() => { ripple.remove(); }, 600);
                    };
                });
            }
            
            // MutationObserver para reaplicar al cambiar de Tab
            const observer = new MutationObserver(() => {
                aplicarRippleBotones();
            });
            
            const appBody = doc.querySelector('.stApp') || doc.body;
            observer.observe(appBody, { childList: true, subtree: true });
            
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
        fig.patch.set_facecolor('#F4EFF5') /* Fondo Lila para emparejar */
        ax.set_facecolor('#FFFFFF')
        ax.plot(q_arr, p_arr, color='#4A3554', linewidth=2.5, label='Curva IPR')
        ax.scatter(qo, pwf, color='#D29B7F', s=120, zorder=5, label='Punto Operativo')
        ax.set_xlabel('Caudal (STB/d)', fontweight='bold', color='#4A3554')
        ax.set_ylabel('Pwf (psi)', fontweight='bold', color='#4A3554')
        ax.grid(True, linestyle='--', alpha=0.4)
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
        fig.patch.set_facecolor('#F4EFF5')
        ax.set_facecolor('#FFFFFF')
        ax.plot([0, ph], [0, tvd], color='#4A3554', linewidth=2.5, label='P. Hidrostática')
        ax.scatter(pform, tvd, color='#D29B7F', s=100, label='P. Formación')
        ax.invert_yaxis()
        ax.set_xlabel('Presión (psi)', fontweight='bold', color='#4A3554')
        ax.set_ylabel('Profundidad TVD (ft)', fontweight='bold', color='#4A3554')
        ax.grid(True, linestyle='--', alpha=0.4)
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
        fig.patch.set_facecolor('#F4EFF5')
        ax.set_facecolor('#FFFFFF')
        ax.bar(['POES Original', 'Recuperable'], [p_mmstb, r_mmstb], color=['#4A3554', '#D29B7F'], width=0.6)
        ax.set_ylabel('Volumen (MMSTB)', fontweight='bold', color='#4A3554')
        st.pyplot(fig, use_container_width=True)
