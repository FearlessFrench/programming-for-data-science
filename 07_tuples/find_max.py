
def main():
    list_a = [166, 164, 156, 175, 172]    
    print(find_max(list_a))

def find_max(list_a):
    
    # Base case
    if len(list_a) == 1:
        return list_a[0]

    head = list_a[0]
    tail = list_a[1:]
    max_tail = \
    find_max(tail)
    if max_tail > head:
        return max_tail
    else:
        return head

if __name__ == '__main__':
    main()