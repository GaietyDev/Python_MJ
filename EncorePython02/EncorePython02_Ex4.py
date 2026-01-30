minute = 1
hour = 60 * minute
day = 24 * hour
week = 7 * day
year = 365.25 * day

user_age_years = int(input("Enter your age(years): "))
user_age_minutes = year * user_age_years
print("Your age in minutes is:", user_age_minutes)
