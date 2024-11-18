import os
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from utils.string_utils import extract_after_str, remove_tag, remove_connected_br

current_path = Path.cwd()
parent_path = current_path.parent
data_path = os.path.join(parent_path, "data/")


def parse_page_content(page_content : str , problem_str : str):
    soup = BeautifulSoup(page_content, 'html.parser')
    div = soup.find('span', class_='lang-ja')
    section_strs = [section.get_text("\n") for section in div.find_all("section")]
    timelimit_str = extract_after_str(page_content, '実行時間制限', length = 40)
    point_str = extract_after_str(page_content, '配点', length = 30)
    title_str = extract_after_str(page_content, problem_str.upper() + " -")
    parsed_page_content = [title_str, point_str, timelimit_str] + section_strs
    parsed_page_content = [remove_connected_br(content) for content in parsed_page_content]
    return parsed_page_content

def read_promlem_content(contest_num : int, problem_str : str):
    problem_url = "https://atcoder.jp/contests/abc" + str(contest_num) + "/tasks/abc" + str(contest_num) + "_" + problem_str + "?lang=ja"
    page_content = requests.get(problem_url).text
    parsed_page_content = parse_page_content(page_content, problem_str)
    return "\n".join(parsed_page_content)

def read_content():
    for i in range(380, 381):
        for problem_str in ["a","b","c","d","e","f","g"]:
            problem_content  = read_promlem_content(i, problem_str)
            os.makedirs(data_path + "abc" + str(380) + "/problem", exist_ok=True)
            with open(data_path + "abc" + str(380) + "/problem/" + problem_str + ".txt" , "w") as f:
                f.write(problem_content)
                
if __name__ == "__main__":
    read_content()
    
    

