print(""" 
**********************
Hesap Makinesi

Toplama = 1

Çikarma = 2

Çarpma = 3

Bölme = 4

Üs almak için = 5

Sayinin karekökünü almak için = 6

Sayinin logaritmasi için = 7

dereceyi radyana çevirmek için = 8

radyani dereceye çevirmek için = 9

sinüs ü bulmak için = 10

cos u bulmak için = 11

tanjanti bulmak için = 12

cotenjanti bulmak için = 13

çikmak için 'q' ya basin
 **********************
""")

import math
import time

while True:
    işlem = int(input("işleminizi giriniz:"))
    
    if ( işlem == 'q'):
        print("işleminiz sonlandiriliyor")
        time.sleep(1)
        print("tekrar bekleriz")
        break

    elif(işlem == 1):
        sayi1 = int(input( "lütfen birinci sayiyi giriniz:"))
        sayi2 = int(input( "lütfen ikinci sayiyi giriniz"))
        print("işleminiz yapiliyor...")
        time.sleep(1)
        print("{} + {} = {} ".format(sayi1,sayi2,sayi1+sayi2))


    elif(işlem == 2):
        sayi1 =int(input("lütfen birinci sayiyi giriniz:"))
        sayi2 =int(input("lütfen ikinci sayiyi giriniz:"))
        print("işleminiz yapiliyor...")
        time.sleep(1)
        print("{} - {} = {}".format(sayi1,sayi2,sayi1-sayi1))


    elif (işlem == 3):
        sayi1= int(input("lütfen birinci sayıyı giriniz:"))
        sayi2= int(input("lütfen ikinci sayiyi giriniz:"))
        print("işleminiz yapiliyor...")
        time.sleep(1)
        print("{} x {} = {}".format(sayi1,sayi2,sayi1*sayi2))


    elif( işlem == 4):
        sayi1 =int(input("lütfen birinici sayiyi giriniz:"))
        sayi2 =int(input("lütfen ikinci sayiyi giriniz"))
        print("işleminiz yapiliyor...")
        time.sleep(1)
        print("{} % {} = {}".format(sayi1,sayi2,sayi1 / sayi2))


    elif( işlem == 5):
        sayi1 =int(input("lütfen birinici sayiyi giriniz:"))
        sayi2 =int(input("lütfen ikinci sayiyi giriniz"))
        print("işleminiz yapiliyor...")
        time.sleep(1)
        x = math.pow(sayi1,sayi2)
        print("{} % {} = {}".format(sayi1,sayi2,math.pow(sayi1,sayi2)))


    elif( işlem == 6):
        sayi1 =int(input("lütfen karakökünü almak istediğiniz sayiyi giriniz:"))
        print("işleminiz yapiliyor...")
        time.sleep(1)
        x = math.sqrt(sayi1)
        print("{} sayisinin karakökü = {}".format(sayi1,math.sqrt(sayi1)))


    elif( işlem == 7):
        sayi1 =int(input("lütfen birinici sayiyi giriniz:"))
        sayi2 =int(input("lütfen ikinci sayiyi giriniz"))
        print("işleminiz yapiliyor...")
        time.sleep(1)
        x = math.log(sayi1,sayi2)
        print("{} sayisinin {} tabaninda logaritmasi = {}".format(sayi1,sayi2,math.log(sayi1,sayi2)))


    elif( işlem == 8):
        sayi1 =int(input("lütfen lütfen radyanini öğrenmek istediğiniz dereceyi giriniz:"))
        print("işleminiz yapiliyor...")
        time.sleep(1)
        x = math.degrees(sayi1)
        print("{} derece {} radyandir.".format(sayi1,math.degrees(sayi1)))


    elif( işlem == 9):
        sayi1 =int(input("lütfen derecesini öğrenmek istediğiniz radyani giriniz:"))
        print("işleminiz yapiliyor...")
        time.sleep(1)
        x = math.radians(sayi1)
        print("{} radyan {} derecedir.".format(sayi1,math.radians(sayi1))) 


    elif( işlem == 10):

       a=input("radyan için 'r' derece için 'd' giriniz:") 
       
       
       if( a == "d" or a == "D"):
        sayi1 = int(input(" dereceyi giriniz : "))
        x = math.sin(sayi1)
        print("işleminiz yapiliyor...")
        time.sleep(1)
        print("sin {} = {} ".format(sayi1,x))
        
        
       elif(a == "r" or a == "R"):
            sayi1 = int(input(" radyanı giriniz : "))
            x = math.sin(sayi1)
            y = math.radians(x)
            print("işleminiz yapiliyor...")
            time.sleep(1)
            print("sin {} = {} ".format(sayi1,math.sin(math.radians(sayi1))))

        
    elif(işlem == 11):
        sayi1 = int(input(" dereceyi giriniz : "))
        print("işleminiz yapiliyor...")
        time.sleep(1)
        print("cos {} = {} ".format(sayi1,math.cos(sayi1)))


    elif(işlem == 12):
        sayi1 = int(input(" Dereceyi giriniz : "))
        print("işleminiz yapiliyor...")
        time.sleep(1)
        print("tanjant {} = {} ".format(sayi1,math.tan(sayi1)))


    elif(işlem == 13):
        sayi1 = int(input(" Dereceyi giriniz : "))
        print("işleminiz yapiliyor...")
        time.sleep(1)
        x = math.cos(sayi1)/math.sin(sayi1)
        print("cotanjant {} = {} ".format(sayi1,x))

        
        
        








