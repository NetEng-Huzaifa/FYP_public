# from tkinter import *
# from tkinter import ttk
#
# root = Tk()
# root.geometry("400x500")
#
# # root.lower()
#
#
# main_bg_frame = Frame(root)
# main_bg_frame.pack(fill=X)
# bg_top_frame = Frame(main_bg_frame, bg="red", height="250")
# bg_top_frame.pack(fill=X)
# bg_mid_frame = Frame(main_bg_frame, bg="blue", height=250)
# bg_mid_frame.pack(fill=X)
# bg_bottom_frame = Frame(main_bg_frame, bg="green", height=250)
# bg_bottom_frame.pack(fill=X)
#
# Label(main_bg_frame, text= "Welcome Folks!", font= ('Aerial 18 bold italic'), background= "white").pack(pady= 50)
# main_bg_frame.place(x=260, y=50)
#
#
# fg_top_frame = Frame(root, bg="orange", height="250")
# fg_top_frame.pack()

# root.mainloop()


# Import the required libraries
# from tkinter import *
# from tkinter import ttk

# Create an instance of tkinter frame
# win = Tk()
#
# # Set the size of the tkinter window
# win.geometry("700x350")
#
# # Add a Frame
# frame1= Frame(win, bg= "LightPink1")
#
# # Add an optional Label widget
# Label(frame1, text= "Welcome Folks!", font= ('Aerial 18 bold italic'), background= "white").pack(pady= 50)
# frame1.place(x= 260, y= 50)
#
# # Add a Button widget in second frame
# ttk.Button(frame1, text= "Button").place(x= 260, y=50)
# win.mainloop()


# info = []
#
# with open("login_info.txt","r") as f:
#
#     print([f.readline()])
#     var = f.readline()
#     print(var)
#     vari = var.split(",")
#     print(vari[0])
#     print(vari[0])
#     print(vari[1])

# info = []
#
# with open("login_info.txt", "r") as f:
#     print(f.readline())
#     var = f.read()
#     print(type(var))
#     var = var.split(",")
#     print(var)
#     print(type(var))
# info.append(var)
# print(var[0])
# print(var[1])
# print(var[2])
#
# print(info)



    # var = f.readline()
    #
    # print([f.readline()])
    # var = f.readline()
    # print(var)
    # vari = var.split(",")
    # print(vari[0])
    # print(vari[0])
    # print(vari[1])

from netmiko import ConnectHandler
cisco_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.33.133',
    'username': 'huzaifa',
    'password': '123',
    'secret': '123',
    'port': 22,
}
# ssh = ConnectHandler(**cisco_router)
# ssh.enable()
# result = ssh.send_command('term len 0')
# print(result)
# result = ssh.send_command('show run')
# print(result)

class SshDevice:
    def __init__(self):
        self.ssh = ConnectHandler(**cisco_router)
    def enable(self):
        self.ssh.enable()
        result = self.ssh.send_command('show run')
        return result

c1 = SshDevice()
result = c1.enable()
print(result)












