# assignment-1
# Python Business Fundamentals Exercises

## Exercise 1: Profit Margin Calculator (Variables & Basic Arithmetic)

**Concepts:** Input, variables (`int`/`float`), arithmetic, print formatting (`f-strings`, commas).

**Business Context:**
As a financial analyst, you often need to evaluate whether a product is financially viable. One key metric is **profit margin**, which shows how much of each dollar earned becomes profit.

**Task:**

* Prompt the user for revenue (`float`) and cost (`float`).
* Compute `profit = revenue - cost`.
* Compute `margin = (profit / revenue) * 100` if `revenue > 0`.
* If `revenue <= 0`, print `"Invalid revenue."`
* Print results with formatting, e.g.:

  ```
  Profit: $1,500.00 | Margin: 30.00%
  ```

**Sample Input/Output:**

```
What's the revenue? 5000.0  
What's the cost? 3500.0  
Profit: $1,500.00 | Margin: 30.00%
```

**GitHub Tip:** Commit with the message:
`Exercise 1: Profit Margin Calculator with float inputs.`

---

## Exercise 2: Credit Score Evaluator (Conditionals)

**Concepts:** Input, `int` conversion, `if`/`elif`/`else`, logical operators.

**Business Context:**
Banks evaluate a customer's **credit score** before issuing loans. Different score ranges affect loan decisions and interest rates.

**Task:**

* Prompt the user for a credit score (`int`, 300–850 range).
* Use conditionals to categorize:

  * `>= 750`: "Excellent - Loan Approved"
  * `700 <= score < 750`: "Good - Loan Approved with Review"
  * `600 <= score < 700`: "Fair - Loan Conditional"
  * `< 600`: "Poor - Loan Denied"
* If outside the 300–850 range, print `"Invalid score."`
* Add a message: If approved, append `"Interest rate: Low"`; otherwise `"Seek credit improvement."`

**Sample Input/Output:**

```
What's your credit score? 720  
Good - Loan Approved with Review. Interest rate: Low
```

**GitHub Tip:** Use a branch named `feat/exercise2` for testing.

---

## Exercise 3: Customer Greeting Formatter (Strings & Functions)

**Concepts:** String methods (`strip`, `title`, `split`, `lower`), functions with parameters/defaults, return values.

**Business Context:**
Marketing teams personalize greetings to improve customer engagement.

**Task:**

* Define a function `format_greeting(name, title="Customer")`.
* It should:

  * Strip whitespace.
  * Title-case the name.
  * Extract the first name if multiple words.
* Return: `"Hello, FirstName (Title)!"`
* If the name is empty, return `"Hello, Valued Customer!"`

**Sample Input/Output:**

```
What's your full name?   john doe  
Hello, John (Customer)!
```

**Extension:** Add a parameter for a custom title.

**GitHub Tip:** Include comments explaining each string method used.

---

## Exercise 4: Tax Bracket Determiner (Conditionals & Functions)

**Concepts:** Functions returning values, modulo (optional), ternary expressions.

**Business Context:**
Tax advisors need to quickly determine a client's income tax bracket to calculate deductions.

**Task:**

* Define a function `get_tax_bracket(income)` returning a `str`:

  * `< 50,000`: `"Low (10%)"`
  * `50,000 <= income < 100,000`: `"Medium (20%)"`
  * `>= 100,000`: `"High (30%)"`
  * `< 0`: `"Invalid income."`
* In `main`, prompt for income, call the function, and print:

  ```
  Your bracket: [bracket]. Estimated tax: [income * rate]
  ```
* Bonus: Use a ternary to check if income is even and append `" (Deduction Eligible)"`.

**Sample Input/Output:**

```
What's your annual income? 75000.0  
Your bracket: Medium (20%). Estimated tax: 15000.0
```

**GitHub Tip:** Add a sample run output in `README.md`.

---

## Exercise 5: Product Category Matcher (Match-Case)

**Concepts:** `match` statements, string comparisons (`lower`, `startswith`), input sanitization.

**Business Context:**
Retailers categorize products to inform pricing and margin strategies.

**Task:**

* Prompt for a product name (`str`), strip, and lowercase it.
* Use `match` to categorize:

  * `"electronics"`, `"gadget"`, or starts with `"tech"`: `"High Margin"`
  * `"clothing"`, `"apparel"`: `"Medium Margin"`
  * `"food"`, `"grocery"`: `"Low Margin"`
  * `_`: `"Uncategorized - Review Needed"`
* Print:

  ```
  Product: [name] | Category: [category]
  ```

**Sample Input/Output:**

```
What's the product name? TechWidget  
Product: techwidget | Category: High Margin
```

**GitHub Tip:** Use clear, descriptive commit messages like:
`Exercise 5: Implemented product category matcher using match-case.`
