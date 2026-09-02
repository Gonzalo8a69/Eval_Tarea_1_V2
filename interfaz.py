import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

def aplicar_estilos():
    """Inyecta CSS global con paleta de alto contraste, corrige inputs y potencia efectos visuales."""
    css = """
    <style>
        /* --- FONDO PRINCIPAL --- */
        .stApp { background-color: #E8EEF2; } /* Gris-azulado claro para contraste */
        
        /* --- TIPOGRAFÍA Y TÍTULOS --- */
        .texto-principal { font-size: 1.125rem !important; color: #1E293B; line-height: 1.6; text-align: justify; }
        h1 { color: #0F4C75 !important; font-size: 2.5rem !important; font-weight: 800; text-align: center; }
        h2, h3 { color: #0F4C75 !important; font-size: 1.75rem !important; text-align: center; margin-bottom: 0.5rem; font-weight: 700; }
        .metadato-home { color: #3282B8 !important; font-size: 1.1rem !important; text-transform: uppercase; text-align: center; display: block; margin-bottom: 2.5rem; font-weight: bold; }
        .metadato { color: #64748B !important; font-size: 0.875rem !important; text-transform: uppercase; font-weight: 600; }
        
        /* --- CORRECCIÓN DE CAJAS DE ENTRADA (INPUTS) NATIVOS DE STREAMLIT --- */
        div[data-baseweb="input"] {
            background-color: #FFFFFF !important;
            border: 2px solid #B0C4DE !important;
            border-radius: 6px !important;
        }
        div[data-baseweb="input"]:focus-within { border-color: #F2A900 !important; }
        div[data-baseweb="input"] input { color: #0F4C75 !important; font-weight: bold !important; font-size: 1.1rem !important; }
        
        /* --- NAVEGACIÓN Y TABS --- */
        [data-testid="stSidebar"] .stRadio label p,
        [data-testid="stSidebar"] .stRadio label div {
            font-size: 1.5rem !important; font-weight: 700 !important; color: #0F4C75 !important; padding: 10px 0;
        }
        [data-testid="stTabs"] button[data-baseweb="tab"] p,
        [data-testid="stTabs"] button[data-baseweb="tab"] div,
        [data-testid="stTabs"] button[data-baseweb="tab"] span {
            font-size: 1.5rem !important; font-weight: bold !important; color: #0F4C75 !important;
        }
        
        /* --- TARJETAS RESULTADOS (LIFT & NEON VIBRANTE) --- */
        .tarjeta-resultado {
            background-color: #FFFFFF; 
            padding: 20px; 
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08); 
            border: 2px solid transparent;
            border-left: 6px solid #F2A900; /* Acento Naranja Vibrante */
            margin-bottom: 1rem; 
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        }
        .tarjeta-resultado:hover { 
            transform: translateY(-6px) scale(1.02); 
            border-color: #F2A900;
            box-shadow: 0 12px 24px rgba(242, 169, 0, 0.4); /* Resplandor Neón visible */
        }
        .valor-destacado { font-size: 1.85rem !important; font-weight: 900; color: #0F4C75; margin-top: 5px; }
        
        /* --- TARJETA INFO HOME --- */
        .tarjeta-info {
            background-color: #FFFFFF; padding: 35px; border-radius: 10px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.1); border-top: 6px solid #0F4C75;
            margin: 0 auto; max-width: 850px;
        }
        
        /* --- BOTONES NATIVOS (COLOR VIVO Y EFECTO RIPPLE JS) --- */
        .stButton>button { 
            background: linear-gradient(135deg, #0F4C75, #3282B8) !important; /* Degradado vivo */
            color: #FFFFFF !important; 
            font-weight: bold !important;
            font-size: 1.1rem !important;
            border: none !important; 
            border-radius: 6px !important; 
            width: 100%; 
            position: relative; 
            overflow: hidden;   
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(15, 76, 117, 0.3);
        }
        .stButton>button:hover { 
            box-shadow: 0 6px 12px rgba(242, 169, 0, 0.5); /* Sombra naranja al hover */
            transform: translateY(-2px);
        }
        .stButton>button:active { transform: scale(0.98); }
        
        /* Clase CSS para el efecto Ripple en JS */
        .efecto-ripple {
            position: absolute;
            background: rgba(242, 169, 0, 0.7); /* Ripple en color naranja/dorado */
            border-radius: 50%;
            transform: scale(0);
            animation: animacionRipple 0.6s ease-out;
            pointer-events: none; 
            width: 200px;
            height: 200px;
            margin-top: -100px;
            margin-left: -100px;
            z-index: 10;
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
        fig.patch.set_facecolor('#E8EEF2') # Sincronizado con el nuevo fondo
        ax.set_facecolor('#FFFFFF')
        ax.plot(q_arr, p_arr, color='#0F4C75', linewidth=3, label='Curva IPR')
        ax.scatter(qo, pwf, color='#F2A900', s=150, zorder=5, edgecolors='black', label='Punto Operativo')
        ax.set_xlabel('Caudal (STB/d)', fontweight='bold', color='#0F4C75')
        ax.set_ylabel('Pwf (psi)', fontweight='bold', color='#0F4C75')
        ax.grid(True, linestyle='--', alpha=0.6)
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
        fig.patch.set_facecolor('#E8EEF2')
        ax.set_facecolor('#FFFFFF')
        ax.plot([0, ph], [0, tvd], color='#0F4C75', linewidth=3, label='P. Hidrostática')
        ax.scatter(pform, tvd, color='#F2A900', s=120, edgecolors='black', label='P. Formación')
        ax.invert_yaxis()
        ax.set_xlabel('Presión (psi)', fontweight='bold', color='#0F4C75')
        ax.set_ylabel('Profundidad TVD (ft)', fontweight='bold', color='#0F4C75')
        ax.grid(True, linestyle='--', alpha=0.6)
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
        fig.patch.set_facecolor('#E8EEF2')
        ax.set_facecolor('#FFFFFF')
        ax.bar(['POES Original', 'Recuperable'], [p_mmstb, r_mmstb], color=['#0F4C75', '#F2A900'], width=0.6)
        ax.set_ylabel('Volumen (MMSTB)', fontweight='bold', color='#0F4C75')
        st.pyplot(fig, use_container_width=True)
