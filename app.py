import streamlit as st
import matplotlib.pyplot as plt

# Importaciones modulares
from modelos import ReservorioSubsaturado, DatosPozo, PropiedadesPetrofisicas
from validaciones import validar_ipr, validar_perforacion, validar_poes
from calculos import calcular_ipr, calcular_hidrostatica, calcular_volumetria
from interfaz import aplicar_estilos, renderizar_tarjeta, inyectar_js_animacion

# Configuración y Estilos
st.set_page_config(page_title="Oil & Gas Analytics", layout="wide")
aplicar_estilos()

# Navegación estricta
menu = st.sidebar.radio("Navegación Principal", ["Home", "Ejercicios"])

if menu == "Home":
    st.title("Plataforma de Analítica para Oil & Gas")
    st.markdown("### Desarrollado por: JOSE GONZALO OCHOA PAZ")
    st.markdown("<p class='metadato'>Programa: Bootcamp Data Analytics for Oil & Gas</p>", unsafe_allow_html=True)
    st.write("---")
    st.write("Esta aplicación web profesional está diseñada para ejecutar cálculos críticos de ingeniería petrolera. A través de un enfoque modular, resuelve escenarios técnicos en las áreas de Producción, Perforación y Reservorios, integrando visualizaciones dinámicas para la toma de decisiones.")
    inyectar_js_animacion()

elif menu == "Ejercicios":
    tab1, tab2, tab3 = st.tabs(["Producción (IPR)", "Perforación (Presiones)", "Reservorios (POES)"])
    
    # --- TAB 1: PRODUCCIÓN ---
    with tab1:
        st.header("Análisis de IPR Compuesta")
        c1, c2 = st.columns(2)
        pr = c1.number_input("Presión Reservorio (Pr) [psi]", value=3000.0)
        pb = c1.number_input("Presión Burbuja (Pb) [psi]", value=2000.0)
        j = c2.number_input("Índice de Productividad (J)", value=1.5)
        pwf = c2.number_input("Pwf Actual [psi]", value=1500.0)
        
        if st.button("Calcular Curva IPR"):
            valido, msg = validar_ipr(pr, pb, j, pwf)
            if valido:
                res = ReservorioSubsaturado(pr, pb, j)
                qo, qb, qmax, estado, p_arr, q_arr = calcular_ipr(res, pwf)
                
                st.info(f"**Régimen actual:** {estado}")
                col1, col2, col3 = st.columns(3)
                with col1: renderizar_tarjeta("Caudal Actual (qo)", qo, "STB/d")
                with col2: renderizar_tarjeta("Caudal a Burbuja (qb)", qb, "STB/d")
                with col3: renderizar_tarjeta("Caudal Máximo (qmax)", qmax, "STB/d")
                
                # Gráfica optimizada con etiquetas en negrilla
                fig, ax = plt.subplots(figsize=(7, 4))
                ax.plot(q_arr, p_arr, color='#1f3b4d', linewidth=2, label='Curva IPR')
                ax.scatter(qo, pwf, color='#d35400', s=100, label='Punto Operativo', zorder=5)
                ax.set_xlabel('Caudal (STB/d)', fontweight='bold')
                ax.set_ylabel('Presión de Fondo Pwf (psi)', fontweight='bold')
                ax.grid(True, linestyle='--', alpha=0.6)
                ax.legend()
                st.pyplot(fig)
            else:
                st.error(msg)
                
    # --- TAB 2: PERFORACIÓN ---
    with tab2:
        st.header("Perfil de Presión Hidrostática")
        c1, c2 = st.columns(2)
        mw = c1.number_input("Peso Lodo (MW) [ppg]", value=10.0)
        pform = c2.number_input("Presión Formación [psi]", value=4000.0)
        md = c1.number_input("Profundidad Medida (MD) [ft]", value=9000.0)
        tvd = c2.number_input("Profundidad Vertical (TVD) [ft]", value=8500.0)
        
        if st.button("Evaluar Pozo"):
            valido, msg = validar_perforacion(mw, md, tvd, pform)
            if valido:
                pozo = DatosPozo(mw, md, tvd, pform)
                gh, ph, dp, cond = calcular_hidrostatica(pozo)
                
                st.info(f"**Condición de Balance:** {cond}")
                col1, col2, col3 = st.columns(3)
                with col1: renderizar_tarjeta("Gradiente", gh, "psi/ft")
                with col2: renderizar_tarjeta("P. Hidrostática", ph, "psi")
                with col3: renderizar_tarjeta("Diferencial (\u0394P)", dp, "psi")
                
                # Gráfica de perfil de presión
                fig, ax = plt.subplots(figsize=(4, 6))
                ax.plot([0, ph], [0, tvd], color='#1f3b4d', linewidth=2, label='Presión Lodo')
                ax.scatter(pform, tvd, color='red', s=80, label='P. Formación')
                ax.invert_yaxis() # Profundidad hacia abajo
                ax.set_xlabel('Presión (psi)', fontweight='bold')
                ax.set_ylabel('TVD (ft)', fontweight='bold')
                ax.grid(True, linestyle='--', alpha=0.5)
                ax.legend()
                st.pyplot(fig)
            else:
                st.error(msg)
                
    # --- TAB 3: RESERVORIOS ---
    with tab3:
        st.header("Estimación Volumétrica (POES)")
        c1, c2, c3 = st.columns(3)
        area = c1.number_input("Área [acres]", value=500.0)
        h = c2.number_input("Espesor (h) [ft]", value=100.0)
        ntg = c3.number_input("Net-to-Gross [frac]", value=0.8)
        poro = c1.number_input("Porosidad [frac]", value=0.2)
        swi = c2.number_input("Swi [frac]", value=0.25)
        boi = c3.number_input("Boi [rb/STB]", value=1.2)
        fr = c1.number_input("Factor de Recobro [frac]", value=0.3)
        
        if st.button("Calcular Volúmenes"):
            valido, msg = validar_poes(area, h, ntg, poro, swi, boi, fr)
            if valido:
                prop = PropiedadesPetrofisicas(area, h, ntg, poro, swi, boi, fr)
                hn, p_stb, p_mmstb, r_stb, r_mmstb = calcular_volumetria(prop)
                
                col1, col2, col3 = st.columns(3)
                with col1: renderizar_tarjeta("Espesor Neto", hn, "ft")
                with col2: renderizar_tarjeta("POES", p_mmstb, "MMSTB")
                with col3: renderizar_tarjeta("Reservas Rec.", r_mmstb, "MMSTB")
                
                # Gráfico de barras comparativo
                fig, ax = plt.subplots(figsize=(6, 4))
                categorias = ['POES', 'Recuperable']
                valores = [p_mmstb, r_mmstb]
                ax.bar(categorias, valores, color=['#1f3b4d', '#d35400'])
                ax.set_ylabel('Volumen (MMSTB)', fontweight='bold')
                st.pyplot(fig)
            else:
                st.error(msg)