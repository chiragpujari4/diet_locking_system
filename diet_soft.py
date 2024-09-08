# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 13:53:31 2023

@author: Chirag Pujari
"""

#Jay Shree Ganeshaya Namah
#Jay Mata Di

#{Health management system with time and date}
#{Diet}

import datetime


a=input("Enter the Name of the Dish: ")
b=int(input("Category(1=Green vegetable,2=Junk food,3=Protein,4=Normal residential food,5=Juice,6=Fruit): "))
c=input("Does you ate any dry fruit i.e. Kaju or Badam {Y for yes and N for no} : " )
ti=datetime.datetime.now()
form=str(ti)
f=open("diettry.txt", "a")
f.writelines(["[",form,"]","   ",a,"\n"])
f.close()

f=open("diettry.txt", "r")
print(f.read())
f.close()

print("Comment: ")
if(b==1):
    print("Very Good ! , it's great to eat a lot of green vegetables.")
if(b==2):
    print("Please eat any green vegetable next time to compensate it.")
if(b==3):
    print("Great to have protein in the diet but keep remember that it should be consumed in limits.")
if(b==4):
    print("Ghar Ka Khana is best as it contains all the necessary diets in a single plate.")
if(b==5):
    print("You entaked vitamin C, but keep remember to consume it in limited amount as it contains a lot of sugar.")
if(b==6):
    print("It's great to have some fruits in a day for your skin health !")
if(c=="Y"):
    d=input("Kaju or Badam ? : ")
    if(d=="Kaju"):
        print("Congratulation ! , you gained 18g protein for each kaju.")
    if(d=="Badam"):
        print("Congratulation ! , you gained 20g protein for each badam.")
print("Thank You ! for using our services.")    
        



        