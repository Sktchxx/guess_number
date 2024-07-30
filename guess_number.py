from random import randint
s = randint(1,100)
print('Угадайте число от 1 до 100')
while True:
    guess = int(input('Ввведите число: '))
    if guess < s:
        print('Ваше число меньше того, что загадано')
    if guess > s:
        print('Ваше число больше того, что загадано')
    if  guess == s:
        break
print('отличная интуиция! Вы угадали число :)')