import streamlit as st
import sympy as sp
from core.utils import parse_expression
from core.calculator import show_detailed_triple_integral_steps, show_triple_integral_volume_steps

def render_triple_integral_tab(ax, bx, ay, by, az, bz):
    st.header("📘 Integral Triple")

    expr_input = st.text_input("Ingrese la funcion f(x, y, z): ", "xyz + 1")
    st.info("Funciones especiales permitidas: sin(x), cos(x), tan(x), log(x), exp(x), sqrt(x), asin(x), acos(x), atan(x)")

    expression = parse_expression(expr_input)

    if expression:
        steps, result = show_detailed_triple_integral_steps(expression, (ax, bx), (ay, by), (az, bz))

        st.latex(f"\\iiint_{{D}} {sp.latex(expression)} \\, dz \\, dy \\, dx = {sp.latex(result)}")

        with st.expander("🧮 Ver pasos detallados de la solución"):
            for description, formula in steps:
                st.markdown(f"**{description}**")
                st.latex(formula)
                
def render_triple_volume_tab(ax, bx, ay, by, az, bz):
    st.header("📘 Volumen con Integral Triple")

    expr_input = st.text_input("Ingrese la funcion f(x, y, z):", "xyz + 1", key="triple_vol_input")
    st.info("Esta función se integrará como volumen bajo la superficie f(x, y, z). Puedes usar sin(x), cos(x), log(x), etc.")

    expression = parse_expression(expr_input)

    if expression:
        steps, result = show_triple_integral_volume_steps(
            expression,
            (ax, bx),
            (ay, by),
            (az, bz)
        )

        st.latex(f"V = \\iiint_{{E}} {sp.latex(expression)} \\, dz \\, dy \\, dx = {sp.latex(result)}")

        with st.expander("🧮 Ver pasos detallados de la solución"):
            for description, formula in steps:
                st.markdown(f"**{description}**")
                st.latex(formula)
