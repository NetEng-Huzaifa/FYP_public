from tkinter import ttk
from CISCO.router.router_main_frames import *
from .vtp_config_function import *

def vtp():
    notebook = ttk.Notebook(right_main_frame)
    notebook.pack(expand=True, anchor=tk.N, fill=tk.X)
    # create frames
    vtp_main_frame = tk.Frame(notebook)

    vtp_main_frame.pack(fill='both', expand=True)

    # add frames to notebook
    notebook.add(vtp_main_frame, text='VTP')

    # =============================vtp Config Section================================
    # ===========> vtp define section
    vtp_frame = tk.LabelFrame(vtp_main_frame, text="Create a Virtual LAN")
    vtp_frame.pack(fill=tk.X, padx=20, pady=15)
    # label section
    vtp_name_label = tk.Label(vtp_frame, text="domain name")
    vtp_mode_label = tk.Label(vtp_frame, text="vtp mode")
    vtp_pruning_label = tk.Label(vtp_frame, text="pruning")

    vtp_name_label.grid(row=1, column=1)
    vtp_mode_label.grid(row=1, column=2)
    vtp_pruning_label.grid(row=1, column=3)

    # Entries Section
    vtp_name_value = tk.StringVar()
    vtp_mode_value = tk.StringVar()
    vtp_pruning_value = tk.StringVar()

    vtp_name_entry = tk.Entry(vtp_frame, textvariable = vtp_name_value)
    vtp_mode_entry = ttk.Combobox(vtp_frame, values = ["client", "server", "transparent"], textvariable = vtp_mode_value)
    vtp_pruning_entry = ttk.Combobox(vtp_frame, values = ["enable", "disable"], textvariable = vtp_pruning_value)

    vtp_name_entry.grid(row=2, column=1, padx=10, pady=10)
    vtp_mode_entry.grid(row=2, column=2, padx=20, pady=10)
    vtp_pruning_entry.grid(row=2, column=3, padx=20, pady=10)

    # Buttons Section
    vtp_config_run_button = tk.Button(vtp_frame, text="Execute", width=12, command=lambda: vtp_config(vtp_name_value.get(), vtp_mode_value.get(), vtp_pruning_value.get()))

    vtp_config_run_button.grid(row=5, column=3, padx=20, pady=10, sticky=tk.E)