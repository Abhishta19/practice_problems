def avg():
    a=int(input("Enter a Number:"))
    b=int(input("Enter a Number:"))
    c=int(input("Enter a Number:"))
    result=(a+b+c)//3
    return result

final_result=avg()
print(f"The average of 3 nos is {final_result}")


def sum(a,b):
    return a+b

a=9
b=10
res=sum(a,b)
print(res)
print(min(a,b))