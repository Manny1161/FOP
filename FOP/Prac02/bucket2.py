print('\nBUCKET LIST BUILDER\n')

bucket = []

choice = input('Enter selection: e(X)it, (A)dd, (L)ist, (D)elete...')

while choice[0].lower() != 'x':
    if choice[0].lower()  == 'a':
        print('Enter list item... ')
        newitem = input()
        bucket.append(newitem)
    elif choice[0].lower() == 'l':
        for item in bucket:
            print(item)
    elif choice[0].lower() == 'd':
        print('Enter the item you want to delete...')
        delitem = input()
        del bucket[int(delitem)]
    else:
        print('Invalid selection.')
    choice = input('Enter selection: e(X)it, (A)dd, (L)ist..')
print('\nGOODBYE!\n')
