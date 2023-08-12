from tkinter import ttk
from CISCO.router.router_main_frames import *
from .dynamic_routing_config_functions import *

def dynamic_routing():
    notebook = ttk.Notebook(right_main_frame)
    notebook.pack(expand=True, anchor=tk.N, fill=tk.X)
    # create frames
    rip_main_frame = tk.Frame(notebook)
    eigrp_main_frame = tk.Frame(notebook)
    ospf_main_frame = tk.Frame(notebook)

    rip_main_frame.pack(fill='both', expand=True)
    eigrp_main_frame.pack(fill='both', expand=True)
    ospf_main_frame.pack(fill='both', expand=True)

    # add frames to notebook
    notebook.add(rip_main_frame, text='RIP')
    notebook.add(eigrp_main_frame, text='EIGRP')
    notebook.add(ospf_main_frame, text='OSPF')



    # =============================RIP Config Section================================
    # ===========> RIP parent section
    rip_frame = tk.LabelFrame(rip_main_frame, text="Routing Information Protocol (RIP)")
    rip_frame.pack(fill=tk.X, padx=20, pady=15)

    # Entries Section
    rip_ver_2_value = tk.StringVar()
    rip_ver_2_value.set("0")
    rip_dir_con_int_value = tk.StringVar()
    rip_dir_con_int_value.set("0")
    rip_dir_con_lopbak_int_value = tk.StringVar()
    rip_dir_con_lopbak_int_value.set("0")

    rip_ver_2_entry = tk.Checkbutton(rip_frame, text='Version 2', variable=rip_ver_2_value, onvalue=1, offvalue=0)
    rip_dir_con_int_entry = tk.Checkbutton(rip_frame, text='Advertise Directly connected Interfaces', variable=rip_dir_con_int_value, onvalue=1, offvalue=0)
    rip_dir_con_lopbak_int_entry = tk.Checkbutton(rip_frame, text='Advertise Directly connected and loopback Interfaces(Preferred)', variable=rip_dir_con_lopbak_int_value, onvalue=1, offvalue=0)

    rip_ver_2_entry.grid(row=1, column=1, sticky=tk.W, padx=20, pady=5)
    rip_dir_con_int_entry.grid(row=2, column=1, sticky=tk.W, padx=20, pady=5)
    rip_dir_con_lopbak_int_entry.grid(row=3, column=1, sticky=tk.W, padx=20, pady=5)

    # ===========> RIP Add Network Manually section
    rip_ANM_frame = tk.LabelFrame(rip_frame, text="Add Network Manually")
    rip_ANM_frame.grid(row=4, column=1, sticky=tk.EW, padx=20, pady=10)

    # label+checkbox section
    rip_add_net_label_value = tk.StringVar()
    rip_add_net_label_value.set("0")
    rip_add_net_label = tk.Checkbutton(rip_ANM_frame, text="Network Address", variable=rip_add_net_label_value, onvalue=1, offvalue=0)
    rip_add_net_label.grid(row=1, column=1, padx=20, pady=10)

    #entry section
    rip_add_net_value = tk.StringVar()
    rip_add_net_entry = tk.Entry(rip_ANM_frame, textvariable=rip_add_net_value)
    rip_add_net_entry.grid(row=1, column=2, padx=20, pady=10)

    #button section
    rip_add_net_button = tk.Button(rip_ANM_frame, text="Add", width=12, command=lambda: rip_add_net_config(rip_add_net_label_value.get(), rip_add_net_value.get()))
    rip_add_net_button.grid(row=1, column=3, padx=20, pady=10, sticky=tk.E)

    rip_run_button = tk.Button(rip_frame, text="Execute", width=12, command=lambda: rip_run_config(rip_ver_2_value.get(), rip_dir_con_int_value.get(), rip_dir_con_lopbak_int_value.get(), rip_add_net_label_value.get(), rip_add_net_value.get()))
    rip_run_button.grid(row=5, column=1, padx=40, pady=10, sticky=tk.E)



    # =============================EIGRP Config Section================================
    # ===========> EIGRP parent section
    eigrp_frame = tk.LabelFrame(eigrp_main_frame, text="Enhanced Interior Gateway Routing Protocol (EIGRP)")
    eigrp_frame.pack(fill=tk.X, padx=20, pady=15)

    # label section
    eigrp_asn_label = tk.Label(eigrp_frame, text="Autonomous System Number (1-65535)")
    eigrp_asn_label.grid(row=0, column=1, sticky=tk.W, padx=20, pady=5)


    # Entries Section
    eigrp_asn_value = tk.StringVar()
    eigrp_dir_con_int_value = tk.StringVar()
    eigrp_dir_con_int_value.set("0")
    eigrp_dir_con_lopbak_int_value = tk.StringVar()
    eigrp_dir_con_lopbak_int_value.set("0")

    eigrp_asn_entry = tk.Entry(eigrp_frame, textvariable=eigrp_asn_value, width=37)
    eigrp_dir_con_int_entry = tk.Checkbutton(eigrp_frame, text='Advertise Directly connected Interfaces', variable=eigrp_dir_con_int_value, onvalue=1, offvalue=0)
    eigrp_dir_con_lopbak_int_entry = tk.Checkbutton(eigrp_frame, text='Advertise Directly connected and loopback Interfaces(Preferred)', variable=eigrp_dir_con_lopbak_int_value, onvalue=1, offvalue=0)

    eigrp_asn_entry.grid(row=1, column=1, sticky=tk.W, padx=20, pady=5)
    eigrp_dir_con_int_entry.grid(row=2, column=1, sticky=tk.W, padx=20, pady=5)
    eigrp_dir_con_lopbak_int_entry.grid(row=3, column=1, sticky=tk.W, padx=20, pady=5)

    # ===========> eigrp Add Network Manually section
    eigrp_ANM_frame = tk.LabelFrame(eigrp_frame, text="Add Network Manually")
    eigrp_ANM_frame.grid(row=4, column=1, sticky=tk.EW, padx=20, pady=10)

    # label+checkbox section
    eigrp_add_net_label_value = tk.StringVar()
    eigrp_add_net_label_value.set("0")
    eigrp_add_net_label = tk.Checkbutton(eigrp_ANM_frame, text="Network Address", variable=eigrp_add_net_label_value, onvalue=1, offvalue=0)
    eigrp_wcm_label = tk.Label(eigrp_ANM_frame, text="Wildcard Mask ")

    eigrp_add_net_label.grid(row=1, column=1, padx=20, pady=10)
    eigrp_wcm_label.grid(row=2, column=1, padx=20, pady=5)
    #entry section

    eigrp_wcm_value = tk.StringVar()
    eigrp_add_net_value = tk.StringVar()
    eigrp_add_net_entry = tk.Entry(eigrp_ANM_frame, textvariable=eigrp_add_net_value)
    eigrp_wcm_entry = tk.Entry(eigrp_ANM_frame, textvariable=eigrp_wcm_value)
    eigrp_add_net_entry.grid(row=1, column=2, padx=20, pady=10)
    eigrp_wcm_entry.grid(row=2, column=2, padx=20, pady=10)

    #button section
    eigrp_add_net_button = tk.Button(eigrp_ANM_frame, text="Add", width=12, command=lambda: eigrp_add_net_config(eigrp_add_net_label_value.get(), eigrp_add_net_value.get(), eigrp_wcm_value.get()))
    eigrp_add_net_button.grid(row=2, column=3, padx=20, pady=10, sticky=tk.E)

    eigrp_run_button = tk.Button(eigrp_frame, text="Execute", width=12, command=lambda: eigrp_run_config(eigrp_asn_value.get(), eigrp_dir_con_int_value.get(), eigrp_dir_con_lopbak_int_value.get(), eigrp_add_net_label_value.get()))
    eigrp_run_button.grid(row=5, column=1, padx=40, pady=10, sticky=tk.E)



