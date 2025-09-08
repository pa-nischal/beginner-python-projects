#This python program lets you calculate what your bank balance
# will be after certain years of compounding.

print("Compound frequency?")
print("Type 1 for Annually")
print("Type 2 for Semi annually")
print("Type 3 for Quarterly")
print("Type 4 for Monthly")
frequency = int(input())


principal = float(input("Enter your principal amount:"))
increment = float(input("Enter the amount you want to add every month:"))
time = float(input("Enter the number of years:"))
rate = float(input("Enter the annual rate(in %):"))

time1 = time

if frequency == 1:
    while time>0:
        principal += (rate /100)*principal
        principal += increment*12
        time -= 1
elif frequency == 2:
    while time>0:
        principal += (rate / 200) * principal
        principal += increment * 6
        time -= 0.5
elif frequency == 3:
    while time>0:
        principal += (rate / 400) * principal
        principal += increment * 3
        time -= 0.25
elif frequency == 4:
    while time>1e-9:
        principal += (rate / 1200) * principal
        principal += increment
        time -= (1/12)
print(f"The principal amount after {time1} years will be ${principal:,}.")
input("Press any key to exit..")
