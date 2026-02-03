from datetime import datetime, timedelta

# 1. Get the current time
now = datetime.now()
print(f"Original Object: {now}")
print("Type: ", type(now))

# 2. Format with seconds
formatted_with_seconds = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted (with seconds):", formatted_with_seconds)

# 3. Format without seconds (This is where the string is created)
formatted_date_string = now.strftime("%Y-%m-%d %H:%M")
print("Formatted (no seconds):  ", formatted_date_string)
print("Type of variable:        ", type(formatted_date_string))

# 4. Convert back to an object (FIXED)
# The format string must EXACTLY match the string variable's structure
manufacture_date = datetime.strptime(formatted_date_string, "%Y-%m-%d %H:%M")

print("Date time object again:  ", manufacture_date)
print("Type after strptime:     ", type(manufacture_date))

future_date = now + timedelta(days=100)
print("Date after 100 days:     ", future_date.date())