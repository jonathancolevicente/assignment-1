credit_score = int(input("Enter credit score: "))

if credit_score < 300 or credit_score > 850:
    print("Invalid score.")

elif credit_score >= 750:

    print("Excellent - Loan Approved")

elif 700 <= credit_score < 750:
    print("Good - Loan Approved with Review")

elif 600 <= credit_score < 700:
    print("Fair - Loan Conditional")

else:
    print("Poor - Loan Denied")

if credit_score >= 600:
    print("Interest rate: Low")
else:
    print("Seek credit improvement.")
