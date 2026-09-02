import streamlit as st
import streamlit.components.v1 as components

def aplicar_estilos():
    """Inyecta CSS con la jerarquía tipográfica y paleta corporativa solicitada."""
    css = """
    <style>
        /* Fondo general */
        .stApp { background-color: #f8f9fa; }
        
        /* Reglas Tipográficas */
        p, div, span { font-size: 1.125rem !important; color: #333333; } /* 18px */
        h1 { font-size: 2.5rem !important; color: #1f3b4d; font-weight: bold; } /* 40px */
        h2, h3 { font-size: 1.75rem !important; color: #2c3e50; } /* 28px */
        .metadato { font-size: 0.875rem !important; color: #7f8c8d; } /* 14px */
        
        /* Diseño de Tarjetas */
        .tarjeta-resultado {
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            border-left: 6px solid #d35400;
            margin-bottom: 1rem;
            transition: transform 0.3s ease;
        }
        .tarjeta-resultado:hover { transform: translateY(-3px); }
        .valor-destacado { font-size: 1.75rem !important; font-weight: bold; color: #1f3b4d; margin-top: 5px;}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def renderizar_tarjeta(titulo, valor, unidad=""):
    """Crea una tarjeta HTML dinámica."""
    html = f"""
    <div class="tarjeta-resultado">
        <div class="metadato">{titulo.upper()}</div>
        <div class="valor-destacado">{valor:,.2f} {unidad}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def inyectar_js_animacion():
    """Implementa una interacción visible mediante JavaScript."""
    js = """
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            console.log("Aplicación Oil & Gas cargada exitosamente.");
            // Efecto de aparición suave para el contenedor principal
            const app = document.querySelector('.stApp');
            if(app) {
                app.style.opacity = '0';
                app.style.transition = 'opacity 1s ease-in-out';
                setTimeout(() => { app.style.opacity = '1'; }, 100);
            }
        });
    </script>
    """
    components.html(js, height=0)