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
# cisco_router = {
#     'device_type': 'cisco_ios',
#     'host': '192.168.33.133',
#     'username': 'huzaifa',
#     'password': '123',
#     'secret': '123',
#     'port': 22,
# }
# ssh = ConnectHandler(**cisco_router)
# ssh.enable()
# result = ssh.send_command('term len 0')
# print(result)
# result = ssh.send_command('show run')
# print(result)

# class SshDevice:
#     def __init__(self):
#         self.ssh = ConnectHandler(**cisco_router)
#     def enable(self):
#         self.ssh.enable()
#         result = self.ssh.send_command('show run')
#         return result
#
# c1 = SshDevice()
# result = c1.enable()
# print(result)




import re
# data = """
# Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
#        D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
#        N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
#        E1 - OSPF external type 1, E2 - OSPF external type 2
#        i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
#        ia - IS-IS inter area, * - candidate default, U - per-user static route
#        o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
#        + - replicated route, % - next hop override
#
# Gateway of last resort is 182.176.2.36 to network 0.0.0.0
#
# B*    0.0.0.0/0 [20/10] via 182.176.2.36, 1w0d
#       10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
# C        10.255.212.176/30 is directly connected, Vlan3192
# L        10.255.212.178/32 is directly connected, Vlan3192
#       103.0.0.0/8 is variably subnetted, 7 subnets, 3 masks
# B        103.131.212.0/24 [200/0] via 192.168.250.1, 6d03h
# B        103.131.213.0/24 [200/0] via 192.168.250.1, 6d03h
# B        103.131.214.0/24 [200/0] via 192.168.250.1, 6d03h
# B        103.131.215.0/24 [200/0] via 192.168.250.1, 6d03h
# C        103.131.215.208/29 is directly connected, Vlan501
# L        103.131.215.209/32 is directly connected, Vlan501
# S        103.131.215.214/32 [1/0] via 103.131.215.210
#       182.176.0.0/16 is variably subnetted, 2 subnets, 2 masks
# C        182.176.2.36/31 is directly connected, Vlan959
# L        182.176.2.37/32 is directly connected, Vlan959
#       192.168.250.0/32 is subnetted, 2 subnets
# O E2     192.168.250.1 [110/1] via 10.255.212.177, 6d03h, Vlan3192
# C        192.168.250.3 is directly connected, Loopback1
# """



# data_without_spaces = """
# Codes:L-local,C-connected,S-static,R-RIP,M-mobile,B-BGP
# D-EIGRP,EX-EIGRPexternal,O-OSPF,IA-OSPFinterarea
# N1-OSPFNSSAexternaltype1,N2-OSPFNSSAexternaltype2
# E1-OSPFexternaltype1,E2-OSPFexternaltype2
# i-IS-IS,su-IS-ISsummary,L1-IS-ISlevel-1,L2-IS-ISlevel-2
# ia-IS-ISinterarea,*-candidatedefault,U-per-userstaticroute
# o-ODR,P-periodicdownloadedstaticroute,H-NHRP,l-LISP
# +-replicatedroute,%-nexthopoverride
#
# Gatewayoflastresortis182.176.2.36tonetwork0.0.0.0
#
# B*0.0.0.0/0[20/10]via182.176.2.36,1w0d
# 10.0.0.0/8isvariablysubnetted,2subnets,2masks
# C10.255.212.176/30isdirectlyconnected,Vlan3192
# L10.255.212.178/32isdirectlyconnected,Vlan3192
# 103.0.0.0/8isvariablysubnetted,7subnets,3masks
# B103.131.212.0/24[200/0]via192.168.250.1,6d03h
# B103.131.213.0/24[200/0]via192.168.250.1,6d03h
# B103.131.214.0/24[200/0]via192.168.250.1,6d03h
# C103.131.214.3/24isdirectlyconnected,6d03h
# B103.131.215.0/24[200/0]via192.168.250.1,6d03h
# C103.131.215.208/29isdirectlyconnected,Vlan501
# L103.131.215.209/32isdirectlyconnected,Vlan501
# S103.131.215.214/32[1/0]via103.131.215.210
# 182.176.0.0/16isvariablysubnetted,2subnets,2masks
# C182.176.2.36/31isdirectlyconnected,interface1/2
# L182.176.2.37/32isdirectlyconnected,Vlan959
# 192.168.250.0/32issubnetted,2subnets
# OE2192.168.250.1[110/1]via10.255.212.177,6d03h,Vlan3192
# C192.168.250.3isdirectlyconnected,Loopback1
# """


