#!/bin/python3

months = open("month.txt")

print(months)
# print(months.mode)
# print(months.readable())
# print(months.read())
# print(months.readline())
# print(months.readline())
# print(months.readlines())
# months.seek(0)
# print(months.readlines())

for month in months:
    print(month.strip())


months.close()

days=open("day.txt",'a')
days.write("Tuesday")
print(days.mode)

days.close()



