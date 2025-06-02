# Name: 크로아티아 알파벳
# Number: 2941
# Link: https://www.acmicpc.net/problem/2941

def count_croatian_letters(string):
    i = 0
    count = 0

    while i < len(string):
        if i + 2 < len(string) and string[i:i+3] == 'dz=':
            count += 1
            i += 3
        elif i + 1 < len(string) and string[i:i+2] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
            count += 1
            i += 2
        else:
            count += 1
            i += 1

    # print(f"The number of Croatian letters is {count}")
    return count

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        input_string = sys.argv[1]
        count_croatian_letters(input_string)
    else:
        count_croatian_letters("dz=ak")
