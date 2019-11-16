def findLeapYears(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

print("Enter a year to out if that bastard was a leap year or a boring normal year and how many years since has been a leap year.")
year = int(input())

if findLeapYears(year):
    print(str(year) + " is a leap year.")
else:
    print(str(year) + " is not a leap year.")

leapYears = []

for i in range(year + 1, 2020):
    if findLeapYears(i):
        leapYears.append(i)

print("all leap years since " + str(year) + ":")
for i in range(len(leapYears)):
    print(leapYears[i])
