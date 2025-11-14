#!/usr/bin/env python
# coding: utf-8

# In[ ]:



from socket import *
from threading import Thread
import time

def accept_connections():
    """Accepts connection requests from clients."""
    while True:
        client, client_address = server.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Hello honey! Please type your name and press Enter.", "utf8"))           
        addresses[client] = client_address
        Thread(target=manage_connections, args=(client,)).start()



def manage_connections(client):  
    try:
        c=0
        while c==0:
            name = client.recv(BUFSIZ).decode("utf8")
            list=[clients[client] for client in clients]
            if name not in list:
                c=1
                welcome = 'Welcome %s! If you ever want to quit, type {bye} to exit.' % name
                client.send(bytes(welcome, "utf8"))
            else:
                client.send(bytes("This name is already taken, please try with another one!", "utf8"))
        count_info='There are %d users connected with you at the moment!' % len(clients)
        client.send(bytes(count_info+"\n --------------", "utf8"))
        msg = "%s has joined the chat!" % name
        broadcast(bytes(msg, "utf8"),server)
        clients[client] = name

        while True:
            msg = client.recv(BUFSIZ)
            if msg != bytes("{bye}", "utf8"):
                broadcast(msg, client, name+": ")
            else:
                client.send(bytes("{bye}", "utf8"))
                client.shutdown(1)
                client.close()
                del clients[client]
                broadcast(bytes("%s has left the chat." % name, "utf8"),server)
                break
    except ConnectionResetError:
        print("someone has disconnected.")

def broadcast(msg, client, prefix=""):  # prefix is for name identification.
    for sock in clients:
        if prefix=="":
            sock.send(msg)
        else:
            if sock!=client:
                sock.send(bytes(prefix, "utf8")+msg)
            else:
                sock.send(bytes("you: ", "utf8")+msg)


        
clients = {}
addresses = {}

HOST = ''
PORT = 28000
BUFSIZ = 1024
ADDR = (HOST, PORT)
server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(ADDR)



if __name__ == "__main__":
    server.listen(5)
    print("Ready to connect...")
    ACCEPT_THREAD = Thread(target=accept_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    server.close()

