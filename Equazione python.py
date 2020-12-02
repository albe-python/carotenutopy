import math
print("equazione ax+b=0")
a = int(input("qual è il valore di a?"))
b = int(input("qual è il valore di b?"))
print("x=-b:a")
x = (-b/a)
print (x)
max(a,b,x)
print("il numero più grande tra a,b e x è")
print(max(a,b,x))
def swap(a,b):
    a,b=b,a
    print("a è uguale a",a,"e b è uguale a",b)

swap(a,b)
