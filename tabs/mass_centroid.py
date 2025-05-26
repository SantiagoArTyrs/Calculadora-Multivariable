import streamlit as st
import sympy as sp
from core.utils import parse_expression
from core.calculator import show_mass_and_centroid_steps

x, y = sp.symbols('x y')

def render_mass_and_centroid_tab(a, b, c, d):
    st.header("⚖️ Masa y Centro de Masa")

    density_input = st.text_input("ρ(x, y) =", "x^2 + y^2", key="density_mass")
    st.info("Funciones especiales permitidas: sin(x), cos(x), tan(x), log(x), exp(x), sqrt(x), etc.")

    density = parse_expression(density_input)

    if density:
        steps, mass, x_cm, y_cm = show_mass_and_centroid_steps(density, (a, b), (c, d))
        st.latex(f"M = {sp.latex(mass)}")
        st.latex(f"\\bar{{x}} = {sp.latex(x_cm)} \\quad \\bar{{y}} = {sp.latex(y_cm)}")

        with st.expander("🧮 Ver pasos detallados de la solución"):
            for description, formula in steps:
                st.markdown(f"**{description}**")
                st.latex(formula)

        st.info("Nota: El centroide (x̄, ȳ) es el punto donde se encuentra el centro de masa de la figura.")
