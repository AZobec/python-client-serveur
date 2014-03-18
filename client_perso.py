###############################################
# Mise en place d'un client simple
# simulation d'une connexion client/serveur
#"""""""""""""""""  verson basique """""""""""#

import socket, sys
 

#Création de l'annuaire
Annuaire ={"OULMI": ("Celine",600000000), "Exemple1":("test1",620000000), }

# création d'un socket pour la connexion avec le serveur en local
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
# connexion au serveur, bloc surveillé, et gestion de l'exception
    sock.connect(('127.0.0.1',2020))

except socket.error:
   print("la connexion a échoué.......")
   sys.exit()

print(">>> Connexion établie avec le serveur...")
# Envoi et réception de messages
msgServer=sock.recv(1024) # taille par défaut

print(">>> S :", msgServer.decode())
 
#On envoie d'abord le dictionnaire au serveur via une boucle

for nom in Annuaire : # le prenom est-il répertorié ?
  item = Annuaire[nom] # consultation proprement dite
  prenom, num = item[0], item[1]
  msgClient="0;%s;%s;%s"%(nom,prenom,num)
  msgClient=msgClient.encode()
  print(">>> Envoi vers le serveur")
  sock.send(msgClient)         
  msgServer=sock.recv(1024)
  print(">>> Reception du serveur")
  print(msgServer.decode())



#Ensuite on a la boucle de connexion habituelle
while 1:
 
         if msgServer==b'FIN':
              break
         print(">>> Tapez votre message au dictionnaire")
         print(">>> CODE 0: Ajout d'une ligne au dictionnaire")
         print(">>> CODE 1: Consultation d'une ligne du dictionnaire")
         print(">>> CODE 2: Modification d'une ligne du dictionnaire")
         print(">>> Choisi")        
         msgClient=input("")
         print("")
         msgClient=msgClient.encode()
         print(">>> Envoi vers le serveur")
         sock.send(msgClient)         
         msgServer=sock.recv(1024)
         print(">>> Reception du serveur")
         print(msgServer.decode())

print (">>> Connexion interrompue par le serveur!!!")
sock.close()