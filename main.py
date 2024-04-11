import socket
import threading
import tkinter as tk
from PIL import ImageTk, Image
from informacion import *

#_______________________________________________________________________________________________________________________
#Создание и настройка окна программы
root = tk.Tk()
root.title("Chat_УКБ")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2
h = h // 2
w = w - 440
h = h - 280
root.overrideredirect(False)
root.minsize(width=850, height=500)
root.geometry(f"850x500+{w}+{h}")
root.maxsize(width=850, height=500)
root.configure(background="#4d4d39")


#Подключение к серверу / клиенту
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5554))


#_______________________________________________________________________________________________________________________
#Принятие сообщений от сервера / клиента
def receive_message():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            message_list.insert(tk.END, message)
        except ConnectionResetError:
            break


#Отправка сообщения / обработка кнопки send_button0
def send_message():
    if len(name_entry.get())>=3 and name_entry.get()!="Имя" and len(my_message.get())>0 and family_entry.get() == "Фамилия(необязательно)":
        client_socket.send((f"{name_entry.get()}: {my_message.get()}").encode('utf-8'))
        message_list.insert(tk.END, f"Я: {my_message.get()}")
        my_message.delete(0, tk.END)
    elif len(name_entry.get())>=3 and name_entry.get()!="Имя" and len(my_message.get())>0 and family_entry.get() != "Фамилия(необязательно)" and len(family_entry.get())>3:
        client_socket.send((f"{family_entry.get()} {name_entry.get()[0]}.: {my_message.get()}").encode('utf-8'))
        message_list.insert(tk.END, f"Я: {my_message.get()}")
        my_message.delete(0, tk.END)

#_______________________________________________________________________________________________________________________
#Обработка кнопки send_button2
def gotovo():
    for i1 in range(len(family_entry.get())):
        if family_entry.get()!="Фамилия(необязательно)":
            family_entry.delete(first=12)
    for i2 in range(len(family_entry.get())):
        name_entry.delete(first=12)
    if len(family_entry.get())<=3 and len(name_entry.get())<=3 and family_entry.get()!="Фамилия(необязательно)":
        family_entry.delete(0, tk.END)
        family_entry.insert(0, "Фамилия(необязательно)")
        name_entry.delete(0, tk.END)
        name_entry.insert(0, "Имя")
    if len(family_entry.get())<3 and len(name_entry.get())>=3:
        family_entry.delete(0, tk.END)
        family_entry.insert(0, "Фамилия(необязательно)")
    if len(family_entry.get())>=3 and len(name_entry.get())<3:
        name_entry.delete(0, tk.END)
        name_entry.insert(0, "Имя")
    family_entry.configure(background="#8d9b76", font='Helvetica 15', fg="#000000", highlightthickness=0, bd=0.5, state=tk.DISABLED, disabledbackground="#8d9b76")
    name_entry.configure(background="#8d9b76", font='Helvetica 15', fg="#000000", highlightthickness=0, bd=0.5, state=tk.DISABLED, disabledbackground="#8d9b76")
    send_button4.place(height=30, width=30, x=340, y=410)

#Обработка кнопки send_button4
def redakt():
    family_entry.configure(background="#8d9b76", font='Helvetica 15', fg="#000000", highlightthickness=0, bd=0.5, state=tk.NORMAL, disabledbackground="#8d9b76")
    name_entry.configure(background="#8d9b76", font='Helvetica 15', fg="#000000", highlightthickness=0, bd=0.5, state=tk.NORMAL, disabledbackground="#8d9b76")
    send_button4.place(height=30, width=30, x=1340, y=410)
    send_button3.place(height=30, width=30, x=340, y=410)

#Обработка кнопки send_button3
def delite():
    family_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)

