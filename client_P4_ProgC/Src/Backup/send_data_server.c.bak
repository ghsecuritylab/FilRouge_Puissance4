/*
 * send_data_server.c
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

#include "connexion_serveur.h"


//Envoi d'une DATA au serveur distant
void envoi_data_serveur(int loc_socket_desc) {

	char *loc_message = "Connexion réussi, attente message en arrivance!!!\n";

	if ( send(loc_socket_desc , loc_message , strlen(loc_message) , 0) < 0) {
		printf(" %d, %s", errno, strerror(errno));
		printf("\nEnvoi loupé\n");

	}
	else
	{


		printf("\nData envoyé\n");
		printf("%s\n", loc_message);
	}
}
