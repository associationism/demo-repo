#import konstans
from konstans import *
#import konstans as k
import random


def circle(r: float):
    return 2 * r * PI


print(circle(5))


lotto = []

while len(lotto) < 5:
    number = random.randint(0,90)
    if number in lotto:
        continue
    lotto.append(number)

print(lotto)