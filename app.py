import streamlit as st
import sympy as sp
from core.utils import parse_expression, cargar_historial

# Import sections
from tabs.derivation import render_derivation_tab
from tabs.double_integration import render_double_integration_tab
from tabs.mass_centroid import render_mass_and_centroid_tab
from tabs.triple_integration import render_triple_integral_tab
from tabs.visualization import render_visualization_tab

# Symbolic variables
x, y, z = sp.symbols('x y z')

st.set_page_config(page_title="Calculadora Multivariable", layout="centered")
st.title("🧠 Calculadora Multivariable")
st.markdown("Calcula derivadas, integrales dobles y triples, masa y centroide. Visualiza todo en 3D.")

# Leer parámetros de URL para navegación desde historial
query_params = st.query_params
redirect_tipo = query_params.get("tipo", [None])[0]


# Sidebar menu
section = st.sidebar.radio("Selecciona una sección:", [
    "🧠 Derivacion",
    "📗 Integración doble",
    "📘 Integral Triple",
    "⚖️ Masa y Centro de Masa",
    "📊 Visualización 3D",
    "📜 Historial de Cálculos"
])

# Cambiar automáticamente de sección si viene de historial
if redirect_tipo:
    mapping = {
        "Derivación": "🧠 Derivacion",
        "Integración doble": "📗 Integración doble",
        "Integral triple": "📘 Integral Triple",
        "Masa y Centroide": "⚖️ Masa y Centro de Masa"
    }
    section = mapping.get(redirect_tipo, section)

# Límite para 2D (x, y)
if section in ["📗 Integración doble", "⚖️ Masa y Centro de Masa"]:
    st.sidebar.markdown("📐 **Límites para x y y:**")
    st.sidebar.info("Puedes usar expresiones como: pi, sqrt(2), log(3), etc.")
    a = parse_expression(st.sidebar.text_input("Límite inferior en x:", "0", key="a1"))
    b = parse_expression(st.sidebar.text_input("Límite superior en x:", "1", key="b1"))
    c = parse_expression(st.sidebar.text_input("Límite inferior en y:", "0", key="c1"))
    d = parse_expression(st.sidebar.text_input("Límite superior en y:", "1", key="d1"))
    if None in (a, b, c, d):
        st.warning("Revisa los límites de integración.")
        st.stop()

# Límite para integración triple
if section == "📘 Integral Triple":
    st.sidebar.markdown("📐 **Límites para x, y y z:**")
    st.sidebar.info("Puedes usar expresiones como: pi, sqrt(2), log(3), etc.")
    ax = parse_expression(st.sidebar.text_input("Límite inferior en x:", "0", key="tx0"))
    bx = parse_expression(st.sidebar.text_input("Límite superior en x:", "1", key="tx1"))
    ay = parse_expression(st.sidebar.text_input("Límite inferior en y:", "0", key="ty0"))
    by = parse_expression(st.sidebar.text_input("Límite superior en y:", "1", key="ty1"))
    az = parse_expression(st.sidebar.text_input("Límite inferior en z:", "0", key="tz0"))
    bz = parse_expression(st.sidebar.text_input("Límite superior en z:", "1", key="tz1"))
    if None in (ax, bx, ay, by, az, bz):
        st.warning("Revisa los límites de integración triple.")
        st.stop()

# Render de la sección activa
if section == "🧠 Derivacion":
    render_derivation_tab()

elif section == "📗 Integración doble":
    render_double_integration_tab(a, b, c, d)

elif section == "⚖️ Masa y Centro de Masa":
    render_mass_and_centroid_tab(a, b, c, d)

elif section == "📘 Integral Triple":
    render_triple_integral_tab(ax, bx, ay, by, az, bz)

elif section == "📊 Visualización 3D":
    render_visualization_tab()

elif section == "📜 Historial de Cálculos":
    st.header("📜 Historial de Cálculos Guardados")
    historial = cargar_historial()
    if not historial:
        st.info("No hay cálculos guardados todavía.")
    else:
        for idx, entry in enumerate(historial[::-1]):
            tipo = entry.get("tipo", "Desconocido")
            funcion = entry.get("expresion", "")
            resultado = entry.get("resultado", "")
            with st.expander(f"{tipo}: f(x,y,z) = {funcion}"):
                st.markdown(f"**Resultado:** {resultado}")
                if entry.get("limites"):
                    st.markdown("**Límites:**")
                    st.json(entry["limites"])
                if entry.get("pasos"):
                    st.markdown("**Pasos:**")
                    for paso in entry["pasos"]:
                        st.markdown(f"**{paso[0]}**")
                        st.latex(paso[1])
                

