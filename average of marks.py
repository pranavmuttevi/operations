print("Enter Marks Obtained in 4 Subjects:")
math = int(input("Maths: "))
english = int(input("English: "))
science = int(input("Science: "))
hindi = int(input("Hindi: "))

sum = math + english + science + hindi
print("Sum of Maths, English, Science and Hindi =", sum)

perc = (sum / 400) * 100
print("Percentage Mark =", perc)
