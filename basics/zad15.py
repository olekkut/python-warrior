# Zadanie 15. Sprawdzenie, czy liczba jest parzysta
# Pobierz liczbę od użytkownika.
# Sprawdź, czy jest parzysta (operator %).


number = int(input('Proszę wprowadzić liczbę: '))
print('Jeżeli ta liczba ->', number % 2, 'Jest równa 1, to wprowadzona liczba', number, 'jest nieparzysta')
print('Jeśli ta liczba ->', number % 2,'jest równa 0, to wprowadzona liczba', number, 'jest liczbą parzystą')

# I know this is a naive and inefficient way to simulate a conditional statement,
# but the goal is to achieve the desired logic without using an explicit 'if' statement.