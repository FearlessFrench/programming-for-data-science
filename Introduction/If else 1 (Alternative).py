a_int = int(input("Enter a number : "))
b_int = int(input("Enter a number : "))
c_int = int(input("Enter a number : "))
d_int = int(input("Enter a number : "))

Max = a_int

if(Max < b_int):
    Max = b_int
if(Max < c_int):
    Max = c_int
if(Max < d_int):
    Max = d_int
    
print("Max : ", Max)
