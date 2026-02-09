# Topic : List
#Challenge: Calculate weekly wages with overtime pay, If total hours > 40, extra hours are paid at 1.5x rate
# Take wages as input.
# Number of hours he has worked in a week as input.
# Print total_wages he earned in the week.

weekend_work = list(map(int, input("Enter Hours: ").split()))
hourly_wages = int(input("Enter Hourly Wages: "))

total_hour = 0

for x in weekend_work:
    total_hour+=x

extra_hours=0
total_wages = 0

if total_hour <= 40:
    total_wages =  total_hour*hourly_wages
else:
    extra_hours =  total_hour - 40
    extra_hours *= 1.5
    total_wages += extra_hours * hourly_wages + hourly_wages * 40

print("Total Wages: ",total_wages)

