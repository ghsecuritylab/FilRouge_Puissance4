from apply import *
import json
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from settings import TCP_HOST, TCP_PORT, BUFFER_SIZE, ENCODING, BYTE_ORDER


# On crée un socket TCP (famille INET, type STREAM)
with socket(AF_INET, SOCK_STREAM) as sock:

    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((TCP_HOST, TCP_PORT))  # On lie ce socket à l'adresse 127.0.0.1:5000
    sock.listen(1)  # On se met en attente de connexions
    print("Server listening at {}:{}".format(TCP_HOST, TCP_PORT))

    while True:

        (conn, addr) = sock.accept()  # Un nouveau client se connecte
        print("Connection received from {}:{}".format(*addr))
        msg = conn.recv(BUFFER_SIZE)  # On lit les 2 premiers bytes qu'il nous envoie et qui nous donnes la longueur du msg
        length = int.from_bytes(msg, byteorder='big')
        print(length)
        msg_recu = conn.recv(length)
        msg_recu_dict = json.loads(msg_recu)

        if msg_recu_dict.get("Msg type") == "STATS":
            #  Création d'un dico avec le msg reçu
            print("Received message: {}".format(msg_recu.decode("utf-8")))
            reponse = {"Msg type": "ACK", "Msg ID": msg_recu_dict["Msg ID"]}
            reponse_convert = json.dumps(reponse)
            first_bytes = len(reponse_convert).to_bytes(BUFFER_SIZE, byteorder=BYTE_ORDER)
            encoded_message = bytes(reponse_convert.encode(ENCODING))
            full_message = first_bytes + encoded_message
            conn.send(full_message)  # On les lui renvoie telles quelles
            record_data(messages_str)

        elif msg_recu_dict.get("Msg type") == "CONFIG":
            print("Received message: {}".format(msg_recu.decode("utf-8")))
            # Interception de la connexion si serveur existe on continue si serveur existe pas création
            reponse = {"Msg type": "CONFIG", "Msg ID": msg_recu_dict["Msg ID"], "Max player delay": "12",
                       "Max coin blink delay": "3", "Victory blink delay": "10", "Level": 4,
                       "Player1 color": "blue", "Player2 color": "yellow"}
            reponse_convert = json.dumps(reponse)
            first_bytes = len(reponse_convert).to_bytes(BUFFER_SIZE, byteorder=BYTE_ORDER)
            encoded_message = bytes(reponse_convert.encode(ENCODING))
            full_message = first_bytes + encoded_message
            conn.send(full_message)  # On les lui renvoie telles quelles

        conn.close()  # On ferme la connexion avec ce client

