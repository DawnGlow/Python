def get_mullist(num):
    result = []
    for i in range(1, 10):
        result.append(num * i)
    return result

num = int(input("Enter number: "))
print(type(num))
print(get_mullist(num))