# Lulugram
## General introduction
*Lulugram* is a chatroom application in Python. The application was written using python `socket` library, with more than one client connecting to the same server that gets the clients messages and forwards them to all the currently connected users. The application has a basic graphic interface created using python `tkinter` library.
## Functioning
The application works in the following way: once you open the server, clients can connect to it inserting IP address and port they mean to connect to. After that, the application opens a basic graphic iterface where we print a welcome message. The client is asked to choose a username for the communication with the other users in the chatroom, and after that the application tells the user the number of people currently connected to the chatroom. The username must be unique for each user.
Each time someone joins or leaves the conversation, the other users get notified.
To abandon the communication, the user can simply close the GUI or print an exit message ({bye}).
The protocol used for the communication is TCP.
## Setup
Execute the `server.py` file, making sure you setup an IP address and port that are reachable from other addresses. Then you can use a client to connect to it and exchange messages with the other participants. 
