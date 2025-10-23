# Author: Nil Altinordu
# Lab: Mathematical Computation - Convert hours to hours and minutes

# Test Case 1:
# Input: 4.5
# Expected Output: 4.5 hours is equivalent to 4 hours 30 minutes

# Test Case 2:
# Input: 9.3
# Expected Output: 9.3 hours is equivalent to 9 hours 18 minutes

# Ask the user for the number of hours
hours_input = input("Enter an amount of time in hours (such as 3.5 hours or 4.1 hours): ")
hours = float(hours_input)

# Convert to total minutes 
whole_hours = int(hours)
minutes = round((hours - whole_hours) * 60)

# Display the result
print(f"{hours_input} hours is equivalent to {whole_hours} hours {minutes} minutes")
