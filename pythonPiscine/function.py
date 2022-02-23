#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:35:50 2022

@author: aichajeledi
"""

from math import*

#Question 1 :
    
def saisir():
    try:
        nom = input("entrez votre nom  : ")
        prenom = input("entrez votre prénom : ")
            
        return "nom : {} \nprenom : {}".format(nom, prenom)
     
    except TypeError: 
        print("veuillez saisir une chaine de caractère!!!! ")


#Question 2:
    
def afficheAge():
    try: 
        age_actuelle = input("entrez votre age : ")
        age_actuelle = int(age_actuelle)
        
        age_plus = 100 - age_actuelle
    
        age_cent = 2022 + age_plus
        
        print("age actuelle :  {} \n vous fetez vos 100 ans en : {} ".format(age_actuelle, age_cent))
    except ValueError:
        print("l'age est un entier !!!! ")
#Question 3 : 
    
def calculer():
    try :
        hauteur = input(" saisir une hauteur : ")
        h = int(hauteur)
        rayon = input(" saisir un rayon : ")
        r= int(rayon)
        
        # b = pi * r^2
        b = pi * r**2
        float(b)
        #TypeError
        
        # v =  1/3 b*h
        v = (b * h) / 3
        
        print(" le volume du cône = {} ".format(v))
    except ValueError:
        print("entrer des entiers !!! ")
    
#Duestion 4 :
def paire_impaire():
    try : 
        nb = input("veuillez entrer un nombre : ")
        nb = int(nb)
        
        if nb % 2 == 0 :
            print("le nombre saisie est paire ! ")
        else:
            print("le nombre saisie est impaire ! ")

    except ValueError:
        print(" veuillez saisir un nombre !!!!")
        
#Question 5 : 

def s_fibo():    
      
   try:
       n = int(input("Entrer un entier supérieur à 1 : "))
        
        
       fibo = [0]*(n)
        
       fibo[0] = 0
        
       fibo[1] = 1
        
        
       for i in range(2,n):
        
         fibo[i] = fibo[i-1] + fibo[i-2]
        
       print(fibo)
   except TypeError:
        print("saisir un entier !!! ")
        
