from tkinter import ttk
from CISCO.router.router_main_frames import *
from CISCO.router.get_info_from_device import interface_info


def dhcp():
    notebook = ttk.Notebook(right_main_frame)
    notebook.pack(expand=True, anchor=tk.N, fill=tk.X)
    # create frames
    dhcpServer_main_frame = tk.Frame(notebook)
    dhcpClient_main_frame = tk.Frame(notebook)

    dhcpServer_main_frame.pack(fill='both', expand=True)
    dhcpClient_main_frame.pack(fill='both', expand=True)

    # add frames to notebook
    notebook.add(dhcpServer_main_frame, text='DHCP Server')
    notebook.add(dhcpClient_main_frame, text='DHCP client')
    # notebook.add(deviceManagement_frame, text='DeviceManagement')

    # =============================DHCP Config Section================================
    # ===========> DHCP SERVER section
    dhcpServer_frame = tk.LabelFrame(dhcpServer_main_frame, text="DHCP SERVER")
    dhcpServer_frame.pack(fill=tk.X, padx=20, pady=15)
    # label section
    dhcpServer_pool_label = tk.Label(dhcpServer_frame, text="Enter Network Pool : ")
    dhcpServer_pool_name_label = tk.Label(dhcpServer_frame, text="Name")
    dhcpServer_pool_ip_label = tk.Label(dhcpServer_frame, text="Network Address")
    dhcpServer_pool_prefixLength_label = tk.Label(dhcpServer_frame, text="Prefix Length")
    dhcpServer_exclude_label = tk.Label(dhcpServer_frame, text="Enter Exclude addresses: ")
    dhcpServer_exclude_from_label = tk.Label(dhcpServer_frame, text="From")
    dhcpServer_exclude_to_label = tk.Label(dhcpServer_frame, text="TO")
    dhcpServer_gateway_label = tk.Label(dhcpServer_frame, text="Gateway Address : ")

    dhcpServer_pool_label.grid(row=1, column=1)
    dhcpServer_pool_name_label.grid(row=2, column=1)
    dhcpServer_pool_ip_label.grid(row=2, column=2)
    dhcpServer_pool_prefixLength_label.grid(row=2, column=3)
    dhcpServer_exclude_label.grid(row=4, column=1)
    dhcpServer_exclude_from_label.grid(row=5, column=1)
    dhcpServer_exclude_to_label.grid(row=5, column=2)
    dhcpServer_gateway_label.grid(row=7, column=1)

    # Entries Section
    dhcpServer_pool_name_value = tk.StringVar()
    dhcpServer_pool_ip_value = tk.StringVar()
    dhcpServer_pool_prefixLength_value = tk.StringVar()
    dhcpServer_exclude_from_value = tk.StringVar()
    dhcpServer_exclude_to_value = tk.StringVar()
    dhcpServer_gateway_value = tk.StringVar()

    dhcpServer_pool_name_entry = tk.Entry(dhcpServer_frame, textvariable=dhcpServer_pool_name_value)
    dhcpServer_pool_ip_entry = tk.Entry(dhcpServer_frame, textvariable=dhcpServer_pool_ip_value)
    dhcpServer_pool_prefixLength_entry = tk.Entry(dhcpServer_frame, textvariable=dhcpServer_pool_prefixLength_value)
    dhcpServer_exclude_from_entry = tk.Entry(dhcpServer_frame, textvariable=dhcpServer_exclude_from_value)
    dhcpServer_exclude_to_entry = tk.Entry(dhcpServer_frame, textvariable=dhcpServer_exclude_to_value)
    dhcpServer_gateway_entry = tk.Entry(dhcpServer_frame, textvariable=dhcpServer_gateway_value)

    dhcpServer_pool_name_entry.grid(row=3, column=1, padx=20, pady=10)
    dhcpServer_pool_ip_entry.grid(row=3, column=2, padx=20, pady=10)
    dhcpServer_pool_prefixLength_entry.grid(row=3, column=3, padx=20, pady=10)
    dhcpServer_exclude_from_entry.grid(row=6, column=1, padx=20)
    dhcpServer_exclude_to_entry.grid(row=6, column=2, padx=20)
    dhcpServer_gateway_entry.grid(row=7, column=2, padx=20, pady=10)


    # Buttons Section
    dhcpServer_run_button = tk.Button(dhcpServer_frame, text="Execute", bg="#ecebec", width=12, command=lambda: interface_config(hostname_value))

    dhcpServer_run_button.grid(row=7, column=3, padx=20, pady=10, sticky=tk.E)



    # ===========> DHCP CLIENT section
    dhcpClient_frame = tk.LabelFrame(dhcpClient_main_frame, text="DHCP Client ")
    dhcpClient_frame.pack(fill=tk.X, padx=20, pady=15)
    # label section
    dhcpClient_interface_label = tk.Label(dhcpClient_frame, text="Interface(port) : ")

    dhcpClient_interface_label.grid(row=0, column=0)
    # Entries Section
    dhcpClient_interface_value = tk.StringVar()

    dhcpClient_interface_entry = ttk.Combobox(dhcpClient_frame,values = interface_info, textvariable=dhcpClient_interface_value)

    dhcpClient_interface_entry.grid(row=0, column=1, padx=20, pady=10)
    # Buttons Section
    interface_run_button = tk.Button(dhcpClient_frame, text="Execute", width=12, command=lambda: interface_config(hostname_value))

    interface_run_button.grid(row=2, column=3, padx=20, pady=10, sticky=tk.E)