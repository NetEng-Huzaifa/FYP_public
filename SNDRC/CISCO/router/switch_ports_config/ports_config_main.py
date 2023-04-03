from tkinter import ttk
from CISCO.router.router_main_frames import *
from .ports_config_function import *
from tkinter import messagebox as mgbx
from CISCO.router.get_info_from_device import interface_info, vlan_info

def ports():
    notebook = ttk.Notebook(right_main_frame)
    notebook.pack(expand=True, anchor=tk.N, fill=tk.X)
    # create frames
    ports_main_frame = tk.Frame(notebook)

    ports_main_frame.pack(fill='both', expand=True)

    # add frames to notebook
    notebook.add(ports_main_frame, text='Ports')

    # =============================ports Config Section================================
    # ===========> ports define section
    ports_frame = tk.LabelFrame(ports_main_frame, text="SWITCHPORT")
    ports_frame.pack(fill=tk.X, padx=20, pady=15)
    # label section
    ports_interface_label = tk.Label(ports_frame, text="Interface")
    ports_mode_label = tk.Label(ports_frame, text="switchport mode")

    ports_interface_label.grid(row=1, column=1)
    ports_mode_label.grid(row=1, column=2)

    # Entries Section
    ports_interface_value = tk.StringVar()
    ports_mode_value = tk.StringVar()

    ports_interface_entry = ttk.Combobox(ports_frame, values=interface_info, textvariable=ports_interface_value)
    ports_mode_entry = ttk.Combobox(ports_frame, values=["trunk", "access"], textvariable=ports_mode_value)

    ports_interface_entry.grid(row=2, column=1, padx=10, pady=10)
    ports_mode_entry.grid(row=2, column=2, padx=20, pady=10)


    ports_select_button = tk.Button(ports_frame, text="Select", width=12, command=lambda: post_ports_decision())
    ports_select_button.grid(row=5, column=3, padx=20, pady=10, sticky=tk.E)


    def post_ports_decision():
        if ports_interface_value.get() != "":
            if ports_mode_value.get() == "trunk" or ports_mode_value.get() == "access":
                if ports_mode_value.get() == "access":
                    # ===========> access port section
                    access_ports_frame = tk.LabelFrame(ports_main_frame, text="SWITCHPORT MODE ACCESS")
                    access_ports_frame.pack(fill=tk.X, padx=20, pady=15)
                    # label section
                    access_ports_type_label = tk.Label(access_ports_frame, text="Traffic type")
                    access_ports_vlan_label = tk.Label(access_ports_frame, text="Select VLAN")

                    access_ports_type_label.grid(row=1, column=1)
                    access_ports_vlan_label.grid(row=1, column=2)

                    # Entries Section
                    access_ports_type_value = tk.StringVar()
                    access_ports_vlan_value = tk.StringVar()

                    access_ports_type_entry = ttk.Combobox(access_ports_frame, values = ["data", "voice"], textvariable = access_ports_type_value)
                    access_ports_vlan_entry = ttk.Combobox(access_ports_frame, values = vlan_info, textvariable = access_ports_vlan_value)

                    access_ports_type_entry.grid(row=2, column=1, padx=10, pady=10)
                    access_ports_vlan_entry.grid(row=2, column=2, padx=10, pady=10)

                    #access run button
                    access_config_run_button = tk.Button(access_ports_frame, text="Execute", width=12, command=lambda: access_config(ports_interface_value.get(), ports_mode_value.get(), access_ports_type_value.get(), access_ports_vlan_value.get()))

                    access_config_run_button.grid(row=3, column=3, padx=20, pady=10, sticky=tk.E)

                elif ports_mode_value == "trunk":
                    # ===========> trunk ports section
                    trunk_ports_frame = tk.LabelFrame(ports_main_frame, text="SWITCHPORT MODE TRUNK")
                    trunk_ports_frame.pack(fill=tk.X, padx=20, pady=15)
                    # label section
                    trunk_ports_mode_label = tk.Label(trunk_ports_frame, text="switchport mode")
                    # ports_mode_label = tk.Label(ports_frame, text="ports mode")
                    # ports_pruning_label = tk.Label(ports_frame, text="pruning")


                    trunk_ports_mode_label.grid(row=1, column=1)
                    # ports_mode_label.grid(row=1, column=2)
                    # ports_pruning_label.grid(row=1, column=3)

                    # Entries Section
                    trunk_ports_mode_value = tk.StringVar()
                    # ports_mode_value = tk.StringVar()
                    # ports_pruning_value = tk.StringVar()

                    trunk_ports_mode_entry = ttk.Combobox(trunk_ports_frame, values=["trunk", "access"], textvariable=trunk_ports_mode_value)
                    # ports_mode_entry = ttk.Combobox(ports_frame, values=["client", "server", "transparent"], textvariable=ports_mode_value)
                    # ports_pruning_entry = ttk.Combobox(ports_frame, values=["enable", "disable"], textvariable=ports_pruning_value)

                    trunk_ports_mode_entry.grid(row=2, column=1, padx=10, pady=10)
                    # ports_mode_entry.grid(row=2, column=2, padx=20, pady=10)
                    # ports_pruning_entry.grid(row=2, column=3, padx=20, pady=10)
            else:
                mgbx.showinfo("Error", "Please select given mode")
        else:
            mgbx.showinfo("Error", "Please select the interface first")




    # Buttons Section
    # ports_config_run_button = tk.Button(ports_frame, text="Execute", width=12, command=lambda: ports_config(ports_name_value.get(), ports_mode_value.get(), ports_pruning_value.get()))
    #
    # ports_config_run_button.grid(row=5, column=3, padx=20, pady=10, sticky=tk.E)