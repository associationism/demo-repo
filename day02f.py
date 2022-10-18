def add(a, b):
    return a + b


def get_number():
    try:
        return int(input("Adjon meg egy számot: "))
    except:
        print("Ez nem szám te f*sz!")
        return get_number()

a = get_number()
b = get_number()

print(add(a,b))