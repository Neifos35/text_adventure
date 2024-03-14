import time
import os
import pygame
from Bakugo import Bakugo
from Allmight import Allmight
from Deku import Deku
from Ochaco import Ochaco
from Shoto import Shoto
from Tsuyu import Tsuyu
from Toya import Toya
from Evil import Evil
from Yaomomo import Yaomomo


import cgi

# Récupérer les données de la requête CGI
form = cgi.FieldStorage()
pygame.init()

pygame.mixer.init()

pygame.mixer.music.load("MHA.mp3")

pygame.mixer.music.play()

# Votre logique de jeu ici en utilisant les données de la requête

# Imprimer le contenu généré au format HTML
print("Content-type: text/html\n")
print("<html>")
print("<head>")
print("<title>Mon Jeu Textuel</title>")
print("</head>")
print("<body>")
print("<h1>Bienvenue dans Mon Jeu Textuel</h1>")
# ... Affichez ici le contenu généré par votre jeu ...




"""
Cours "Introduction 2" - Exercice "Text Adventure"
"""

personnage = {
    "PV": 70
}
mannequin = {
    "PV": 50
}
evil= {
    "PV":150
}


pouvoirs = [
    "Un pour Tous",
    "Contrôler la gravité",
    "Faire des explosions",
    "Être une grenouille",
    "Créer des objets",
    "Mi-chaud mi-froid",
    "Aller très vite"
]


plats = ["Ramen", "Onigiri", "Udon", "Curry"]

plats_stock = {
    "Ramen": 2,
    "Onigiri": 2,
    "Udon": 2,
    "Curry": 2,
}

objets_cles = ["smartphone"]
inventaire = {
    "badges":0,
    "contact":0
}

print("🔊🔊🔊🔊🔊🔊🔊🔊🔊🔊🔊")



# ********************************************************************************
# FONCTIONS UTILITAIRES
# ********************************************************************************

print("\nSOUND ON")
print('\nVeux-tu le typewritter? (entre "oui" si tu veux l\'activer, sinon saisis n\'importe quel touche)')
enable = input("Typewritter :")

if (enable == "oui"):
    def typewriter(text):
        for i in range(len(text)):
            time.sleep(0.02)
            print(text[i], end="", flush=True)
else:
    def typewriter(text):
        print(text)


def menu():
    print("_____________________________")
    for i in plats_stock:
        if(plats_stock[i]>0):
            print("|"+ i + " : " + str(plats_stock[i]) )
        else:
            print("SOLD OUT, la cafétéria ne peux pas subvenir à toutes les demandes nous vous prions de bien vouloir nous excusez pour la gêne occassionnée et allez vous faire un mcdo à ma place !")
    print("_____________________________")

def manger():
    print('Que veux-tu manger? (Selon stock)')
    print("|1.Ramen")
    print("|2.Onigiri ")
    print("|3.Udon")
    print("|4.Curry")
    reponse2=input("├─> ")


    if(reponse2=="1" or reponse2=="Ramen" or reponse2=="ramen"):
        if(plats_stock["Ramen"]>0):
            plats_stock["Ramen"]-=1
            personnage["PV"]+=10
            print("Ce fut rassasiant... On dirait qu'on a repris des forces !!! (+10PV)")
            print("Vous possédez maintenant : "+ str(personnage["PV"])+ " PV")

        else:
            print("Désolé mais l'article séléctionné n'est plus disponible")

    elif(reponse2=="2" or reponse2=="Onigiri" or reponse2=="onigiri"):
        if(plats_stock["Onigiri"]>0):
            plats_stock["Onigiri"]-=1
            personnage["PV"]+=10
            print("Ce fut rassasiant... On dirait qu'on a repris des forces !!! (+10PV)")
            print("Vous possédez maintenant : "+ str(personnage["PV"])+ " PV")
        else:
            print("Désolé mais l'article séléctionné n'est plus disponible")

    elif(reponse2=="3" or reponse2=="Udon" or reponse2=="udon"):
        if(plats_stock["Udon"]>0):
            plats_stock["Udon"]-=1
            personnage["PV"]+=10
            print("Ce fut rassasiant... On dirait qu'on a repris des forces !!! (+10PV)")
            print("Vous possédez maintenant : "+ str(personnage["PV"])+ " PV")
        else:

            print("Désolé mais l'article séléctionné n'est plus disponible")

    elif(reponse2=="4" or reponse2=="Curry" or reponse2=="curry"):
        if(plats_stock["Curry"]>0):
            plats_stock["Curry"]-=1
            personnage["PV"]+=10
            print("Ce fut rassasiant... On dirait qu'on a repris des forces !!! (+10PV)")
            print("Vous possédez maintenant : "+ str(personnage["PV"])+ " PV")

        else:
            print("Désolé mais l'article séléctionné n'est plus disponible")


