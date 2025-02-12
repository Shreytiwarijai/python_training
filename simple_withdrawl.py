cr = 15000
pin = 5755

dr = int(input("Enter the amount to withdraw: "))

if dr <= cr:
    entered_pin = int(input("Enter your pin: "))
    if entered_pin == pin:
        print("Withdrawal successful")
        print("You're remaining balance is: ", cr - dr)
    else:
        print("You've entered the wrong pin")
else:
    print("Invalid withdrawal amount")