# =============================OSPF Config Section================================
    # ===========> OSPF parent section
    ospf_frame = tk.LabelFrame(ospf_main_frame, text="Open Shortest Path First (OSPF)")
    ospf_frame.pack(fill=tk.X, padx=20, pady=15)

    #Label
    ospf_pid_label = tk.Label(ospf_frame, text="Process ID (1-65535)")
    ospf_area_label = tk.Label(ospf_frame, text="Area (0-4294967295)")

    ospf_pid_label.grid(row=1, column=1, sticky=tk.W, padx=20, pady=5)
    ospf_area_label.grid(row=3, column=1, sticky=tk.W, padx=20, pady=5)


    # Entries Section
    ospf_pid_value = tk.StringVar()
    ospf_area_value = tk.StringVar()
    ospf_dir_con_int_value = tk.StringVar()
    ospf_dir_con_int_value.set("0")
    ospf_dir_con_lopbak_int_value = tk.StringVar()
    ospf_dir_con_lopbak_int_value.set("0")

    ospf_pid_entry = tk.Entry(ospf_frame, textvariable=ospf_pid_value, width=37)
    ospf_area_entry = tk.Entry(ospf_frame, textvariable=ospf_area_value, width=37)
    ospf_dir_con_int_entry = tk.Checkbutton(ospf_frame, text='Advertise Directly connected Interfaces', variable=ospf_dir_con_int_value, onvalue=1, offvalue=0)
    ospf_dir_con_lopbak_int_entry = tk.Checkbutton(ospf_frame, text='Advertise Directly connected and loopback Interfaces(Preferred)', variable=ospf_dir_con_lopbak_int_value, onvalue=1, offvalue=0)

    ospf_pid_entry.grid(row=2, column=1, sticky=tk.W, padx=20)
    ospf_area_entry.grid(row=4, column=1, sticky=tk.W, padx=20)
    ospf_dir_con_int_entry.grid(row=5, column=1, sticky=tk.W, padx=20, pady=5)
    ospf_dir_con_lopbak_int_entry.grid(row=6, column=1, sticky=tk.W, padx=20, pady=5)

    # ===========> ospf Add Network Manually section
    ospf_ANM_frame = tk.LabelFrame(ospf_frame, text="Add Network Manually")
    ospf_ANM_frame.grid(row=7, column=1, sticky=tk.EW, padx=20, pady=10)

    # label+checkbox section
    ospf_add_net_label_value = tk.StringVar()
    ospf_add_net_label_value.set("0")
    ospf_add_net_label = tk.Checkbutton(ospf_ANM_frame, text="Network Address", variable=ospf_add_net_label_value, onvalue=1, offvalue=0)
    ospf_wcm_label = tk.Label(ospf_ANM_frame, text="Wildcard Mask ")

    ospf_add_net_label.grid(row=1, column=1, padx=20, pady=10)
    ospf_wcm_label.grid(row=2, column=1, padx=20, pady=5)

    #entry section
    ospf_add_net_value = tk.StringVar()
    ospf_wcm_value = tk.StringVar()

    ospf_add_net_entry = tk.Entry(ospf_ANM_frame, textvariable=ospf_add_net_value)
    ospf_wcm_entry = tk.Entry(ospf_ANM_frame, textvariable=ospf_wcm_value)

    ospf_add_net_entry.grid(row=1, column=2, padx=20, pady=10)
    ospf_wcm_entry.grid(row=2, column=2, padx=20, pady=10)


    #button section
    ospf_add_net_button = tk.Button(ospf_ANM_frame, text="Add", width=12, command=lambda: ospf_add_net_config(ospf_area_value.get(), ospf_add_net_label_value.get(), ospf_add_net_value.get(), ospf_wcm_value.get()))
    ospf_add_net_button.grid(row=2, column=3, padx=20, pady=10, sticky=tk.E)

    ospf_run_button = tk.Button(ospf_frame, text="Execute", width=12, command=lambda: ospf_run_config(ospf_pid_value.get(), ospf_area_value.get(), ospf_dir_con_int_value.get(), ospf_dir_con_lopbak_int_value.get(), ospf_add_net_label_value.get()))
    ospf_run_button.grid(row=8, column=1, padx=40, pady=10, sticky=tk.E)

