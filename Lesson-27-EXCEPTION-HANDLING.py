try:
    celcius = int (input("Enter the tempeature of celcious scale :"))
    farenite = (celcius * (9/5)) + 32
    print(farenite)
    print(f"F to celcious ratio(F/C): {farenite / celcius}")
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Celcious can not be 0")    