def telephone():
    print("|1.Donner")
    print("|2.Refuser")
    reponse=input("|->")
    if(reponse=="1" or "Donner" or "donner"):
        inventaire["contact"]+=1
    else:
        typewriter("Ce n'est pas grave, peut-être une prochaine fois...")
   
    

# ********************************************************************************
# INTRODUCTION
# ********************************************************************************


def intro():
    print(" _____________           _____________")
    print(" |___|___|___|           |___|___|___|")
    print(" |___|___|___|           |___|___|___|")
    print(" |___|___|___|           |___|___|___|")
    print(" |___|___|___|           |___|___|___|")
    print(" |___|___|___|           |___|___|___|")
    print(" |___|___|___|___________|___|___|___|")
    print(" |___|___|___|___|___|___|___|___|___|")
    print(" |___|___|___|___|___|___|___|___|___|")
    print(" |___|___|___|___|___|___|___|___|___|")
    print(" |___|___|___|___|___|___|___|___|___|")
    print(" |___|___|___|           |___|___|___|")
    print(" |___|___|___|           |___|___|___|")
    print(" |___|___|___|           |___|___|___|")
    print(" |___|___|___|           |___|___|___|")
    print(" |___|___|___|           |___|___|___|")
    print(" |___|___|___|           |___|___|___|\n")
    print("         ////////    ///  ///")
    print("         ///  ///    ///  ///")
    print("         ////////    ///  ///")
    print("         ///  ///    ////////")
    print("========================================")
    print("   || Bienvenue au lycée A.U. ! || \n")
    time.sleep(1)
    Allmight.allmight_text("Salut à toi, et bienvenue au lycée de AU, comme tu dois surement le savoir AU est un lycée de super-hero. Je me présente, je m'appelle HallNight, je vais te présenter le lycée, je te ferai choisir ton Halter(pouvoir), mais avant tout, parles moi un peu de toi !                                             ")

    # Demander un âge et écrire cette information dans le dictionnaire "personnage"
    typewriter("\nBonjour !!! Avant de commencer merci de renseigner ton prénom ?")
    prenom = str(input("\nPrénom : "))

    typewriter("\nParfait, peux-tu également renseigner ton age ?")
    age = int(input("\nAge : "))

    os.system('cls' if os.name == 'nt' else 'clear')

    if (15 <= age <= 35):
        text = "Super !!! " + prenom + " à " + \
            str(age) + " ans, tu as l'âge d'être au Lycée !!! Nous allons pouvoir passer à la sélection de ton Halter ! Voici la liste des Halters disponibles"
        Allmight.allmight_text(text)
        typewriter("Voici les Halters (pouvoirs) disponibles : \n")

    elif (age < 16):
        time.sleep(1)
        Allmight.allmight_text(
            "Désolé, mais tu es encore trop jeune pour rentrer au lycée, mais ne t'inquiétes pas, tu pourras revenir quand tu en auras l'âge !!!")
        exit()
    else:
        time.sleep(1)
        Allmight.allmight_text(
            "Le lycée est derrière toi maintenant, arrête de te prendre pour un hero à ton grand âge là et va travailler comme tout le monde !!!                                ")
        exit()

    # Afficher la liste des pouvoirs (avec leur position) et demander d'en choisir un

    index = 0

    for i in pouvoirs:
        index = index+1
        print(index, " | ", i)
    typewriter(
        "Tu peux maintenant choisir un pouvoir (entre le chiffre associé au pouvoir) ")
    global pouvoir
    pouvoir = int(input("\nPouvoir : "))

    os.system('cls' if os.name == 'nt' else 'clear')

    Allmight.allmight_text(
        "Excellent choix, toutefois, il semblerait que ton halter ait modifié ton apparence, veux tu voir à quoi tu ressembles maintenant? ")
    time.sleep(1)
    print("┌────────────────────────────────────────")
    print("|1.Voir")
    print("|2.Ne pas voir")
    reponse = input("├─> ")
    print("└────────────────────────────────────────")
    if (reponse == "voir" or reponse =="1" or reponse =="Voir"):
        if (pouvoir == 1):
            Deku.deku()
        elif (pouvoir == 2):
            Ochaco.ochaco()

        elif (pouvoir == 3):
            Bakugo.bakugo()

        elif (pouvoir == 4):
            Tsuyu.tsuyu()
        elif (pouvoir == 5):
            Yaomomo.yaomomo()
        elif (pouvoir == 6):
            Shoto.shoto()
        elif (pouvoir == 7):
            Toya.toya()
        time.sleep(3)
        Allmight.allmight_text("Wouahhh mais quel BG regarde moi ça !!!")

    else:
        typewriter("Très bien, tu préfères garder la surprise, je comprends !!! ")
    personnage = {
        "Prenom": prenom,
        "PV": 70,
        "Age": age,
        "Pouvoir": pouvoirs[pouvoir-1],
    }
    time.sleep(2)
    typewriter("Faisons un petit recapitulatif de ta carte étudiante : \n\n")
    time.sleep(1)
    # Afficher tout le contenu (clé et valeur) du dictionnaire "personnage"
    for i in personnage:
        print(i, personnage[i])
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    Allmight.allmight_text(
        "Nous nous retrouverons, un peu plus tard lorsque tu voudras t'entraîner, en attendant visite le lycée et profites en pour te faire des amis ! ")
    # ********************************************************************************
    # LIEUX
    # ********************************************************************************
    time.sleep(2)


