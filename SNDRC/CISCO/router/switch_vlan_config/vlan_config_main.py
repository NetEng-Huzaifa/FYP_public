from tkinter import ttk
from CISCO.router.router_main_frames import *
from .vlan_config_function import *

def vlan():
    notebook = ttk.Notebook(right_main_frame)
    notebook.pack(expand=True, anchor=tk.N, fill=tk.X)
    # create frames
    vlan_main_frame = tk.Frame(notebook)

    vlan_main_frame.pack(fill='both', expand=True)

    # add frames to notebook
    notebook.add(vlan_main_frame, text='VLANs')

    # =============================VLAN Config Section================================
    # ===========> VLAN define section
    vlan_frame = tk.LabelFrame(vlan_main_frame, text="Create a Virtual LAN")
    vlan_frame.pack(fill=tk.X, padx=20, pady=15)
    # label section
    vlan_number_label = tk.Label(vlan_frame, text="VLAN number(1-4094)")
    vlan_state_label = tk.Label(vlan_frame, text="VLAN state")
    vlan_name_label = tk.Label(vlan_frame, text="name")
    vlan_info_label = tk.Label(vlan_frame, text="VTP mode must be transparent if you use Extended VLANs (1006-4094)!")

    vlan_number_label.grid(row=1, column=1)
    vlan_state_label.grid(row=1, column=2)
    vlan_name_label.grid(row=1, column=3)
    vlan_info_label.grid(row=3, column=1, columnspan=3, sticky=tk.W, padx=20, pady=5)

    # Entries Section
    vlan_number_value = tk.StringVar()
    vlan_state_value = tk.StringVar()
    vlan_name_value = tk.StringVar()

    vlan_number_entry = tk.Entry(vlan_frame, textvariable = vlan_number_value)
    vlan_state_entry = ttk.Combobox(vlan_frame, values = ["UP", "Shutdown"], textvariable = vlan_state_value)
    vlan_name_entry = tk.Entry(vlan_frame, textvariable = vlan_name_value)

    vlan_number_entry.grid(row=2, column=1, padx=20, pady=10)
    vlan_state_entry.grid(row=2, column=2, padx=20, pady=10)
    vlan_name_entry.grid(row=2, column=3, padx=10, pady=10)

    # Buttons Section
    vlan_config_run_button = tk.Button(vlan_frame, text="Execute", width=12, command=lambda: vlan_config(vlan_number_value.get(), vlan_state_value.get(), vlan_name_value.get()))

    vlan_config_run_button.grid(row=3, column=4, padx=20, pady=10, sticky=tk.E)