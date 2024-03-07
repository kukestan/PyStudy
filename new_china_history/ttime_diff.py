import datetime
from dateutil import rrule
from dateutil.relativedelta import *

def month_diff(d1, d2):
    months = rrule.rrule(rrule.MONTHLY, dtstart=d1, until=d2).count()
#    print(f"months={months}")
    return months
print((datetime.date(1921, 7, 1) + relativedelta(months = +1)).month)
#d1 = datetime.date(1921, 7, 1)
#d2 = datetime.date(1928, 7, 1)
#month_diff(d1, d2)