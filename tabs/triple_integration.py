import streamlit as st
import sympy as sp
from core.utils import parse_expression, guardar_en_historial_json
from core.calculator import show_detailed_triple_integral_steps

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

        guardar_en_historial_json({
            "tipo": "Integral triple",
            "expresion": expr_input,
            "resultado": str(result),
            "limites": {
                "x": [str(ax), str(bx)],
                "y": [str(ay), str(by)],
                "z": [str(az), str(bz)]
            },
            "pasos": steps
        })
