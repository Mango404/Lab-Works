# TODO Найдите количество книг, которое можно разместить на дискете
import numbers

weight_book = 4 * 25 * 50 * 100
Mb_to_b = 1.44 * 1024 * 1024
numb_of_books = Mb_to_b // weight_book
numb_of_books = int(numb_of_books)
print("Количество книг, помещающихся на дискету:", numb_of_books)
