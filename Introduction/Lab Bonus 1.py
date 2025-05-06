# รับจำนวนเต็ม 5 จำนวน แล้วหาค่าน้อยที่สุดลำดับที่ 2
# รับคะแนนสอบ (0-100) แล้วตัดเกรด A ถึง F ตามเกณฑ์ปกติ
# รับวันที่และเดือนเป็นจำนวนเต็ม แล้วตรวจสอบว่าถูกต้องหรือไม่

# 1st Task: Get 5 user input (INT) and print the 2nd lowest value

# Using for loop
print(sorted([int(input()) for _ in range(5)])[1])

# 2nd Task: Get score (0-100) and grading from A to F by normal threshold

score = int(input("Enter score (0-100): "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
    
# 3rd Task: Get date input as INT and check if its in the right format
date_input = input("Enter date (YYYYMMDD): ")

if date_input.isdigit() and len(date_input) == 8:
    year = int(date_input[:4])
    month = int(date_input[4:6])
    day = int(date_input[6:])

    try:
        from datetime import datetime
        datetime(year, month, day)
        print("Valid date format.")
    except ValueError:
        print("Invalid date values.")
else:
    print("Invalid format. Please enter 8 digits as YYYYMMDD.")
