import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

def aplicar_estilos():
    """Inyecta CSS global con la paleta de alta energía y las clases para animaciones avanzadas."""
    css = """
    <style>
        /* --- FONDO Y TIPOGRAFÍA BASE --- */
        .stApp { background-color: #E8EEF2; }
        .texto-principal { font-size: 1.125rem !important; color: #1E293B; line-height: 1.6; text-align: justify; }
        h1 { color: #0F4C75 !important; font-size: 2.5rem !important; font-weight: 800; text-align: center; }
        h2, h3 { color: #0F4C75 !important; font-size: 1.75rem !important; text-align: center; margin-bottom: 0.5rem; }
        .metadato-home { color: #3282B8 !important; font-size: 1.1rem !important; text-transform: uppercase; text-align: center; display: block; margin-bottom: 2.5rem; font-weight: bold; }
        .metadato { color: #64748B !important; font-size: 0.875rem !important; text-transform: uppercase; font-weight: 600; }
        
        /* --- NAVEGACIÓN Y TABS --- */
        [data-testid="stSidebar"] .stRadio label p, [data-testid="stSidebar"] .stRadio label div { font-size: 1.5rem !important; font-weight: 700 !important; color: #0F4C75 !important; padding: 10px 0; }
        [data-testid="stTabs"] button[data-baseweb="tab"] p { font-size: 1.5rem !important; font-weight: bold !important; color: #0F4C75 !important; }
        
        div[data-baseweb="input"] { background-color: #FFFFFF !important; border: 2px solid #B0C4DE !important; border-radius: 6px !important; }
        div[data-baseweb="input"]:focus-within { border-color: #F2A900 !important; }
        div[data-baseweb="input"] input { color: #0F4C75 !important; font-weight: bold !important; }

        /* --- EFECTO 1: TARJETAS MAGNÉTICAS 3D (TAB PERFORACIÓN) --- */
        .tarjeta-magnetica {
            background-color: #FFFFFF; padding: 20px; border-radius: 8px;
            border-left: 6px solid #F2A900; margin-bottom: 1rem;
            transform-style: preserve-3d; 
            transition: transform 0.1s ease-out, box-shadow 0.1s ease-out;
            will-change: transform;
        }
        .valor-destacado { font-size: 1.85rem !important; font-weight: 900; color: #0F4C75; margin-top: 5px; transform: translateZ(20px); }
        .metadato { transform: translateZ(10px); }

        /* --- EFECTO 2: TARJETA NORMAL Y HOME --- */
        .tarjeta-resultado {
            background-color: #FFFFFF; padding: 20px; border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08); border-left: 6px solid #3282B8; margin-bottom: 1rem;
        }
        .tarjeta-info {
            background-color: #FFFFFF; padding: 35px; border-radius: 10px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.1); border-top: 6px solid #0F4C75; margin: 0 auto; max-width: 850px;
        }

        /* --- EFECTO 3: BOTONES Y RIPPLE LÍQUIDO (TAB PRODUCCIÓN) --- */
        .stButton>button { 
            background: linear-gradient(135deg, #0F4C75, #3282B8) !important; color: #FFFFFF !important; 
            font-weight: bold !important; font-size: 1.1rem !important; border: none !important; 
            border-radius: 6px !important; width: 100%; position: relative; overflow: hidden;   
            box-shadow: 0 4px 6px rgba(15, 76, 117, 0.3); transition: transform 0.1s ease;
        }
        .stButton>button:active { transform: scale(0.96); }
        
        .efecto-ripple-liquido {
            position: absolute; background: radial-gradient(circle, rgba(242,169,0,0.8) 0%, rgba(255,255,255,0) 70%);
            border-radius: 50%; transform: scale(0); animation: animacionRippleLiq 0.8s cubic-bezier(0.1, 0.7, 0.3, 1);
            pointer-events: none; width: 300px; height: 300px; margin-top: -150px; margin-left: -150px;
        }
        @keyframes animacionRippleLiq { to { transform: scale(3); opacity: 0; } }

        /* --- EFECTO 4: SKELETON LOADER (TAB RESERVORIOS) --- */
        .skeleton-box {
            width: 100%; height: 350px; background: linear-gradient(90deg, #E8EEF2 25%, #FFFFFF 50%, #E8EEF2 75%);
            background-size: 200% 100%; animation: skeletonLoading 1.5s infinite; border-radius: 8px;
            margin-top: 10px; display: flex; align-items: center; justify-content: center; color: #B0C4DE; font-weight: bold;
        }
        @keyframes skeletonLoading { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }
        .grafico-oculto { animation: fadeInGrafico 1s ease-in forwards; }
        @keyframes fadeInGrafico { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def renderizar_tarjeta_info(texto):
    """Renderiza el bloque descriptivo del Home con clases para el efecto Cyber-Text."""
    html = f"""<div class="tarjeta-info cyber-text-target"><p class="texto-principal">{texto}</p></div>"""
    st.markdown(html, unsafe_allow_html=True)

def renderizar_tarjeta_magnetica(titulo, valor, unidad=""):
    """Renderiza una tarjeta 3D específica para el Tab de Perforación."""
    html = f"""<div class="tarjeta-magnetica">
                <div class="metadato">{titulo}</div>
                <div class="valor-destacado">{valor:,.2f} {unidad}</div>
              </div>"""
    st.markdown(html, unsafe_allow_html=True)

def renderizar_tarjeta_normal(titulo, valor, unidad=""):
    """Renderiza tarjeta estándar para otros Tabs."""
    html = f"""<div class="tarjeta-resultado">
                <div class="metadato">{titulo}</div>
                <div class="valor-destacado">{valor:,.2f} {unidad}</div>
              </div>"""
    st.markdown(html, unsafe_allow_html=True)

def inyectar_js_animacion():
    """Inyecta el MEGA SCRIPT JS que orquesta los 4 efectos de interactividad solicitados."""
    js = """<script>
        document.addEventListener("DOMContentLoaded", function() {
            const doc = window.parent.document;
            
            // --- 1. EFECTO CYBER-TEXT (HOME) ---
            function desencriptarTexto(element, velocidad = 30) {
                if (element.dataset.cyberDone) return;
                const originalText = element.innerText;
                const caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*<>";
                let iteraciones = 0;
                element.dataset.cyberDone = "true"; // Evita que se repita en el mismo objeto
                
                const intervalo = setInterval(() => {
                    element.innerText = originalText.split("").map((letra, index) => {
                        if (index < iteraciones || letra === " ") return originalText[index];
                        return caracteres[Math.floor(Math.random() * caracteres.length)];
                    }).join("");
                    if (iteraciones >= originalText.length) clearInterval(intervalo);
                    iteraciones += 1/2; // Velocidad de resolución
                }, velocidad);
            }

            // --- 2. EFECTO RIPPLE LÍQUIDO (PRODUCCIÓN) ---
            function aplicarRipple() {
                const botones = doc.querySelectorAll('.stButton > button');
                botones.forEach(btn => {
                    if (!btn.dataset.rippleAgregado) {
                        btn.dataset.rippleAgregado = "true";
                        btn.addEventListener('mousedown', function(e) {
                            // Detectar si estamos en el Tab de Producción (el primer tab activo o buscando texto)
                            const tabActivo = doc.querySelector('[data-baseweb="tab"][aria-selected="true"]');
                            if (tabActivo && tabActivo.innerText.includes("Producción")) {
                                const rect = btn.getBoundingClientRect();
                                const x = e.clientX - rect.left;
                                const y = e.clientY - rect.top;
                                const ripple = doc.createElement('span');
                                ripple.classList.add('efecto-ripple-liquido');
                                ripple.style.left = x + 'px';
                                ripple.style.top = y + 'px';
                                btn.appendChild(ripple);
                                setTimeout(() => ripple.remove(), 800);
                            }
                        });
                    }
                });
            }

            // --- 3. EFECTO TARJETAS MAGNÉTICAS 3D (PERFORACIÓN) ---
            function aplicarTarjetasMagneticas() {
                const tarjetas = doc.querySelectorAll('.tarjeta-magnetica');
                tarjetas.forEach(tarjeta => {
                    if (!tarjeta.dataset.magneticoAgregado) {
                        tarjeta.dataset.magneticoAgregado = "true";
                        tarjeta.addEventListener('mousemove', e => {
                            const rect = tarjeta.getBoundingClientRect();
                            const x = e.clientX - rect.left;
                            const y = e.clientY - rect.top;
                            const centroX = rect.width / 2;
                            const centroY = rect.height / 2;
                            // Rotación máxima de 15 grados
                            const rotX = ((y - centroY) / centroY) * -15; 
                            const rotY = ((x - centroX) / centroX) * 15;
                            tarjeta.style.transform = `perspective(1000px) rotateX(${rotX}deg) rotateY(${rotY}deg) scale3d(1.02, 1.02, 1.02)`;
                            tarjeta.style.boxShadow = `${-rotY}px ${rotX}px 20px rgba(242, 169, 0, 0.2)`;
                        });
                        tarjeta.addEventListener('mouseleave', () => {
                            tarjeta.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
                            tarjeta.style.boxShadow = `none`;
                        });
                    }
                });
            }

            // --- ORQUESTADOR (MUTATION OBSERVER) ---
            // Streamlit recarga el DOM constantemente, necesitamos re-aplicar los efectos
            const observador = new MutationObserver(() => {
                // Cyber-Text para los H1 y H3 del Home
                const titulosHome = doc.querySelectorAll('h1, h3');
                titulosHome.forEach(t => desencriptarTexto(t, 20));
                
                aplicarRipple();
                aplicarTarjetasMagneticas();
                
                // Ocultar Skeletons cuando las gráficas de Streamlit (imágenes) terminan de cargar
                const skeletons = doc.querySelectorAll('.skeleton-box');
                skeletons.forEach(sk => {
                    // Si existe un gráfico adyacente (stImage renderizado por Matplotlib)
                    const contenedorGrafico = sk.parentElement.parentElement.querySelector('[data-testid="stImage"]');
                    if(contenedorGrafico) {
                        sk.style.display = 'none'; // Oculta el esqueleto
                        contenedorGrafico.classList.add('grafico-oculto'); // Añade animación fade-in a la gráfica
                    }
                });
            });
            
            observador.observe(doc.body, { childList: true, subtree: true });
            
            // Ejecución inicial
            setTimeout(() => {
                doc.querySelectorAll('h1, h3').forEach(t => desencriptarTexto(t, 30));
                aplicarRipple();
                aplicarTarjetasMagneticas();
            }, 300);
        });
    </script>"""
    components.html(js, height=0)

# --- COMPONENTES GRÁFICOS MODULARES ---

def mostrar_panel_ipr(qo, qb, qmax, pwf, q_arr, p_arr):
    """PANEL PRODUCCIÓN: Tarjetas normales + Gráfica (Ripple en el botón gestionado por JS)."""
    c1, c2, c3 = st.columns(3)
    with c1: renderizar_tarjeta_normal("Caudal Actual", qo, "STB/d")
    with c2: renderizar_tarjeta_normal("Caudal a Burbuja", qb, "STB/d")
    with c3: renderizar_tarjeta_normal("Caudal Máximo", qmax, "STB/d")
    
    _, col_graf, _ = st.columns([1, 3, 1])
    with col_graf:
        fig, ax = plt.subplots(figsize=(6, 3.5))
        fig.patch.set_facecolor('#E8EEF2')
        ax.set_facecolor('#FFFFFF')
        ax.plot(q_arr, p_arr, color='#0F4C75', linewidth=3, label='Curva IPR')
        ax.scatter(qo, pwf, color='#F2A900', s=150, zorder=5, edgecolors='black', label='Punto Operativo')
        ax.set_xlabel('Caudal (STB/d)', fontweight='bold', color='#0F4C75')
        ax.set_ylabel('Pwf (psi)', fontweight='bold', color='#0F4C75')
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
    """PANEL RESERVORIOS: Inyecta SKELETON LOADER de carga antes del gráfico."""
    c1, c2, c3 = st.columns(3)
    with c1: renderizar_tarjeta_normal("Espesor Neto", hn, "ft")
    with c2: renderizar_tarjeta_normal("POES", p_mmstb, "MMSTB")
    with c3: renderizar_tarjeta_normal("Reservas Rec.", r_mmstb, "MMSTB")
    
    _, col_graf, _ = st.columns([1, 2, 1])
    with col_graf:
        # Inyección del HTML del esqueleto. JS lo ocultará cuando Matplotlib renderice la imagen.
        st.markdown('<div class="skeleton-box">Calculando Volúmenes...</div>', unsafe_allow_html=True)
        
        fig, ax = plt.subplots(figsize=(5, 3.5))
        fig.patch.set_facecolor('#E8EEF2')
        ax.set_facecolor('#FFFFFF')
        ax.bar(['POES Original', 'Recuperable'], [p_mmstb, r_mmstb], color=['#0F4C75', '#F2A900'], width=0.6)
        ax.set_ylabel('Volumen (MMSTB)', fontweight='bold', color='#0F4C75')
        st.pyplot(fig, use_container_width=True)
