# 1. Implement a generator function fibonacci_generator that yields Fibonacci
# numbers indefinitely. Write a function sum_fibonacci that computes the sum of
# the first 10 Fibonacci numbers generated by this function.

def fiboseries():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b  

def sum_fibonacci(n=10):
    fibo=fiboseries()
    sum=0
    for i in range(n):
        sum+=next(fibo)
    return sum

print(sum_fibonacci(10))



# 2.Define a generator function prime_number_generator that yields prime
# numbers indefinitely. Print the first 15 prime numbers generated by this function.

def is_prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def prime_number_generator():
    num=2
    while True:
        if is_prime(num):
            yield num
        num+=1

prime_gen=prime_number_generator()

for i in range(15):
    print(next(prime_gen))
