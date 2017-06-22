import datetime

today = datetime.date.today()
print today
print today.year
print today.month
print today.day

bday = datetime.date(1969,2,6)
print bday
print bday.isoweekday()

print type(today)
print type(bday)

print today - bday

yDays = 365
tdelta1 = datetime.timedelta(yDays)

print tdelta1

daysUp = (today - bday).days
print "Days:",daysUp
print "tdelta:",type(tdelta1)
print "daysUp:",type(daysUp)
print daysUp / 365.25
afd = datetime.date(today.year, 4,1)
if afd < today:
    print "April Fool's Day already went by %d days ago" % ((today-afd).days)
    afd = afd.replace(year=today.year + 1)

time_to_afd = abs(afd - today)
print time_to_afd.days, "days until next April Fool's Day"


dt_UTC = datetime.datetime.now(tz=pytz.UTC)
dt_mtn = dt .astimezone(pytz.timezone('US/Mountain'))

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
