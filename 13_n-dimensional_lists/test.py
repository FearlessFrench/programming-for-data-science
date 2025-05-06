def main():
  a = [(2, 7, 1.5), (3.2, 2.5, 4.06), (-5.5, -4.5, 2.5), (2, -5.2, 3),
       (7.2, -2.8, 1.2)]
  print(count_segment(a))


def count_segment(list_a):
    a = list(map(lambda x: x[0], list_a))
    print(a)
    b = list(map(lambda x: x[1], list_a))
    print(b)
    c = list(map(lambda x: x[2], list_a))
    print(c)

    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    for i in range(len(a)):  # len(a) = 5
        # => 0 1 2 3 4
        if a[i] > 0 and b[i] > 0:  # ++
            num1 += 1
            continue
        elif a[i] < 0 and b[i] > 0:  # -+
            num2 += 1
            continue
        elif a[i] < 0 and b[i] < 0:  # --
            num3 += 1
            continue
        else:
            num4 += 1
            continue
    for j in range(len(c)): # len(c) = 5
        # => 0 1 2 3 4
        if a[i] > 0 and b[i] > 0: # Q1
            if a[i] - c[i] < 0: # q2
                num2 += 1
            elif b[i] - c[i] < 0: # q4
                num4 += 1
        elif a[i] < 0 and b[i] > 0: # Q2
            if a[i] + c[i] > 0: # q1
                num1 += 1
            elif b[i] - c[i] < 0: # q3
                num3 += 1
        elif a[i] < 0 and b[i] < 0: # Q3
            if a[i] + c[i] > 0: # q4
                num4 += 1
            elif b[i] + c[i] < 0: # q2
                num2 += 1
        else:
            if a[i] - c[i] > 0: # q4
                num3 += 1
            elif b[i] + c[i] < 0: # q2
                num1 += 1
    return (num1, num2, num3, num4)
    


if __name__ == "__main__":
  main()