a=10
b=7
print(min(a,b))
print(max(a,b))

if a<b:
    print(a)
else:
    print(b)

if a>b:
    print(a)
else:
    print(b)

num=int(input("Enter a no to find a factorial"))
result=1
for i in range (2,num+1):
    result*=i

print(result)

def simple_interest(p,t,r):
    return (p*t*r)/100

p,t,r=1000,5,2
print(simple_interest(p,t,r))

def area_of_a_circle(pi,r):
    return pi*r**2

pi=22/7
r=10
result= round(area_of_a_circle(pi,r),2)
print(f"The area of the circle is:{result}")

n = int(input("Enter a number: "))

if n <= 1:   # invalid case
    print("Enter a valid number greater than 1")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

#  check result outside the loop/else
if n > 1:   # only print if it's a valid number
    if is_prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")

num=int(input("Enter a Number"))
if num%2==0:
    print("Even")
else:
    print("Odd")


n=100
for i in range(0,n,2):
    print(i,end=" ")
print(" ")

n=100
for i in range(n,0,-2):
    print(i,end=" ")

n=10
for i in range(11):
    print(f"{n}*{i}={n*i}")