import socket
import threading



# Adresse IP et port du serveur
IP = "127.0.0.1"
PORT = 5000







clients = []

num_client = len(clients)

# Fonction pour gérer les messages des clients
def gerer_client(client):
    while True:
        try:
            # Recevoir le message du client
            message = client.recv(1024).decode("utf-8")
            if message:

                broadcast(message, client)
            else:
                supprimer_client(client)
                break
        except:
            supprimer_client(client)
            break
            




# Fonction pour diffuser un message à tous les clients
def broadcast(message, expediteur):
    for client in clients:
        if client != expediteur:
            try:
                client.send(message.encode("utf-8"))
            except:
                supprimer_client(client)




# Fonction pour supprimer un client de la liste
def supprimer_client(client):
    if client in clients:
        clients.remove(client)




def start():
    # Créer un socket pour le serveur
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind((IP, PORT))
    serveur.listen()

    print("Le serveur de chat a démarré sur {}:{}".format(IP, PORT))

    while True:
        client, adresse = serveur.accept()
        print("new connection", adresse)
        clients.append(client)

        # Démarrer un nouveau thread pour gérer le client
        thread = threading.Thread(target=gerer_client, args=(client,))
        thread.start()



# Démarrer le serveur de chat
start()
