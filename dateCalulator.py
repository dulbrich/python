from datetime import datetime
from calendar import monthrange

class Passed_Time:
	
	def __init__(self, years, months, days):
		self.years = years
		self.months = months
		self.days = days

def diff(d1, d2):
	diff_months = (d1.year - d2.year) * 12 + d1.month - d2.month
	diff_days = d1.day - d2.day
	if diff_days < 0:
		diff_months -= 1
		diff_days = monthrange(d1.year,d1.month-1)[1] + diff_days
	years = d1.year - d2.year
	diff_months = diff_months % 12
	if d1.month < d2.month:
		years -= 1
	if d1.month == d2.month and d1.day < d2.day:
		years -= 1
	return Passed_Time(years, diff_months, diff_days)

def price(time, today):
	months = (time.years*12) + time.months
	price = 100 * months
	month_percentage = time.days / monthrange(today.year,today.month)[1]
	price += 100 * month_percentage
	return price
	
bday = datetime(1986,9,12)
today = datetime(2018,10,22)
pt = diff(today, bday)
price = price(pt, today)
print("Years: " + str(pt.years) + " Months: " + str(pt.months) + " Days: " + str(pt.days))
#print("Price: " + str(price))
