import streamlit as st
import matplotlib.pyplot as plt

# Importación de la estructura modular interna
from modelos import ReservorioSubsaturado, DatosPozo, PropiedadesPetrofisicas
from validaciones import validar_ipr, validar_perforacion, validar_poes
from calculos import calcular_ipr, calcular_hidrostatica, calcular_volumetria

# IMPORTACIÓN CORREGIDA: Se incluyó renderizar_tarjeta_info
from interfaz import aplicar_estilos, renderizar_tarjeta, renderizar_tarjeta_info, inyectar_js_animacion

# Configuración base de la aplicación
st.set_page_config(page_title="Data Analytics Oil & Gas", layout="wide")
aplicar_estilos()

# Estructura obligatoria de navegación
menu = st.sidebar.radio("Navegación", ["Home", "Ejercicios"])

if menu == "Home":
    # Uso de HTML seguro para centrar los títulos e inyectar el CSS configurado
    st.markdown("<h1>Plataforma de Analítica para Oil & Gas</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Desarrollado por: JOSE GONZALO OCHOA PAZ</h3>", unsafe_allow_html=True)
    st.markdown("<span class='metadato-home'>Programa: Bootcamp Data Analytics for Oil & Gas</span>", unsafe_allow_html=True)
    
    # Texto descriptivo encapsulado en la nueva tarjeta visual
    texto_proposito = (
        "Esta aplicación web profesional está diseñada para ejecutar cálculos críticos de ingeniería petrolera. "
        "A través de un enfoque modular, resuelve escenarios técnicos en las áreas de Producción, Perforación "
        "y Reservorios, integrando visualizaciones dinámicas y análisis paramétrico para la toma de decisiones "
        "ágil y fundamentada en operaciones de campo."
    )
    renderizar_tarjeta_info(texto_proposito)
    
    # Interacción JS requerida
    inyectar_js_animacion()

