def main():
    income = float(input("What's your annual income? "))
    bracket, rate = get_tax_bracket(income)
    if rate is not None:
        estimated_tax = income * rate
        print(f"Your bracket: {bracket}. Estimated tax: {estimated_tax:.2f}")
    else:
        print(bracket)

def get_tax_bracket(income):
    if income < 0:
        return "Invalid income.", None
    elif income < 50000:
        bracket = "Low (10%)"
        rate = 0.10
    elif income < 100000:
        bracket = "Medium (20%)"
        rate = 0.20
    else:
        bracket = "High (30%)"
        rate = 0.30

    # Bonus: Check if income is even for deduction eligibility
    bracket += " (Deduction Eligible)" if int(income) % 2 == 0 else ""
    return bracket, rate

main()
