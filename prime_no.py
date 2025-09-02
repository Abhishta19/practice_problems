def prime_no_check(num):
    if num<=1:
        return f"Its not a prime no"
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return f"{num}  is not a prime no"
    return f"{num} is a prime no"
print(prime_no_check(8))
print(prime_no_check(7))





