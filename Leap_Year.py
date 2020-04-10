check = input("Enter Year- ")
year = int(check)

if year <= 1752:
    print("First leap year was 1752. You've to input a year from 1752.")

elif year > 1752 and year % 4 == 0 and year % 100 != 0:
    print(year, "is a leap year.")

elif year > 1752 and year % 100 == 0:
    print(year, "is not a leap year.")

elif year > 1752 and year % 400 == 0:
    print(year, "is a leap year")

else:
    print(year, "is not a leap year.")
