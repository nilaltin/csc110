# HW3: Saving Calculator
# Author: Nil Altinordu

# Description:
#   This program helps a user estimate how much money they'll have
#   after saving a fixed amount monthly with compound interest.
#   The user enters a monthly deposit amount and an annual
#   interest rate. The program then displays:
#   Final balance and total interest after 20 years
#   Final balance and total interest after 30 years
#   Final balance and total interest for double the monthly deposit over 20 years

#   Extra Credit:
#     It also computes the monthly deposit required to reach the
#     20-year original-balance target in only 10 years.

def compute_balance(d_monthly, r_percent, years, k):
    """Compute final balance for an annuity with monthly deposits.

    Parameters:
        d_monthly (float): monthly deposit in dollars
        r_percent (float): annual interest rate in percent (e.g., 6.2 for 6.2%)
        years (int): number of years saving (e.g., 20 or 30)
        k (int): compounding periods per year (use 12 for monthly)

    Returns:
        float: final balance after 'years' years, compounded 'k' times per year
    """
    r_decimal = r_percent / 100.0
    periods = years * k
    if r_decimal == 0.0:
        return d_monthly * periods
    periodic_rate = r_decimal / k
    growth = (1 + periodic_rate) ** periods
    balance = d_monthly * ((growth - 1) / periodic_rate)
    return balance


def compute_interest(final_balance, d_monthly, years, k):
    """Compute total interest earned.

    Parameters:
        final_balance (float): final balance returned by compute_balance
        d_monthly (float): monthly deposit in dollars
        years (int): number of years
        k (int): compounding periods per year (12)

    Returns:
        float: total interest earned
    """
    total_contributed = d_monthly * years * k
    return final_balance - total_contributed


def display_results_row(label_years, balance, interest):
    """Display a single formatted row of results.

    Parameters:
        label_years (int): number of years to label the row
        balance (float): final balance to display
        interest (float): total interest to display

    Returns:
        None (prints formatted row)
    """
    print(f"{label_years:<6}\t${balance:>12.2f}\t${interest:>12.2f}")


def required_deposit_for_target(target_balance, r_percent, years, k):
    """Extra Credit: compute monthly deposit required to hit a target.

    Parameters:
        target_balance (float): desired final balance
        r_percent (float): annual interest rate in percent
        years (int): years allowed to reach target
        k (int): compounding periods per year (12)

    Returns:
        float: required monthly deposit to reach target_balance in 'years'
    """
    r_decimal = r_percent / 100.0
    periods = years * k
    if r_decimal == 0.0:
        return target_balance / periods
    periodic_rate = r_decimal / k
    growth = (1 + periodic_rate) ** periods
    d = target_balance * periodic_rate / (growth - 1)
    return d


def main():
    print("Welcome to the Saving Calculator!")
    print("This tool estimates your final balance and interest earned when saving monthly.")
    print("You will enter the monthly deposit (dollars) and the ANNUAL interest rate (percent).")
    print()

    monthly_deposit_input = input("Enter the monthly deposit (in dollars, e.g., 100): ").strip()
    annual_rate_input = input("Enter the ANNUAL interest rate (in percent, e.g., 6.2 for 6.2%): ").strip()

    d = float(monthly_deposit_input)
    r_percent = float(annual_rate_input)

    k = 12
    years_20 = 20
    years_30 = 30

    print()
    print(f"Given {r_percent}% annual interest rate and depositing ${d:.2f} monthly:\n")

    bal_20 = compute_balance(d, r_percent, years_20, k)
    int_20 = compute_interest(bal_20, d, years_20, k)

    bal_30 = compute_balance(d, r_percent, years_30, k)
    int_30 = compute_interest(bal_30, d, years_30, k)

    d_double = d * 2
    bal_20_double = compute_balance(d_double, r_percent, years_20, k)
    int_20_double = compute_interest(bal_20_double, d_double, years_20, k)

    print("Years \tFINAL BALANCE \tINTEREST")
    display_results_row(years_20, bal_20, int_20)
    display_results_row(years_30, bal_30, int_30)
    print()
    print("With doubling the monthly deposit:")
    display_results_row(years_20, bal_20_double, int_20_double)

    # Extra credit: how big of a deposit to reach the 20-year balance in 10 years
    target = bal_20
    years_10 = 10
    req_d_10 = required_deposit_for_target(target, r_percent, years_10, k)
    print()
    print("Extra Credit:")
    print(f"To reach the same ${bal_20:.2f} balance in {years_10} years,")
    print(f"you would need to deposit approximately ${req_d_10:.2f} per month.")


if __name__ == "__main__":
    main()


# Test Case 1
# Inputs:
#   monthly deposit = $250
#   annual interest = 5.0%
# Expected (rounded to 2 decimals):
#   20 years: final balance = $102,758.42 , interest = $42,758.42
#   30 years: final balance = $208,064.66 , interest = $118,064.66
#   Double deposit (20y): final balance = $205,516.83 , interest = $85,516.83
#   Extra credit (10y to reach 20y target): required monthly deposit ≈ $661.75

# Test Case 2
# Inputs:
#   monthly deposit = $75
#   annual interest = 3.2%
# Expected (rounded to 2 decimals):
#   20 years: final balance = $25,168.11 , interest = $7,168.11
#   30 years: final balance = $45,235.17 , interest = $18,235.17
#   Double deposit (20y): final balance = $50,336.22 , interest = $14,336.22
#   Extra credit (10y to reach 20y target): required monthly deposit ≈ $178.24

# Edge Case (No interest to verify the 0% branch
# Inputs:
#   monthly deposit = $120
#   annual interest = 0.0%
# Expected:
#   20 years: final balance = 120 * (20*12) = $28,800.00 , interest = $0.00
#   30 years: final balance = 120 * (30*12) = $43,200.00 , interest = $0.00
#   Double deposit (20y): final balance = 240 * (20*12) = $57,600.00 , interest = $0.00
#   Extra credit (10y to reach 20y target): required monthly deposit = target / (10*12) = $240.00


# WRITTEN REPORT
# 1) How I approached the assignment:
#    I first implemented compute_balance() directly from the annuity formula,
#    using parameters for deposit, rate (percent), years, and k=12. I handled
#    the r=0% case separately to avoid division by zero. I then wrote
#    compute_interest() and tested both functions with small, known values.
#    After the math was correct, I built main() to gather inputs and format
#    the output. Finally, I added the extra-credit function by solving the
#    annuity formula for the monthly deposit d.

#    Where I got stuck:
#    Initially I forgot to divide the annual rate by 100 to convert percent
#    to a decimal before dividing by k. The numbers looked too large. I fixed
#    it by re-reading the formula and adding r_percent/100.0 in the code.

# 2) How I tested the program:
#    I used the two test cases above plus the 0% edge case. For each case,
#    I computed the expected result using the exact annuity formula and then
#    compared the program’s output (rounded to two decimals). I also checked
#    that the labels/columns were clear and that the prompts told users the
#    correct units (dollars and percent).

#    What I’d improve next:
#    With more time, I’d add input validation (reject negatives, non-numbers), and commas to the displayed results.

# 3) What I learned:
#    I practiced writing functions with parameters and return values, and I reinforced the difference between percent vs decimal
#    rates and how compounding is applied. I also learned to handle special cases (like 0% interest).
