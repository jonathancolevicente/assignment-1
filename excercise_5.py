def main():
    revenue = float(input("Enter total revenue: "))
    cost = float(input("Enter total cost: "))
    product_name = input("What's the product name? ").strip().lower()

    profitable = is_profitable(revenue, cost)
    category = categorize_product(product_name)

    if profitable:
        profit = revenue - cost
        print(f"Business is profitable. Profit: ${profit:.2f}")
        suggest_investment(category)
    else:
        print("Business is not profitable. Focus on reducing costs or increasing revenue.")

def is_profitable(revenue, cost):
    return revenue > cost

def categorize_product(product_name):
    match product_name:
        case "electronics" | "gadget":
            return "High Margin"
        case _ if product_name.startswith("tech"):
            return "High Margin"
        case "clothing" | "apparel":
            return "Medium Margin"
        case "food" | "grocery":
            return "Low Margin"
        case _:
            return "Uncategorized - Review Needed"

def suggest_investment(category):
    match category:
        case "High Margin":
            print("Suggestion: Reinvest profits")
        case "Medium Margin":
            print("Suggestion: Moderate reinvestment.")
        case "Low Margin":
            print("Suggestion: Cost optimization.")
        case _:
            print("Suggestion: Review category strategy.")

main()