def observer(Lieu):
   
    if(Lieu=="hall"):
        global compteur
        compteur=0
        typewriter("Il s'agit d'un hall très spacieux, et dire que les plus grands héros ont foulés les sol de ce hall ! Tiens il y a une élève et si on allait lui parler ? (oui/non)")
        interraction = input("\nLui parler:")
        
        if (interraction == "oui"):
            if(compteur==0):
                if (pouvoir == 2):
                    
                    Tsuyu.tsuyu_text("Bienvenue dans notre Lycée! Je suis Tsyouyou Assis et je suis contente de te rencontrer croa. Je sais que tu dois être un peu nerveux à propos de l'entrée dans un nouveau lieu et entouré de nouvelles personnes. Si tu as besoin d'aide ou si tu as des questions, n'hésites pas à venir me parler. J'ai hâte de travailler avec toi!")
                    typewriter("Tsyouyou te demandes ton numéro")
                    telephone()
                    
                else:
                    
                    Ochaco.ochaco_text("Bienvenue dans notre Lycée! Je suis Hourara Ochapeau. Je sais que tu dois être un peu nerveux à propos de l'entrée dans un nouveau lieu et entouré de nouvelles personnes. Si tu as besoin d'aide ou si tu as des questions, n'hésites pas à venir me parler. J'ai hâte de travailler avec toi!")
                    print("Ochapeau te demandes ton numéro")
                    telephone()

                compteur+=1
        else:
            if (pouvoir == 2):
                Tsuyu.tsuyu_text("Bienvenue dans notre Lycée! Je suis Tsyouyou Assis et je suis contente de te rencontrer croa. Je sais que tu dois être un peu nerveux à propos de l'entrée dans un nouveau lieu et entouré de nouvelles personnes. Si tu as besoin d'aide ou si tu as des questions, n'hésites pas à venir me parler. J'ai hâte de travailler avec toi!")
            else:
                Ochaco.ochaco_text("Bienvenue dans notre Lycée! Je suis Hourara Ochapeau. Je sais que tu dois être un peu nerveux à propos de l'entrée dans un nouveau lieu et entouré de nouvelles personnes. Si tu as besoin d'aide ou si tu as des questions, n'hésites pas à venir me parler. J'ai hâte de travailler avec toi!")
                
    elif (Lieu== "couloir1"):
        index=0
        typewriter("Il s'agit du couloir et de l'escalier menant au premier étage, là où se trouve ta nouvelle classe ! \nTiens il y a un élève et si on allait lui parler ? (oui/non)")
        interraction = input("\nLui parler:")

        if(index<=1):
            if (interraction == "oui"):
            
                if (pouvoir == 1):
                
                    Shoto.shoto_text("Bonjour, tu dois être le nouveau, je suis Chateau Tadoreki je sais pas si tu le sais, mais le lycée dispose d'une salle d'entrainement, ça serait bien qu'on y aille un de ces jours ensemble, il faudrait juste que tu ailles demander le pass à Hallnight en classe 1A")
                    typewriter("Chateau te demandes ton numéro")
                    telephone()
                else:
                
                    Deku.deku_text("Bonjour, tu dois être le nouveau je m'appelle Dukou, je sais pas si tu le sais, mais le lycée dispose d'une salle d'entrainement, ça serait bien qu'on y aille un de ces jours ensemble, il faudrait juste que tu ailles demander le pass à Hallnight en classe 1A")
                    typewriter("Dukou te demandes ton numéro")
                    telephone()
                index+=1
        else:
            if (interraction == "oui"):
        
                if (pouvoir == 1):
            
                    Shoto.shoto_text("Bonjour, tu dois être le nouveau, je suis Chateau Tadoreki je sais pas si tu le sais, mais le lycée dispose d'une salle d'entrainement, ça serait bien qu'on y aille un de ces jours ensemble, il faudrait juste que tu ailles demander le pass à Hallnight en classe 1A")
            
                else:
            
                    Deku.deku_text("Bonjour, tu dois être le nouveau je m'appelle Dukou, je sais pas si tu le sais, mais le lycée dispose d'une salle d'entrainement, ça serait bien qu'on y aille un de ces jours ensemble, il faudrait juste que tu ailles demander le pass à Hallnight en classe 1A")
            
    elif (Lieu== "Classe1A"):
        typewriter("Il s'agit d'une classe joliment décoré, on voit déjà que les élèves sont investis dans cette classe! Ohhh il y a Hallnight et si on allait lui parler ? (oui/non)")
        interraction = input("\nLui parler:")
       
        if (interraction == "oui"):
            if(inventaire["badges"]==3):

                Allmight.allmight_text("Ah te revoilà, alors, tu as finis de t'entrainer ? Ca c'est bien passé?")
                print("|1.Montrer")
                print("|2.Sortir (quête surprise)")

                answer=input("|->")

                if(answer=="1" or answer=="Montrer" or answer=="montrer" or answer=="m"):
                    if(inventaire["badges"]==3):
                        Allmight.allmight_text("FELICITATIONS !!!!!!!!!!!")
                        typewriter("Félicitations !!! Tu as finis le jeu, tu as obtenu les 3 badges !!!")
                        time.sleep(3)
                        exit()
                    else:
                        typewriter("Désolé mon enfant, mais tu n'as pas encore obtenu un nombre de badges suffissant")
                else:
                    lieu("sortir")
            elif("pass" in objets_cles):
                Allmight.allmight_text("EH bien, tu as déjà le pass d'entrainement, mais tu n'as pas encore les 3 badges, de quoi veux tu me parler?")
                
            else:
                Allmight.allmight_text("Comment se passe ta journée, tu t'es fait des amis en chemin ?")
                typewriter("As-tu fait des rencontres? (oui/non)")
                reponse=input("|->")

                os.system('cls' if os.name == 'nt' else 'clear')

                if(reponse=="oui"):
                    Allmight.allmight_text("Super, j'imagine que tes camarades t'ont parlés de la salle d'entrainement et que c'est pour ça que tu es là ?")
                    print("|1.Demander le pass")
                    print("|2.Ne pas demander le pass")
                    resp=input("|->")
                    if(resp=="1" or resp=="Demander" or resp=="demander"):
                        objets_cles.append("pass")

                else:
                    if(pouvoir==1):
                        Allmight.allmight_text("Ce n'est pas bien, reviens me voir quand tu te seras fait au moins un ami, tiens je crois justement que Chateau Tadoreki se trouve justement dans le couloir précédent et si tu allais lui parler ")
                    else:
                        Allmight.allmight_text("Ce n'est pas bien, reviens me voir quand tu te seras fait au moins un ami, tiens je crois justement que Dukou se trouve justement dans le couloir précédent et si tu allais lui parler ")

    elif (Lieu== "couloir2"): 
        typewriter("Il s'agit du couloir et de l'escalier menant au deuxième étage ! Tiens il y a une élève et si on allait lui parler ? (oui/non)")
        interraction = input("\nLui parler:")
       
        if (interraction == "oui"):
           
            if (pouvoir == 5):
           
                Deku.deku_smile("Tiens te revoilà, tout à l'heure j'ai complétement oublié de te prévenir mais si tu croises un dénommé Bacougo ne t'étonnes pas s'il est... disons un peu tendu ... ")
                typewriter("A ce propos, acceptes-tu que je lui donne ton numéro?")
                telephone()
            else:
           
                Yaomomo.yaomomo_text("Bonjour, tu dois être le nouveau, ça serait sympa qu'on apprenne à se connaître !")
                typewriter("Yaomomo te demandes ton numéro")
                telephone()
    elif (Lieu== "cafet"):
        typewriter("Il s'agit de la cafet, c'est le héro SuperLunchMegaBon qui s'occupe de faire de bons petits plats ! Tiens il y a une élève et si on allait lui parler ? (oui/non)")
        interraction = input("\nLui parler:")
       
        if (interraction == "oui"):
         
            if (pouvoir == 7):
                Shoto.shoto_text("Bonjour, tu dois être le nouveau !")

            else:
          
                Toya.toya_text("BONJOUR A TOI ET BIENVENUE EN CLASSE 1A, JE ME PRESENTE JE SUIS ANGINEIUM ET JE SUIS TON DELEGUE, J'AI HATE QUE L'ON REVISE ENSEMBLE !!!")
                typewriter("Angineium te demandes ton numéro")
                telephone()           
         
                

    elif (Lieu== "entrainement"): 
        typewriter("Il s'agit d'une salle d'entrainement remise à neuf et qui présente bon nombre de mannequins d'entrainements !!! Tiens il y a une élève et si on allait lui parler ? (oui/non)")
        interraction = input("\nLui parler:")
       
        if (interraction == "oui"):
         
            if (pouvoir == 3):
          
                Deku.deku_emerveille("Tiens te revoilà, tout à l'heure j'ai complétement oublié de te prévenir mais si tu croises un dénommé Bacougo ne t'étonnes pas s'il est... disons un peu tendu ... ")
                typewriter("A ce propos, acceptes-tu que je lui donne ton numéro?")
                telephone()
            else:
                
                Bakugo.bakugo_enerve("QU'EST CE QUE TU REGARDES LE NOUVEAU ?!?! TU VEUX QUE JE T'EXPLOSE LA TRONCHE !!??! On peut régler ça tout de suite et maintenant !")

