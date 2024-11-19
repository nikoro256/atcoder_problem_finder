
def parse_file_path(filepath):
    path_dat = filepath.split('/')
    contest_name = path_dat[0]
    problem_name = path_dat[-1].split('.')[0]
    return contest_name, problem_name