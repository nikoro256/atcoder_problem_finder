import os
from pathlib import Path
from models.problem import Problem
from utils.data_loader import read_all_problems

current_path = Path.cwd()
parent_path = current_path.parent
data_path = os.path.join(parent_path, "data/")


class DataTable:
    
    def __init__(self):
        self.problems : list[Problem] = read_all_problems()
        
    def find(self, query_word):
        retrieval_res = {}
        for problem in self.problems:
            if query_word in problem.content:
                retrieval_res[problem.title] = {"type" : "全体一致"}
        return retrieval_res