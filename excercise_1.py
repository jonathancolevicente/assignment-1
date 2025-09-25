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
        return profit, None
    margin = (profit / revenue) * 100
    return profit, margin

main()
