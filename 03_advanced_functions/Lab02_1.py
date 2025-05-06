#!/usr/bin/env python3
# Panutad Sirikul
# 650510714
# Lab02_1
# 229223 Sec 001
import math


def main():
    # รับข้อมูลพื้นที่ผิวจาก user
    surface_area = float(input("input surface area: "))

    # นำพื้นที่ผิวที่ได้มาคำนวณหารัศมี
    radius = find_r_from_surface_area(surface_area)

    # นำรัศมีที่คำนวณได้มาคำนวณหาปริมาตร
    volume = sphere_volume(radius)

    # แสดงปริมาตรทรงกลม แบบทศนิยมสองต่ำแหน่ง
    print("volume = {0:.2f}".format(volume))


def find_r_from_surface_area(surface_area):
    radius = math.sqrt(surface_area/(4*(math.pi)))  # Surface_area = sqrt/4πr^2
    return radius


def sphere_volume(radius):
    volume = ((4/3)*(math.pi))*(radius**3)  # Volume = 4π/3*r^3
    return volume


if __name__ == '__main__':
    main()
