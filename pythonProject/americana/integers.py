positive = 0
negative = 0
zeros = 0

while True:
    number = int(input('enter a number or (-1) to stop: '))

    if number == -1:
        break

    if number == 0:
        zeros += 1
    if number > 0:
        positive += 1
    if number < 0:
        negative += 1

print('you have entered positive: ', positive, ' negative: ', negative, ' zeros: ', zeros)
