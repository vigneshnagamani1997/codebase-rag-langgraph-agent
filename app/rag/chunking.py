import ast

def chunk_python_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    chunks = []

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            chunks.append({
                "name": node.name,
                "type": type(node).__name__,
                "code": ast.get_source_segment(open(file_path).read(), node)
            })

    return chunks