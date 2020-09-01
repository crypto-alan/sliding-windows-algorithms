
import sys


def set_t_dict_map(t):
    t_dict_map = {}
    for n in range(0, len(t)):
        tmp = t[n]
        if t_dict_map.get(tmp) is None:
            t_dict_map[tmp] = 1
        else:
            t_dict_map[tmp] += 1
    return t_dict_map


def check_totally_fulfill(t_dict_map, result):
    tmp_dict_map = t_dict_map
    r_len = len(result)
    for n in range(0, r_len):
        current_char = result[n]
        tmp = tmp_dict_map.get(current_char)
        if tmp is not None and tmp > 0:
            tmp_dict_map[current_char] = tmp - 1
            if tmp_dict_map.get(current_char) <= 0:
                del tmp_dict_map[current_char]
    if len(tmp_dict_map) == 0:
        return True
    else:
        return False


def sliding_windows(s, t):
    t_dict_map = set_t_dict_map(t)
    minimum = sys.maxsize
    s_len = len(s)
    first_flag = 0
    second_flag = 0
    current = ''
    result = ''
    while first_flag < s_len:
        current = s[first_flag:second_flag]
        if check_totally_fulfill(t_dict_map, current):
            minimum = min(minimum, len(current))
            first_flag += 1
            t_dict_map = set_t_dict_map(t)
            result = current
        else:
            if second_flag < s_len:
                second_flag += 1
            else:
                first_flag += 1
    return result


if __name__ == '__main__':
    S = 'ADOBECODEBANC'
    T = 'ABC'
    output = 'BANC'
    assert output == sliding_windows(S, T)

    S = 'ZYDKFDUIREFNEFVK'
    T = 'REFN'
    output = 'REFN'
    assert output == sliding_windows(S, T)