data = """
S*    0.0.0.0/0 [254/0] via 192.168.56.2
      1.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C        1.1.1.0/24 is directly connected, Loopback3
L        1.1.1.1/32 is directly connected, Loopback3
      10.0.0.0/32 is subnetted, 1 subnets
C        10.10.10.10 is directly connected, Loopback5
      192.168.10.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.10.0/24 is directly connected, Ethernet1/0
L        192.168.10.2/32 is directly connected, Ethernet1/0
      192.168.20.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.20.0/24 is directly connected, Ethernet1/1
L        192.168.20.2/32 is directly connected, Ethernet1/1
      192.168.56.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.56.0/24 is directly connected, Ethernet0/0
L        192.168.56.135/32 is directly connected, Ethernet0/0
"""
# data_without_spaces = data.replace(" ", "")
# print(data_without_spaces)

# C182.176.2.36/31isdirectlyconnected,Vlan959
#                       ^C182.176.2.36/31isdirectlyconnected

# lines = data.split('\n')
# filtered_lines = [line for line in lines if "Loopback" not in line]
#
# data_without_spaces = data.replace(" ", "")
# lines = re.findall(r".*\d*.\d*.\d*.\d*/32 is directly connected.*", data, re.MULTILINE)
# data_without_spaces = '\n'.join([line for line in lines if "Loopback" not in line]).replace(" ", "")
# ip = re.findall(r"\d*\.\d*\.\d*\.\d*", data_without_spaces, re.MULTILINE)
# for line in ip:
#     network_ip_addresses = 'network ' + line + f' 0.0.0.0 area 0'
# print(network_ip_addresses)


# filtered_lines = [line for line in lines if not re.search(r'\bLoopback\b', line)]
# for line in filtered_lines:
#     ip = re.findall(r"\d+\.\d+\.\d+\.\d+", line)
#     network_ip_addresses = 'network ' + ip[0]
#     print(network_ip_addresses)
# print(filtered_lines)


# lines = data.split('\n')
# filtered_lines = [line for line in lines if "Loopback" not in line]
#
# # for line in filtered_lines:
# print(filtered_lines)





# =====================important
# import tkinter as tk
#
# def on_double_click(event):
#     selected_index = listbox.curselection()
#     if selected_index:
#         selected_index = selected_index[0]
#         selected_item = listbox.get(selected_index)
#         print("Double-clicked:", selected_item)
#
# data = "192.168.56.135,abc,123,123,Cisco,Router,Telnet"
# info_list = data.split(',')
#
# root = tk.Tk()
# root.title("Display and Select Information")
#
# listbox = tk.Listbox(root, font=("Times New Roman", 12))
# listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
#
# for info in info_list:
#     listbox.insert(tk.END, info)
#
# listbox.bind("<Double-Button-1>", on_double_click)
#
# root.mainloop()

# ===============================

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk


def main():
    root = ThemedTk(theme="Adapta")  # Choose a theme you like

    root.title("Custom Title Bar Style")

    label = ttk.Label(root, text="Hello, Tkinter!", font=("Helvetica", 16))
    label.pack(padx=20, pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()




# |^L.*Loopback

# data = [
#     "['10.255.212.176']",
#     "['103.131.214.3']",
#     "['103.131.215.208']",
#     "['182.176.2.36']"
# ]
#
# cleaned_data = [s.strip("[]'") for s in data]
#
# print(cleaned_data)






