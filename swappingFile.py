def swapFileData():
    file1 = input('1st file to swap contents: ')
    with open(file1, 'r') as a:
        data_a = a.read()
        print('current contents of '+file1+': '+data_a)
    file2 = input('2nd file to swap contents: ')
    with open(file2, 'r') as a:
        data_b = a.read()
        print('current contents of '+file2+': '+data_b)
    quest = input('Do you want to swap the contents listed above?, answer with y/n: ')
    if quest=='y':
        with open(file1, 'w') as a:
            a.write(data_b)
        with open(file1, 'r') as a:
            data_c = a.read()
        with open(file2, 'w') as a:
            a.write(data_a)
        with open(file2, 'r') as a:
            data_d = a.read()
        print('new contents of '+file1+': '+data_c)
        print('new contents of '+file2+': '+data_d)
    elif quest=='n':
        print('Your wish has been granted...')
swapFileData()