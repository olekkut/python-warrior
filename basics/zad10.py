# Zadanie 10. Formatowanie napisów
# Pobierz imię i wiek użytkownika.
# Wyświetl komunikat w formacie:
# Cześć, [imię]! Masz [wiek] lat.

name = input('Proszę wprowadzić swoje imię: ')
age = int(input('Proszę wprowadzić swój wiek: '))
print('Cześć, ', name,'! ','Masz ', age, ' lat.',sep='')