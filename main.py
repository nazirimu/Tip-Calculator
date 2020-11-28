print('Welcome to the tip calculator!')
amount = float(input("What is the total bill? $"))
percentage = float(input("What percentage of tip would you like to give? %"))/100
people = int(input("How many people are splitting the bill? "))
total = (amount + amount*percentage)/people
print(f"The total for each person is ${total}")