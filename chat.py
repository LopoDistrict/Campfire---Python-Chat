import socket
import threading
import time
import os
from termcolor import colored


# Adresse IP et port du serveur
os.system('cls')
IP = "127.0.0.1" #localhost 
PORT = 5000


nickname = input("enter your nickname: ")

# Fonction pour recevoir les messages du serveur
def recevoir_messages(client):
    while True:
        message = client.recv(1024).decode("utf-8")
        print(message)
       





# Fonction principale pour demarrer le client de chat
def demarrer_client():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Se connecter au serveur
        client.connect((IP, PORT))
        print("connect to", IP ,":" , PORT,)
        print("WELCOME TO CAMPFIRE - V0.0.3 - BETA")
        time.sleep(0.4)
        print("""
                (                 ,&&&.
                 )                .,.&&
                (  (              \=__/
                    )             ,'-'.
                (    (  ,,      _.__|/ /|
                ) /\ -((------((_|___/ |
                (  // | (`'      ((  `'--|
            _ -.;_/ \\--._      \\ \-._/.
            (_;-// | \ \-'.\    <_,\_\`--'|
            ( `.__ _  ___,')      <_,-'__,'
             `'(_ )_)(_)_)'                                     
""")
    
            
    except:
        print("Error :  cant connect to server")
        return

    # Demarrer un nouveau thread pour recevoir les messages du serveur
    thread = threading.Thread(target=recevoir_messages, args=(client,))
    thread.start()

    while True:
        time.sleep(0.3)
        message = f'{nickname}: {input("")}'
        
        # Envoyer le message au serveur
        client.send(message.encode("utf-8"))

        
        if message.lower() == "quit":
            break

    
    client.close()

# Démarrer le client de chat
demarrer_client()