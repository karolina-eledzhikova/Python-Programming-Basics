searched_book = input()
books_counter = 0
book_is_found = False # reshavame da;i da bude False ili True v zavisimost ot tova dali sme namerili ili ne sme namerili knigata , a imenno v sluchaq Ne e namerena *(False)
next_book = input()
while next_book != 'No More Books':
    if next_book == searched_book:
        book_is_found = True
        break  # ne sojihme else zashtoto imame break i taka ili inache nqma da produlji cikula nadolu
    books_counter += 1
    next_book = input()
if book_is_found:   # if books_is_found == True:
        print(f'You checked {books_counter} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {books_counter} books.')




