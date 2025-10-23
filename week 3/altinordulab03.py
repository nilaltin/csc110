# CSC 110 - Lab 3
# Name: Nil Altinordu

import math

def main():
    print("This program tests the areaTrapezoid() and volumeCone() functions.\n")

    # --- Part 1: Testing areaTrapezoid() ---
    print("Testing areaTrapezoid():")

    # Test case 1: base1=4, base2=5, height=8 → expected area = 36
    area1 = areaTrapezoid(4, 5, 8)
    print(f"Test 1 - Expected: 36, Actual: {area1}")

    # Test case 2: base1=2, base2=7, height=9 → expected area = 40.5
    area2 = areaTrapezoid(2, 7, 9)
    print(f"Test 2 - Expected: 40.5, Actual: {area2}")

    # --- Part 2: Testing volumeCone() ---
    print("\nTesting volumeCone():")

    # Test case 1: r=3, h=5 → expected volume ≈ 47.12
    vol1 = volumeCone(3, 5)
    print(f"Test 1 - Expected: 47.12, Actual: {vol1:.2f}")

    # Test case 2: r=4, h=10 → expected volume ≈ 167.55
    vol2 = volumeCone(4, 10)
    print(f"Test 2 - Expected: 167.55, Actual: {vol2:.2f}")


# This function calculates and returns the area of a trapezoid
# parameter: base1, the length of the top of the trapezoid
# parameter: base2, the length of the bottom of the trapezoid
# parameter: height, the height of the trapezoid
# formula: area = (height / 2) * (base1 + base2)
def areaTrapezoid(base1, base2, height):
    area = height / 2.0 * (base1 + base2)
    return area


# This function calculates and returns the volume of a cone
# parameter: radius, the radius of the circular base
# parameter: height, the height of the cone
# formula: volume = (1/3) * π * r^2 * h
def volumeCone(radius, height):
    volume = (1.0 / 3.0) * math.pi * radius**2 * height
    return volume


# Call main once
main()
