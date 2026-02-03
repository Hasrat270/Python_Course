from datetime import datetime, timedelta

mfg_str = input("Manufacture date (YYYY-MM-DD): ")
days = int(input("Validity in days: "))

mfg_date = datetime.strptime(mfg_str, "%Y-%m-%d")
expiry_date = mfg_date + timedelta(days=days)
today = datetime.now()

print(f"Expiry Date: {expiry_date.strftime('%Y-%m-%d')}")

if today > expiry_date:
    print("Status: EXPIRED")
else:
    print("Status: VALID")