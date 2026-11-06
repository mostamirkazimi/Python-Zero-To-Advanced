import datetime

# زمان فعلی
now = datetime.datetime.now()
print("زمان فعلی:", now)

# تاریخ خاص
birthday = datetime.date(1999, 5, 16)
print("تاریخ تولد:", birthday)

# محاسبه فاصله بین دو تاریخ
today = datetime.date.today()
age_days = (today - birthday).days
print("تعداد روزهای عمر:", age_days)
