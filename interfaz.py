import streamlit as st
import streamlit.components.v1 as components

def aplicar_estilos():
    """
    Inyecta CSS global para configurar el fondo, tipografía, paleta de colores corporativa
    y el diseño de las tarjetas, asegurando que las etiquetas HTML no sean visibles.
    """
    css = """
    <style>
        /* Fondo Principal */
        .stApp { background-color: #F3EFE6; }
        
        /* Tipografía y Títulos Centrados (Reglas de rem/px) */
        .texto-principal { font-size: 1.125rem !important; color: #333333; line-height: 1.6; text-align: justify; }
        h1 { color: #1A365D !important; font-size: 2.5rem !important; font-weight: bold; text-align: center; }
        h2, h3 { color: #1A365D !important; font-size: 1.75rem !important; text-align: center; margin-bottom: 0.5rem; }
        .metadato-home { color: #64748B !important; font-size: 1rem !important; text-transform: uppercase; text-align: center; display: block; margin-bottom: 2.5rem; }
        .metadato { color: #64748B !important; font-size: 0.875rem !important; text-transform: uppercase; }
        
        /* Tarjetas de Resultados (Métricas de Ingeniería) */
        .tarjeta-resultado {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            border-left: 6px solid #C5A880; /* Color de Acento */
            margin-bottom: 1rem;
            transition: transform 0.2s ease;
        }
        .tarjeta-resultado:hover { transform: translateY(-3px); }
        .valor-destacado { font-size: 1.75rem !important; font-weight: bold; color: #1A365D; margin-top: 5px; }
        
        /* Tarjeta Amplia para Información Técnica (Home) */
        .tarjeta-info {
            background-color: #FFFFFF;
            padding: 35px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08);
            border-top: 6px solid #1A365D; /* Borde superior distintivo */
            margin: 0 auto;
            max-width: 850px; /* Ancho máximo para no fatigar la vista */
        }
        
        /* Modificación de Botones Nativos de Streamlit */
        .stButton>button {
            background-color: #1A365D;
            color: #FFFFFF;
            border: none;
            border-radius: 5px;
            width: 100%;
        }
        .stButton>button:hover { background-color: #C5A880; color: #1A365D; }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def renderizar_tarjeta(titulo, valor, unidad=""):
    """Renderiza una tarjeta HTML para mostrar métricas numéricas dinámicas."""
    html = f"""
    <div class="tarjeta-resultado">
        <div class="metadato">{titulo}</div>
        <div class="valor-destacado">{valor:,.2f} {unidad}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def renderizar_tarjeta_info(texto):
    """Renderiza un contenedor especial (tarjeta) para los párrafos descriptivos en el Home."""
    html = f"""
    <div class="tarjeta-info">
        <p class="texto-principal">{texto}</p>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def inyectar_js_animacion():
    """Inyecta un script JS para un efecto de aparición (fade-in) cumpliendo el requerimiento de interactividad."""
    js = """
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const container = document.querySelector('.stApp');
            if(container) {
                container.style.opacity = '0';
                container.style.transition = 'opacity 0.8s ease-in';
                setTimeout(() => { container.style.opacity = '1'; }, 50);
            }
        });
    </script>
    """
    components.html(js, height=0)
