import streamlit as st
import sympy as sp
from core.utils import parse_expression, guardar_en_historial_json

x, y = sp.symbols('x y')

def render_derivation_tab():
    st.header("🧠 Derivación Parcial")

    expr_input = st.text_input("✏️ Ingresa la función f(x, y):", "x^2 * y + y^3")
    st.info("Funciones especiales permitidas: sin(x), cos(x), tan(x), log(x), exp(x), sqrt(x), asin(x), acos(x), atan(x)")

    parsed_expr = parse_expression(expr_input)

    if parsed_expr:
        st.latex(f"f(x, y) = {sp.latex(parsed_expr)}")

        first_order_dx = sp.diff(parsed_expr, x)
        first_order_dy = sp.diff(parsed_expr, y)

        st.subheader("📘 Derivadas Parciales de Primer Orden")
        st.latex(f"\\frac{{\\partial f}}{{\\partial x}} = {sp.latex(first_order_dx)}")
        st.latex(f"\\frac{{\\partial f}}{{\\partial y}} = {sp.latex(first_order_dy)}")

        second_order_dxx = sp.diff(parsed_expr, x, x)
        second_order_dyy = sp.diff(parsed_expr, y, y)
        second_order_dxy = sp.diff(sp.diff(parsed_expr, x), y)
        second_order_dyx = sp.diff(sp.diff(parsed_expr, y), x)

        st.subheader("📙 Derivadas Parciales de Segundo Orden")
        st.latex(f"\\frac{{\\partial^2 f}}{{\\partial x^2}} = {sp.latex(second_order_dxx)}")
        st.latex(f"\\frac{{\\partial^2 f}}{{\\partial y^2}} = {sp.latex(second_order_dyy)}")
        st.latex(f"\\frac{{\\partial^2 f}}{{\\partial x \\partial y}} = {sp.latex(second_order_dxy)}")
        st.latex(f"\\frac{{\\partial^2 f}}{{\\partial y \\partial x}} = {sp.latex(second_order_dyx)}")

        hessian_matrix = sp.Matrix([
            [second_order_dxx, second_order_dxy],
            [second_order_dyx, second_order_dyy]
        ])

        st.subheader("📐 Matriz Hessiana de f(x, y)")
        st.latex(f"H(f) = {sp.latex(hessian_matrix)}")

        # Guardar en historial
        guardar_en_historial_json({
            "tipo": "Derivación",
            "expresion": expr_input,
            "resultado": f"∂f/∂x = {first_order_dx}, ∂f/∂y = {first_order_dy}",
            "pasos": [
                ["∂f/∂x", sp.latex(first_order_dx)],
                ["∂f/∂y", sp.latex(first_order_dy)],
                ["∂²f/∂x²", sp.latex(second_order_dxx)],
                ["∂²f/∂y²", sp.latex(second_order_dyy)],
                ["∂²f/∂x∂y", sp.latex(second_order_dxy)],
                ["∂²f/∂y∂x", sp.latex(second_order_dyx)],
                ["Hessiana", sp.latex(hessian_matrix)]
            ]
        })
