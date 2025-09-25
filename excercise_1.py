# Prompt the user for revenue (float) and cost (float).
# Calculate profit = revenue - cost.
# Calculate margin = (profit / revenue) * 100 if revenue > 0, else print "Invalid revenue."
# Print the results formatted nicely, e.g., "Profit: $X.XX | Margin: Y.YY%" (round margin to 2 decimals using round or f-string formatting).
# Handle division carefully (no zero division needed beyond check).

def main()
    if margin > 0
    print("invalid revenue")
    else
    print("Profit:" profit | "Margin:" margin) 

def inputs()
    revenue = input(float("Enter revenue"))
    cost = input(float("Enter costs"))

def calcs()
    profit = revenue - cost
    margin - (profit / revenue) * 100

main



def main():
    revenue, cost = inputs()
    profit, margin = calcs(revenue, cost)

    if margin is None:
        print("Invalid revenue.")
    else:
        print(f"Profit: ${profit:.2f} | Margin: {margin:.2f}%")

def inputs():
    revenue = float(input("Enter revenue: "))
    cost = float(input("Enter costs: "))
    return revenue, cost

def calcs(revenue, cost):
    profit = revenue - cost
    if revenue <= 0:
        return profit, None  # None signals invalid revenue
    margin = (profit / revenue) * 100
    return profit, margin


main()

