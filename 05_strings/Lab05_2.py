#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab05_2
# 229223 Sec 001

# แทน [พลังหยินหยาง] [ปีนักษัตรจีน] [และธาตุประจำปี] ในการคำนวณทางโหราศาสตร์แบบจีน
# เช่น ปี 2004 เป็นปี "ลิงไม้หยาง" (Yang Wood Monkey)

# ปีหยิน = ปีเลขคี่ (Ex.1997) | ปีหยาง = ปีเลขคู่ (Ex.1998)
# <<------------1996---1997---1998------1999------2000-----2001-----2002-----2003-----2004------2005-----2006---2007---->>
# ปีนักษัตร 12 ปี = Rat -> Ox -> Tiger -> Rabbit -> Dragon -> Snake -> Horse -> Goat -> Monkey -> Rooster -> Dog -> Pig
# ธาตุทุก 2 ปี = Wood, Fire, Earth, Metal, Water เช่น ปี 1990-1991 มีธาตุโลหะ

def main():

    # input
    y = str(input())
    # output
    print(zodiac_element(y))

def zodiac_element(year):
    def yin_yang(year):
        # ลงท้ายเลขคี่ => 1,3,5,7,9 | ลงท้ายเลขคู่ => 0,2,4,6,8
        yin_yang = year[-1]
        if yin_yang == "0":
            return("Yang")
        elif yin_yang == "1":
            return("Yin")
        elif yin_yang == "2":
            return("Yang")
        elif yin_yang == "3":
            return("Yin")
        elif yin_yang == "4":
            return("Yang")
        elif yin_yang == "5":
            return("Yin")
        elif yin_yang == "6":
            return("Yang")
        elif yin_yang == "7":
            return("Yin")
        elif yin_yang == "8":
            return("Yang")
        elif yin_yang == "9":
            return("Yin")


    def element(year):
        # ธาตุทุก 2 ปี = Wood, Fire, Earth, Metal, Water
        # 1990-1991 = Metal | 1992-1993 = Water | 1994-1995 = Wood | 1996-1997 = Fire | 1998-1999 = Earth => แล้วก็วนลูปตามปี
        # ลงท้ายด้วย ==> Metal = 0,1 | Water = 2,3 | Wood = 4,5 | Fire = 6,7 | Earth = 8,9
        element = year[-1]
        if element == "0":
            return("Metal")
        elif element == "1":
            return("Metal")
        elif element == "2":
            return("Water")
        elif element == "3":
            return("Water")
        elif element == "4":
            return("Wood")
        elif element == "5":
            return("Wood")
        elif element == "6":
            return("Fire")
        elif element == "7":
            return("Fire")
        elif element == "8":
            return("Earth")
        elif element == "9":
            return("Earth")


    def zodiac(year):
        # 
        # <<------------1996---1997---1998------1999------2000-----2001-----2002-----2003-----2004------2005-----2006---2007---->>
        # ปีนักษัตร 12 ปี = Rat -> Ox -> Tiger -> Rabbit -> Dragon -> Snake -> Horse -> Goat -> Monkey -> Rooster -> Dog -> Pig
        # Rat = 1996%12 = 4 | Ox = 1997%12 = 5 | Tiger = 1998%12 = 6 | Rabbit = 1999%12 = 7 | Dragon = 2000%12 = 8 | Snake = 2001%12 = 9
        # Horse = 2002%12 = 10 | Goat = 2003%12 = 11 | Monkey = 2004%12 = 0 | Rooster = 2005%12 = 1 | Dog = 2006%12 = 2 | Pig = 2007%12 = 3
        zodiac = int(year) % 12
        if zodiac == 0:
            return("Monkey")
        elif zodiac == 1:
            return("Rooster")
        elif zodiac == 2:
            return("Dog")
        elif zodiac == 3:
            return("Pig")
        elif zodiac == 4:
            return("Rat")
        elif zodiac == 5:
            return("Ox")
        elif zodiac == 6:
            return("Tiger")
        elif zodiac == 7:
            return("Rabbit")
        elif zodiac == 8:
            return("Dragon")
        elif zodiac == 9:
            return("Snake")
        elif zodiac == 10:
            return("Horse")
        elif zodiac == 11:
            return("Goat")
            
    new_zodiac_element = yin_yang(year) + " " + element(year) + " " + zodiac(year)

    return new_zodiac_element

def test_zodiac_element():
    assert zodiac_element(1997) == "Yin Fire Ox"
    assert zodiac_element(2022) == "Yang Water Tiger"   
    assert zodiac_element(1979) == "Yin Earth Goat"
    assert zodiac_element(2003) == "Yin Water Goat"   
    assert zodiac_element(2003) == "Yang Earth Monkey"     
    print("Great job!")

if __name__ == '__main__':
    main()