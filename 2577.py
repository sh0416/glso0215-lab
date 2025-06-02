a = int(input())
b = int(input())
c = int(input())

li = []
multiply_result = str(a * b * c)
for i in range(len(multiply_result)):
    num_int_value = int(multiply_result[i])
    li.append(num_int_value)
for i in range(10):
    print(li.count(i))