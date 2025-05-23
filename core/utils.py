import sympy as sp
import numpy as np
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor
)

# Dictionary of allowed special functions for parsing
special_functions = {
    'sin': sp.sin,
    'cos': sp.cos,
    'tan': sp.tan,
    'log': sp.log,
    'ln': sp.log,
    'sqrt': sp.sqrt,
    'exp': sp.exp,
    'pi': sp.pi,
    'e': sp.E
}

# Parser transformations: allow implicit multiplication and ^ for powers
transformations = standard_transformations + (
    implicit_multiplication_application,
    convert_xor
)

def parse_expression(expression_str):
    try:
        return parse_expr(expression_str, transformations=transformations, local_dict=special_functions)
    except Exception as e:
        print("❌ Failed to parse expression:", e)
        return None

def validate_expression(expression_str):
    try:
        return sp.sympify(expression_str)
    except Exception as e:
        print("❌ Invalid expression:", e)
        return None

def validate_range(range_str):
    try:
        parts = list(map(float, range_str.strip().split()))
        if len(parts) != 2 or parts[0] >= parts[1]:
            print("❌ Range must be in format: a b with a < b")
            return None
        return parts
    except:
        print("❌ Error: Enter two valid numbers separated by a space.")
        return None

def convert_to_numpy_function(sym_function, variables):
    try:
        return sp.lambdify(variables, sym_function, modules=['numpy'])
    except Exception as e:
        print("❌ Failed to convert function:", e)
        return None

def save_result(text, file_name="results.txt"):
    try:
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(text + "\n")
        print(f"📁 Result saved in {file_name}")
    except Exception as e:
        print("❌ Failed to save result:", e)

def evaluate_symbolic(value_str):
    try:
        return float(sp.sympify(value_str, locals=special_functions).evalf())
    except Exception as e:
        print("❌ Failed to interpret symbolic value:", e)
        return None
