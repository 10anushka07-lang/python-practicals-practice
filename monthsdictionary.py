months = {
    "January": 31,"February": 28,"March": 31,"April": 30,"May": 31,"June": 30,"July": 31,"August": 31,"September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}
month_name=(input("enter a month name:"))
if (month_name in months):
    print(month_name,months[month_name])
print("list in alphabetical order")    
for month in sorted(months.keys()):
    print(month)
print("Months with 31 days:")
for month, days in months.items():
    if days == 31:
        print(month)
