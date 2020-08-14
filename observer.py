#_*_ coding: utf-8 _*_

class Observable():
    
    viewer = []

    def register(self, obj):
        self.viewer.append(obj)

    def remove(self, obj):
        self.viewer.remove(obj)

    def notify(self, message):
        for observer in self.viewer:
            observer.Aviso(message)

class Observer():
    
    def Aviso(self):
        raise print("algo, no sé")

class Watcher(Observer):

    def __init__(self, obj):
        self.someone = obj
        self.someone.register(self)
        return 

    def Aviso(self, message):
        print('Alguien fue "{}" en la base de datos'.format(message))


#afmb_89