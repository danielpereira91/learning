name = input("Type your first name: ")
age = int(input("Type your age: "))

if age > 17:
    print(f"Hello, {name}! You can start your studies with us. You are {age} years old. We ask, at least, 18.")
else:
    age_diff = 18 - age
    print(f"Hello, {name}! We're sorry, but you'll have to wait to study with us. You are {age} years old. Come back when you're 18. It will take a maximum of {age_diff} year(s).")