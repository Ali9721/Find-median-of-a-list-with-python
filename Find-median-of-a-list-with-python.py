# Define "numbers" as a variable to get numbers & use "sorted" & "map" & "split"
numbers = sorted(map(int, input("Please enter numbers separated by spaces:  ").split()))


# Define "n" & "median" as a variables & use "len" & "if" & "else"
n = len(numbers)
if n % 2 == 0:
    median = (numbers[n//2 - 1] + numbers[n//2]) / 2
else:
    median = numbers[n//2]

# Output the result.
print(f"the median is: {median}")