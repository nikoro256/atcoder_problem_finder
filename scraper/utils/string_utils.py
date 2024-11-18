def remove_tag(string : str):
    inside_tag = False
    res = []
    for i in range(len(string)):
        if string[i] == "<":
            res.append('\n')
            inside_tag = True
        elif string[i] == ">":
            res.append(' ')
            inside_tag = False
        else:
            if not inside_tag :
                res.append(string[i])
    return ''.join(res)

def remove_connected_br(string : str):
    res = []
    connected = False
    for i in range(len(string)):
        if string[i] == "\n":
            if not connected:
                res.append(string[i])
            connected = True
        else:
            res.append(string[i])
            connected = False
    return ''.join(res)


def extract_after_str(html_str : str, search_str : str, length : int = 20):
    try:
        point_idx = html_str.index(search_str)
    except ValueError:
        return None
    return html_str[point_idx: min(len(html_str), point_idx + length)]