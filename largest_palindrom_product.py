# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

max_number = 999
i = max_number - 1
palindrom = []
while i < max_number and i > 0:
    result = max_number * i
    print(f"{max_number} x {i} = {result}")
    reverse = int(str(result)[::-1])
    if reverse == result:
        print(f"palindrom = {result}")
        palindrom.append(result)
    if i == 1:
        max_number = max_number - 1
        i = max_number - 1
    i = i - 1

print(max(palindrom))