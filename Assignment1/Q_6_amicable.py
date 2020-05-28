def sum_of_divisors(x):
    sum = 0 
    for i in range(1, (int(x / 2) + 1)):
        if (x % i == 0):
            sum += i
    return sum

for i in range(1, 7000):
    for j in range(i + 1, 7000):
        if (i == sum_of_divisors(j) and j == sum_of_divisors(i)):
            print(i,j)

