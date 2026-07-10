temperature = int(input("What is the temperature right now? "))

if temperature > 25:
    print("It is Summer right now!")
elif temperature > 10 and temperature <= 25:
    print("It is in between Summer and Winter right now!")
else:
    print("It is winter right now!")