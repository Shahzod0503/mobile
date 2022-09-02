from abc import ABC

import shelve

from settings import db_path

from utlities import db_path,getAbtolutePath

class Bast_Model(ABC):
    table=""
    def __init__(self):
        self.inValite=True
        self.id=None

    @property
    def inValite(self):
        return self.__inValite
    @inValite.setter
    def inValite(self,inValite):
        self.__inValite=inValite

    def save(self):
        if  self.__inValite==True :
            db_path = getAbtolutePath(self.table)
            with shelve.open(db_path) as db:
                if self.id is None :
                    keys=tuple(db.keys())
                    if len(keys)>0:
                        self.id=int(keys[-1])+1
                    else:
                        self.id=1
                db[str(self.id)]=self
        else :
            print("saqlanmadi...")

    def update(self):
        pass


class Mobile_Phone(Bast_Model):

    table="Mobile_Phone"
    def __init__(self,name,price):
        super().__init__()
        self.id=None
        self.name=name
        self.price=price
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        if isinstance(name,str):
            self.__name=name
        else:
            self.__inValite=False
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,price):
        if isinstance(price,float):
            self.__price=price
        else:
            self.__inValite=False

    def qoshish():
        name=input("Nomi: ")
        price=float(input("Price: "))
        return Mobile_Phone(name,price)

    def update(self):
        self.name=input("Nomi: ")
        self.price=float(input("Price: "))
        self.save()

    def print():
        with shelve.open(getAbtolutePath(Mobile_Phone.table)) as db:
            for item in db:
                print(db[item])
    def delite(self):
        with shelve.open(getAbtolutePath(Mobile_Phone.table)) as db:
            del db[str(self.id)]

    def __str__(self):
        return f"{self.name} | {self.price}"
class Android(Mobile_Phone):
    table="Android"
    def __init__(self,name,price,brand,nfc):
        super().__init__(name,price)
        self.brand=brand
        self.nfc=nfc
    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self,brand):
        if isinstance(brand,str):
            self.__brand=brand
        else:
            self.__inValite=False

    @property
    def nfc(self):
        return self.__nfc
    @nfc.setter
    def nfc(self,nfc):
        if isinstance(nfc,bool):
            if nfc == "True":
                self.__nfc=nfc
            else :
                self.__nfc=nfc
        else:
            self.__inValite=False
    def qoshish():
        name=input("Nomi: ")
        price=float(input("Price: "))
        brand=input("Brand: ")
        nfc=bool(input("NFC ga true yoki false kiriting: "))
        return Android(name,price,brand,nfc)

    def update(self):
        self.name=input("Nomi: ")
        self.price=float(input("Price: "))
        self.brand=input("Brand: ")
        self.nfc=bool(input("NFC ga true yoki false kiriting: "))
        self.save()

    def print():
        with shelve.open(getAbtolutePath(Android.table)) as db:
            for item in db:
                print(db[item])
    def __str__(self):
        return super().__str__() + f"{self.brand} | {self.nfc}"
class IOS(Mobile_Phone):
    table="IOS"
    def __init__(self,name,price,drop):
        super().__init__(name,price)
        self.drop=drop
    @property
    def drop(self):
        return self.__drop
    @drop.setter
    def drop(self,drop):
        if isinstance(drop,bool):
            if drop == "True":
                self.__drop=drop
            else:
                self.__drop=drop
        else:
            self.__inValite=False
    def qoshish():
        name=input("Nomi: ")
        price=float(input("Price: "))
        drop=bool(input("Drop ga true yoki float bering: "))
        return IOS(name,price,drop)

    def update(self):
        self.name=input("Nomi: ")
        self.price=float(input("Price: "))
        self.drop=bool(input("Drop ga true yoki float bering: "))
        self.save()

    def print():
        with shelve.open(getAbtolutePath(IOS.table)) as db:
            for item in db:
                print(db[item])

    def __str__(self):  
        return super().__str__() + f"| {self.drop}"
class Windows(Mobile_Phone):
    table="Windows"
    def __init__(self,name,price,brand):
        super().__init__(name,price)
        self.brand=brand
    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self,brand):
        if isinstance(brand,str):
            self.__brand=brand
        else:
            self.__inValite=False


    def qoshish():
        name=input("Nomi: ")
        price=float(input("Price: "))
        brand=input("Brand: ")
        return Windows(name,price,brand)

    def update(self):
        self.name=input("Nomi: ")
        self.price=float(input("Price: "))
        self.brand=input("Brand: ")
        self.save()

    def print():
        with shelve.open(getAbtolutePath(Windows.table)) as db:
            for item in db:
                print(db[item])
    def __str__(self):
        return super().__str__() + f"| {self.brand}"
