/*
 * connexion_serveur.c
 *
 *  Created on: 20 août 2019
 *      Author: daugustin
 */


#include "connexion_serveur.h"

#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <inet.h>
#include <string.h>
#include <errno.h>
//#include "lwip.h"

int connexion(const char *addr, int port) {
	struct sockaddr_in server;
	int return_connect_create;
	int loc_socket_desc;


	//Creation d'une socket
	loc_socket_desc = socket(AF_INET, SOCK_STREAM, 0);

	if(loc_socket_desc ==-1)
	{
		printf(" %d, %s", errno, strerror(errno));
		printf("\nSocket non créé\n");
	}
	else
	{
		printf("\nSocket créé\n");
//		return_connect_create= -1;

		server.sin_addr.s_addr = inet_addr(addr);
		server.sin_family = AF_INET;
		server.sin_port = htons(port);

		//Connexion au serveur distant
		return_connect_create = connect (loc_socket_desc, (struct sockaddr *)&server, sizeof (server)) <0;

		if (return_connect_create<0) {

			printf(" %d, %s", errno, strerror(errno));
			printf("\nErreur de connexion\n");
			close(loc_socket_desc);
			loc_socket_desc =-1;
		}
		else
		{
			printf("\nConnecté\n");

		}
	}

	return loc_socket_desc;
}
