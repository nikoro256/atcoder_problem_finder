import os
from pathlib import Path
from models.problem import Problem
from utils.data_loader import read_all_problems
from utils.filepath_analyzer import parse_file_path

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
                problem_data = {"type" : "全体一致"}
                contest_name, problem_name = parse_file_path(problem.title)
                problem_data["problem_name"] = problem_name
                problem_data["contest_name"] = contest_name
                retrieval_res[problem.title] = problem_data
        return retrieval_res