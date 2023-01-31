# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

def find_nth_prime_factor(number):
    prime_number = []
    print(f"number = {number}")
    i = 2
    found = False
    counter = 1
    while found == False:
        print(f"{counter} - {i}")
        if counter < i:
            counter = counter + 1
            continue
        if counter % i:
            print(f"masuk = {counter} - {i}")
            i = i + 1
        else:
            prime_number.append(i)
            counter = counter + 1
            print("genal")
        uniq_list = sorted(list(set(prime_number)))
        if len(uniq_list) == 3:
            found = True

        # print(f"i = {i}")
        # print(f"{counter} % {i} = {counter % i}")
        # if counter % i:
        #     i = i + 1
        #     print(f"n = {counter}")
        # else:
        #     print(f"bagi -> {counter} / {i}")
        #     counter = counter / i
        #     prime_number.append(i)

        #     print(f"result -> {counter}")

        # counter = counter + 1
        # print(f"=========")
        # # while i * i <= counter * i:
        # uniq_list = sorted(list(set(prime_number)))
        # if len(uniq_list) == number:
        #     found = True
    print(set(prime_number))


find_nth_prime_factor(6)
