Income = int(input("Enter your monthly income:"))
Expenses = int(input("Enter your total monthly expenses"))
Monthly_Savings = Income - Expenses
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)
print("Your monthlysavings are $",Monthly_Savings)
print("Projected_savings after one year, with interest, is: $",Projected_Savings)

