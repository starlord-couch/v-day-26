#python

import time

print("Initializing Valentine Protocol...")
time.sleep(1)

cats = input("\nDo you love cats? (yes/no): ")
time.sleep(1)

fries = input("\nWould you still love me if I stole your fries? (yes/no): ")
time.sleep(1)

adventures = input("\nDo you see more adventures with me? (yes/no): ")
time.sleep(1)

print("Checking compatibility...")
time.sleep(1)
print("Result: 100% match ❤️")
time.sleep(1)

while True:
    answer = input("\nWill you be my Valentine? (yes/no): ").strip().lower()

    if answer.startswith("y"):
        print("""
💖💖💖 ACCESS GRANTED 💖💖💖
You are officially my Valentine.
""")
        break
    else:
        print("""
🚨 Recalibrating... 🚨
""")
        time.sleep(1)

input("\nPress Enter to continue our wonderful life together 💖💖💖")
