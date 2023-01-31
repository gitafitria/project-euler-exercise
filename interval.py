# result should return 1 => from interval 1 & 2

def smallestInterval(numbers):
    print(numbers)
    smallest = numbers[0]
    for i in range(0, len(numbers)):
        for j in range(i, len(numbers)):
            if i != j:
                interval = abs(numbers[i] - numbers[j])
                if smallest > interval:
                    smallest = interval
                print(f"{numbers[i]} - {numbers[j]} = {interval}")
    print(smallest)

numbers = [1, 3, 2, 4]
smallestInterval(numbers)