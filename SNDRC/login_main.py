import subprocess
import tkinter as tk
from tkinter import ttk
from login_functions import *

def login_button_press(ip, user, pwd, vendor, device, access_method):
    if ip_checking(ip) == "IP_Pass":
        if selection_device(vendor, device) == "Cisco Router":
            if access_method == "Telnet":
                # if telnet_device(ip, user, pwd) == "Successful":  # call telnet_device function
                #     root.destroy()
                subprocess.call(["python", '/first_ssh/first_ssh_main.py'], cwd="cd ../first_ssh/", shell=True)
            elif access_method == "SSH1" or "SSH2":
                if telnet_device(ip, user, pwd) == "Successful":  # call telnet_device function
                    root.destroy()
                    # subprocess.call(["python", "Cisco/Router/main/main_router.py"], shell=True)
        elif selection_device(vendor, device) == "Cisco Switch":
            if telnet_device(ip, user, pwd) == "Successful":  # call telnet_device function
                root.destroy()

            elif selection_device(vendor, device) == "Huawei Router":
                if telnet_device(ip, user, pwd) == "Successful":  # call telnet_device function
                    root.destroy()

        elif selection_device(vendor, device) == "Huawei Switch":
            if telnet_device(ip, user, pwd) == "Successful":  # call telnet_device function
                root.destroy()

        else:
            mgbx.showinfo("Selection", "Select valid Device")
    else:
        mgbx.showinfo("Selection", "Please! Enter correct IP address")



root = tk.Tk()
#set width and height of login window
root.geometry("650x210")
root.title("Login")
root.resizable(False, False)
# Main frame
top_frame = tk.Frame(bg="gray", borderwidth=10, relief="groove")
top_frame.pack(fill=tk.X)
# labels
ip_label = tk.Label(top_frame, text="Connect to: ", fg="white", bg="grey", font=10)
username_label = tk.Label(top_frame, text="Username: ", fg="white", bg="grey", font=10)
password_label = tk.Label(top_frame, text="Password: ", fg="white", bg="grey", font=10)

ip_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
username_label.grid(row=1, column=0, sticky=tk.W, padx=10)
password_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
# Enteries
ip_value = tk.StringVar()
username_value = tk.StringVar()
password_value = tk.StringVar()

ip_entry = tk.Entry(top_frame, textvariable=ip_value, width=50)
username_entry = tk.Entry(top_frame, textvariable=username_value, width=50)
password_entry = tk.Entry(top_frame, textvariable=password_value, show="*", width=50)

ip_entry.grid(row=0, column=1, padx=10, pady=10)
username_entry.grid(row=1, column=1, padx=10)
password_entry.grid(row=2, column=1, padx=10, pady=10)
#Vendor Selection
vendor_value = tk.StringVar()
vendor_combobox = ttk.Combobox(top_frame, textvariable=vendor_value, values=["Cisco", "Huawei"], width=10)
vendor_combobox.grid(row=0, column=2, padx=20)
#Access method Selection
access_method_value = tk.StringVar()
access_method_combobox = ttk.Combobox(top_frame, textvariable=access_method_value, values=["Telnet", "SSH1", "SSH2"], width=15)
access_method_combobox.grid(row=3, column=0)
# Radiobuttons
device_var = tk.StringVar()
device_var.set("Please Select a Device!")
device_selection = tk.Radiobutton(top_frame, text="Router", bg="grey", font=10, variable=device_var, value="Router")
device_selection.grid(row=1, column=2, padx=10)
device_selection = tk.Radiobutton(top_frame, text="Switch", bg="grey", font=10, variable=device_var, value="Switch")
device_selection.grid(row=2, column=2, padx=10)
# Actionbuttons
# Add_button = tk.Button(top_frame, text="Add/set", fg="white", bg="grey", font=10, command=Add_button_press)
# Add_button.grid(row=3, column=0, sticky=tk.W, ipadx=15, padx=10, pady=5)
login_button = tk.Button(top_frame, text="Connect", fg="white", bg="grey", font=5, command= lambda:login_button_press(ip_value.get(), username_value.get(), password_value.get(), vendor_value.get(), device_var.get(), access_method_value.get()))
login_button.grid(row=3, column=2, sticky=tk.E, ipadx=20, padx=10, pady=5)

root.mainloop()
