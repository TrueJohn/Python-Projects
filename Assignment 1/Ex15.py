from datetime import date

'''
we input the day , month and year for each date and then we calculate the days between them
'''

print('Please input the Day , Month and Year')
print('DATE1:')
d1 = int(input('Day='))
m1 = int(input('Month='))
y1 = int(input('Year='))
d0 = date(y1, m1, d1)
print('')
print('Date2:')
d2 = int(input('Day='))
m2 = int(input('Month='))
y2 = int(input('Year='))
d1 = date(y2, m2, d2)
delta = d1 - d0

print('The number of days between Date1 and Date2 is =', delta.days + 1)

print('')
input('Press any key to exit')
