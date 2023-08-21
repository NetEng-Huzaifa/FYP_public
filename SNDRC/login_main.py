import tkinter as tk
from tkinter import ttk
from login_functions import *
import subprocess

def access_device_telnet(ip, user, pwd, enable_pass, vendor, device, access_method):
    if pre_telnet_device(ip, user, pwd) == "Successful":
        with open("Files/login_info.txt", "w") as f:
            f.write(f"{ip},{user},{pwd},{enable_pass},{vendor},{device},{access_method}")
        root.destroy()
        subprocess.call(["python", 'first_ssh_main.py'], shell=True)

def access_device_ssh(ip, user, pwd, enable_pass, vendor, device, access_method):
    with open("Files/login_info.txt", "w") as f:
        f.write(f"{ip},{user},{pwd},{enable_pass},{vendor},{device},{access_method}")
    root.destroy()
    subprocess.call(["python", 'CISCO/router/router_main.py'], shell=True)

def login_button_press(ip, user, pwd, enable_pass, vendor, device, login_telnet_label_value, login_ssh_label_value):
    def login_func():
        if vendor in ["Cisco", "Huawei"]:
            if ip_checking(ip) == "IP_Pass":
                if selection_device(vendor, device) == "Cisco Router":
                    if access_method == "Telnet":
                        access_device_telnet(ip, user, pwd, enable_pass, vendor, device, access_method)
                    elif access_method == "SSH":
                        access_device_ssh(ip, user, pwd, enable_pass, vendor, device, access_method)
                    else:
                        mgbx.showinfo("Selection missing", f"Select Method to access {vendor} {device}")
                elif selection_device(vendor, device) == "Cisco Switch":
                    if pre_telnet_device(ip, user, pwd) == "Successful":
                        pass
                    elif selection_device(vendor, device) == "Huawei Router":
                        if pre_telnet_device(ip, user, pwd) == "Successful":
                            pass
                elif selection_device(vendor, device) == "Huawei Switch":
                    if pre_telnet_device(ip, user, pwd) == "Successful":
                        pass
                else:
                    mgbx.showinfo("Selection Missing", "Select valid Device")
            else:
                mgbx.showinfo("Error!", "Please! Enter correct IP address")
        else:
            mgbx.showinfo("Error!", "Please select correct given VENDOR")


    if ip:
        if user and pwd and enable_pass and vendor and device:
            if login_telnet_label_value == login_ssh_label_value == "1":
                mgbx.showinfo("Error!", "You cannot select SSH and Telnet simultaneously")
            elif login_telnet_label_value == "1":
                access_method = "Telnet"
                login_func()
            elif login_ssh_label_value == "1":
                access_method = "SSH"
                login_func()
            else:
                mgbx.showinfo("Error!", "Please Select the Protocol to access device")
        else:
            mgbx.showinfo("Error!", "All Fields are required")
    else:
        mgbx.showinfo("Error!", "Please Enter IP Address of your device")




root = tk.Tk()
#set width and height of login window
# root.geometry("700x200")
root.geometry()
root.title("Login")
root.resizable(False, False)

# Main frame
top_frame = tk.Frame(root, borderwidth=10, relief="groove")
top_frame.pack(fill=tk.X)

# labels
ip_label = tk.Label(top_frame, text="Connect To : ", font=("Times New Roman", 14))
username_label = tk.Label(top_frame, text="Username: ", font=("Times New Roman", 14))
password_label = tk.Label(top_frame, text="Password: ", font=("Times New Roman", 13))
# enable_pass_label = tk.Label(top_frame, text="EnPassword: ", fg="white", bg="grey", font=("Times New Roman", 12))
enable_pass_label = tk.Label(top_frame, text="EnPassword: ", font=("Times New Roman", 12))
text_label = tk.Label(top_frame, text="Don't Forget to change Default Credentials once you logged in! ", font=("Times New Roman", 11))

