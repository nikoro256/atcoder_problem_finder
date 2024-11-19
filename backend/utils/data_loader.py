import os
from pathlib import Path
from models.problem import Problem

current_path = Path.cwd()
parent_path = current_path.parent
data_path = os.path.join(parent_path, "data/")


def read_all_problems():
    """
    指定したフォルダ内のすべてのドキュメントを読み込む。
    
    Returns:
        dict: 各ファイルのパスをキーとして、内容を値とする辞書。
    """
    documents = []

    for root, _, files in os.walk(data_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    if ".gitkeep" not in file_path:
                        content = f.read()
                        problem = Problem(title = file_path[len(data_path):] , 
                                          content = content)
                        documents.append(problem)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    return documents