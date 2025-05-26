import sympy as sp

x, y, z = sp.symbols('x y z')

def show_detailed_double_integral_steps(f, x_lim, y_lim):
    steps = []
    x0, x1 = x_lim
    y0, y1 = y_lim

    steps.append(("Planteamiento completo:",
        f"\\int_{{{x0}}}^{{{x1}}} \\left[ \\int_{{{y0}}}^{{{y1}}} {sp.latex(f)} \\, dy \\right] dx"))

    steps.append(("Se integra primero respecto a \\( y \\), manteniendo \\( x \\) constante:", ""))

    if isinstance(f, sp.Add):
        decomposition = " + ".join([sp.latex(term) for term in f.args])
        steps.append(("Descomposición del integrando:", f"{sp.latex(f)} = {decomposition}"))

    raw_y = sp.Integral(f, y)
    steps.append(("Antiderivada respecto a y (sin evaluar):", f"\\int {sp.latex(f)} \\, dy = {sp.latex(raw_y)}"))

    int_y = sp.integrate(f, (y, y0, y1))
    steps.append((f"Evaluando de y={y0} a y={y1}:", f"\\left[ {sp.latex(raw_y)} \\right]_{{y={y0}}}^{{y={y1}}} = {sp.latex(int_y)}"))

    steps.append(("Se integra ahora respecto a \\( x \\):", f"\\int_{{{x0}}}^{{{x1}}} {sp.latex(int_y)} \\, dx"))

    if isinstance(int_y, sp.Add):
        outer_decomposition = " + ".join([sp.latex(term) for term in int_y.args])
        steps.append(("Descomposición del integrando externo:", f"{sp.latex(int_y)} = {outer_decomposition}"))

    raw_x = sp.Integral(int_y, x)
    steps.append(("Antiderivada respecto a x (sin evaluar):", f"\\int {sp.latex(int_y)} \\, dx = {sp.latex(raw_x)}"))

    int_x = sp.integrate(int_y, (x, x0, x1))
    steps.append((f"Evaluando de x={x0} a x={x1}:", f"\\left[ {sp.latex(raw_x)} \\right]_{{x={x0}}}^{{x={x1}}} = {sp.latex(int_x)}"))

    steps.append(("🎉 Resultado final de la integral doble:", f"{sp.latex(int_x)}"))

    return steps, int_x


def show_mass_and_centroid_steps(density, x_lim, y_lim):
    steps = []

    mass = sp.integrate(sp.integrate(density, (y, y_lim[0], y_lim[1])), (x, x_lim[0], x_lim[1]))
    steps.append(("Integral para la masa:", f"M = \\iint_{{D}} {sp.latex(density)} \\, dx \\, dy = {sp.latex(mass)}"))

    x_cm = sp.integrate(sp.integrate(x * density, (y, y_lim[0], y_lim[1])), (x, x_lim[0], x_lim[1])) / mass
    steps.append(("Cálculo de la coordenada x del centro de masa:",
                  f"\\bar{{x}} = \\frac{{\\iint x \\cdot \\rho(x, y) \\, dx \\, dy}}{{M}} = {sp.latex(x_cm)}"))

    y_cm = sp.integrate(sp.integrate(y * density, (y, y_lim[0], y_lim[1])), (x, x_lim[0], x_lim[1])) / mass
    steps.append(("Cálculo de la coordenada y del centro de masa:",
                  f"\\bar{{y}} = \\frac{{\\iint y \\cdot \\rho(x, y) \\, dx \\, dy}}{{M}} = {sp.latex(y_cm)}"))

    return steps, mass, x_cm, y_cm


def show_detailed_triple_integral_steps(f, x_lim, y_lim, z_lim):
    steps = []
    x0, x1 = x_lim
    y0, y1 = y_lim
    z0, z1 = z_lim

    steps.append(("Planteamiento de la integral triple:",
        f"\\iiint_{{D}} {sp.latex(f)} \\, dz \\, dy \\, dx = \\int_{{{x0}}}^{{{x1}}} \\int_{{{y0}}}^{{{y1}}} \\int_{{{z0}}}^{{{z1}}} {sp.latex(f)} \\, dz \\, dy \\, dx"))

    if isinstance(f, sp.Add):
        decomposition = " + ".join([sp.latex(term) for term in f.args])
        steps.append(("Descomposición del integrando:", f"{sp.latex(f)} = {decomposition}"))

    raw_z = sp.Integral(f, z)
    steps.append(("Paso 1: Antiderivada respecto a z:", f"\\int {sp.latex(f)} \\, dz = {sp.latex(raw_z)}"))

    int_z = sp.integrate(f, (z, z0, z1))
    steps.append((f"Evaluando de z={z0} a z={z1}:", f"\\left[ {sp.latex(raw_z)} \\right]_{{z={z0}}}^{{z={z1}}} = {sp.latex(int_z)}"))

    raw_y = sp.Integral(int_z, y)
    steps.append(("Paso 2: Antiderivada respecto a y:", f"\\int {sp.latex(int_z)} \\, dy = {sp.latex(raw_y)}"))

    int_y = sp.integrate(int_z, (y, y0, y1))
    steps.append((f"Evaluando de y={y0} a y={y1}:", f"\\left[ {sp.latex(raw_y)} \\right]_{{y={y0}}}^{{y={y1}}} = {sp.latex(int_y)}"))

    raw_x = sp.Integral(int_y, x)
    steps.append(("Paso 3: Antiderivada respecto a x:", f"\\int {sp.latex(int_y)} \\, dx = {sp.latex(raw_x)}"))

    int_x = sp.integrate(int_y, (x, x0, x1))
    steps.append((f"Evaluando de x={x0} a x={x1}:", f"\\left[ {sp.latex(raw_x)} \\right]_{{x={x0}}}^{{x={x1}}} = {sp.latex(int_x)}"))

    steps.append(("🎉 Resultado final de la integral triple:", f"{sp.latex(int_x)}"))

    return steps, int_x
