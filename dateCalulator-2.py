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
	
def print_age(person):
	age = diff(datetime.today(), person[1])
	pstrng = person[0] + ": " + str(age.years) + "yrs " 
	pstrng += str(age.months) + "mnths & " + str(age.days) + "dys old"
	return pstrng
	
def age_diff(p_one, p_two):
	d = diff(p_one[1], p_two[1])
	pstrng = p_one[0] + " & " + p_two[0] + " are "
	pstrng += str(d.years) + "yrs " + str(d.months) + "mnths & " + str(d.days) + "dys apart."
	return pstrng

melody_bday = datetime(1982, 12, 24)
david_bday = datetime(1986, 9, 12)
kylie_bday = datetime(2016, 5, 30)
harvey_bday = datetime(2018, 7, 1)
dad_bday = datetime(1954, 10, 3)
mom_bday = datetime(1955, 7, 17)
kurt_bday = datetime(1976, 12, 7)
stephanie_bday = datetime(1978, 6, 30)
angie_bday = datetime(1980, 3, 13)
michelle_bday = datetime(1982, 2, 10)
jonathan_bday = datetime(1992, 6, 15)
christian_bday = datetime(1998, 4, 11)
ulbrichs = [
	("MELODY", melody_bday), #0
	("DAVID", david_bday), #1
	("KYLIE", kylie_bday), #2
	("HARVEY", harvey_bday), #3
	("DAD", dad_bday), #4
	("MOM", mom_bday), #5
	("KURT", kurt_bday), #6
	("STEPHANIE", stephanie_bday), #7
	("ANGIE", angie_bday), #8
	("MICHELLE", michelle_bday), #9
	("JONATHAN", jonathan_bday), #10
	("CHRISTIAN", christian_bday) #11
]

for member in ulbrichs:
	print(print_age(member))

#print(age_diff(ulbrichs[6], ulbrichs[4]))
#print(age_diff(ulbrichs[11], ulbrichs[6]))
#print(age_diff(ulbrichs[11], ulbrichs[4]))

#print(age_diff(ulbrichs[1], ulbrichs[0]))
