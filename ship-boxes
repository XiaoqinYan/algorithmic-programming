height_big = float(input(''))
height_small = float(input(''))
thickness_book = float(input(''))
num_books = int(input('')) 

if (height_small >= (thickness_book*num_books)):
    print('Ship 1 small box')
if height_big >= (thickness_book * num_books):
    print('Ship 1 large box')

if (thickness_book * num_books > height_big) and (thickness_book * num_books > height_small) :
    num_book_per_large = int(height_big / thickness_book)
    num_large= int(num_books / num_book_per_large)
    remind_book = num_books % num_book_per_large
    if (remind_book * thickness_book < height_small):
        num_small = 1
        total = num_large +num_small   
        print('Shipping',total,'boxes')
        print(num_large,'large')
        print(num_small,'small')
elif (remind_book * thickness_book % height_small == 0):
        num_small =remind_book * thickness_book / height_small
        total = num_large +num_small   
        print('Shipping',total,'boxes')
        print(num_large,'large')
        print(num_small,'small')
        
else:
        num_small =int(remind_book * thickness_book / height_small)+1
        total = num_large +num_small   
        print('Shipping',total,'boxes')
        print(num_large,'large')
        print(num_small,'small')
