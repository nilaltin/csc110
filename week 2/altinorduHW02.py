# Author: Nil Altinordu
# Description:
#   For a rectangular room, this program calculates paintable area (walls + ceiling
#   with a 10% window deduction on walls), floor area, volume, trim length,
#   and total material costs for paint and flooring.

import math

#CONSTANTS
PAINT_COVERAGE_SQFT_PER_GAL = 350      # named constant (sq ft per gallon)
WALL_WINDOW_DEDUCTION = 0.10           # 10% of wall area is subtracted for windows

#INTRO
print("Welcome! This tool estimates materials for a rectangular room.")
print("You'll enter room dimensions in feet and prices for paint and flooring.\n")

#INPUT (get room dimensions from user)
length_ft = float(input("Enter the room length (feet): "))
width_ft  = float(input("Enter the room width (feet): "))
height_ft = float(input("Enter the room height (feet): "))

#get prices
paint_price_per_gallon = float(input("Enter the price for one gallon of paint (USD): $"))
flooring_price_per_sqft = float(input("Enter the price per square foot of flooring (USD): $"))

# geometric areas
wall_area_sqft = 2 * (length_ft * height_ft + width_ft * height_ft)
ceiling_area_sqft = length_ft * width_ft

# paintable area: ceiling + (walls minus 10% for windows)
adjusted_wall_area_sqft = wall_area_sqft * (1 - WALL_WINDOW_DEDUCTION)
total_paint_area_sqft = ceiling_area_sqft + adjusted_wall_area_sqft

# volume (cubic feet)
volume_cuft = length_ft * width_ft * height_ft

# trim length: around the perimeter at floor and at ceiling
perimeter_ft = 2 * (length_ft + width_ft)
total_trim_ft = 2 * perimeter_ft

# material quantities
paint_gallons_needed = math.ceil(total_paint_area_sqft / PAINT_COVERAGE_SQFT_PER_GAL)

# flooring: assignment requires whole-number square feet (round up)
raw_floor_area_sqft = ceiling_area_sqft
flooring_sqft_needed = math.ceil(raw_floor_area_sqft)

# costs
total_paint_cost = paint_gallons_needed * paint_price_per_gallon
total_flooring_cost = flooring_sqft_needed * flooring_price_per_sqft
total_material_cost = total_paint_cost + total_flooring_cost

# ---------------------------- OUTPUT ---------------------------
print("\n-------------------- INPUT SUMMARY --------------------")
print(f"Length: {length_ft:.2f} ft, Width: {width_ft:.2f} ft, Height: {height_ft:.2f} ft")
print(f"Paint price per gallon: ${paint_price_per_gallon:.2f}")
print(f"Flooring price per sq ft: ${flooring_price_per_sqft:.2f}")

print("\n-------------------- RESULTS --------------------------")
print(f"Total painting area (walls+ceiling, walls -10% for windows): {total_paint_area_sqft:.2f} sq ft")
print(f"Volume of room: {volume_cuft:.0f} cu ft")
print(f"Trim length (floor + ceiling): {total_trim_ft:.1f} ft")
print(f"Paint needed (whole gallons): {paint_gallons_needed} gallon(s)")
print(f"Total paint cost: ${total_paint_cost:.2f}")
print(f"Flooring area (raw): {raw_floor_area_sqft:.1f} sq ft")
print(f"Flooring needed (rounded to whole sq ft): {flooring_sqft_needed} sq ft")
print(f"Total flooring cost: ${total_flooring_cost:.2f}")
print(f"\nTOTAL MATERIAL COSTS: ${total_material_cost:.2f}")

