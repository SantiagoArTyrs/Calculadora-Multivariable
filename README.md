# Calculadora Multivariable en Streamlit 🧠

Esta app permite calcular derivadas, integrales dobles y triples, masa y centroide, y visualizar funciones 3D en tiempo real.
### 🎯 Qué puedes hacer en la app

* **Derivadas parciales**: Calcula derivadas de funciones con 2 variables.
* **Integrales dobles y triples**: Ingresa funciones y límites simbólicos.
* **Masa y centro de masa**: Evalúa densidades en una región.
* **Visualización 3D**: Dibuja gráficamente funciones de 2 variables.

---


  
### ✅ Requisitos previos

Antes de comenzar, asegúrate de tener lo siguiente instalado en tu computador:

1. **Python 3.10 o superior**: [Descargar aquí](https://www.python.org/downloads/)
2. **Git**: [Descargar aquí](https://git-scm.com/downloads)
3. **Editor de código recomendado (opcional)**: Visual Studio Code [descargar aquí](https://code.visualstudio.com/)

---

### 🔧 Paso 1: Clonar el repositorio

1. Abre una ventana de comandos:

   * En Windows: Busca `cmd` y ábrelo.
   * En Mac o Linux: Abre la terminal.
2. Escribe el siguiente comando (reemplaza el enlace si tienes otro):

```bash
git clone https://github.com/TU-USUARIO/TU-REPOSITORIO.git
```

3. Entra al proyecto:

```bash
cd TU-REPOSITORIO
```

---

### 📦 Paso 2: Crear un entorno virtual (opcional pero recomendado)

Esto evita conflictos con otras aplicaciones en tu sistema.

```bash
python -m venv env
```

Para activarlo:

* En Windows:

```bash
env\Scripts\activate
```

* En Mac/Linux:

```bash
source env/bin/activate
```

---

### 📥 Paso 3: Instalar dependencias

Dentro de la carpeta del proyecto, ejecuta:

```bash
pip install -r requirements.txt
```

> Si no tienes un archivo `requirements.txt`, puedes instalar las dependencias manualmente:

```bash
pip install streamlit sympy numpy plotly
```

---

### 🚀 Paso 4: Ejecutar la aplicación

Lanza el proyecto con el siguiente comando:

```bash
streamlit run app.py
```

Verás que se abre una pestaña en tu navegador con la calculadora.

---

### 📚 Si algo falla

* Asegúrate de escribir bien las funciones (usa `^` para potencias, por ejemplo `x^2`).
* Si algo no carga, revisa que estés en la carpeta del proyecto y que hayas activado el entorno virtual.

---