#Обработка кнопки send_button1
def info():
    wind = tk.Toplevel(root)
    wind.title("INFO")
    w = wind.winfo_screenwidth()
    h = wind.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - 490
    h = h - 330
    wind.overrideredirect(False)
    wind.minsize(width=435, height=500)
    wind.geometry(f"435x500+{w}+{h}")
    wind.maxsize(width=435, height=500)
    wind.configure(background="#4d4d39")
    wind.transient(root)
    wind.grab_set()
    wind.focus_set()
    text = tk.Label(wind)
    text.configure(background="#4d4d39", fg="#000000", font='Helvetica 15', justify=tk.LEFT, text=inf)
    text.place(x=5, y=5)
    def on_closing2():
        wind.destroy()
    wind.protocol("WM_DELETE_WINDOW", on_closing2)
    wind.mainloop()


#_______________________________________________________________________________________________________________________
#Вывод сообщений
message_list = tk.Listbox(root)
message_list.configure(background="#8d9b76", font='Helvetica 18', selectbackground="#8d9b76", bd=0, fg="#000000", highlightthickness=0)
message_list.place(height=350, width=830, x=10, y=10)

#Ввод сообщения от пользователя
my_message = tk.Entry(root)
my_message.configure(background="#8d9b76", font='Helvetica 15', state=tk.NORMAL)
my_message.place(height=30, width=790, x=10, y=370)

#Ввод фамилии
family_entry = tk.Entry(root)
family_entry.insert(0, "Фамилия(необязательно)")
family_entry.configure(background="#8d9b76", font='Helvetica 15', fg="#000000", highlightthickness=0, bd=0.5, state=tk.DISABLED, disabledbackground="#8d9b76")
family_entry.place(height=30, width=135, x=10, y=410)

#Ввод имени
name_entry = tk.Entry(root)
name_entry.insert(0, "Имя")
name_entry.configure(background="#8d9b76", font='Helvetica 15', fg="#000000", highlightthickness=0, bd=0.5, state=tk.DISABLED, disabledbackground="#8d9b76")
name_entry.place(height=30, width=135, x=155, y=410)


#_______________________________________________________________________________________________________________________
#Кнопка отправки сообщения
img0 = ImageTk.PhotoImage(Image.open("images/Go.png").resize((30, 30)))
send_button0 = tk.Button(root, image=img0, command=send_message)
send_button0.configure(background="#557a86", activebackground="#2f575c", bd=0.5)
send_button0.place(height=30, width=30, x=810, y=370)

#Кнопка открытия информации
img1 = ImageTk.PhotoImage(Image.open("images/info.png").resize((30, 30)))
send_button1 = tk.Button(root, image=img1, command=info)
send_button1.configure(border=0.5, bg="#8d9b76", activebackground="#3a3a2b")
send_button1.place(height=30, width=30, x=380, y=410)

#Кнопка готово / подтверждение
img2 = ImageTk.PhotoImage(Image.open("images/gotovo.png").resize((30, 30)))
send_button2 = tk.Button(root, image=img2, command=gotovo)
send_button2.configure(border=0.5, bg="#8d9b76", activebackground="#3a3a2b")
send_button2.place(height=30, width=30, x=300, y=410)

#Кнопка удаления
img3 = ImageTk.PhotoImage(Image.open("images/delite.png").resize((30, 30)))
send_button3 = tk.Button(root, image=img3, command=delite)
send_button3.configure(border=0.5, bg="#8d9b76", activebackground="#3a3a2b")
send_button3.place(height=30, width=30, x=1340, y=410)

#Кнопка редактирования
img4 = ImageTk.PhotoImage(Image.open("images/redak.png").resize((30, 30)))
send_button4 = tk.Button(root, image=img4, command=redakt)
send_button4.configure(border=0.5, bg="#8d9b76", activebackground="#3a3a2b")
send_button4.place(height=30, width=30, x=340, y=410)


#_______________________________________________________________________________________________________________________
#Включение многопоточности
receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

#Обработка закрытия окна программы / портов
def on_closing():
    client_socket.close()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)
tk.mainloop()

























































