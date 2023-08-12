from tkinter import ttk
from CISCO.router.router_main_frames import *
from .nat_config_function import *
from CISCO.router.get_info_from_device import interface_info

def nat():
    notebook = ttk.Notebook(right_main_frame)
    notebook.pack(expand=True, anchor=tk.N, fill=tk.X)
    # create frames
    nat_main_frame = tk.Frame(notebook)
    pat_main_frame = tk.Frame(notebook)

    nat_main_frame.pack(fill='both', expand=True)
    pat_main_frame.pack(fill='both', expand=True)

    # add frames to notebook
    notebook.add(nat_main_frame, text='NAT')
    notebook.add(pat_main_frame, text='PAT')

    # =============================S-NAT Config Section================================
    # ===========> S-NAT section
    snat_frame = tk.LabelFrame(nat_main_frame, text="STATIC NAT", borderwidth=3, relief="ridge")
    snat_frame.pack(fill=tk.X, padx=20, pady=15)
    snat_interface_frame = tk.LabelFrame(snat_frame, text="Interfaces")
    snat_interface_frame.pack(fill=tk.X, padx=20, pady=15)
    snat_pub_ip_frame = tk.LabelFrame(snat_frame, text="IP Addresses")
    snat_pub_ip_frame.pack(fill=tk.X, padx=20)


    # label section
    snat_int_inside_label = tk.Label(snat_interface_frame, text="Inside")
    snat_int_outside_label = tk.Label(snat_interface_frame, text="Outside")
    snat_public_ip_label = tk.Label(snat_pub_ip_frame, text="Public")
    snat_private_ip_label = tk.Label(snat_pub_ip_frame, text="Private")

    snat_int_inside_label.grid(row=1, column=1, padx=20, pady=10)
    snat_int_outside_label.grid(row=2, column=1, padx=20, pady=10)
    snat_public_ip_label.grid(row=4, column=3)
    snat_private_ip_label.grid(row=4, column=2)


    # Entries Section
    snat_int_inside_value = tk.StringVar()
    snat_int_outside_value = tk.StringVar()
    snat_public_ip_value = tk.StringVar()
    snat_private_ip_value = tk.StringVar()

    snat_int_inside_entry = ttk.Combobox(snat_interface_frame, values=interface_info, textvariable=snat_int_inside_value)
    snat_int_outside_entry = ttk.Combobox(snat_interface_frame, values=interface_info, textvariable=snat_int_outside_value)
    snat_public_ip_entry = tk.Entry(snat_pub_ip_frame, textvariable=snat_public_ip_value)
    snat_private_ip_entry = tk.Entry(snat_pub_ip_frame, textvariable=snat_private_ip_value)

    snat_int_inside_entry.grid(row=1, column=2)
    snat_int_outside_entry.grid(row=2, column=2)
    snat_public_ip_entry.grid(row=5, column=3, padx=20, pady=10)
    snat_private_ip_entry.grid(row=5, column=2, padx=20, pady=10)

    #Button
    snat_run_button = tk.Button(snat_frame, text="Execute", width=12, command=lambda: snat_config(snat_int_inside_value.get(), snat_int_outside_value.get(), snat_public_ip_value.get(), snat_private_ip_value.get(), interface_info))
    snat_run_button.pack(padx=20, pady=10)



    # =============================D-NAT Config Section================================
    # ===========> D-NAT section
    dnat_frame = tk.LabelFrame(nat_main_frame, text="DYNAMIC NAT", borderwidth=3, relief="ridge")
    dnat_frame.pack(fill=tk.X, padx=20)
    dnat_interface_frame = tk.LabelFrame(dnat_frame, text="Interfaces")
    dnat_interface_frame.pack(fill=tk.X, padx=20, pady=15)
    dnat_pub_ip_frame = tk.LabelFrame(dnat_frame, text="Public IP Addresses")
    dnat_pub_ip_frame.pack(fill=tk.X, padx=20, pady=15)
    dnat_Apply_frame = tk.LabelFrame(dnat_frame, text="Apply Dynamic NAT")
    dnat_Apply_frame.pack(fill=tk.X, padx=20, pady=15)



    # label section
    dnat_int_inside_label = tk.Label(dnat_interface_frame, text="Inside")
    dnat_int_outside_label = tk.Label(dnat_interface_frame, text="Outside")
    dnat_set_pool_name_label = tk.Label(dnat_pub_ip_frame, text="Pool name")
    dnat_pool_from_label = tk.Label(dnat_pub_ip_frame, text="From")
    dnat_pool_to_label = tk.Label(dnat_pub_ip_frame, text="TO")
    dnat_pool_prefixLength_label = tk.Label(dnat_pub_ip_frame, text="Prefix Length i.e 24")
    dnat_source_list_label = tk.Label(dnat_Apply_frame, text="Access-list number")
    # dnat_pool_name_label = tk.Label(dnat_Apply_frame, text="Pool name")

    dnat_int_inside_label.grid(row=1, column=1)
    dnat_int_outside_label.grid(row=1, column=2)
    dnat_set_pool_name_label.grid(row=4, column=1)
    dnat_pool_from_label.grid(row=4, column=2)
    dnat_pool_to_label.grid(row=4, column=3)
    dnat_pool_prefixLength_label.grid(row=4, column=4)
    dnat_source_list_label.grid(row=6, column=1, padx=20, pady=10)
    # dnat_pool_name_label.grid(row=6, column=2)


    # Entries Section
    dnat_int_inside_value = tk.StringVar()
    dnat_int_outside_value = tk.StringVar()
    dnat_set_pool_name_value = tk.StringVar()
    dnat_pool_from_value = tk.StringVar()
    dnat_pool_to_value = tk.StringVar()
    dnat_pool_prefixLength_value = tk.StringVar()
    dnat_source_list_value = tk.StringVar()
    # dnat_pool_name_value = tk.StringVar()

    dnat_int_inside_entry = ttk.Combobox(dnat_interface_frame, values=interface_info, textvariable=dnat_int_inside_value)
    dnat_int_outside_entry = ttk.Combobox(dnat_interface_frame, values=interface_info, textvariable=dnat_int_outside_value)
    dnat_set_pool_name_entry = tk.Entry(dnat_pub_ip_frame, textvariable=dnat_set_pool_name_value)
    dnat_pool_from_entry = tk.Entry(dnat_pub_ip_frame, textvariable=dnat_pool_from_value)
    dnat_pool_to_entry = tk.Entry(dnat_pub_ip_frame, textvariable=dnat_pool_to_value)
    dnat_pool_prefixLength_entry = tk.Entry(dnat_pub_ip_frame, textvariable=dnat_pool_prefixLength_value)
    dnat_source_list_entry = tk.Entry(dnat_Apply_frame, textvariable=dnat_source_list_value)
    # dnat_pool_name_entry = tk.Entry(dnat_Apply_frame, textvariable=dnat_pool_name_value)

    dnat_int_inside_entry.grid(row=2, column=1, padx=20, pady=10)
    dnat_int_outside_entry.grid(row=2, column=2, padx=20, pady=10)
    dnat_set_pool_name_entry.grid(row=5, column=1, padx=20, pady=10)
    dnat_pool_from_entry.grid(row=5, column=2, padx=20, pady=10)
    dnat_pool_to_entry.grid(row=5, column=3, padx=20, pady=10)
    dnat_pool_prefixLength_entry.grid(row=5, column=4, padx=20, pady=10)
    dnat_source_list_entry.grid(row=6, column=2, padx=20, pady=10)
    # dnat_pool_name_entry.grid(row=7, column=2, padx=20, pady=10)

    #Button
    dnat_run_button = tk.Button(dnat_frame, text="Execute", width=12, command=lambda: dnat_config(dnat_int_inside_value.get(), dnat_int_outside_value.get(), dnat_set_pool_name_value.get(), dnat_pool_from_value.get(), dnat_pool_to_value.get(), dnat_pool_prefixLength_value.get(), dnat_source_list_value.get(), interface_info))
    dnat_run_button.pack(padx=20, pady=10)



