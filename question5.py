#write a program to find if the given number is prime no or not

#solution
import math

a=int(input())
if a<=2:
    print("prime")
else:
    temp=0
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            print("it is not a prime number")
            temp=1
    if temp==0:
        print("It is prime number")
        
