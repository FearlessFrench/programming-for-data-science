# from sympy import poly, var
def high_and_low(numbers):
    nums = [int(i) for i in numbers.split()]
    return " ".join([str(max(nums)), str(min(nums))])

numbers = "1 9 3 4 -5"
print(high_and_low(numbers))