from tkinter import ttk
from CISCO.router.router_main_frames import *
from CISCO.router.get_info_from_device import interface_info

def acl():
    notebook = ttk.Notebook(right_main_frame)
    notebook.pack(expand=True, anchor=tk.N, fill=tk.X)
    # create frames
    acl_standard_main_frame = tk.Frame(notebook)
    acl_extended_main_frame = tk.Frame(notebook)

    acl_standard_main_frame.pack(fill='both', expand=True)
    acl_extended_main_frame.pack(fill='both', expand=True)

    # add frames to notebook
    notebook.add(acl_standard_main_frame, text='Standard ACL')
    notebook.add(acl_extended_main_frame, text='Extended ACL')

    # =============================ACL Standard Config Section================================
    # ===========> ACL define section
    acl_standard_frame = tk.LabelFrame(acl_standard_main_frame, text="Define Access Control List")
    acl_standard_frame.pack(fill=tk.X, padx=20, pady=15)
    # label section
    aclStandard_number_label = tk.Label(acl_standard_frame, text="ACL number(1-99)")
    aclStandard_action_label = tk.Label(acl_standard_frame, text="ACL action")
    aclStandard_host_label = tk.Label(acl_standard_frame, text="host IP/network")
    aclStandard_WCM_label = tk.Label(acl_standard_frame, text="WildCard Mask")

    aclStandard_number_label.grid(row=1, column=1)
    aclStandard_action_label.grid(row=1, column=2)
    aclStandard_host_label.grid(row=1, column=3)
    aclStandard_WCM_label.grid(row=1, column=4)

    # Entries Section
    aclStandard_number_value = tk.StringVar()
    aclStandard_action_value = tk.StringVar()
    aclStandard_host_value = tk.StringVar()
    aclStandard_WCM_value = tk.StringVar()

    aclStandard_number_entry = tk.Entry(acl_standard_frame, textvariable = aclStandard_number_value)
    aclStandard_action_entry = ttk.Combobox(acl_standard_frame, values = ["deny", "permit"], textvariable = aclStandard_action_value)
    aclStandard_host_entry = tk.Entry(acl_standard_frame, textvariable = aclStandard_host_value)
    aclStandard_WCM_entry = tk.Entry(acl_standard_frame, textvariable = aclStandard_WCM_value)

    aclStandard_number_entry.grid(row=2, column=1, padx=20, pady=10)
    aclStandard_action_entry.grid(row=2, column=2, padx=20, pady=10)
    aclStandard_host_entry.grid(row=2, column=3, padx=10, pady=10)
    aclStandard_WCM_entry.grid(row=2, column=4, padx=10, pady=10)

    # Buttons Section
    acl_standard_define_run_button = tk.Button(acl_standard_frame, text="Execute", width=12, command=lambda: interface_config(hostname_value))

    acl_standard_define_run_button.grid(row=5, column=3, padx=20, pady=10, sticky=tk.E)


    # ===========> ACL apply section
    acl_standard_apply_frame = tk.LabelFrame(acl_standard_main_frame, text="Apply Access Control List")
    acl_standard_apply_frame.pack(fill=tk.X, padx=20, pady=15)
    # label section
    aclStandard_apply_interface_label = tk.Label(acl_standard_apply_frame, text="Interface")
    aclStandard_apply_accessgroup_label = tk.Label(acl_standard_apply_frame, text="Access_group No.")
    aclStandard_apply_action_label = tk.Label(acl_standard_apply_frame, text="ACL action")

    aclStandard_apply_interface_label.grid(row=1, column=1)
    aclStandard_apply_accessgroup_label.grid(row=1, column=2)
    aclStandard_apply_action_label.grid(row=1, column=3)

    # Entries Section
    aclStandard_apply_interface_value = tk.StringVar()
    aclStandard_apply_accessgroup_value = tk.StringVar()
    aclStandard_apply_action_value = tk.StringVar()

    aclStandard_apply_interface_entry = ttk.Combobox(acl_standard_apply_frame, values = interface_info, textvariable = aclStandard_apply_interface_value)
    aclStandard_apply_accessgroup_entry = tk.Entry(acl_standard_apply_frame, textvariable = aclStandard_apply_accessgroup_value)
    aclStandard_apply_action_entry = ttk.Combobox(acl_standard_apply_frame, values = ["inbound", "outbound"], textvariable = aclStandard_apply_action_value)

    aclStandard_apply_interface_entry.grid(row=2, column=1, padx=20, pady=10)
    aclStandard_apply_accessgroup_entry.grid(row=2, column=2, padx=20, pady=10)
    aclStandard_apply_action_entry.grid(row=2, column=3, padx=20, pady=10)

    # Buttons Section
    acl_standard_apply_run_button = tk.Button(acl_standard_apply_frame, text="Execute", width=12, command=lambda: interface_config(hostname_value))

    acl_standard_apply_run_button.grid(row=5, column=3, padx=20, pady=10, sticky=tk.E)


