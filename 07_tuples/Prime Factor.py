
def prime_factor(x):
    prime_factor_helper(x, 2)


def prime_factor_helper(x, div):
    # base case
    if div > x ** 0.5:
        print(x)
      # return x # divide & conquer

    if (x % div == 0):
        print(div, end=' ')
        prime_factor_helper(x // div, div)
    else:
        prime_factor_helper(x, div + 1)