def lieu(localisation):
    if (localisation == "hall"):
        print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        typewriter("Tu es dans le hall d'entrée de l'école.")
        typewriter("\nOn peut aller à de nombreux endroits d'ici. \n")

        while True:
            print("\nQue faisons nous ensuite?")
            print("\n┌────────────────────────────────────────")
            print("|1.Observer")
            print("|2.Premier Couloir")
            print("|3.Quitter")
            
            reponse = input("├─> ")
            if (reponse == "Observer" or reponse =="1" or reponse =="observer"):
                print("└────────────────────────────────────────")
                observer("hall")          

            elif (reponse == "couloir1" or reponse =="2" or reponse =="Premier Couloir" or reponse =="premier couloir"):
                print("└────────────────────────────────────────")
                lieu("couloir1")

            elif (reponse == "Quitter" or reponse =="3" or reponse =="quitter"):
                break

    elif (localisation == "couloir1"):
        print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        typewriter("C'est le couloir du 1er étage.")
        typewriter("\nOn y trouve entre autres la classe 1-A.")

        while True:
            print("\n\nQue faisons nous ensuite?")
            print("\n┌────────────────────────────────────────")
        
            print("|1.Observer")
            print("|2.Classe-1A")
            print("|3.Hall")
            reponse = input("├─> ")
            if (reponse == "Observer" or reponse =="1" or reponse =="observer"):
                print("└────────────────────────────────────────")
                observer("couloir1")
            
            elif (reponse == "classe" or reponse =="2" or reponse =="Classe-1A" or reponse =="Classe1A" or reponse =="classe1A"):
                print("└────────────────────────────────────────")
                lieu("Classe1A")
                
            elif (reponse == "Hall" or reponse =="3" or reponse =="hall"):
                print("└────────────────────────────────────────")
                observer("hall")


    elif (localisation == "Classe1A"):
        print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        typewriter("\nTu te situes dans la classe 1 A de la fillière héroïque")
        typewriter("\nIl semblerait que le professeur Hall Night soit dans la salle, et si on allait lui parler?")

        while True:
            print("\n\nQue faisons nous ensuite?")
            print("\n┌────────────────────────────────────────")
       
            print("|1.Observer")
            print("|2.Deuxieme Couloir(vers le deuxième étage)")
            print("|3.Premier Couloir (vers le hall)")
            reponse = input("├─> ")
            if (reponse == "Observer"or reponse =="1" or reponse =="observer"):
                print("└────────────────────────────────────────")
                observer("Classe1A")
            
            elif (reponse == "couloir2" or reponse =="2" or reponse =="deuxieme couloir" or reponse =="Deuxieme couloir" or reponse =="Deuxieme Couloir"):
                print("└────────────────────────────────────────")
                lieu("couloir2")

            elif (reponse == "couloir1" or reponse =="3" or reponse =="premier couloir" or reponse =="Premier couloir" or reponse =="Premier Couloir"):
                print("└────────────────────────────────────────")
                lieu("couloir1")

    elif (localisation == "couloir2"):

        print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        typewriter("\nTu te trouves à présent dans le couloir/escalier qui mène au 2 ème étage.")
        typewriter("\nLa cafet et la salle d'enntrainement se trouve justement au 2 ème, et si on y jettait un oeil?")

        while True:
            print("\n\nQue faisons nous ensuite?")
            print("\n┌────────────────────────────────────────")
            print("|1.Observer")
            print("|2.Cafet")
            print("|3.Classe-1A")
            print("|4.Salle d'entrainement")
            
            reponse = input("├─> ")
            if (reponse == "Observer" or reponse =="1" or reponse =="observer"):
                print("└────────────────────────────────────────")
                observer("couloir2")
            elif (reponse == "cafet" or reponse =="2" or reponse =="Cafet" or reponse =="Cafétéria" or reponse =="cafeteria" or reponse =="Cafeteria" or reponse =="cafétéria"):
                lieu("cafet")
                print("└────────────────────────────────────────")
            elif (reponse == "classe" or reponse =="3" or reponse =="Classe-1A" or reponse =="Classe1A" or reponse =="classe1A"):
                print("└────────────────────────────────────────")
                lieu("Classe1A")
            elif (reponse == "entrainement" or reponse =="4" or reponse =="Salle d'entrainement" or reponse =="entraînement"):
                lieu("entrainement")
                print("└────────────────────────────────────────")

    elif (localisation == "cafet"):
        print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        typewriter("\nTu es dans la cafétéria de l'école")
        typewriter("\nEt si on en profittait pour se restaurer et reprendre des forces?")

        while True:
            print("\n\nQue faisons nous ensuite?")
            print("\n┌────────────────────────────────────────")
           
            print("|1.Observer")
            print("|2.Salle d'entrainement ")
            print("|3.Deuxieme Couloir ")
            print("|4.Manger")
            reponse = input("├─> ")
            if (reponse == "Observer" or reponse =="1" or reponse =="observer"):
                print("└────────────────────────────────────────")
                observer("cafet")
            
            elif (reponse == "entrainement" or reponse =="2" or reponse =="Salle d'entrainement" or reponse =="entraînement"):
                lieu("entrainement")
                print("└────────────────────────────────────────")

            elif (reponse == "couloir2" or reponse =="3" or reponse =="deuxieme couloir" or reponse =="Deuxieme couloir" or reponse =="Deuxieme Couloir"):
                print("└────────────────────────────────────────")
                lieu("couloir2")
            elif (reponse == "manger" or reponse =="4" or reponse =="Manger"):
                print("└────────────────────────────────────────")
                typewriter("Excellent choix, je meurs de faim... Voyons voir le menu...")
                menu()
                manger()
               
                

    elif (localisation == "entrainement"):
        
        if("pass" in objets_cles):
            print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            typewriter("\nBienvenue dans la salle d'entraînement !")
            typewriter("\nOn peut s'entraîner avec un mannequin d'entraînement si tu le désires")

            while True:
                print("\n\nQue faisons nous ensuite?")
                print("\n┌────────────────────────────────────────")
                print("|1.Observer")
                print("|2.Combattre")
                print("|3.Deuxieme Couloir")
                reponse = input("├─> ")
                if ( reponse == "Observer" or reponse == "1" or reponse == "observer"):
                    print("└────────────────────────────────────────")
                    observer("entrainement")
                elif(reponse=="2" or reponse =="Combattre" or reponse =="combattre"):
                    print("└────────────────────────────────────────")
                    combat()
                elif (reponse == "3" or reponse == "couloir2" or reponse =="3" or reponse =="deuxieme couloir" or reponse =="Deuxieme couloir" or reponse =="Deuxieme Couloir"):
                    print("└────────────────────────────────────────")
                    lieu("couloir2")
        else:
            typewriter("Désolé mais pour accéder à la salle d'entrainement, il faut un pass...")

    elif (localisation == "sortir"):
        print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        typewriter("\nL'année est enfin terminée, j'ai fais d'énormes progrès cette année...")
        typewriter("\nBOOOOMMMMMMMMMMMMMM")
        time.sleep(1)
        typewriter("AHHHHHH, Qu'est ce que c'était ?!?!?")
        time.sleep(3)

        Evil.himiko_toga("CoUcOu LeS hErOs !!! Devinez qui a voulu se joindre à la fête de fin d'année ?!?!! Et oui c'est nous la coopération des grosméchants !!")

        while True:
            print("\n\nQue faire?")
            print("\n┌────────────────────────────────────────")
            print("|1.Kamino")
            print("|2.Combattre")
            print("|3.Fuir")
            reponse = input("├─> ")
            if (reponse == "1" or reponse =="Kamino" or reponse =="kamino"):
                print("└────────────────────────────────────────")
                typewriter("\nHeureusement que j'ai pris le numéro de mes camarades, je vais pouvoir lancer un message d'alerte à tous mes contacts!!!")
                personnage["PV"]=personnage["PV"]*5*inventaire["contact"]
                typewriter("Le message d'alerte a bien été envoyé et tes amis sont venus te prêter mains fortes")
                text="tu as " + str(inventaire["contact"]) + " numéros dans tes contacts, ton nombre de PV a donc été multiplié par ce nombre de contacts"
                typewriter(text)
                print("Tu possèdes donc "+ str(personnage["PV"])+ " PV")
                time.sleep(2)
                combat_evil()
                
            elif (reponse == "2" or reponse =="Combattre" or reponse =="combattre"):
                print("└────────────────────────────────────────")
                print("RIP, la coopération des grosméchants était plus forte que toi, tu es mort(e) dans t'affreuses souffrances")
            elif(reponse=="2" or reponse =="Combattre" or reponse =="combattre"):
                print("└────────────────────────────────────────")
                combat()
            elif (reponse == "3" or reponse =="3" or reponse =="fuir" or reponse =="Fuir"):
                print("└────────────────────────────────────────")
                exit()
        

