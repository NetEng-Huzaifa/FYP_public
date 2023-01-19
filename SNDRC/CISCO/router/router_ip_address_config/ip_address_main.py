from tkinter import ttk
from CISCO.router.router_main_frames import *
from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
import re


def ip_address():
    notebook = ttk.Notebook(right_main_frame)
    notebook.pack(expand=True, anchor=tk.N, fill=tk.X)
    # create frames
    ipAddress_main_frame = tk.Frame(notebook)
    # ssh_main_frame = tk.Frame(notebook)
    # deviceManagement_frame = tk.Frame(notebook)

    ipAddress_main_frame.pack(fill='both', expand=True)
    # ssh_main_frame.pack(fill='both', expand=True)
    # deviceManagement_frame.pack(fill='both', expand=True)

    # add frames to notebook
    notebook.add(ipAddress_main_frame, text='IP Addresses')
    # notebook.add(ssh_main_frame, text='SSH')
    # notebook.add(deviceManagement_frame, text='DeviceManagement')

    # =============================ipAddress Config Section================================
    # ===========> ipAddress section
    ipAddress_frame = tk.LabelFrame(ipAddress_main_frame, text="IP ADDRESS ")
    ipAddress_frame.pack(fill=tk.X, padx=20, pady=15)
    # label section
    ip_interface_label = tk.Label(ipAddress_frame, text="Interface(port) : ")
    ip_label = tk.Label(ipAddress_frame, text="IP Address : ")
    ip_prefixLength_label = tk.Label(ipAddress_frame, text="Prefix length(i.e 24) : ")
    ip_priority_label = tk.Label(ipAddress_frame, text="Priority : ")

    ip_interface_label.grid(row=1, column=1)
    ip_label.grid(row=3, column=1)
    ip_prefixLength_label.grid(row=3, column=2)
    ip_priority_label.grid(row=3, column=3)

    # Entries Section
    ip_interface_value = tk.StringVar()
    ipAddress_value = tk.StringVar()
    ip_prefixLength_value = tk.StringVar()
    ip_priority_value = tk.StringVar()

    ip_interface_entry = ttk.Combobox(ipAddress_frame, values = re.findall(r"^[A-Za-z].+?[\d/.]+", conn.get_info_from_router("sh ip int br"), re.MULTILINE), textvariable = ip_interface_value)
    ipAddress_entry = tk.Entry(ipAddress_frame, textvariable=ipAddress_value)
    ip_prefixLength_entry = tk.Entry(ipAddress_frame, textvariable=ip_prefixLength_value)
    ip_priority_entry = ttk.Combobox(ipAddress_frame, values=["primary", "Secondary"], textvariable=ip_priority_value)

    ip_interface_entry.grid(row=2, column=1, padx=20, pady=10)
    ipAddress_entry.grid(row=4, column=1, padx=20, pady=10)
    ip_prefixLength_entry.grid(row=4, column=2, padx=10, pady=10)
    ip_priority_entry.grid(row=4, column=3, padx=10, pady=10)

    # Buttons Section
    interface_run_button = tk.Button(ipAddress_frame, text="Execute", width=12, command=lambda: interface_config(hostname_value))

    interface_run_button.grid(row=5, column=3, padx=20, pady=10, sticky=tk.E)
