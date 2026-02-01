photo = input("Did you upload your photo? (yes/no): ").lower()
id_card = input("Did you upload your ID card? (yes/no): ").lower()
sign = input("Did you sign the form? (yes/no): ").lower()

has_photo = (photo == "yes")
has_id = (id_card == "yes")
has_signed = (sign == "yes")

status = has_photo and has_id and has_signed

print(f"Form completion status: {status}")