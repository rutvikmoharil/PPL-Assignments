def armstrong(x):
    a = []
    i = 0
    temp = x
    while(1):
        a.append(x % 10)
        x = int(x / 10)
        if x != 0:
            i+=1
        else:
            break
    sum = 0
    for j in range(0, (i + 1)):
        sum = sum + a[j] ** 3
    if sum == temp:
        print("{} is an armstrong number".format(temp))

def armstrong_range(x,y):
    for i in range(x, y  +1):
        armstrong(i)

print("Enter the range of numbers")
x = int(input())
y = int(input())
armstrong_range(x,y)


