
def check_duplicate_seq(array):
    t_dict_map = {}
    for n in range(0, len(array)):
        tmp = array[n]
        if t_dict_map.get(tmp) is None:
            t_dict_map[tmp] = 1
        else:
            return False
    return True


def sliding_windows(s):
    first_flag = 0
    second_flag = 0
    longest = 0
    longest_seq_char = ''
    if longest_seq_char == '':
        longest_seq_char = s[first_flag]
        second_flag = 2
    s_len = len(s)
    while first_flag < s_len:
        current = s[first_flag : second_flag]
        temp_size = len(current)
        if check_duplicate_seq(current) and temp_size > longest:
            longest_seq_char = current
            longest = temp_size
        else:
            first_flag += 1
        second_flag += 1
    return longest_seq_char


if __name__ == '__main__':
    S = 'abcdbananaqueenkingjackabcdef'
    output = 'kingjac'
    assert output == sliding_windows(S)

    S = 'abcabcbb'
    output = 'abc'
    assert output == sliding_windows(S)
