import ast
import os

def build_graph(repo_path):
    graph = {"nodes": [], "edges": []}

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)

                with open(path) as f:
                    tree = ast.parse(f.read())

                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef):
                        graph["nodes"].append({
                            "id": node.name,
                            "file": path
                        })

                        for child in ast.walk(node):
                            if isinstance(child, ast.Call) and hasattr(child.func, "id"):
                                graph["edges"].append({
                                    "source": node.name,
                                    "target": child.func.id
                                })

    return graph