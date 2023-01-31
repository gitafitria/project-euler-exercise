# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# time complexity: O(n)

def multiply_of_3_or_5_sum(num):
    total = 0
    for i in range(1, num):
        mod3 = i % 3
        mod5 = i % 5
        if mod3 == 0 or mod5 == 0:
            total = total + i
    print(total)


multiply_of_3_or_5_sum(1000)