ip_label.grid(row=0, column=0, sticky=tk.W, padx=10)
username_label.grid(row=1, column=0, sticky=tk.W, padx=10)
password_label.grid(row=2, column=0, sticky=tk.W, padx=10)
enable_pass_label.grid(row=3, column=0, sticky=tk.W, padx=10)
text_label.grid(row=4, column=0, columnspan=2, sticky=tk.W, padx=10, pady=5)
# Enteries
ip_value = tk.StringVar()
username_value = tk.StringVar()
username_value.set("abc")
password_value = tk.StringVar()
password_value.set("123")
enable_pass_value = tk.StringVar()
enable_pass_value.set("123")

ip_entry = tk.Entry(top_frame, textvariable=ip_value, width=60)
username_entry = tk.Entry(top_frame, textvariable=username_value, width=60)
password_entry = tk.Entry(top_frame, textvariable=password_value, show="*", width=60)
enable_pass_entry = tk.Entry(top_frame, textvariable=enable_pass_value, show="*", width=60)

ip_entry.grid(row=0, column=1, padx=10, pady=10)
username_entry.grid(row=1, column=1, padx=10)
password_entry.grid(row=2, column=1, padx=10, pady=10)
enable_pass_entry.grid(row=3, column=1, padx=10, pady=10)
#Vendor Selection
vendor_value = tk.StringVar()
vendor_value.set("Cisco")
vendor_combobox = ttk.Combobox(top_frame, textvariable=vendor_value, values=["Cisco"], width=12)
# vendor_combobox.insert(0, "Select vendor")
vendor_combobox.grid(row=0, column=2, padx=20)

#Access method Selection
# access_method_value = tk.StringVar()
# access_method_combobox = ttk.Combobox(top_frame, textvariable=access_method_value, values=["Telnet", "SSH"], width=12)
# access_method_combobox.grid(row=1, column=2)
# Radiobuttons
device_var = "Router"
# device_var = tk.StringVar()
# device_var.set("Please Select Device!")
# device_selection = tk.Radiobutton(top_frame, text="Router", bg="grey", font=10, variable=device_var, value="Router")
# device_selection.grid(row=1, column=2, padx=10)
# device_selection = tk.Radiobutton(top_frame, text="Switch", bg="grey", font=10, variable=device_var, value="Switch")
# device_selection.grid(row=2, column=2, padx=10)
# Actionbuttons
# Add_button = tk.Button(top_frame, text="Add/set", fg="white", bg="grey", font=10, command=Add_button_press)
# Add_button.grid(row=3, column=0, sticky=tk.W, ipadx=15, padx=10, pady=5)



#check buttons
login_telnet_label_value = tk.StringVar()
login_telnet_label_value.set("0")
login_telnet_label = tk.Checkbutton(top_frame, text="Telnet", variable=login_telnet_label_value, onvalue=1, offvalue=0)
login_telnet_label.grid(row=1, column=2, padx=20, sticky=tk.W)

login_ssh_label_value = tk.StringVar()
login_ssh_label_value.set("0")
login_ssh_label = tk.Checkbutton(top_frame, text="SSH", variable=login_ssh_label_value, onvalue=1, offvalue=0)
login_ssh_label.grid(row=2, column=2, padx=20, sticky=tk.W)


def add_button_press(ip, username, password, enable_pass, vendor, device, login_telnet, login_ssh):
    file = pd.read_excel("Files/addset_info.xlsx")
    addSet_frame = tk.LabelFrame(top_frame, text="MANAGED:", borderwidth=3, relief="ridge")
    addSet_frame.pack(fill=tk.X, padx=10, pady=10)

    # listbox = tk.Listbox(addSet_frame, font=("Times New Roman", 12))
    # listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)




#button Section
# add_button = tk.Button(top_frame, text="Add/set", width=12, command= lambda:add_button_press(ip_value.get(), username_value.get(), password_value.get(), enable_pass_value.get(), vendor_value.get(), device_var, login_telnet_label_value.get(), login_ssh_label_value.get()))
# add_button.grid(row=3, column=2, padx=10, pady=5)

login_button = tk.Button(top_frame, text="Connect", width=12, command= lambda:login_button_press(ip_value.get(), username_value.get(), password_value.get(), enable_pass_value.get(), vendor_value.get(), device_var, login_telnet_label_value.get(), login_ssh_label_value.get()))
login_button.grid(row=3, column=2, padx=10, pady=5)

root.mainloop()
