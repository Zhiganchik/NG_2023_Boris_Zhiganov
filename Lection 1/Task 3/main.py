x = ("Converter temperature")
print (x)
def celcius_in_Fahrenheit(Cel):
    return (Cel * 95 / 5) + 32
def Fahrenheit_in_Fahrenheit(Far):
    return (Far - 32) * 5/9
if conversion == "Cel in Far":
    Cel = float(input("Load t in Cel: "))
    Far = celcius_in_Fahrenheit(Cel)
    print (str(Cel) + "degrees celcius equals" + str(Far) + "degrees in Fahrenheit")
elif conversion == "Far in Cel":
    Far = float(input("Load t in Far: "))
    Cel = Fahrenheit_in_Fahrenheit(Far)
    print (str(Far) + "degrees Fahrenheit equals" + str(Cel) + "degrees in celcius")

