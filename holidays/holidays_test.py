import holidays

us_holidays = holidays.country_holidays('US')
start_date = '2024-01-01'
end_date = '2024-12-31'
holidays_in_range = us_holidays[start_date:end_date]
for date in holidays_in_range:
    print(f'{date}---{us_holidays.get(date)}')

cn_holidays = holidays.country_holidays('CN')
holidays_in_range = cn_holidays[start_date:end_date]
for date in holidays_in_range:
    print(f'{date}---{cn_holidays.get(date)}')