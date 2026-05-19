name = input("Enter the freelancer's name :")
h_rate = float(input("Enter the hourly rate :"))
h_worked = float(input("Enter the hours worked :"))


pay = h_rate * h_worked
tax =0.1 * pay
net_pay = pay - tax
currency = "rupees"

print(f"Gross pay : {pay} {currency}")
print(f"tax Deducted : {tax} {currency}")
print(f"Net pay : {net_pay} {currency}")