def combat():
    os.system('cls' if os.name == 'nt' else 'clear')
    if(pouvoir==1):
        Deku.deku_combat("Je veux devenir un héro qui sauve les autres en gagnant !! C'est l'heure de l'entrainement !!!! !!!!!!!!!!!!!! ")
    elif(pouvoir==3):
        Bakugo.bakugo_combat("Tu veux m'affronter ?!?! SSSSHHHHHHIIIIIINNNNNNNNNNNNEEEEEEEEEEEEEE !!!")
    time.sleep(3)

    while (mannequin["PV"]>0 or personnage["PV"]>0):
        print("\nVotre adversaire possède : "+ str(mannequin["PV"])+" PV")
        print("\nIl vous reste : "+ str(personnage["PV"])+" PV")
        print("\n┌────────────────────────────────────────")
        if(pouvoir == 1):
            print("|1.Delaware Smash")
        else:
            print("|1.Attaque")
        print("|2.Fuir")
        reponse = input("├─> ")
        if (reponse == "1" or "Attaque" or "attaque" or "Delaware Smash" or "Delaware" or "delawaware" or "delaware smash" or "Smash" or "smash"):
            print("└────────────────────────────────────────")
            mannequin["PV"]-= 15
            typewriter("\nVous avez réussi à infliger 15 dégats au mannequin")
            typewriter("\nLe mannequin a répliqué et vous a infligé 10 dégats")
            personnage["PV"]-= 10
            if(personnage["PV"]<=0):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("GAME OVER")
                time.sleep(5)
                exit()
            elif(mannequin["PV"]<=0):
                if(inventaire["badges"]<3):
                    inventaire["badges"]+=1
                    typewriter("Félicitation tu as battu le mannequin d'entrainement, tu viens d'ajouter un badge à ta collection !! ")
                else:
                    typewriter("Félicitation tu as battu le mannequin d'entrainement, malheureusement tu possèdes déjà tous les badges !! ")
                typewriter("Il te reste maintenant: "+ str(personnage["PV"])+" PV")
                mannequin["PV"]=50
                time.sleep(3)
                lieu("entrainement")



        elif (reponse == "2" or reponse == "fuir" or reponse == "Fuir"):
            print("└────────────────────────────────────────")
            typewriter("Je comprends, le combat était rude... n'hésites pas à reprendre des forces en te rendant à la cafétéria !")
            lieu("entrainement")
        
        

