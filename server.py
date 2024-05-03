import socket
from tkinter import *
def send(listbox,entry):
    message=entry.get()
    listbox.insert('end','Server:'+message)
    entry.delete(0,END)
    client.send(bytes(message, 'utf-8'))
def receive(listbox):
    message_from_client = client.recv(50)
    listbox.insert('end','Client:'+message_from_client.decode('utf-8'))
root=Tk()

entry=Entry()
entry.pack(side=BOTTOM)
listbox=Listbox(root)
listbox.pack()

bt=Button(root,text='Send',command=lambda :send(listbox,entry))
bt.pack(side=BOTTOM)
rbt=Button(root,text='Recieve',command=lambda :receive(listbox))
rbt.pack(side=BOTTOM)
root.title('Server')

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT=12345
s.bind((HOST_NAME,PORT))
s.listen(4)

client,address=s.accept()
# while True:
#     message=input('Server:')
#     client.send(bytes('hello,how are you ?','utf-8'))
root.mainloop()