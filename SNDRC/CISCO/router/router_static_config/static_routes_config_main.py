from tkinter import ttk
from CISCO.router.router_main_frames import *

def static_routing():
    notebook = ttk.Notebook(right_main_frame)
    notebook.pack(expand=True, anchor=tk.N, fill=tk.X)
    # create frames
    static_main_frame = tk.Frame(notebook)

    static_main_frame.pack(fill='both', expand=True)

    # add frames to notebook
    notebook.add(static_main_frame, text='Static Routing')

    # =============================Static route Config Section================================
    # ===========> Static section
    static_frame = tk.LabelFrame(static_main_frame, text="STATIC :")
    static_frame.pack(fill=tk.X, padx=20, pady=15)
    # label section
    static_network_label = tk.Label(static_frame, text="Network/IP address")
    static_prefixLength_label = tk.Label(static_frame, text="Prefix Length")
    static_gateway_label = tk.Label(static_frame, text="Gateway")

    static_network_label.grid(row=1, column=1)
    static_prefixLength_label.grid(row=1, column=2)
    static_gateway_label.grid(row=1, column=3)

    # Entries Section
    static_network_value = tk.StringVar()
    static_prefixLength_value = tk.StringVar()
    static_gateway_value = tk.StringVar()

    static_network_entry = tk.Entry(static_frame, textvariable=static_network_value)
    static_prefixLength_entry = tk.Entry(static_frame, textvariable=static_prefixLength_value)
    static_gateway_entry = tk.Entry(static_frame, textvariable=static_gateway_value)

    static_network_entry.grid(row=2, column=1, padx=20, pady=10)
    static_prefixLength_entry.grid(row=2, column=2, padx=20, pady=10)
    static_gateway_entry.grid(row=2, column=3, padx=20, pady=10)

    # Buttons Section
    static_run_button = tk.Button(static_frame, text="Execute", bg="#ecebec", width=12, command=lambda: interface_config(hostname_value))
    static_run_button.grid(row=5, column=3, padx=20, pady=10, sticky=tk.E)



    # ===========> Static Default section
    static_default_frame = tk.LabelFrame(static_main_frame, text="DEFAULT STATIC ROUTE: ")
    static_default_frame.pack(fill=tk.X, padx=20, pady=15)
    # label section
    static_default_gateway_label = tk.Label(static_default_frame, text="Gateway")

    static_default_gateway_label.grid(row=1, column=3)

    # Entries Section
    static_default_gateway_value = tk.StringVar()

    static_default_gateway_entry = tk.Entry(static_default_frame, textvariable=static_default_gateway_value)

    static_default_gateway_entry.grid(row=2, column=3, padx=20, pady=10)

    # Buttons Section
    static_default_run_button = tk.Button(static_default_frame, text="Execute", bg="#ecebec", width=12, command=lambda: interface_config(hostname_value))
    static_default_run_button.grid(row=5, column=3, padx=20, pady=10, sticky=tk.E)