def combat_evil():
    
    if(pouvoir==1):
        Deku.deku_combat("Je veux devenir un héro qui sauve les autres en gagnant !! C'est l'heure du FIGHT !!!! !!!!!!!!!!!!!! Un pour tous, rêvetement intégral à 45% ")
    elif(pouvoir==3):
        Bakugo.bakugo_combat("Tu veux m'affronter ?!?! SSSSHHHHHHIIIIIINNNNNNNNNNNNEEEEEEEEEEEEEE !!!")
    time.sleep(3)

    while (evil["PV"]>0 or personnage["PV"]>0):
        print("\nVotre adversaire possède : "+ str(evil["PV"])+" PV")
        print("\nIl vous reste : "+ str(personnage["PV"])+" PV")
        print("\n┌────────────────────────────────────────")
        if(pouvoir == 1):
            print("|1.Delaware Smash")
        else:
            print("|1.Attaque")
        print("|2.Fuir")
        if(inventaire["contact"]>=4):
            print("|3.Pouvoir de l'amitié")
            reponse = input("├─> ")
            if (reponse == "1" or reponse =="Attaque" or reponse =="attaque" or reponse =="Delaware Smash" or reponse =="Delaware" or reponse =="delawaware" or reponse =="delaware smash" or reponse =="Smash" or reponse =="smash"):
                print("└────────────────────────────────────────")
                evil["PV"]-= 15
                typewriter("\nVous avez réussi à infliger 15 dégats à Himiko")
                typewriter("\nHimiko a répliqué et vous a infligé 20 dégats")
                personnage["PV"]-= 20
                if(personnage["PV"]<=0):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("GAME OVER")
                    time.sleep(5)
                    exit()
                elif(evil["PV"]<=0):    
                    typewriter("Félicitation tu as su prouver que le pouvoir de l'amitié était le plus fort des pouvoirs !!! ")
                    time.sleep(3)
                    exit()

                    



            elif (reponse == "2" or reponse == "fuir" or reponse == "Fuir"):
                print("└────────────────────────────────────────")
                typewriter("Je comprends, le combat était rude... Parfois être un héro signifie savoir partir la queue entre les jambes afin de chercher l'aide de héros plus... compétent...")
                exit()
                
            elif (reponse == "3" or reponse == "Pouvoir" or reponse == "pouvoir"or reponse == "Pouvoir de l'amitié" or reponse == "pouvoir de l'amitié"):
                print("└────────────────────────────────────────")
                
                typewriter("-1500 PV, le pouvoir de l'amitié est surpuissant... Himiko est totalement dead")
                exit()
        else:
            resp = input("├─> ")
            if (resp == "1" or resp =="Attaque" or resp =="attaque" or resp =="Delaware Smash" or resp =="Delaware" or resp =="delawaware" or resp =="delaware smash" or resp =="Smash" or resp =="smash"):
                print("└────────────────────────────────────────")
                evil["PV"]-= 15
                typewriter("\nVous avez réussi à infliger 15 dégats à Himiko")
                typewriter("\nHimiko a répliqué et vous a infligé 20 dégats")
                personnage["PV"]-= 20
                if(personnage["PV"]<=0):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("GAME OVER")
                    time.sleep(5)
                    exit()
                elif(evil["PV"]<=0):    
                    typewriter("Félicitation tu as su prouver que le pouvoir de l'amitié était le plus fort des pouvoirs !!! ")
                    time.sleep(3)
                    exit()


            elif (reponse == "2" or reponse == "fuir" or reponse == "Fuir"):
                print("└────────────────────────────────────────")
                typewriter("Je comprends, le combat était rude... Parfois être un héro signifie savoir partir la queue entre les jambes afin de chercher l'aide de héros plus... compétent...")
                exit()

# Gérer ici toutes les réponses possibles, qu'elles soient correctes ou non


# Pour lancer le jeu, on appelle la fonction d'introduction
if __name__ == "__main__":
    intro()
    lieu("hall")
    print("Fin du jeu.")
    pygame.quit()


# ********************************************************************************
# EXECUTION
# ********************************************************************************
print("</body>")
print("</html>")