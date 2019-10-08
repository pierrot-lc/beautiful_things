# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 20:10:55 2016

@author: Tubuntu
"""

def tree(etage_max):
    milieu = calcul_milieu(etage_max)
    
    for etage in range(1, etage_max + 1):#Varie de 1 à etage_max (inclu)
        nbr_lignes = calcul_nbr_ligne(etage)
        numero_ligne = numero_ligne_debut_etage(etage)
        for ligne in range(numero_ligne, nbr_lignes + numero_ligne):
            print_symbole(nombre_etoile_ligne(ligne), milieu, "*")
            
    for i in range(etage_max):#Affichage du pied du sapin
        print_symbole(longueur_pied(etage_max), milieu, "|")
                
def print_symbole(nbr_symbole, milieu, symbole):
    nbr_blancs = int(milieu - ((nbr_symbole - 1)/2))
    for i in range(nbr_blancs):
        print(" ", end="")
    for i in range(nbr_symbole):
        print(symbole, end="")
    print("", end="\n")
    
def calcul_milieu(etage_max):
    nbr_lignes_max = numero_ligne_fin_etage(etage_max)
    nbr_etoiles_max = nombre_etoile_ligne(nbr_lignes_max)
    milieu = int((nbr_etoiles_max - 1)/2)
    return milieu

def calcul_nbr_ligne(etage):#Nombre de ligne à écrire pour 1 étage
    return etage + 3
    
def nombre_etoile_ligne(numero_ligne):#Renvois le nombre d'étoiles pour un numéro de ligne demandé
    return 1 + 2*(numero_ligne-1)
    
    
def numero_ligne_fin_etage(etage):
    numero_ligne = 0
    for i in range(etage):#Ajoute toutes les lignes comme si il n'y avait pas de décalage
        numero_ligne += 4 + i
    for i in range(1, etage):#Soustrait le décalage en fonction de l'étage traité
        decalage = i
        if i%2 == 1:
            decalage += 1
        numero_ligne -= int(decalage/2) + 1
    return numero_ligne
    
def numero_ligne_debut_etage(etage):#Détermine le numéro de la ligne en fonction de l'étage demandé
    if etage == 1:#Pour éviter des problèmes de boucle
        return 1
        
    numero_ligne = numero_ligne_fin_etage(etage)
    numero_ligne -= calcul_nbr_ligne(etage) - 1#Recule jusqu'au début de l'étage
    return numero_ligne
    
def longueur_pied(etage_max):
    if etage_max%2 == 0:
        return etage_max + 1
    else:
        return etage_max