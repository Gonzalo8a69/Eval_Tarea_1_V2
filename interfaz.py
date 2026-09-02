import streamlit as st
import streamlit.components.v1 as components

def aplicar_estilos():
    css = """
    <style>
        /* Fondo Principal */
        .stApp { background-color: #F3EFE6; }
        
        /* Tipografía y Títulos */
        p, div, span { font-size: 1.125rem !important; }
        h1 { color: #1A365D !important; font-size: 2.5rem !important; font-weight: bold; }
        h2, h3 { color: #1A365D !important; font-size: 1.75rem !important; }
        .metadato { color: #64748B !important; font-size: 0.875rem !important; text-transform: uppercase; }
        
        /* Tarjetas y Superficies */
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
        
        /* Botones nativos de Streamlit */
        .stButton>button {
            background-color: #1A365D;
            color: #FFFFFF;
            border: none;
            border-radius: 5px;
        }
        .stButton>button:hover { background-color: #C5A880; color: #1A365D; }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)def aplicar_estilos():
    css = """
    <style>
        /* Fondo Principal */
        .stApp { background-color: #F3EFE6; }
        
        /* Tipografía y Títulos Centrados */
        .texto-principal { font-size: 1.125rem !important; color: #333333; line-height: 1.6; }
        h1 { color: #1A365D !important; font-size: 2.5rem !important; font-weight: bold; text-align: center; }
        h2, h3 { color: #1A365D !important; font-size: 1.75rem !important; text-align: center; }
        .metadato { color: #64748B !important; font-size: 1rem !important; text-transform: uppercase; text-align: center; display: block; margin-bottom: 2rem;}
        
        /* Tarjetas de Resultados (Métricas) */
        .tarjeta-resultado {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            border-left: 6px solid #C5A880; 
            margin-bottom: 1rem;
            transition: transform 0.2s ease;
        }
        .tarjeta-resultado:hover { transform: translateY(-3px); }
        .valor-destacado { font-size: 1.75rem !important; font-weight: bold; color: #1A365D; margin-top: 5px; }
        
        /* Nueva Tarjeta para Información (Home) */
        .tarjeta-info {
            background-color: #FFFFFF;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            border-top: 6px solid #1A365D;
            margin: 0 auto;
            max-width: 800px; /* Controla el ancho máximo para mejor lectura */
            text-align: justify;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def renderizar_tarjeta_info(texto):
    """Renderiza una tarjeta HTML para bloques de texto largos."""
    html = f"""
    <div class="tarjeta-info">
        <p class="texto-principal">{texto}</p>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def renderizar_tarjeta(titulo, valor, unidad=""):
    html = f"""
    <div class="tarjeta-resultado">
        <div class="metadato">{titulo}</div>
        <div class="valor-destacado">{valor:,.2f} {unidad}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def inyectar_js_animacion():
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
