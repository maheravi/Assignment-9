import ClassMedia


def read_from_database():
    ff = open('media_database.csv', 'r')
    big_text = ff.read()
    product_list = big_text.split('\n')
    media_data = ClassMedia.Collection()
    for i in range(len(product_list)):
        data = product_list[i].split(',')
        print(data)
        if data[0] == 'film':
            media_data.addProduct(ClassMedia.Film(data))
        elif data[0] == 'series':
            media_data.addProduct(ClassMedia.Series(data))
        elif data[0] == 'documentary':
            media_data.addProduct(ClassMedia.Documentary(data))
        elif data[0] == 'clip':
            media_data.addProduct(ClassMedia.Clip(data))
    return media_data


def show_menu():
    print('Welcome to store')
    print('1- add new products')
    print('2- search')
    print('3- edit')
    print('4- remove')
    print('5- show all')
    print('6- Exit')


products = read_from_database()

while True:
    show_menu()
    choice = int(input('enter your choice: '))

    if choice == 1:
        category = input('enter the category of data\n ( film, series, documentary, and clip ): ')

        if category == 'film':
            name = input('name: ')
            director = input('director: ')
            score = input('IMDB score: ')
            url = input('url: ')
            duration = input('duration: ')
            casts = input('casts: ')
            data = [category, name, director, score, url, duration, casts]
            products.addProduct(ClassMedia.Film(data))
        elif category == 'series':
            name = input('name: ')
            director = input('director: ')
            score = input('IMDB score: ')
            url = input('url: ')
            duration = input('duration: ')
            casts = input('casts: ')
            seasons = input('number of seasons: ')
            episode = input('number of episode: ')
            data = [category, name, director, score, url, duration, casts, episode, seasons]
            products.addProduct(ClassMedia.Series(data))
        elif category == 'documentary':
            name = input('name: ')
            director = input('director: ')
            url = input('url: ')
            duration = input('duration: ')
            episode = input('number of episode: ')
            data = [category, name, director, 0, url, duration, 0, episode]
            products.addProduct(ClassMedia.Documentary(data))
        elif category == 'clip':
            name = input('name: ')
            director = input('director: ')
            url = input('url: ')
            duration = input('duration: ')
            casts = input('casts: ')
            data = [category, name, director, 0, url, duration, casts]
            products.addProduct(ClassMedia.Clip(data))
        else:
            print('Wrong! Please correct your input')

    elif choice == 2:
        user_input = input('enter name of media to search: ')
        products.search(user_input)

    elif choice == 3:
        user_input = input('enter name of media to edit: ')
        a = products.search(user_input)
        category = input('enter the category of data\n ( film, series, documentary, and clip ): ')
        name = input('name: ')
        director = input('director: ')
        score = input('IMDB score: ')
        duration = input('duration: ')
        url = input('url: ')
        casts = input('casts (divided by -): ')
        episode = input('episode: ')
        products.removeProduct(a)
        data = [category, name, director, score, url, duration, casts, episode]

        if category == 'film':
            products.addProduct(ClassMedia.Film(data))
        elif category == 'clip':
            products.addProduct(ClassMedia.Clip(data))
        elif category == 'documentary':
            products.addProduct(ClassMedia.Documentary(data))
        elif category == 'series':
            products.addProduct(ClassMedia.Series(data))
        else:
            print('Wrong! Please correct your input')

    elif choice == 4:
        user_input = input('enter name of media to remove: ')
        a = products.search(user_input)
        products.removeProduct(a)

    elif choice == 5:
        products.inventory()

    elif choice == 6:
        choice = input('Would you like to save your change in database? (y or n): ')
        if choice == 'y':
            f = open("database.csv", "w")
            for product in products:
                pass
        if choice == 'n':
            exit()