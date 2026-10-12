# Developer's Arena - Week 1 Project

name = input("What is your name? ").title()
age = int(input("What is your age? "))
hobby = input("What are your favourite hobbies? ").title()

print(f"\nWelcome, {name}!!")
print(f"Nice to meet a {age}-year-old buddy!")

if (age < 18):
    print(f"It's awesome that you're learning about {hobby} at such a young age!")
else:
    print(f"It's great to meet an adult who loves {hobby}.")

