from tkinter import ttk
from CISCO.router.router_main_frames import *
from CISCO.router.get_info_from_device import interface_info
from .acl_config_functions import *

def acl():
    notebook = ttk.Notebook(right_main_frame)
    notebook.pack(expand=True, anchor=tk.N, fill=tk.X)
    # create frames
    acl_standard_main_frame = tk.Frame(notebook)
    # acl_extended_main_frame = tk.Frame(notebook)

    acl_standard_main_frame.pack(fill='both', expand=True)
    # acl_extended_main_frame.pack(fill='both', expand=True)

    # add frames to notebook
    notebook.add(acl_standard_main_frame, text='ACL')
    # notebook.add(acl_extended_main_frame, text='Extended ACL')

    # =============================ACL Standard Config Section================================
    # ===========>Standard ACL define section
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
    acl_standard_permit_other_button = tk.Button(acl_standard_frame, text="Permit Remaining", width=12,
                                               command=lambda: acl_standard_permit_other_config(aclStandard_number_entry.get()))
    acl_standard_deny_other_button = tk.Button(acl_standard_frame, text="Deny Remaining", width=12,
                                               command=lambda: acl_standard_deny_other_config(aclStandard_number_entry.get()))
    acl_standard_define_run_button = tk.Button(acl_standard_frame, text="Execute", width=12,
                                               command=lambda: acl_standard_define_config(aclStandard_number_entry.get(), aclStandard_action_value.get(), aclStandard_host_value.get(), aclStandard_WCM_value.get()))

    acl_standard_permit_other_button.grid(row=5, column=1, padx=20, pady=10)
    acl_standard_deny_other_button.grid(row=5, column=2, padx=20, pady=10, sticky=tk.E)
    acl_standard_define_run_button.grid(row=5, column=4, padx=20, pady=10, sticky=tk.E)


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
    acl_standard_apply_run_button = tk.Button(acl_standard_apply_frame, text="Execute", width=12, command=lambda: acl_standard_apply_config(aclStandard_apply_interface_value.get(), aclStandard_apply_accessgroup_value.get(), aclStandard_apply_action_value.get()))

    acl_standard_apply_run_button.grid(row=5, column=3, padx=20, pady=10, sticky=tk.E)



    # # =============================ACL Extended Config Section================================
    # # ===========> Extended ACL define section
    # acl_extended_frame = tk.LabelFrame(acl_extended_main_frame, text="Define Access Control List")
    # acl_extended_frame.pack(fill=tk.X, padx=20, pady=15)
    # # label section
    # aclExtended_number_label = tk.Label(acl_extended_frame, text="ACL number(100-199)")
    # aclExtended_action_label = tk.Label(acl_extended_frame, text="ACL action")
    # aclExtended_protocol_label = tk.Label(acl_extended_frame, text="Protocol")
    # aclExtended_srcAdd_label = tk.Label(acl_extended_frame, text="Src IP/network")
    # aclExtended_srcWCM_label = tk.Label(acl_extended_frame, text="Src WildCard Mask")
    # aclExtended_dstAdd_label = tk.Label(acl_extended_frame, text="Dst IP/network")
    # aclExtended_dstWCM_label = tk.Label(acl_extended_frame, text="Dst WildCard Mask")
    #
    # aclExtended_number_label.grid(row=1, column=1)
    # aclExtended_action_label.grid(row=1, column=2)
    # aclExtended_protocol_label.grid(row=1, column=3)
    # aclExtended_srcAdd_label.grid(row=1, column=4)
    # aclExtended_srcWCM_label.grid(row=1, column=5)
    # aclExtended_dstAdd_label.grid(row=3, column=1)
    # aclExtended_dstWCM_label.grid(row=3, column=2)
    #
    # # Entries Section
    # aclExtended_number_value = tk.StringVar()
    # aclExtended_action_value = tk.StringVar()
    # aclExtended_protocol_value = tk.StringVar()
    # aclExtended_srcAdd_value = tk.StringVar()
    # aclExtended_srcWCM_value = tk.StringVar()
    # aclExtended_dstAdd_value = tk.StringVar()
    # aclExtended_dstWCM_value = tk.StringVar()
    #
    # aclExtended_number_entry = tk.Entry(acl_extended_frame, textvariable = aclExtended_number_value)
    # aclExtended_action_entry = ttk.Combobox(acl_extended_frame, values = ["deny", "permit"], textvariable = aclExtended_action_value)
    # aclExtended_protocol_entry = ttk.Combobox(acl_extended_frame, values = ['eigrp', 'icmp', 'igmp', 'ip', 'ospf', 'tcp', 'udp'], textvariable = aclExtended_protocol_value)
    # aclExtended_srcAdd_entry = tk.Entry(acl_extended_frame, textvariable = aclExtended_srcAdd_value)
    # aclExtended_srcWCM_entry = tk.Entry(acl_extended_frame, textvariable = aclExtended_srcWCM_value)
    # aclExtended_dstAdd_entry = tk.Entry(acl_extended_frame, textvariable=aclExtended_dstAdd_value)
    # aclExtended_dstWCM_entry = tk.Entry(acl_extended_frame, textvariable=aclExtended_dstWCM_value)
    #
    # aclExtended_number_entry.grid(row=2, column=1, padx=20, pady=10)
    # aclExtended_action_entry.grid(row=2, column=2, padx=20, pady=10)
    # aclExtended_protocol_entry.grid(row=2, column=3, padx=20, pady=10)
    # aclExtended_srcAdd_entry.grid(row=2, column=4, padx=10, pady=10)
    # aclExtended_srcWCM_entry.grid(row=2, column=5, padx=10, pady=10)
    # aclExtended_dstAdd_entry.grid(row=4, column=1, padx=10, pady=10)
    # aclExtended_dstWCM_entry.grid(row=4, column=2, padx=10, pady=10)
    #
    # # Buttons Section
    # acl_extended_permit_other_button = tk.Button(acl_extended_frame, text="Permit Remaining", width=12,
    #                                            command=lambda: acl_standard_permit_other_config(aclExtended_number_entry.get()))
    # acl_extended_deny_other_button = tk.Button(acl_extended_frame, text="Deny Remaining", width=12,
    #                                            command=lambda: acl_standard_deny_other_config(aclExtended_number_entry.get()))
    # acl_extended_define_run_button = tk.Button(acl_extended_frame, text="Execute", width=12,
    #                                            command=lambda: acl_standard_define_config(aclExtended_number_entry.get(), aclStandard_action_value.get(), aclStandard_host_value.get(), aclStandard_WCM_value.get()))
    #
    # acl_extended_permit_other_button.grid(row=5, column=1, padx=20, pady=10)
    # acl_extended_deny_other_button.grid(row=5, column=2, padx=20, pady=10, sticky=tk.E)
    # acl_extended_define_run_button.grid(row=5, column=4, padx=20, pady=10, sticky=tk.E)


    # ===========> ACL extended apply section
    # acl_extended_apply_frame = tk.LabelFrame(acl_extended_main_frame, text="Apply Access Control List")
    # acl_extended_apply_frame.pack(fill=tk.X, padx=20, pady=15)
    # # label section
    # aclExtended_apply_interface_label = tk.Label(acl_extended_apply_frame, text="Interface")
    # aclExtended_apply_accessgroup_label = tk.Label(acl_extended_apply_frame, text="Access_group No.")
    # aclExtended_apply_action_label = tk.Label(acl_extended_apply_frame, text="ACL action")
    #
    # aclExtended_apply_interface_label.grid(row=1, column=1)
    # aclExtended_apply_accessgroup_label.grid(row=1, column=2)
    # aclExtended_apply_action_label.grid(row=1, column=3)
    #
    # # Entries Section
    # aclExtended_apply_interface_value = tk.StringVar()
    # aclExtended_apply_accessgroup_value = tk.StringVar()
    # aclExtended_apply_action_value = tk.StringVar()
    #
    # aclExtended_apply_interface_entry = ttk.Combobox(acl_extended_apply_frame, values = interface_info, textvariable = aclExtended_apply_interface_value)
    # aclExtended_apply_accessgroup_entry = tk.Entry(acl_extended_apply_frame, textvariable = aclExtended_apply_accessgroup_value)
    # aclExtended_apply_action_entry = ttk.Combobox(acl_extended_apply_frame, values = ["inbound", "outbound"], textvariable = aclExtended_apply_action_value)
    #
    # aclExtended_apply_interface_entry.grid(row=2, column=1, padx=20, pady=10)
    # aclExtended_apply_accessgroup_entry.grid(row=2, column=2, padx=20, pady=10)
    # aclExtended_apply_action_entry.grid(row=2, column=3, padx=20, pady=10)
    #
    # # Buttons Section
    # acl_extended_apply_run_button = tk.Button(acl_extended_apply_frame, text="Execute", width=12, command=lambda: acl_extended_apply_config(aclExtended_apply_interface_value.get(), aclExtended_apply_accessgroup_value.get(), aclExtended_apply_action_value.get()))
    #
    # acl_extended_apply_run_button.grid(row=5, column=3, padx=20, pady=10, sticky=tk.E)


