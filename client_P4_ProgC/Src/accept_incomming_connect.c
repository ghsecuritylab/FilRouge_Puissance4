/*
 * accept_incomming_connect.c
 *
 *  Created on: 20 août 2019
 *      Author: daugustin
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <inet.h>
#include <string.h>
#include <errno.h>
//#include "lwip.h"
//#include "connexion_au_client.h"

//Création de la fonction qui accepte la demande de connexion

void accept_incoming_connect(int loc_serversocket_desc) {
	int connect;
	int new_socket; //création d'une socket dédié a la comm entre le client et le serveur
	char *loc_message;
	struct sockaddr_in client;

	printf("En attente de connection....");
	connect = sizeof(struct sockaddr_in);
	while ((new_socket = accept(loc_serversocket_desc,
			(struct sockaddr * )&client, (socklen_t* )&connect))) {

		printf("Connection accepté");

		//réponse du serveur
		loc_message =
				"Welcome, i am here for you. We are connected.....YOU and ME!!! ";
		write(new_socket, loc_message, strlen(loc_message));
	}
}
