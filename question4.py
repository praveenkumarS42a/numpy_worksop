#write a program to find the sum of digits of a given number'

#solution
a=int(input())
sum1=0
while a!=0:
    rem=a%10
    sum1+=rem
    a=a/10
print(sum1)
