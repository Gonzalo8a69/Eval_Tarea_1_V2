import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

def aplicar_estilos():
    """Inyecta CSS global con paleta de Alta Energía, corrige inputs y gestiona efectos 3D y Pop-In."""
    css = """
    <style>
        /* --- FONDO PRINCIPAL --- */
        .stApp { background-color: #E8EEF2; } 
        
        /* --- TIPOGRAFÍA Y TÍTULOS --- */
        .texto-principal { font-size: 1.125rem !important; color: #1E293B; line-height: 1.6; text-align: justify; }
        h1 { color: #0F4C75 !important; font-size: 2.5rem !important; font-weight: 800; text-align: center; }
        h2, h3 { color: #0F4C75 !important; font-size: 1.75rem !important; text-align: center; margin-bottom: 0.5rem; }
        .metadato-home { color: #3282B8 !important; font-size: 1.1rem !important; text-transform: uppercase; text-align: center; display: block; margin-bottom: 2.5rem; font-weight: bold; }
        .metadato { color: #64748B !important; font-size: 0.875rem !important; text-transform: uppercase; font-weight: 600; }
        
        /* --- CORRECCIÓN DE CAJAS DE ENTRADA (INPUTS) --- */
        div[data-baseweb="input"] { background-color: #FFFFFF !important; border: 2px solid #B0C4DE !important; border-radius: 6px !important; }
        div[data-baseweb="input"]:focus-within { border-color: #F2A900 !important; }
        div[data-baseweb="input"] input { color: #0F4C75 !important; font-weight: bold !important; font-size: 1.1rem !important; }
        
        /* --- NAVEGACIÓN Y TABS --- */
        [data-testid="stSidebar"] .stRadio label p,
        [data-testid="stSidebar"] .stRadio label div { font-size: 1.5rem !important; font-weight: 700 !important; color: #0F4C75 !important; padding: 10px 0; }
        [data-testid="stTabs"] button[data-baseweb="tab"] p,
        [data-testid="stTabs"] button[data-baseweb="tab"] div,
        [data-testid="stTabs"] button[data-baseweb="tab"] span { font-size: 1.5rem !important; font-weight: bold !important; color: #0F4C75 !important; }
        
        /* --- TARJETA NORMAL Y HOME --- */
        .tarjeta-resultado {
            background-color: #FFFFFF; padding: 20px; border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-left: 6px solid #F2A900; 
            margin-bottom: 1rem; transition: transform 0.3s ease;
        }
        .valor-destacado { font-size: 1.85rem !important; font-weight: 900; color: #0F4C75; margin-top: 5px; }
        
        .tarjeta-info {
            background-color: #FFFFFF; padding: 35px; border-radius: 10px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.1); border-top: 6px solid #0F4C75; margin: 0 auto; max-width: 850px;
        }
        
        /* --- EFECTO 1: TARJETAS MAGNÉTICAS 3D (CSS PURO - PERFORACIÓN) --- */
        .tarjeta-magnetica {
            background-color: #FFFFFF; padding: 20px; border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-left: 6px solid #F2A900; 
            margin-bottom: 1rem;
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease;
            transform: perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1);
        }
        .tarjeta-magnetica:hover { 
            transform: perspective(1000px) rotateX(5deg) rotateY(-5deg) scale3d(1.05, 1.05, 1.05);
            box-shadow: -8px 12px 20px rgba(242, 169, 0, 0.4); 
            border-color: #0F4C75;
        }

        /* --- EFECTO 2: POP-IN DINÁMICO (CSS PURO - RESERVORIOS) --- */
        .tarjeta-reservorio {
            background-color: #FFFFFF; padding: 20px; border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-left: 6px solid #0F4C75; 
            margin-bottom: 1rem; opacity: 0;
            animation: popIn 0.6s cubic-bezier(0.68, -0.55, 0.27, 1.55) forwards;
        }
        .delay-1 { animation-delay: 0.1s; }
        .delay-2 { animation-delay: 0.3s; }
        .delay-3 { animation-delay: 0.5s; }
        @keyframes popIn { 0% { opacity: 0; transform: scale(0.8) translateY(20px); } 100% { opacity: 1; transform: scale(1) translateY(0); } }
        
        /* --- EFECTO 3: BOTONES Y RIPPLE LÍQUIDO (TAB PRODUCCIÓN) --- */
        .stButton>button { 
            background: linear-gradient(135deg, #0F4C75, #3282B8) !important; color: #FFFFFF !important; 
            font-weight: bold !important; font-size: 1.1rem !important; border: none !important; 
            border-radius: 6px !important; width: 100%; position: relative; overflow: hidden;   
            box-shadow: 0 4px 6px rgba(15, 76, 117, 0.3); transition: all 0.3s ease !important;
        }
        .stButton>button:hover { 
            box-shadow: 0 6px 12px rgba(242, 169, 0, 0.6) !important; 
            transform: translateY(-3px);
        }
        .stButton>button:active { transform: scale(0.96); }
        
        .ripple-fluido {
            position: absolute; background: radial-gradient(circle, rgba(242,169,0,0.8) 0%, rgba(255,255,255,0) 70%);
            border-radius: 50%; transform: scale(0); animation: animacionRippleLiq 0.8s cubic-bezier(0.1, 0.7, 0.3, 1);
            pointer-events: none; width: 300px; height: 300px; margin-top: -150px; margin-left: -150px;
        }
        @keyframes animacionRippleLiq { to { transform: scale(3); opacity: 0; } }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def renderizar_tarjeta_info(texto):
    html = f"""<div class="tarjeta-info"><p class="texto-principal">{texto}</p></div>"""
    st.markdown(html, unsafe_allow_html=True)

def renderizar_tarjeta_normal(titulo, valor, unidad=""):
    html = f"""<div class="tarjeta-resultado"><div class="metadato">{titulo}</div><div class="valor-destacado">{valor:,.2f} {unidad}</div></div>"""
    st.markdown(html, unsafe_allow_html=True)

def renderizar_tarjeta_magnetica(titulo, valor, unidad=""):
    html = f"""<div class="tarjeta-magnetica"><div class="metadato">{titulo}</div><div class="valor-destacado">{valor:,.2f} {unidad}</div></div>"""
    st.markdown(html, unsafe_allow_html=True)

def renderizar_tarjeta_reservorio(titulo, valor, unidad, delay_class):
    html = f"""<div class="tarjeta-reservorio {delay_class}"><div class="metadato">{titulo}</div><div class="valor-destacado">{valor:,.2f} {unidad}</div></div>"""
    st.markdown(html, unsafe_allow_html=True)

def inyectar_js_animacion():
    """Inyecta el script JS para el Cyber-Text y el Ripple fluido."""
    js = """<script>
        document.addEventListener("DOMContentLoaded", function() {
            const doc = window.parent.document;
            
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

            const observer = new MutationObserver(() => {
                iniciarCyberText();
                configurarRipples();
            });
            observer.observe(doc.body, { childList: true, subtree: true });
            
            setTimeout(() => { iniciarCyberText(); configurarRipples(); }, 500);
        });
    </script>"""
    components.html(js, height=0)

def mostrar_panel_ipr(qo, qb, qmax, pwf, q_arr, p_arr):
    c1, c2, c3 = st.columns(3)
    with c1: renderizar_tarjeta_normal("Caudal Actual", qo, "STB/d")
    with c2: renderizar_tarjeta_normal("Caudal a Burbuja", qb, "STB/d")
    with c3: renderizar_tarjeta_normal("Caudal Máximo", qmax, "STB/d")
    
    _, col_graf, _ = st.columns([1, 3, 1])
    with col_graf:
        fig, ax = plt.subplots(figsize=(6, 3.5))
        fig.patch.set_facecolor('#E8EEF2') # Sincronizado con fondo de alta energía
        ax.set_facecolor('#FFFFFF')
        ax.plot(q_arr, p_arr, color='#0F4C75', linewidth=3, label='Curva IPR')
        ax.scatter(qo, pwf, color='#F2A900', s=150, zorder=5, edgecolors='black', label='Punto Operativo')
        ax.set_xlabel('Caudal (STB/d)', fontweight='bold', color='#0F4C75')
        ax.set_ylabel('Pwf (psi)', fontweight='bold', color='#0F4C75')
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()
        st.pyplot(fig, use_container_width=True)

def mostrar_panel_perforacion(gh, ph, dp, tvd, pform):
    c1, c2, c3 = st.columns(3)
    with c1: renderizar_tarjeta_magnetica("Gradiente", gh, "psi/ft")
    with c2: renderizar_tarjeta_magnetica("P. Hidrostática", ph, "psi")
    with c3: renderizar_tarjeta_magnetica("Diferencial (\u0394P)", dp, "psi")
    
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
    c1, c2, c3 = st.columns(3)
    with c1: renderizar_tarjeta_reservorio("Espesor Neto", hn, "ft", "delay-1")
    with c2: renderizar_tarjeta_reservorio("POES", p_mmstb, "MMSTB", "delay-2")
    with c3: renderizar_tarjeta_reservorio("Reservas Rec.", r_mmstb, "MMSTB", "delay-3")
    
    _, col_graf, _ = st.columns([1, 2, 1])
    with col_graf:
        fig, ax = plt.subplots(figsize=(5, 3.5))
        fig.patch.set_facecolor('#E8EEF2')
        ax.set_facecolor('#FFFFFF')
        ax.bar(['POES Original', 'Recuperable'], [p_mmstb, r_mmstb], color=['#0F4C75', '#F2A900'], width=0.6)
        ax.set_ylabel('Volumen (MMSTB)', fontweight='bold', color='#0F4C75')
        st.pyplot(fig, use_container_width=True)
