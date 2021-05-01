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
        self.noe = data[7] # number of episodes
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
            print("---------------------")
        return self

    def search(self, n):
        for i in self.products:
            if i.name == n:
                i.showinfo()
                return i
        else:
            print('wrong! not found')
