import streamlit as st
import sympy as sp
from core.utils import parse_expression, guardar_en_historial_json
from core.calculator import show_detailed_double_integral_steps

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

        guardar_en_historial_json({
            "tipo": "Integración doble",
            "expresion": expr_input,
            "resultado": str(result),
            "limites": {
                "x": [str(a), str(b)],
                "y": [str(c), str(d)]
            },
            "pasos": steps
        })
