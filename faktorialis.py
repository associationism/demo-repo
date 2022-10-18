
def faktorialis(number):
    if number == 0:
        return 1
    elif number > 0:
        return number * faktorialis(number -1)
    else:
        print("Nem értelmezhető.")
        return 0

a = int(input("Adjon meg egy számot: "))

result = faktorialis(a)
print(f'A(z) {a} faktoriálisa: {result}')













