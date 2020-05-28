def harmonic_divisor():
    for i in range(1, 10000):
        a = divisors(i)
        l = len(a)
        sum = 0
        #sum of reciprocals of divisors 
        for j in range(l):
            sum = sum + (1.0 / a[j])
        #print(a , sum, (l / sum), type(l / sum))
        if l / sum == int(l / sum):
            print(i)
        #print(sum)


def divisors(x):
    a = []
    for i in range(1, (int(x / 2) + 1)):
        if(x % i == 0):
            a.append(i)
    a.append(x)
    
    return a

harmonic_divisor()
#print(divisors(50))

