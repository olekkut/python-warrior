# Zadanie 19. Łączenie zmiennych
# Pobierz trzy słowa od użytkownika i połącz je w jedno zdanie.

first_word = input('Podaj pierwsze słowo: ')
second_word = input('Podaj drugie słowo: ')
third_word = input('Podaj trzecie słowo: ')

sentence = first_word + ' ' + second_word + ' ' + third_word

print('Twoje zdanie to: ', sentence, '.', sep='')