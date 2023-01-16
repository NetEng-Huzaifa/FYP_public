from tkinter import ttk
from CISCO.router.router_main_frames import *
from .interface_config_functions import *
from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
import re

def interface():
    notebook = ttk.Notebook(right_main_frame)
    notebook.pack(expand=True, anchor=tk.N, fill=tk.X)
    # create frames
    interface_main_frame = tk.Frame(notebook)
    # user_frame = tk.Frame(notebook)
    # ssh_main_frame = tk.Frame(notebook)
    # deviceManagement_frame = tk.Frame(notebook)

    interface_main_frame.pack(fill='both', expand=True)
    # user_frame.pack(fill='both', expand=True)
    # ssh_main_frame.pack(fill='both', expand=True)
    # deviceManagement_frame.pack(fill='both', expand=True)

    # add frames to notebook
    notebook.add(interface_main_frame, text='Interface Config')
    # notebook.add(user_frame, text='User')
    # notebook.add(ssh_main_frame, text='SSH')
    # notebook.add(deviceManagement_frame, text='DeviceManagement')

    # =============================Interface Config Section================================
    # ===========> interface section
    interface_frame = tk.LabelFrame(interface_main_frame, text="INTERFACE ")
    interface_frame.pack(fill=tk.X, padx=20, pady=15)
    # label section
    interface_label = tk.Label(interface_frame, text="Interface(port) : ")

    interface_label.grid(row=0, column=0)
    # Entries Section
    interface_value = tk.StringVar()

    interface_entry = ttk.Combobox(interface_frame, values = re.findall(r"^[A-Za-z].+?[\d/.]+", conn.get_info_from_router("sh int des"), re.MULTILINE), textvariable = interface_value)

    interface_entry.grid(row=0, column=1, padx=20)
    # Buttons Section
    interface_run_button = tk.Button(interface_frame, text="Execute", width=12, command=lambda: interface_config(hostname_value))

    interface_run_button.grid(row=2, column=3, padx=20, pady=10, sticky=tk.E)