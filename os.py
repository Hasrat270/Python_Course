import os
current_directory = os.getcwd()
print("Current Working Directory:", current_directory)
print("List of files and directories in 'os' module path:", os.listdir())

print("\n OS storage information: ")
print("Total space:", os.statvfs('.').f_blocks * os.statvfs('.').f_frsize)
print("Available space:", os.statvfs('.').f_bavail * os.statvfs('.').f_frsize)

# Storage info in GBs
total_space_gb = (os.statvfs('.').f_blocks * os.statvfs('.').f_frsize) / (1024**3)
available_space_gb = (os.statvfs('.').f_bavail * os.statvfs('.').f_frsize) / (1024**3)
print(f"Total space (GB): {total_space_gb:.2f} GB")
print(f"Available space (GB): {available_space_gb:.2f} GB")

print("\n OS environment variables: ")
for key, value in os.environ.items():
    print(f"{key}: {value}\n")