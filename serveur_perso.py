import socket


TAILLE_BUFFER=1024

#ANNUAIRE
Annuaire={}
num=0
# Déclaration de 3 Méthodes, Remplissage, Consultatio, Modification


def remplissage(nom, prenom, num, connexion):
        Annuaire[nom]= (prenom, num)
        item= Annuaire[nom]
        prenom, num_dico = item[0], item[1]
        msgServer=">>> Vous avez inséré la ligne suivante:Nom :%s / Prénom: %s / Num: %s" %(nom,prenom,num_dico)
        msgServer=msgServer.encode()
        print(">>> Envoi vers le client de la réponse de remplissage")
        connexion.send(msgServer)         
        
def consultation(nom, connexion):
        if nom in Annuaire : # le prenom est-il répertorié ?
            item = Annuaire[nom] # consultation proprement dite
            prenom, num = item[0], item[1]
            msgServer=">>> La personne se nommant %s est répertoriée \nPrenom:%s / Num: %s" %(nom,prenom,num)
        else:
            msgServer=">>> *** nom inconnu ! ***"
              
        #on lui envoie le message
        msgServer=msgServer.encode()
        print(">>> Envoi vers le client de la consultation")
        connexion.send(msgServer)             
 
def modification(nom, new_prenom, new_num, connexion):
    while 1:
        nom=input("Entrez le nom de la personne à modifier ou <enter> pour terminer :")
        if nom=="":
            break
        if nom in Annuaire:
            Num=input("Saisir le nouveau numéro :")
            Annuaire[nom]=(Annuaire[nom][0],Num)
        else :
            print("!!! Nom inconnu !!!")





#Sockets et connexions
HOST='127.0.0.1'
PORT=2020

testMessageClient=""

#Création d'une socket avec la famille IP + TCP
MySocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Liaison Socket avec adresse+PORT
MySocket.bind((HOST, PORT))

#Boucle de traitement tant qu'il y a des clients connectés
print("S > Serveur prêt, en attente d'un client")

#ecoute d'une connexion et une seule
MySocket.listen(1)

#établissement de la connexion
connexion,addresse=MySocket.accept()
print("S > Connexion client réussie, adresse IP %s, port %s \n" %(HOST,PORT))

# dialogue avec le client, envoi de message
connexion.send(b'hello client/ SERVEUR IS UP')
print(">>> Vous êtes sur le serveur, prêt à recevoir vos instructions Dictionnaire")
print(">>> Tapez FIN ou rien si vous souhaitez interrompre la connexion") 

# réception de message du client
# réception de 1024 caractères


# boucle d'échange avec le client
while 1 :
    msgClient=connexion.recv(TAILLE_BUFFER)
    testMessageClient=msgClient.decode()
    if testMessageClient=="FIN" :
        break
    listMessage=testMessageClient.split(";")
    if listMessage[0] == "0" :
        remplissage(listMessage[1], listMessage[2], listMessage[3], connexion)
    if listMessage[0] == "1" :
        consultation(listMessage[1], connexion)

# fermeture de la connexion
connexion.send(b"FIN")
print(">>> connexion interompue par le client!!!!")
MySocket.close()
connexion.close()
