def computation(s, action, d):
    resultat = match action:
        case '+':
            s + d
        case '-':
            s - d
        case '*':
            s * d
        case '/':
            s / d
    return resultat 
s = float(input("enter the first number: "))
action = input("enter action (+, -, *, /): ")
d = float(input("enter second number: "))
resultat = computation(s, action, d)
print("Результат:", resultat)