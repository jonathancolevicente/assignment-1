def main():
    full_name = input("Enter full name: ")
    greeting = format_greeting(full_name)   
    print(greeting)

def format_greeting(name, title="Customer"):
    name = name.strip()
    if not name:
        return "Hello, Valued Customer!"
    name = name.title()
    first_name = name.split()[0]
    return f"Hello, {first_name} ({title})!"

main()