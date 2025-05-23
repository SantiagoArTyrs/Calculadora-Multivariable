import streamlit as st
import sympy as sp
from core.utils import parse_expression, save_result

# Import sections
from tabs.derivation import render_derivation_tab
from tabs.double_integration import render_double_integration_tab, render_double_volume_tab
from tabs.mass_centroid import render_mass_and_centroid_tab
from tabs.triple_integration import render_triple_integral_tab, render_triple_volume_tab
from tabs.visualization import render_visualization_tab

# Symbolic variables
x, y, z = sp.symbols('x y z')

st.set_page_config(page_title="Calculadora Multivariable", layout="centered")
st.title("🧠 Calculadora Multivariable")
st.markdown("Calcula derivadas, integrales dobles y triples, masa y centroide. Visualiza todo en 3D.")

# Historial de cálculos
if 'historial' not in st.session_state:
    st.session_state.historial = []

# Tabs principales
tabs = st.tabs(["🧠 Derivación", "📗 Integración Doble", "📘 Integral Triple", "⚖️ Masa y Centro de Masa", "📊 Visualización 3D"])

# Tab 1: Derivación
with tabs[0]:
    render_derivation_tab()

# Tab 2: Doble Integración
with tabs[1]:
    st.markdown("### 📐 Límites para x y y")
    a = parse_expression(st.text_input("Límite inferior en x:", "0", key="a1"))
    b = parse_expression(st.text_input("Límite superior en x:", "1", key="b1"))
    c = parse_expression(st.text_input("Límite inferior en y:", "0", key="c1"))
    d = parse_expression(st.text_input("Límite superior en y:", "1", key="d1"))
    if None in (a, b, c, d):
        st.warning("Revisa los límites de integración.")
    else:
        render_double_integration_tab(a, b, c, d)
        render_double_volume_tab(a, b, c, d)

# Tab 3: Integral Triple
with tabs[2]:
    st.markdown("### 📐 Límites para x, y y z")
    ax = parse_expression(st.text_input("Límite inferior en x:", "0", key="tx0"))
    bx = parse_expression(st.text_input("Límite superior en x:", "1", key="tx1"))
    ay = parse_expression(st.text_input("Límite inferior en y:", "0", key="ty0"))
    by = parse_expression(st.text_input("Límite superior en y:", "1", key="ty1"))
    az = parse_expression(st.text_input("Límite inferior en z:", "0", key="tz0"))
    bz = parse_expression(st.text_input("Límite superior en z:", "1", key="tz1"))
    if None in (ax, bx, ay, by, az, bz):
        st.warning("Revisa los límites de integración triple.")
    else:
        render_triple_integral_tab(ax, bx, ay, by, az, bz)
        render_triple_volume_tab(ax, bx, ay, by, az, bz)

# Tab 4: Masa y Centroide
with tabs[3]:
    st.markdown("### 📐 Límites para x y y")
    a = parse_expression(st.text_input("Límite inferior en x:", "0", key="mx1"))
    b = parse_expression(st.text_input("Límite superior en x:", "1", key="mx2"))
    c = parse_expression(st.text_input("Límite inferior en y:", "0", key="my1"))
    d = parse_expression(st.text_input("Límite superior en y:", "1", key="my2"))
    if None in (a, b, c, d):
        st.warning("Revisa los límites de integración.")
    else:
        render_mass_and_centroid_tab(a, b, c, d)

# Tab 5: Visualización
with tabs[4]:
    render_visualization_tab()

# Descargar historial
st.sidebar.header("📝 Historial de Cálculos")
historial_text = "\n".join(st.session_state.historial)
st.sidebar.download_button("📥 Descargar Historial", historial_text, file_name="historial_calculos.txt")
