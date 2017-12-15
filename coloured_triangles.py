# coloured triangles

import sys

def get_input_arr():
    return [x for x in sys.stdin.readline().rstrip().split(" ")]

def compare(trail_char, head_char):
    # 3 options:
    #   R, G, B
    options = ["R", "G", "B"]
    
    if trail_char == head_char:
        return trail_char
    else:
        options.remove(trail_char)
        options.remove(head_char)
        return options[0]


def main():
    cur_row = get_input_arr()
    
    head = 1
    trail = 0
    row_len = len(cur_row)

    new_row = []

    while row_len > 1:
        while head < row_len:
            new_row.append(compare(cur_row[trail], cur_row[head]))
            head += 1
            trail += 1
        #print(new_row)
        head = 1
        trail = 0
        cur_row = new_row
        new_row = []
        row_len = len(cur_row)
    print(cur_row[len(new_row) - 1])

main()