elif menu == "Ejercicios":
    # Tabs obligatorios para los módulos técnicos
    tab1, tab2, tab3 = st.tabs(["Producción", "Perforación", "Reservorios"])
    
    # ---------------- TAB 1: PRODUCCIÓN (IPR) ----------------
    with tab1:
        st.header("Análisis de IPR Compuesta")
        c1, c2 = st.columns(2)
        pr = c1.number_input("Presión de Reservorio (Pr) [psi]", value=3000.0, step=100.0)
        pb = c1.number_input("Presión de Burbuja (Pb) [psi]", value=2000.0, step=100.0)
        j = c2.number_input("Índice de Productividad (J) [STB/d/psi]", value=1.5, step=0.1)
        pwf = c2.number_input("Presión de Fondo (Pwf) actual [psi]", value=1500.0, step=100.0)
        
        if st.button("Calcular IPR"):
            valido, msg = validar_ipr(pr, pb, j, pwf)
            if valido:
                res = ReservorioSubsaturado(pr, pb, j)
                qo, qb, qmax, estado, p_arr, q_arr = calcular_ipr(res, pwf)
                
                st.info(f"**Condición de Flujo:** {estado}")
                col1, col2, col3 = st.columns(3)
                with col1: renderizar_tarjeta("Caudal Actual", qo, "STB/d")
                with col2: renderizar_tarjeta("Caudal a Burbuja", qb, "STB/d")
                with col3: renderizar_tarjeta("Caudal Máximo", qmax, "STB/d")
                
                # Gráfico de Curva IPR
                fig, ax = plt.subplots(figsize=(7, 4))
                fig.patch.set_facecolor('#F3EFE6') 
                ax.set_facecolor('#FFFFFF')
                ax.plot(q_arr, p_arr, color='#1A365D', linewidth=2.5, label='Curva IPR')
                ax.scatter(qo, pwf, color='#C5A880', s=120, zorder=5, label='Punto Operativo')
                ax.set_xlabel('Caudal (STB/d)', fontweight='bold', color='#1A365D')
                ax.set_ylabel('Pwf (psi)', fontweight='bold', color='#1A365D')
                ax.grid(True, linestyle='--', alpha=0.5)
                ax.legend()
                st.pyplot(fig)
            else:
                st.error(msg)
                
    # ---------------- TAB 2: PERFORACIÓN ----------------
    with tab2:
        st.header("Perfil de Presión Hidrostática")
        c1, c2 = st.columns(2)
        mw = c1.number_input("Peso del Lodo (MW) [ppg]", value=10.0, step=0.1)
        pform = c2.number_input("Presión de Formación [psi]", value=4000.0, step=100.0)
        md = c1.number_input("Profundidad Medida (MD) [ft]", value=9000.0, step=100.0)
        tvd = c2.number_input("Profundidad Vertical (TVD) [ft]", value=8500.0, step=100.0)
        
        if st.button("Calcular Presiones"):
            valido, msg = validar_perforacion(mw, md, tvd, pform)
            if valido:
                pozo = DatosPozo(mw, md, tvd, pform)
                gh, ph, dp, cond = calcular_hidrostatica(pozo)
                
                st.info(f"**Condición Operativa:** {cond}")
                col1, col2, col3 = st.columns(3)
                with col1: renderizar_tarjeta("Gradiente", gh, "psi/ft")
                with col2: renderizar_tarjeta("P. Hidrostática", ph, "psi")
                with col3: renderizar_tarjeta("Diferencial (\u0394P)", dp, "psi")
                
                # Gráfico Hidrostático
                fig, ax = plt.subplots(figsize=(4, 6))
                fig.patch.set_facecolor('#F3EFE6')
                ax.set_facecolor('#FFFFFF')
                ax.plot([0, ph], [0, tvd], color='#1A365D', linewidth=2.5, label='P. Hidrostática')
                ax.scatter(pform, tvd, color='#C5A880', s=100, label='P. Formación')
                ax.invert_yaxis()
                ax.set_xlabel('Presión (psi)', fontweight='bold', color='#1A365D')
                ax.set_ylabel('Profundidad TVD (ft)', fontweight='bold', color='#1A365D')
                ax.grid(True, linestyle='--', alpha=0.5)
                ax.legend()
                st.pyplot(fig)
            else:
                st.error(msg)
                
    # ---------------- TAB 3: RESERVORIOS (POES) ----------------
    with tab3:
        st.header("Estimación Volumétrica")
        c1, c2, c3 = st.columns(3)
        area = c1.number_input("Área [acres]", value=500.0, step=50.0)
        h = c2.number_input("Espesor (h) [ft]", value=100.0, step=10.0)
        ntg = c3.number_input("Net-to-Gross [frac]", value=0.8, step=0.05)
        poro = c1.number_input("Porosidad [frac]", value=0.2, step=0.02)
        swi = c2.number_input("Swi [frac]", value=0.25, step=0.02)
        boi = c3.number_input("Boi [rb/STB]", value=1.2, step=0.05)
        fr = c1.number_input("Factor de Recobro [frac]", value=0.3, step=0.05)
        
        if st.button("Calcular POES"):
            valido, msg = validar_poes(area, h, ntg, poro, swi, boi, fr)
            if valido:
                prop = PropiedadesPetrofisicas(area, h, ntg, poro, swi, boi, fr)
                hn, p_stb, p_mmstb, r_stb, r_mmstb = calcular_volumetria(prop)
                
                col1, col2, col3 = st.columns(3)
                with col1: renderizar_tarjeta("Espesor Neto", hn, "ft")
                with col2: renderizar_tarjeta("POES", p_mmstb, "MMSTB")
                with col3: renderizar_tarjeta("Reservas Rec.", r_mmstb, "MMSTB")
                
                # Gráfico Comparativo
                fig, ax = plt.subplots(figsize=(6, 4))
                fig.patch.set_facecolor('#F3EFE6')
                ax.set_facecolor('#FFFFFF')
                ax.bar(['POES Original', 'Recuperable'], [p_mmstb, r_mmstb], color=['#1A365D', '#C5A880'])
                ax.set_ylabel('Volumen (MMSTB)', fontweight='bold', color='#1A365D')
                st.pyplot(fig)
            else:
                st.error(msg)
