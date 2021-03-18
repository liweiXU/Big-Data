import numpy as np
import pandas as pd
import random as rd 

#Question 1

def generation_TAD(M,R):
    A= np.zeros(M)
    for i in range (R):
        nb_rand=rd.randrange(M)
        A[nb_rand]=A[nb_rand]+1
    return A,vide(A),np.mean(A),np.max(A),np.min(A),np.median(A),np.var(A)


def vide(TAD):
    compt=0
    for i in TAD:
        if i==0:
            compt+=1
    return compt

#Question 2
file=open('/Users/xuliwei/texte_Shakespeare.txt')
#Nous avons décidé de travailler sur le document "texte_Shakespeare.txt" qui contient 22 000 valeurs
#donc afin d'avoir une efficacité optimale tout en limitant les collisions au maximum, prenons une 
#table de hachage à peu près 5 fois plus grande. Choisir un nombre premier étant avantageux, prenons
#une taille MM = 100 003

#Question 3
#concob_lowercase=pd.read_table('corncob_lowercase.txt')
texte_Shakespeare=pd.read_table('/Users/xuliwei/texte_Shakespeare.txt')
#word2=pd.read_table('word2.txt')
doc ={}
with open("/Users/xuliwei/texte_Shakespeare.txt","r") as f:
    compt=0
    for line in f :
        elements=line.split()
        mot=elements[0]
        doc[compt]=mot
        compt+=1
        
#Question 4 
def fonction_hashage(mot,taille): # somme les codes ASCII des lettres composant le mot
    hash_num=0
    for char in mot :
        hash_num += ord(char)
    return hash_num % taille

def table_hash(taille): # Génère une liste des listes vide de taille M (100003 ici)
    return [[] for i in range(taille)]

def remplissage_hash(liste,taille): # Remplit la table de hashage ainsi que la TAD qui sert pour 
    hash_table=table_hash(taille)   # compter les collisions
    A=np.zeros(taille)
    for i in range (len(liste)):
        hash_table[fonction_hashage(liste.get(i),taille)].append(liste.get(i))
        A[fonction_hashage(liste.get(i),taille)]+=1
    return hash_table,A

#Question 5
def data_collision(mat_coll): # Analyse la fonction A retournée par "remplissage_hash" (collisions,...)
    return vide(mat_coll),(vide(mat_coll)+len(doc))-len(mat_coll),np.mean(mat_coll),np.max(mat_coll),np.min(mat_coll),np.median(mat_coll),np.var(mat_coll)

#Question 6
def fonction_hashage2(mot,taille): # Fonction plus performante qui somme les puissances 4 des codes
    hash_num=0                     # ASCII des lettres composant les mots (creuse les écarts)
    for char in mot : 
        hash_num += ord(char)**4
    return hash_num % taille

def remplissage_hash2(liste,taille): # liste correspond au document texte_Shakespeare.txt sous forme
    hash_table=table_hash(taille)    # de dictionnaire, taille : la taille de la table de hashage
    A=np.zeros(taille)               # TAD pour compter les collisions  
    for i in range (len(liste)):
        hash_table[fonction_hashage2(liste.get(i),taille)].append(liste.get(i))
        A[fonction_hashage2(liste.get(i),taille)]+=1
    return hash_table,A
