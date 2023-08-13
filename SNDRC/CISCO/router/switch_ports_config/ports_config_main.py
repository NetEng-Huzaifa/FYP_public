from tkinter import ttk
from CISCO.router.router_main_frames import *
from .ports_config_function import *
from tkinter import messagebox as mgbx
from CISCO.router.get_info_from_device import interface_info
import re
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
    ports_mode_entry = ttk.Combobox(ports_frame, values=["access", "trunk", "dynamic"], textvariable=ports_mode_value)

    ports_interface_entry.grid(row=2, column=1, padx=10, pady=10)
    ports_mode_entry.grid(row=2, column=2, padx=20, pady=10)


    ports_select_button = tk.Button(ports_frame, text="Select", width=12, command=lambda: post_ports_decision())
    ports_select_button.grid(row=5, column=3, padx=20, pady=10, sticky=tk.E)


    def post_ports_decision():
        if ports_interface_value.get():
            if ports_mode_value.get() in ["access", "trunk", "dynamic"]:
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
                    access_ports_vlan_entry = ttk.Combobox(access_ports_frame, values = re.findall(r"^[\d]+", conn.get_info_from_router("sh vlan br"), re.MULTILINE), textvariable = access_ports_vlan_value)

                    access_ports_type_entry.grid(row=2, column=1, padx=10, pady=10)
                    access_ports_vlan_entry.grid(row=2, column=2, padx=10, pady=10)

                    #access run button
                    access_config_run_button = tk.Button(access_ports_frame, text="Execute", width=12, command=lambda: access_config(ports_interface_value.get(), ports_mode_value.get(), access_ports_type_value.get(), access_ports_vlan_value.get()))

                    access_config_run_button.grid(row=3, column=3, padx=20, pady=10, sticky=tk.E)

                elif ports_mode_value.get() == "trunk":
                    # ===========> access port section
                    trunk_ports_frame = tk.LabelFrame(ports_main_frame, text="SWITCHPORT MODE TRUNK ALLOWED")
                    trunk_ports_frame.pack(fill=tk.X, padx=20, pady=15)
                    # label section
                    trunk_ports_allowed_vlan_label = tk.Label(trunk_ports_frame, text="Single VLAN")
                    trunk_ports_allowed_vlan_add_label = tk.Label(trunk_ports_frame, text="Multiple VLAN")
                    trunk_info_label = tk.Label(trunk_ports_frame, text="Just click EXECUTE if you don't want to add allowed VLAN")
                    MultipleVlan_info = tk.Label(trunk_ports_frame, text="-> comma seperated i.e 2,3,4")

                    trunk_ports_allowed_vlan_label.grid(row=1, column=1)
                    trunk_ports_allowed_vlan_add_label.grid(row=1, column=2)
                    trunk_info_label.grid(row=3, column=1, columnspan=2, sticky=tk.W, padx=10, pady=5)
                    MultipleVlan_info.grid(row=2, column=3)

                    # Entries Section
                    trunk_ports_allowed_vlan_value = tk.StringVar()
                    trunk_ports_allowed_vlan_add_value = tk.StringVar()

                    current_vlans = re.findall(r"^[\d]+", conn.get_info_from_router("sh vlan br"), re.MULTILINE)
                    trunk_ports_allowed_vlan_entry = ttk.Combobox(trunk_ports_frame, values = current_vlans, textvariable = trunk_ports_allowed_vlan_value)
                    trunk_ports_allowed_vlan_add_entry = ttk.Combobox(trunk_ports_frame, values = current_vlans, textvariable = trunk_ports_allowed_vlan_add_value)

                    trunk_ports_allowed_vlan_entry.grid(row=2, column=1, padx=10, pady=10)
                    trunk_ports_allowed_vlan_add_entry.grid(row=2, column=2, padx=10, pady=10)

                    # access run button
                    trunk_config_run_button = tk.Button(trunk_ports_frame, text="Execute", width=12,
                                                         command=lambda: trunk_config(ports_interface_value.get(),
                                                                                       ports_mode_value.get(),
                                                                                       trunk_ports_allowed_vlan_value.get(),
                                                                                       trunk_ports_allowed_vlan_add_entry.get(), current_vlans))

                    trunk_config_run_button.grid(row=3, column=3, padx=20, pady=10, sticky=tk.E)

                elif ports_mode_value.get() == "dynamic":
                    # ===========> dynamic port section
                    dynamic_ports_frame = tk.LabelFrame(ports_main_frame, text="SWITCHPORT MODE DYNAMIC")
                    dynamic_ports_frame.pack(fill=tk.X, padx=20, pady=15)
                    # label section
                    dynamic_ports_np_label = tk.Label(dynamic_ports_frame, text="negotiation parameter")

                    dynamic_ports_np_label.grid(row=1, column=1)

                    # Entries Section
                    dynamic_ports_np_value = tk.StringVar()

                    access_ports_type_entry = ttk.Combobox(dynamic_ports_frame, values = ["desirable", "auto"], textvariable = dynamic_ports_np_value)

                    access_ports_type_entry.grid(row=2, column=1, padx=10, pady=10)

                    #dynamic run button
                    dynamic_config_run_button = tk.Button(dynamic_ports_frame, text="Execute", width=12, command=lambda: dynamic_config(ports_interface_value.get(), ports_mode_value.get(), dynamic_ports_np_value.get()))

                    dynamic_config_run_button.grid(row=3, column=3, padx=20, pady=10, sticky=tk.E)
            else:
                mgbx.showinfo("Error", "Please select given mode")
        else:
            mgbx.showinfo("Error", "Please select the interface first")
