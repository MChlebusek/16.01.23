from operator import xor
from MyModule import *
flag=True
while flag:
    a=int(input("Registreerimine-1, autoriseerimine-2 exit-3: "))
    if a==1:
        login=input("login: ")
        b=input("automaatne parooli genereerimine-1,  sõltumatu-2 ")
        if b==1: 
            sala=salasona(10)
            print(sala)
        else:
            password = input("password:")
            password2 = input("password:")
            while password2 != password:
                print("erinev.")
                password = input("password:")
                password2 = input("password:")
            while len(password) < 10:
                print("Lühike!")
                password = input("password:")
                password2 = input("password:")
            while "123" in password:
                print("Lihtne!")
                password = input("password:")
                password2 = input("password:")           
        print ("olete registreerunud")
    elif a==2:
        login=input("login: ")
        password = input("password:")
        print("olete edukalt sisse loginud")
    elif a==3:
        print("vajutage klaviatuuril (esc)")
    else:
        print("error")


   

