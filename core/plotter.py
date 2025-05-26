import streamlit as st
import sympy as sp
import numpy as np
import plotly.graph_objects as go
from core.utils import parse_expression

x, y = sp.symbols('x y')

def plot_interactive_function():
    expr_input = st.text_input("f(x, y) para graficar:", "x^2 + y^2")
    st.info("Funciones especiales permitidas: sin(x), cos(x), tan(x), log(x), exp(x), sqrt(x), etc.")

    expression = parse_expression(expr_input)

    a_str = st.text_input("Límite inferior en x:", "0")
    b_str = st.text_input("Límite superior en x:", "1")
    c_str = st.text_input("Límite inferior en y:", "0")
    d_str = st.text_input("Límite superior en y:", "1")

    a = parse_expression(a_str)
    b = parse_expression(b_str)
    c = parse_expression(c_str)
    d = parse_expression(d_str)

    if None in (a, b, c, d, expression):
        st.error("❌ Revisa límites y expresión.")
        return

    try:
        f_lambdified = sp.lambdify((x, y), expression, modules=["numpy"])
        X_vals = np.linspace(float(a), float(b), 100)
        Y_vals = np.linspace(float(c), float(d), 100)
        X, Y = np.meshgrid(X_vals, Y_vals)
        Z = f_lambdified(X, Y)

        fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis')])
        fig.update_layout(
            title="Gráfico Interactivo 3D de f(x, y)",
            scene=dict(
                xaxis_title='x',
                yaxis_title='y',
                zaxis_title='f(x, y)'
            ),
            autosize=True,
            margin=dict(l=0, r=0, t=40, b=0)
        )
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"❌ Error al graficar: {e}")
