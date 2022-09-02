from models import *
# a=Mobile_Phone.qoshish()
# a.save()
while True:
    k=int(input("Qaysi class da ishlamoqchisiz MOBIL uchun 1 ni Android uchun 2 ni IOS uchun 3 ni Windows uchun 4 ni bosing: "))
    if k==1:
        c=int(input("Qo'shish uchun 1 ni O'zgartirish uchun 2 ni Print uchun 3 ni bosing"))
        if c==1:
            Mobile_Phone.qoshish().save()
        elif c==2:
            x=input("qaysi qatorni o'zgartirish kerak: ")
# with shelve.open(getAbtolutePath(Mobile_Phone.table)) as db:
#     a=db['1']
#     a.delite()
#                 a=db[x]
#                 a.update()
        elif c==3:
             Mobile_Phone.print()
    elif k==2:
        c=int(input("Qo'shish uchun 1 ni O'zgartirish uchun 2 ni Print uchun 3 ni bosing"))
        if c==1:
            Android.qoshish().save()
        elif c==2:
            x=input("qaysi qatorni o'zgartirish kerak: ")
            with shelve.open(getAbtolutePath(Android.table)) as db:
                a=db[x]
                a.update()
        elif c==3:
             Android.print()
            
    elif k==3:
        c=int(input("Qo'shish uchun 1 ni O'zgartirish uchun 2 ni Print uchun 3 ni bosing"))
        if c==1:
            IOS.qoshish().save()
        elif c==2:
            x=input("qaysi qatorni o'zgartirish kerak: ")
            with shelve.open(getAbtolutePath(IOS.table)) as db:
                a=db[x]
                a.update()
        elif c==3:
             IOS.print()

    elif k==4:
        c=int(input("Qo'shish uchun 1 ni O'zgartirish uchun 2 ni Print uchun 3 ni bosing"))
        if c==1:
            Windows.qoshish().save()
        elif c==2:
            x=input("qaysi qatorni o'zgartirish kerak: ")
            with shelve.open(getAbtolutePath(Windows.table)) as db:
                a=db[x]
                a.update()
        elif c==3:
             Windows.print()

             
