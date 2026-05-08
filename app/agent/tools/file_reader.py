import ast

def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        return str(e)


def analyze_code(code):
    tree = ast.parse(code)
    functions = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
    classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]

    return {
        "functions": functions,
        "classes": classes
    }