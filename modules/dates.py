# https://youtu.be/eirjjyP2qcQ
import datetime
import pytz

# NAIVE  -> do not have any info about timezones
# AWARE  -> have info about timezones

# DATE CLASS

# construct a date object
print(datetime.date(2020, 1, 19))

# get today's date
today = datetime.date.today()
print("Today is {}".format(today))

# get year, month or date from date object
print("Year is {}".format(today.year))
print("Month is {}".format(today.month))
print("Day is {}".format(today.day))

# Monday is 1 and Sunday is 7
print("Day of week is {}".format(today.isoweekday()))

# Monday is 0 and Sunday is 6
print("Day of week is {}".format(today.weekday()))

# TIME DELTA
# adding or subtracting dates gives a timedelta
# adding or subtracting a timedelta with a date gives date

td = datetime.timedelta(days=10)
print('{:%d %b %Y, %A}'.format(today + td))

td = today - datetime.date(2020, 6, 25)
print(td)

# TIME CLASS
sometime = datetime.time(23, 15, 33)
print(sometime)

# get hour, minute or secon from time object
print("Hour is {}".format(sometime.hour))
print("Minute is {}".format(sometime.minute))
print("Second is {}".format(sometime.second))

# DATETIME CLASS
# we can access all attributes like year etc used above
# can also use timedeltas

date_time = datetime.datetime.now()
print("Current date time is {0}".format(date_time))
print("Current time is {0}".format(date_time.time()))
print("Current date is {0}".format(date_time.date()))

# gives current datetime in local timezone
dt_today = datetime.datetime.today()
# allows to pass a timezone, if nothing is specified, takes local timezone
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()  # gives date time of UTC

# al the above three are naive datetimes

print(f"dt_today is {dt_today}")
print(f"dt_utc is {dt_now}")
print(f"dt_utcnow is {dt_utcnow}")

# TIMEZONE AWARE DATETIMES
dt_aware = datetime.datetime(2020, 11, 23, 10, 12, 25, tzinfo=pytz.UTC)
print(dt_aware)
dt_aware = datetime.datetime.now(tz=pytz.UTC)
print("Current UTC time is : {}".format(dt_aware))
print(dt_aware.tzinfo)

# after time, it prints the offset which indicates that this object is timezone aware
dt_local = dt_aware.astimezone(tz=pytz.timezone('Asia/Kolkata'))
print("Local date time is {}".format(dt_local))

# all the timezones available in pytz can be seen in pytz.all_timezones

# to make a naive datetime, datetime aware use localize
# create a naive date time object in local timezone
local_now = datetime.datetime.now()
my_tz = pytz.timezone('Asia/Kolkata')
# create a aware datetime and then use astimzone to convert it
useast_now = my_tz.localize(
    local_now).astimezone(tz=pytz.timezone("US/Eastern"))
print("Local now is {}".format(local_now))
print("US Eastern now is {}".format(useast_now))

# use strftime for time formatting i.e, converts date to string
local_now_str = local_now.strftime("%B %d, %Y")
print(local_now_str)

# to convert string into date object use strptime
local_now = datetime.datetime.strptime(local_now_str, '%B %d, %Y')
print(local_now)
