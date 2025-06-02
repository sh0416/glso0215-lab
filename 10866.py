mport sys

n = int(sys.stdin.readline())

my_list = []

results = []

for _ in range(n):
    command_line = sys.stdin.readline().split()
    command = command_line[0]

    if command == "push_front":
        my_list.insert(0, int(command_line[1])) 
    elif command == "push_back":
        my_list.append(int(command_line[1]))
    elif command == "pop_front":
        if my_list:
            results.append(str(my_list.pop(0)))
        else:
            results.append("-1")
    elif command == "pop_back":
        if my_list:
            results.append(str(my_list.pop()))
        else:
            results.append("-1")
    elif command == "size":
        results.append(str(len(my_list)))
    elif command == "empty":
        if not my_list:
            results.append("1")
        else:
            results.append("0")
    elif command == "front":
        if my_list:
            results.append(str(my_list[0]))
        else:
            results.append("-1")
    elif command == "back":
        if my_list:
            results.append(str(my_list[-1]))
        else:
            results.append("-1")


print("\n".join(results))