# =============================PAT Config Section================================
    # ===========> PAT section
    pat_frame = tk.LabelFrame(pat_main_frame, text="PORT ADDRESS TRANSLATION ", borderwidth=3, relief="ridge")
    pat_frame.pack(fill=tk.X, padx=20, pady=15)
    pat_interface_frame = tk.LabelFrame(pat_frame, text="Interfaces")
    pat_interface_frame.pack(fill=tk.X, padx=20, pady=15)
    pat_pub_ip_frame = tk.LabelFrame(pat_frame, text="Public IP Addresses")
    pat_pub_ip_frame.pack(fill=tk.X, padx=20, pady=15)
    pat_Apply_frame = tk.LabelFrame(pat_frame, text="Apply Dynamic NAT")
    pat_Apply_frame.pack(fill=tk.X, padx=20, pady=15)



    # label section
    pat_int_inside_label = tk.Label(pat_interface_frame, text="Inside")
    pat_int_outside_label = tk.Label(pat_interface_frame, text="Outside")
    pat_set_pool_name_label = tk.Label(pat_pub_ip_frame, text="Pool name")
    pat_pool_from_label = tk.Label(pat_pub_ip_frame, text="From")
    pat_pool_to_label = tk.Label(pat_pub_ip_frame, text="TO")
    pat_pool_prefixLength_label = tk.Label(pat_pub_ip_frame, text="Prefix Length")
    pat_source_list_label = tk.Label(pat_Apply_frame, text="Access-list number")
    # pat_pool_name_label = tk.Label(pat_Apply_frame, text="Pool name")

    pat_int_inside_label.grid(row=1, column=1)
    pat_int_outside_label.grid(row=1, column=2)
    pat_set_pool_name_label.grid(row=4, column=1)
    pat_pool_from_label.grid(row=4, column=2)
    pat_pool_to_label.grid(row=4, column=3)
    pat_pool_prefixLength_label.grid(row=4, column=4)
    pat_source_list_label.grid(row=6, column=1, padx=20, pady=10)
    # pat_pool_name_label.grid(row=6, column=2)


    # Entries Section
    pat_int_inside_value = tk.StringVar()
    pat_int_outside_value = tk.StringVar()
    pat_set_pool_name_value = tk.StringVar()
    pat_pool_from_value = tk.StringVar()
    pat_pool_to_value = tk.StringVar()
    pat_pool_prefixLength_value = tk.StringVar()
    pat_source_list_value = tk.StringVar()
    # pat_pool_name_value = tk.StringVar()

    pat_int_inside_entry = ttk.Combobox(pat_interface_frame, values=interface_info, textvariable=pat_int_inside_value)
    pat_int_outside_entry = ttk.Combobox(pat_interface_frame, values=interface_info, textvariable=pat_int_outside_value)
    pat_set_pool_name_entry = tk.Entry(pat_pub_ip_frame, textvariable=pat_set_pool_name_value)
    pat_pool_from_entry = tk.Entry(pat_pub_ip_frame, textvariable=pat_pool_from_value)
    pat_pool_to_entry = tk.Entry(pat_pub_ip_frame, textvariable=pat_pool_to_value)
    pat_pool_prefixLength_entry = tk.Entry(pat_pub_ip_frame, textvariable=pat_pool_prefixLength_value)
    pat_source_list_entry = tk.Entry(pat_Apply_frame, textvariable=pat_source_list_value)
    # pat_pool_name_entry = tk.Entry(pat_Apply_frame, textvariable=pat_pool_name_value)

    pat_int_inside_entry.grid(row=2, column=1, padx=20, pady=10)
    pat_int_outside_entry.grid(row=2, column=2, padx=20, pady=10)
    pat_set_pool_name_entry.grid(row=5, column=1, padx=20, pady=10)
    pat_pool_from_entry.grid(row=5, column=2, padx=20, pady=10)
    pat_pool_to_entry.grid(row=5, column=3, padx=20, pady=10)
    pat_pool_prefixLength_entry.grid(row=5, column=4, padx=20, pady=10)
    pat_source_list_entry.grid(row=6, column=2, padx=20, pady=10)
    # pat_pool_name_entry.grid(row=7, column=2, padx=20, pady=10)

    #Button
    pat_run_button = tk.Button(pat_frame, text="Execute", width=12, command=lambda: pat_config(pat_int_inside_value.get(),  pat_int_outside_value.get(),  pat_set_pool_name_value.get(),  pat_pool_from_value.get(),  pat_pool_to_value.get(),  pat_pool_prefixLength_value.get(),  pat_source_list_value.get(),  interface_info))
    pat_run_button.pack(padx=20, pady=10)