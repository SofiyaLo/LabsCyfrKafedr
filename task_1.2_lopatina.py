# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
num_strings = 50
num_symbols = 25
sym_weight = 4

storage = 1.44
kilob = 1024
megab = 1024

num_books = storage * megab * kilob // (pages * num_strings * num_symbols * sym_weight)
print("Количество книг, помещающихся на дискету:", int(num_books))
