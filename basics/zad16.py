# Zadanie 16. Zmiana wartości zmiennych
# Przypisz x = 10, y = 20
# Zamień ich wartości bez użycia trzeciej zmiennej.

#Python way
x = 10 
y = 20

print(x, y)
x, y = y, x
print(x, y)

# Classic way

x = x - y 
y = y + x 
x = y - x

print(x, y)