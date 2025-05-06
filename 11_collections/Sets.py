def repeats(a):
    seen = set()
    seen_again = set()
    for element in a:
        if (element in seen):
            seen_again.add(element)
        seen.add(element)
    return sorted(list(seen_again))

print(repeats([2, 5, 3, 4, 6, 4, 2]))