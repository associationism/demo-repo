# írjunk egy függvényt, ami paraméterben kap 2 számot
# majd az eredménnyel tér vissza a hívás helyére

def addition(num1: int, num2: int) -> int:
    return num1 + num2

num3 = addition(5, 8)
print(num3)

a = int(input("Adjon meg egy számot: "))
b = int(input("Adjon meg még egy számot: "))

num4 = addition(a, b)
print(num4)

print(addition(int(input("Adjon meg egy számot: ")), int(input("Adjon meg egy számot: "))))