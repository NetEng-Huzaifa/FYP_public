import tkinter as tk
from tkinter import ttk
from telnetlib import Telnet
from tkinter import messagebox as mgbx
import subprocess

# getting these values from login_info.txt file
with open("login_info.txt", "r") as f:
    var = f.readline()
    # print(type(var))
    # print(var)
    info = var.split(",")
    # print(type(info))
    # print(info)
    # print(info[0])
    # print(info[1])
    # print(info[2])

ip = info[0]
usr = info[1]
pwd = info[2]
en_pwd = info[3]

def ssh_config_using_telnet(ip, user, pwd, en_pwd, ssh_domain_value, ssh_version_value):
    def version_selection(ssh_version_value):
        if ssh_version_value == "1":
            return 600
        elif ssh_version_value == "2":
            return 768
        else:
            mgbx.showinfo("Access Denied", f"Please Enter correct SSH version")
    try:
        telnet = Telnet(ip, timeout=5)

        telnet.read_until(b'sername')
        # print(telnet.read_until(b'sername').decode())
        telnet.write(user.encode('ascii') + b'\n')

        telnet.read_until(b'assword')
        telnet.write(pwd.encode('ascii') + b'\n')

        telnet.read_until(b'>', timeout=5)
        telnet.write(b'enable\n')
        telnet.write(en_pwd.encode('ascii') + b'\n')

        telnet.write(b'configure terminal\n')
        ssh_run_commands = f"ip domain-name {ssh_domain_value}\n crypto key generate rsa\n {version_selection(ssh_version_value)}\n yes \n line vty 0 4\n transport input all\n login local\n exit\n"
        print(ssh_run_commands)
        telnet.write(ssh_run_commands.encode('ascii') + b'\n')
        telnet.write(b'end\n')
        telnet.write(b'exit\n')
        # otpt = telnet.read_all().decode()
        # print(otpt)
        root.destroy()
        subprocess.call(["python", 'CISCO/router/router_main.py'], shell=True)
    except Exception as e:
        mgbx.showinfo("Access Denied", f"{e}")


def ssh_config_error_checking(ssh_domain_value, ssh_version_value):
    if ssh_domain_value and ssh_version_value != "":
        if ssh_version_value.isnumeric():
            if int(ssh_version_value) < 1 or int(ssh_version_value) > 2:
                mgbx.showinfo("Caution", "Please select given SSH version")
            else:
                ssh_config_using_telnet(ip, usr, pwd, en_pwd, ssh_domain_value, ssh_version_value)
        else:
            mgbx.showinfo("Caution", "SSH version must be numeric")
    else:
        mgbx.showinfo("Caution", "Please Fill required fields")




root = tk.Tk()
#set width and height of login window
root.geometry("350x360")
root.title("SSH")
# root.resizable(False, False)
#main frame
main_frame = tk.Frame()
main_frame.pack(fill=tk.X)
#SSH Section
ssh_frame = tk.LabelFrame(main_frame, text="Configure SSH:")
ssh_frame.pack(fill=tk.X, padx=20, pady=15)
# Save label section
ssh_domain_label = tk.Label(ssh_frame, text="IP domain-name : ")
ssh_version_label = tk.Label(ssh_frame, text="SSH Version : ")

ssh_domain_label.grid(row=1, column=1)
ssh_version_label.grid(row=2, column=1)

# Entries Section
ssh_domain_value = tk.StringVar()
ssh_version_value = tk.StringVar()

domain_entry = tk.Entry(ssh_frame, textvariable=ssh_domain_value)
ssh_version_combobox = ttk.Combobox(ssh_frame, values=["1", "2"], textvariable=ssh_version_value)

domain_entry.grid(row=1, column=2, padx=20)
ssh_version_combobox.grid(row=2, column=2, padx=20)

# Buttons Section
# ssh_cmd_button = tk.Button(ssh_frame, text="Commands", width=12)
ssh_run_button = tk.Button(ssh_frame, text="Execute", width=12, command=lambda:ssh_config_error_checking(ssh_domain_value.get(), ssh_version_value.get()))

# ssh_cmd_button.grid(row=3, column=1, padx=20, pady=15,sticky=tk.W)
ssh_run_button.grid(row=3, column=2, padx=20, sticky=tk.E)

root.mainloop()