# Practice 1: 12 Hour Time Format
def main():
    # input hour & minute
    h = int(input("h_input = "))
    m = int(input("m_input = "))


    # call function
    twelve_hr_time(h, m)


def twelve_hr_time(hour, min):
    # calculate hour 00:00-23:59
    if hour<12:  # 3 นาฬิกา
        hour12 = hour
        clock = "am"
    else:        # 15 นาฬิกา
        hour12 = hour-12
        clock = "pm"
    # don't calculate minute

    # result
    print(hour12,":",min, clock)

if __name__ == '__main__' :
    main()