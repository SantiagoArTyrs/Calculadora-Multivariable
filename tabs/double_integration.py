import streamlit as st
import sympy as sp
from core.utils import parse_expression
from core.calculator import show_detailed_double_integral_steps, show_double_integral_volume_steps

x, y = sp.symbols('x y')

def render_double_integration_tab(a, b, c, d):
    st.header("📗 Integración Doble")
    expr_input = st.text_input("Ingrese la funcion f(x, y):", "xy + y2")
    st.info("Funciones especiales permitidas: sin(x), cos(x), tan(x), log(x), exp(x), sqrt(x), asin(x), acos(x), atan(x)")

    expression = parse_expression(expr_input)

    if expression:
        steps, result = show_detailed_double_integral_steps(expression, (a, b), (c, d))
        st.latex(f"\\int_{{{a}}}^{{{b}}} \\int_{{{c}}}^{{{d}}} {sp.latex(expression)} \\, dy \\, dx = {sp.latex(result)}")

        with st.expander("Ver pasos detallados de la solución"):
            for description, equation in steps:
                st.markdown(f"**{description}**")
                st.latex(equation)


def render_double_volume_tab(a, b, c, d):
    st.header("📗 Volumen con Integral Doble")
    expr_input = st.text_input("f(x, y) =", "x2 + y2", key="double_volume_func")
    st.info("Esta función se integrará como volumen bajo la superficie f(x, y). Puedes usar sin(x), xy^2, etc.")

    expression = parse_expression(expr_input)

    if expression:
        steps, result = show_double_integral_volume_steps(expression, (a, b), (c, d))
        st.latex(f"V = \\iint_{{D}} {sp.latex(expression)} \\, dx \\, dy = {sp.latex(result)}")

        with st.expander("Ver pasos detallados de la solución"):
            for description, equation in steps:
                st.markdown(f"**{description}**")
                st.latex(equation)
