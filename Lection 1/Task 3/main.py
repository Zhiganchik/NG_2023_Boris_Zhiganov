print("Converter temperature")
def celcius_in_Fahrenheit(Cel):
    return (Cel * 9 / 5) + 32
def Fahrenheit_in_celcius(Far):
    return (Far - 32) * 5 / 9
conversion = input("what should be done ('1' for 'Cel in Far' or '2' for 'Far in Cel'): ")
if conversion == "1":
    Cel = float(input("Load temperature in Cel: "))
    Far = celcius_in_Fahrenheit(Cel)
    print (str(Cel) + "degrees celcius equals" + str(Far) + "degrees in Fahrenheit")
elif conversion == "2":
    Far = float(input("Load temperature in Far: "))
    Cel = Fahrenheit_in_celcius(Far)
    print (str(Far) + "degrees Fahrenheit equals" + str(Cel) + "degrees in celcius")