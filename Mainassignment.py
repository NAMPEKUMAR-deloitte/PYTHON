

datab={"pavan":"12345"}
title=[]
genre=[]
length=[]
cast=[]
director=[]
admin1=[]
language=[]
timing=[]
shows=[]
first_show=[]
interval=[]
gap=[]
capacity=[]
movie=[title,genre,length,cast,director,admin1,language,timing,shows,first_show,interval,gap,capacity]

n=len(movie)

def book():
    print("1. Book Tickets ")
    print("******Welcome User1*******")
    print("number of tickets :",end=" ")
    nieo=input()
    users()


def cancel():
    print("2.Cancel Tickets")
    print("******Welcome User1*******")
    print("no of tickets to be canceled:",end=" ")
    nei=input()
    users()
def ratings():
    print("3.Give User Rating")
    print("******Welcome User1*******")
    print("Please enter rating for the following movie:",end=" ")
    nai=input()
    users()
def display(qpn):
    qpn=qpn-1
    for i in movie:
        print(i[qpn])

def users():
    print("**welcome user**")
    for i in title:
        yees=title.index(i)+1
        print(yees,i)
    qpn=int(input())
    display(qpn)
    print("1.book tickets")
    print("2.cancel tickets")
    print("3 give rating")
    userin=int(input())
    if userin==1:
        book()
    if userin==2:
        cancel()
    if userin==3:
        ratings()




def register(datab):
    print("**create new account**")
    print("name:",end=" ")
    names=input()
    print("password:",end=" ")
    datab[names]=input()
    welcome()



def admin():
    print("1 admin login")
    print("* welcome admin*")
    print("1.add new")
    print("2.edit")
    print("3.delete")
    print("4.logout")

    print("enter:",end=" ")
    choice=int(input())



    if choice==4:
        print("loged out")
        welcome()



    if choice==1:
        l=1

        print("addd new")
        print("**welcome admin*")
        print("title:",end=" ")
        title.append(input())
        print("genre:",end=" ")
        genre.append(input())
        print("length:",end=" ")
        length.append(input())
        print("cast:",end=" ")
        cast.append(input())
        print("director:",end=" ")
        director.append(input())
        print("admin rating:",end=" ")
        admin1.append(input())
        print("language:",end=" ")
        language.append(input())
        print("timings:",end=" ")
        timing.append(input())
        print("number of shows:",end=" ")
        shows.append(input())
        print("first show:",end=" ")
        first_show.append(input())
        print("interval:",end=" ")
        interval.append(input())
        print("gap between show:",end=" ")
        gap.append(input())
        print("capacity:",end=" ")
        capacity.append(input())
        admin()


    if choice==2:

        print("edit movie")
        print("**welcome admin*")
        print("title:",end=" ")
        ke=input()
        if ke in title:
            p=title.index(ke)
        print("genre:",end=" ")
        genre[p]=input()
        print("length:",end=" ")
        length[p]=input()
        print("cast:",end=" ")
        cast[p]=input()
        print("director:",end=" ")
        director[p]=input()
        print("admin rating:",end=" ")
        admin1[p]=input()
        print("language:",end=" ")
        language[p]=input()
        print("timings:",end=" ")
        timing[p]=input()
        print("number of shows:",end=" ")
        shows[p]=input()
        print("first show:",end=" ")
        first_show[p]=input()
        print("interval:",end=" ")
        interval[p]=input()
        print("gap between show:",end=" ")
        gap[p]=input()
        print("capacity:",end=" ")
        capacity[p]=input()
        admin()


    if choice==3:
        print("delete movie:")
        print("**welcome admin**")
        print("title of the movie to be deleted :",end=" ")
        pq=input()
        kol=title.index(pq)
        for m in movie:
            m.pop(kol)


def verify():
    print("*welcome to BookMyShow**")
    print("User:",end=" ")
    user=input()
    if user in datab:

        print("password",end=" ")
        password=input()
        if password==datab[user]:
            return True
        print("incorrect password")
    else:
        print("no user exist")
        welcome()



def welcome():
    print("*welcome to BookMyShow**")
    print("1.Login")
    print("2.register")
    print("3.exit")
    print("enter :",end=" ")
    uri=int(input())

    if uri==1:
        print("1.admin")
        print("2.user")
        print("enter:",end=" ")
        opt=int(input())
        if opt==1:
            if verify():
                admin()
        if opt==2:
            if verify():
                users()

    if uri==2:
        register(datab)
    if uri==3:
        print("vist again")
        exit()
welcome()
