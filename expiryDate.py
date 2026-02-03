from datetime import datetime, timedelta

# Step 1: Input
mfg_str = input("Manufacture date (YYYY-MM-DD): ")
days = int(input("Validity in days: "))

# Step 2: Calculate
mfg_date = datetime.strptime(mfg_str, "%Y-%m-%d")
expiry_date = mfg_date + timedelta(days=days)
today = datetime.now()

# Step 3: Display
print(f"\nExpiry Date: {expiry_date.strftime('%Y-%m-%d')}")

if today > expiry_date:
    print("Status: EXPIRED")
else:
    print("Status: VALID")