monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
ANNUAL_INTEREST_RATE = 0.05
annual_savings_before_interest = monthly_savings * 12
projected_savings = annual_savings_before_interest * (1 + ANNUAL_INTEREST_RATE)
print(f"Your monthly savings are: ${monthly_savings:,.2f}")
print(f"Projected savings after one year, with interest, is: ${projected_savings:,.2f}")

