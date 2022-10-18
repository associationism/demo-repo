def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

option = ""

while option != "exit":
    option = input("Milyen műveletet akar végrehajtani? + -\n(kilépés 'exit')\n")
    if option == "+":
        a = int(input("Adjon meg egy számot: "))
        b = int(input("Adjon meg még egy számot: "))
        result = addition(a, b)
        print(f'Az eredmény: {result}')
    elif option == "-":
        a = int(input("Adjon meg egy számot: "))
        b = int(input("Adjon meg még egy számot: "))
        result = subtraction(a, b)
        print(f'Az eredmény: {result}')
    elif option == "exit":
        break
    else:
        print("Nincs ilyen opció!")

print("Program vége.")