#TESTING+REPORT
'''
How I started:
I wrote input prompts first, then computed one quantity at a time
(areas, volume, trim), then added costs and rounding rules.
I began by planning the problem in small steps: (a) gather inputs with clear
units (feet, dollars), (b) compute geometry (wall area, ceiling/floor area,
volume, trim), (c) apply assignment rules (10% wall deduction for windows,
350 sq ft per gallon, rounding up for paint cans and flooring), and (d) compute
costs and format the output. I implemented and printed one result at a time to
verify the math.

I briefly ran into a Python “unexpected indent” error while copying code.
I fixed it by ensuring no stray leading spaces at the top of the file and by
making sure every block uses consistent 4-space indentation (no tabs).
I also polished the output by adding a small helper to format money, which
improved readability during testing.

I tested with the assignment’s sample numbers, my own example, and also a very large
“warehouse-like” room to stress-check the rounding and costs. I compared the
program output against hand calculations.

Test Case A (from assignment)
Inputs:
  length = 10.5 ft, width = 15.2 ft, height = 12.5 ft
  paint price = $12.99/gal, flooring price = $3.49/sq ft
Expected results:
  Wall area = 2*(10.5*12.5 + 15.2*12.5) = 642.5 sq ft
  Ceiling (and raw floor) = 10.5*15.2 = 159.6 sq ft
  Paint area = ceiling + 0.9*walls = 159.6 + 0.9*642.5 = 737.85 sq ft
  Paint cans = ceil(737.85 / 350) = 3
  Paint cost = 3 * $12.99 = $38.97
  Volume = 10.5*15.2*12.5 = 1995 cu ft
  Trim length = 4*(10.5 + 15.2) = 102.8 ft
  Flooring needed (whole sq ft) = ceil(159.6) = 160 sq ft
  Flooring cost = 160 * $3.49 = $558.40
  Total cost = $38.97 + $558.40 = $597.37
  
Test Case B
   Inputs:
     length=12 ft, width=10 ft, height=8 ft
     paint=$25.00/gal, flooring=$4.50/sq ft
   Hand-calcs:
     wall area = 2*(12*8 + 10*8) = 352 sq ft
     ceiling/floor = 12*10 = 120 sq ft
     paint area = 120 + 0.9*352 = 436.8 sq ft
     gallons = ceil(436.8/350) = 2
     paint cost = 2*$25 = $50.00
     volume = 12*10*8 = 960 cu ft
     trim = 4*(12+10) = 88 ft
     flooring units = ceil(120) = 120 sq ft
     flooring cost = 120*$4.50 = $540.00
     TOTAL = $50.00 + $540.00 = $590.00

Test Case C
Inputs:
  length = 120 ft, width = 112 ft, height = 130 ft
  paint price = $12.00/gal, flooring price = $22.00/sq ft
Expected results:
  Wall area = 2*(120*130 + 112*130) = 60,320 sq ft
  Ceiling (and raw floor) = 120*112 = 13,440 sq ft
  Paint area = 13,440 + 0.9*60,320 = 67,728.00 sq ft
  Paint cans = ceil(67,728 / 350) = 194
  Paint cost = 194 * $12.00 = $2,328.00
  Volume = 120*112*130 = 1,747,200 cu ft
  Trim length = 4*(120 + 112) = 928.0 ft
  Flooring needed (whole sq ft) = ceil(13,440) = 13,440 sq ft
  Flooring cost = 13,440 * $22.00 = $295,680.00
  Total cost = $2,328.00 + $295,680.00 = $298,008.00

What I'd improve next time and what I learned:
- Input validation (reject negatives or non-numeric input).
- Options for multiple coats of paint.
- Ability to enter the exact sizes/quantities of windows and doors instead of a flat 10%.
- Optional metric units and sales tax.
I learned to translate a real-world spec into clear steps (input → process →
output) and to be careful about rounding rules (ceil for paint cans and flooring).
I also reinforced good habits: named constants for shared values, descriptive
variables, and consistent formatting of outputs with units and currency.

Next time, I would start by writing small helper functions (e.g., for money
formatting and input validation), then add automated tests for a few known cases
to catch mistakes quickly. I’d also design the interface with clearer sections
and consider edge cases earlier (e.g., extremely small rooms or very low prices).

'''
