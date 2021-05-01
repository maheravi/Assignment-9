import pytube
from ClassActors import Actor


class Media:
    def __init__(self, cc, nn, dd, im, ul, du, ca):
        self.category = cc
        self.name = nn
        self.director = dd
        self.score = im
        self.url = ul
        self.duration = du
        self.cast = ca

    def showinfo(self):
        print("---------------------")
        print('category of file is:', self.category)
        print('name of media:', self.name)
        print('name of director:', self.director)
        print('IMDB score:', self.score)
        print('trailer url:', self.url)
        print('duration of movie:', self.duration)

    def download(self):
        pytube.YouTube(self.url).streams.first().download()

    def casts(self):
        List = self.cast.split('-')
        for cast in List:
            Actor(cast).showActor()


class Film(Media):
    def __init__(self, data):
        Media.__init__(self, data[0], data[1], data[2], data[3], data[4], data[6], data[5])


class Series(Media):
    def __init__(self, data):
        Media.__init__(self, data[0], data[1], data[2], data[3], data[4], data[6], data[5])
        self.noe = data[7]  # number of episodes
        self.seasons = data[8]  # number of seasons


class Documentary(Media):
    def __init__(self, data):
        Media.__init__(self, data[0], data[1], data[2], data[3], data[4], data[6], data[5])
        self.topic = data[8]


class Clip(Media):
    def __init__(self, data):
        Media.__init__(self, data[0], data[1], data[2], data[3], data[4], data[6], data[5])
        self.theme = data[8]


class Collection:
    def __init__(self):
        # self.name = name
        self.products = []

    def addProduct(self, n):
        self.products.append(n)
        return self

    def removeProduct(self, n):
        self.products.remove(n)
        return self

    def inventory(self):
        print("displaying inventory:")
        print("---------------------")
        for i in self.products:
            i.showinfo()
            i.casts()
            if i.category == 'series':
                print('number of seasons:', i.seasons)
                print('number of episode:', i.noe)
                print("---------------------")
            if i.category == 'documentary':
                print('topic of documentary:', i.topic)
                print("---------------------")
            if i.category == 'clip':
                print('title of clip:', i.theme)
                print("---------------------")
        return self

    def search(self, n):
        for i in self.products:
            if i.name == n:
                i.showinfo()
                return i
        else:
            print('wrong! not found a media with this name')

    def save(self):
        f = open("database.csv", "w")
        for i in self.products:
            if i.category == 'film':
                f.write(i.category + ',' + i.name + ',' + i.director + ',' + i.score + ',' + i.url + ',' + i.duration +
                        ',' + i.cast + '\n')
            if i.category == 'series':
                f.write(i.category + ',' + i.name + ',' + i.director + ',' + i.score + ',' + i.url + ',' + i.duration +
                        ',' + i.cast + ',' + i.seasons + ',' + i.noe + '\n')
            if i.category == 'documentary':
                f.write(i.category + ',' + i.name + ',' + i.director + ',' + i.score + ',' + i.url + ',' + i.duration +
                        ',' + i.cast + ',' + str(0) + ',' + i.topic + '\n')
            if i.category == 'clip':
                f.write(i.category + ',' + i.name + ',' + i.director + ',' + i.score + ',' + i.url + ',' + i.duration +
                        ',' + i.cast + ',' + str(0) + ',' + i.theme + '\n')

    def searchBetween(self, a, b):
        for i in self.products:
            if i.duration >= a or i.duration <= b:
                print(i.showinfo())
            else:
                print('Sorry! not found the media with these specified duration')

    def downloadMedia(self, n):
        for i in self.products:
            try:
                if i.name == str(n):
                    print('The url of media found')
                    print('downloading...')
                    i.download()
                    print('Done!')
                    break
            except Exception as e:
                print('Wrong! Please correct your input', e)
                break
