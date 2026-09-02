import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

def aplicar_estilos():
    """Inyecta CSS global robusto. Efectos 3D y transiciones gestionados por CSS puro para evitar bloqueos."""
    css = """
    <style>
        /* --- FONDO PRINCIPAL --- */
        .stApp { background-color: #F4EFF5; } 
        
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
        
        /* --- TARJETA NORMAL --- */
        .tarjeta-resultado {
            background-color: #FFFFFF; padding: 20px; border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.04); border-left: 6px solid #D29B7F; 
            margin-bottom: 1rem; transition: transform 0.3s ease;
        }
        .valor-destacado { font-size: 1.75rem !important; font-weight: bold; color: #4A3554; margin-top: 5px; }
        
        /* --- EFECTO 1: TARJETAS MAGNÉTICAS 3D (CSS PURO - PERFORACIÓN) --- */
        .tarjeta-magnetica {
            background-color: #FFFFFF; padding: 20px; border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.04); border-left: 6px solid #D29B7F; 
            margin-bottom: 1rem;
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease;
            transform: perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1);
        }
        .tarjeta-magnetica:hover { 
            transform: perspective(1000px) rotateX(5deg) rotateY(-5deg) scale3d(1.05, 1.05, 1.05);
            box-shadow: -8px 12px 20px rgba(210, 155, 127, 0.4); 
            border-color: #4A3554;
        }

        /* --- EFECTO 2: POP-IN DINÁMICO (CSS PURO - RESERVORIOS) --- */
        .tarjeta-reservorio {
            background-color: #FFFFFF; padding: 20px; border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.04); border-left: 6px solid #4A3554; 
            margin-bottom: 1rem; opacity: 0;
            animation: popIn 0.6s cubic-bezier(0.68, -0.55, 0.27, 1.55) forwards;
        }
        /* Retrasos escalonados para efecto cascada */
        .delay-1 { animation-delay: 0.1s; }
        .delay-2 { animation-delay: 0.3s; }
        .delay-3 { animation-delay: 0.5s; }
        
        @keyframes popIn {
            0% { opacity: 0; transform: scale(0.8) translateY(20px); }
            100% { opacity: 1; transform: scale(1) translateY(0); }
        }

        /* --- TARJETA INFO HOME --- */
        .tarjeta-info {
            background-color: #FFFFFF; padding: 35px; border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.06); border-top: 6px solid #4A3554;
            margin: 0 auto; max-width: 850px;
        }
        
        /* --- EFECTO 3: BOTONES HOVER DINÁMICO --- */
        .stButton>button { 
            background-color: #4A3554 !important; 
            color: #FFFFFF !important; 
            border: none !important; border-radius: 6px !important; width: 100%; 
            position: relative; overflow: hidden;   
            transition: all 0.3s ease !important; 
        }
        /* Cambio de color y elevación al pasar el cursor (Hover) */
        .stButton>button:hover { 
            background-color: #D29B7F !important; /* Naranja/Durazno cálido */
            color: #4A3554 !important; 
            transform: translateY(-3px);
            box-shadow: 0 8px 15px rgba(210, 155, 127, 0.5) !important;
        }
        .stButton>button:active { transform: scale(0.96); }
        
        /* Contenedor inyectado por JS para el fluido naranja */
        .ripple-fluido {
            position: absolute;
            background: rgba(242, 169, 0, 0.7); /* Naranja radiante */
            border-radius: 50%;
            transform: scale(0);
            animation: expandirFluido 0.6s ease-out;
            pointer-events: none;
            width: 250px; height: 250px;
            margin-top: -125px; margin-left: -125px;
        }
        @keyframes expandirFluido { to { transform: scale(3); opacity: 0; } }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def renderizar_tarjeta_info(texto):
    """Renderiza el bloque descriptivo del Home."""
    html = f"""<div class="tarjeta-info"><p class="texto-principal">{texto}</p></div>"""
    st.markdown(html, unsafe_allow_html=True)

def renderizar_tarjeta_normal(titulo, valor, unidad=""):
    """Tarjeta estándar para Producción."""
    html = f"""<div class="tarjeta-resultado">
                <div class="metadato">{titulo}</div>
                <div class="valor-destacado">{valor:,.2f} {unidad}</div>
              </div>"""
    st.markdown(html, unsafe_allow_html=True)

def renderizar_tarjeta_magnetica(titulo, valor, unidad=""):
    """Tarjeta con efecto 3D Hover para Perforación."""
    html = f"""<div class="tarjeta-magnetica">
                <div class="metadato">{titulo}</div>
                <div class="valor-destacado">{valor:,.2f} {unidad}</div>
              </div>"""
    st.markdown(html, unsafe_allow_html=True)

def renderizar_tarjeta_reservorio(titulo, valor, unidad, delay_class):
    """Tarjeta con efecto Cascada Pop-In para Reservorios."""
    html = f"""<div class="tarjeta-reservorio {delay_class}">
                <div class="metadato">{titulo}</div>
                <div class="valor-destacado">{valor:,.2f} {unidad}</div>
              </div>"""
    st.markdown(html, unsafe_allow_html=True)

def inyectar_js_animacion():
    """Inyecta el script JS optimizado para el Cyber-Text y el Ripple fluido."""
    js = """<script>
        document.addEventListener("DOMContentLoaded", function() {
            const doc = window.parent.document;
            
            // 1. Efecto Cyber-Text (Solo ejecuta una vez)
            function iniciarCyberText() {
                const titulos = doc.querySelectorAll('h1, h3');
                titulos.forEach(element => {
                    if (element.dataset.cyberDone) return;
                    const originalText = element.innerText;
                    const caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*<>";
                    let iteraciones = 0;
                    element.dataset.cyberDone = "true";
                    
                    const intervalo = setInterval(() => {
                        element.innerText = originalText.split("").map((letra, index) => {
                            if (index < iteraciones || letra === " ") return originalText[index];
                            return caracteres[Math.floor(Math.random() * caracteres.length)];
                        }).join("");
                        if (iteraciones >= originalText.length) clearInterval(intervalo);
                        iteraciones += 0.5;
                    }, 30);
                });
            }

            // 2. Efecto Ripple Fluido en Botones
            function configurarRipples() {
                const botones = doc.querySelectorAll('.stButton > button');
                botones.forEach(btn => {
                    if (!btn.dataset.rippleActivo) {
                        btn.dataset.rippleActivo = "true";
                        btn.addEventListener('mousedown', function(e) {
                            const rect = btn.getBoundingClientRect();
                            const x = e.clientX - rect.left;
                            const y = e.clientY - rect.top;
                            
                            const ripple = doc.createElement('span');
                            ripple.classList.add('ripple-fluido');
                            ripple.style.left = x + 'px';
                            ripple.style.top = y + 'px';
                            
                            btn.appendChild(ripple);
                            setTimeout(() => ripple.remove(), 600);
                        });
                    }
                });
            }

            // Un observador ligero que re-asigna eventos tras el rerun de Streamlit
            const observer = new MutationObserver(() => {
                iniciarCyberText();
                configurarRipples();
            });
            
            observer.observe(doc.body, { childList: true, subtree: true });
            
            setTimeout(() => {
                iniciarCyberText();
                configurarRipples();
            }, 500);
        });
    </script>"""
    components.html(js, height=0)

# --- COMPONENTES GRÁFICOS MODULARES ---

def mostrar_panel_ipr(qo, qb, qmax, pwf, q_arr, p_arr):
    """PANEL PRODUCCIÓN: Botones con Hover de color dinámico y fluido."""
    c1, c2, c3 = st.columns(3)
    with c1: renderizar_tarjeta_normal("Caudal Actual", qo, "STB/d")
    with c2: renderizar_tarjeta_normal("Caudal a Burbuja", qb, "STB/d")
    with c3: renderizar_tarjeta_normal("Caudal Máximo", qmax, "STB/d")
    
    _, col_graf, _ = st.columns([1, 3, 1])
    with col_graf:
        fig, ax = plt.subplots(figsize=(6, 3.5))
        fig.patch.set_facecolor('#F4EFF5') 
        ax.set_facecolor('#FFFFFF')
        ax.plot(q_arr, p_arr, color='#4A3554', linewidth=3, label='Curva IPR')
        ax.scatter(qo, pwf, color='#D29B7F', s=150, zorder=5, edgecolors='black', label='Punto Operativo')
        ax.set_xlabel('Caudal (STB/d)', fontweight='bold', color='#4A3554')
        ax.set_ylabel('Pwf (psi)', fontweight='bold', color='#4A3554')
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()
        st.pyplot(fig, use_container_width=True)

def mostrar_panel_perforacion(gh, ph, dp, tvd, pform):
    """PANEL PERFORACIÓN: Implementa las TARJETAS MAGNÉTICAS 3D."""
    c1, c2, c3 = st.columns(3)
    with c1: renderizar_tarjeta_magnetica("Gradiente", gh, "psi/ft")
    with c2: renderizar_tarjeta_magnetica("P. Hidrostática", ph, "psi")
    with c3: renderizar_tarjeta_magnetica("Diferencial (\u0394P)", dp, "psi")
    
    _, col_graf, _ = st.columns([1, 1, 1])
    with col_graf:
        fig, ax = plt.subplots(figsize=(3.5, 5))
        fig.patch.set_facecolor('#F4EFF5')
        ax.set_facecolor('#FFFFFF')
        ax.plot([0, ph], [0, tvd], color='#4A3554', linewidth=3, label='P. Hidrostática')
        ax.scatter(pform, tvd, color='#D29B7F', s=120, edgecolors='black', label='P. Formación')
        ax.invert_yaxis()
        ax.set_xlabel('Presión (psi)', fontweight='bold', color='#4A3554')
        ax.set_ylabel('Profundidad TVD (ft)', fontweight='bold', color='#4A3554')
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()
        st.pyplot(fig, use_container_width=True)

def mostrar_panel_reservorios(hn, p_mmstb, r_mmstb):
    """PANEL RESERVORIOS: Inyecta animación Pop-In en cascada."""
    c1, c2, c3 = st.columns(3)
    # Se aplican retrasos progresivos para el efecto cascada
    with c1: renderizar_tarjeta_reservorio("Espesor Neto", hn, "ft", "delay-1")
    with c2: renderizar_tarjeta_reservorio("POES", p_mmstb, "MMSTB", "delay-2")
    with c3: renderizar_tarjeta_reservorio("Reservas Rec.", r_mmstb, "MMSTB", "delay-3")
    
    _, col_graf, _ = st.columns([1, 2, 1])
    with col_graf:
        fig, ax = plt.subplots(figsize=(5, 3.5))
        fig.patch.set_facecolor('#F4EFF5')
        ax.set_facecolor('#FFFFFF')
        ax.bar(['POES Original', 'Recuperable'], [p_mmstb, r_mmstb], color=['#4A3554', '#D29B7F'], width=0.6)
        ax.set_ylabel('Volumen (MMSTB)', fontweight='bold', color='#4A3554')
        st.pyplot(fig, use_container_width=True)
