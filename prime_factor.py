# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

def prime_factor(number):
    prime_number = []
    print(f"number = {number}")
    i = 2
    while i * i <= number * i:
        print(f"i * i <= number = {i * i} <= {number} = {i * i <= number}")
        print(f"i = {i}")
        print(f"number % i = {number % i}")
        if number % i:
            i = i + 1
            print(f"n = {number}")
        else:
            print(f"divide -> {number} / {i}")
            number = number / i
            prime_number.append(i)
            print(f"result -> {number}")
        print(f"=========")
    print(set(prime_number))


prime_factor(600851475143)
