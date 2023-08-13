from tkinter import ttk
from CISCO.router.router_main_frames import *
from .dns_config_function import *

def dns():
    notebook = ttk.Notebook(right_main_frame)
    notebook.pack(expand=True, anchor=tk.N, fill=tk.X)
    # create frames
    dnsServer_main_frame = tk.Frame(notebook)
    dnsClient_main_frame = tk.Frame(notebook)

    dnsServer_main_frame.pack(fill='both', expand=True)
    dnsClient_main_frame.pack(fill='both', expand=True)

    # add frames to notebook
    notebook.add(dnsServer_main_frame, text='DNS Server')
    notebook.add(dnsClient_main_frame, text='DNS client')
    # notebook.add(deviceManagement_frame, text='DeviceManagement')

    # =============================DNS Config Section================================
    # ===========> DNS SERVER section
    dnsServer_frame = tk.LabelFrame(dnsServer_main_frame, text="Domain Name System")
    dnsServer_frame.pack(fill=tk.X, padx=20, pady=15)

    # Radio button section
    dnsServer_service_label = tk.Label(dnsServer_frame, text="DNS Services : ")
    dnsServer_service_label.grid(row=1, column=1, padx=20, pady=10)

    dns_service_value = tk.StringVar()
    dns_service_value.set("off")
    dns_service_selection = tk.Radiobutton(dnsServer_frame, text="OFF", variable=dns_service_value, value="off")
    dns_service_selection.grid(row=1, column=2, padx=10, sticky=tk.W)
    dns_service_selection = tk.Radiobutton(dnsServer_frame, text="ON", variable=dns_service_value, value="on")
    dns_service_selection.grid(row=2, column=2, padx=10, sticky=tk.W)

    dns_service_selection_button = tk.Button(dnsServer_frame, text="RUN", bg="#ecebec", width=12, command=lambda: dns_service_decision(dns_service_value.get()))
    dns_service_selection_button.grid(row=2, column=3, padx=20, pady=10, sticky=tk.E)

    def dns_service_decision(dns_service_value):
        if dns_service_value == "off":
            dns_service_off()
            pass
        elif dns_service_value == "on":
            dnsServer_second_frame = tk.LabelFrame(dnsServer_main_frame, text="DNS SERVER")
            dnsServer_second_frame.pack(fill=tk.X, padx=20, pady=15)
            # label section
            dnsServer_pool_name_label = tk.Label(dnsServer_second_frame, text="Domain name")
            dnsServer_pool_ip_label = tk.Label(dnsServer_second_frame, text="IP address")

            dnsServer_pool_name_label.grid(row=3, column=1)
            dnsServer_pool_ip_label.grid(row=3, column=2)

            # Entries Section
            dnsServer_pool_name_value = tk.StringVar()
            dnsServer_pool_ip_value = tk.StringVar()

            dnsServer_pool_name_entry = tk.Entry(dnsServer_second_frame, textvariable=dnsServer_pool_name_value)
            dnsServer_pool_ip_entry = tk.Entry(dnsServer_second_frame, textvariable=dnsServer_pool_ip_value)

            dnsServer_pool_name_entry.grid(row=4, column=1, padx=20, pady=10)
            dnsServer_pool_ip_entry.grid(row=4, column=2, padx=20, pady=10)


            # Buttons Section
            dnsServer_add_button = tk.Button(dnsServer_second_frame, text="ADD", bg="#ecebec", width=12, command=lambda: dnsServer_add_config(dnsServer_pool_name_value.get(), dnsServer_pool_ip_value.get()))
            dnsServer_run_button = tk.Button(dnsServer_second_frame, text="Execute", bg="#ecebec", width=12, command=lambda: dnsServer_run_config())

            dnsServer_add_button.grid(row=4, column=3, padx=20, pady=10, sticky=tk.E)
            dnsServer_run_button.grid(row=5, column=3, padx=20, pady=10, sticky=tk.E)



    # ===========> DNS CLIENT section
    dnsClient_frame = tk.LabelFrame(dnsClient_main_frame, text="DNS Client ")
    dnsClient_frame.pack(fill=tk.X, padx=20, pady=15)
    # label section
    dnsClient_ServerIP_label = tk.Label(dnsClient_frame, text="Server IP addresses : ")
    dnsClient_ServerIP_primary_label = tk.Label(dnsClient_frame, text="Primary")
    dnsClient_ServerIP_secondary_label = tk.Label(dnsClient_frame, text="Secondary")

    dnsClient_ServerIP_label.grid(row=1, column=1)
    dnsClient_ServerIP_primary_label.grid(row=2, column=1)
    dnsClient_ServerIP_secondary_label.grid(row=2, column=2)

    # Entries Section
    dnsClient_ServerIP_primary_value = tk.StringVar()
    dnsClient_ServerIP_secondary_value = tk.StringVar()

    dnsClient_ServerIP_primary_entry = tk.Entry(dnsClient_frame, textvariable=dnsClient_ServerIP_primary_value)
    dnsClient_ServerIP_secondary_entry = tk.Entry(dnsClient_frame, textvariable=dnsClient_ServerIP_secondary_value)

    dnsClient_ServerIP_primary_entry.grid(row=3, column=1, padx=20, pady=10)
    dnsClient_ServerIP_secondary_entry.grid(row=3, column=2, padx=20, pady=10)

    # Buttons Section
    dnsClient_run_button = tk.Button(dnsClient_frame, text="Execute", bg="#ecebec", width=12, command=lambda: dnsClient_config(dnsClient_ServerIP_primary_value.get(), dnsClient_ServerIP_secondary_value.get()))
    dnsClient_run_button.grid(row=5, column=3, padx=20, pady=10, sticky=tk.E)