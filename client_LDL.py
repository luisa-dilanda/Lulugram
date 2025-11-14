#!/usr/bin/env python
# coding: utf-8

# In[4]:


from threading import Thread
import threading
import tkinter as tk
from socket import *
import winsound
import time
#from winsound import * 


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            #ins_thread = Thread(target=msg_list.insert(tk.END, msg))
            #ins_thread.start()
            msg_list.insert(tk.END, msg)
            msg_list.yview(tk.END)
            msg_list.update()
            msg_sound()
        except OSError:  # Possibly client has left the chat.
            break
        


def send(event=None):
    """Handles sending of messages."""
    try:
        msg = my_msg.get()
        my_msg.set("")  # Clears input field.
        client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            client_socket.shutdown(1)
            #time.sleep(1)
            client_socket.close()
            gui.destroy()

    except ConnectionResetError:
        print("Oops... The server appears to have disconnected.")
        #client_socket.shutdown(1)
        #time.sleep(1)
        client_socket.close()
        gui.destroy()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()
    
def msg_sound():
    sound_thread = threading.Thread(target=lambda:winsound.PlaySound('C:/Users/dilan/2. Reti/Prove chat 1-1/Prova 2 mia/recv_message.wav', winsound.SND_ASYNC))
    sound_thread.start()


gui = tk.Tk()
gui.title("Lulugram")
gui.iconbitmap(r"C:\Users\dilan\Desktop\cloud_icon.ico")


messages_frame = tk.Frame(gui)

my_msg = tk.StringVar()  # For the messages to be sent.

my_msg.set("Type your messages here.")
scrollbar = tk.Scrollbar(messages_frame)
# Following will contain the messages.

msg_list = tk.Listbox(messages_frame, height=15, width=80, background="Blue", fg="white", yscrollcommand=scrollbar.set)
scrollbar.configure(command=msg_list.yview)
msg_list.grid_propagate(True)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
msg_list.pack()
#msg_list.pack(expand=True, fill=tk.X)
messages_frame.pack()

entry_field = tk.Entry(gui, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tk.Button(gui, text="Send", command=send)
send_button.pack()

gui.protocol("WM_DELETE_WINDOW", on_closing)



HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 28000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
receive_thread = Thread(target=receive)
receive_thread.start()
tk.mainloop()
#except ConnectionRefusedError:
#    print("Oops... It looks like the server is temporarily unavailable. Please try again later.")
#    gui.destroy()


# In[ ]:





# In[ ]:





# In[ ]:


from tkinter import filedialog

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

root = tk.Tk()
button = tk.Button(root, text='Open', command=UploadAction)
button.pack()

