marks = int(input("Enter your marks?\n"))

print(f"\nYour marks is {marks}")


if marks < 0 or marks > 100:
    print("Invalid Marks")

elif marks > 60:
    print("Excellent")

elif marks > 32:
    print("Pass")

elif marks == 32:
    print("Just Passed")

elif marks < 32:
    print("Fail")
