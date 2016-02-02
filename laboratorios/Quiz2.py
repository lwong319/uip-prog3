#suma de pares de 10 a 5000 omitiendo el 100 y 1000#

n1=10
p = 0

while n1 <= 5000:

     if n1 == 100 or n1 == 1000:
        pass
     else:
        if n1%2 == 0:
             p += n1
        print(n1)

     n1 += 1
