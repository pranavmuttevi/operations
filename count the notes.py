
Amount = int(input("Please Enter Amount for Withdrawal: "))


note_100 = Amount // 100
note_50 = (Amount % 100) // 50
note_10 = ((Amount % 100) % 50) // 10

print("Notes of 100 rupees:", note_100)
print("Notes of 50 rupees:", note_50)
print("Notes of 10 rupees:", note_10)
