from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
from tkinter import messagebox as mgbx

def vtp_config(vtp_name_value, vtp_mode_value, vtp_pruning_value):
    if vtp_name_value and vtp_mode_value:
        vtp_commands_list = []
        vtp_commands_list.append(f"vtp domain {vtp_name_value}")
        if vtp_mode_value == "client" or vtp_mode_value == "server" or vtp_mode_value == "transparent":
            vtp_commands_list.append(f"vtp mode {vtp_mode_value}")
        else:
            mgbx.showinfo("Error", "Please select given mode")

        if vtp_pruning_value != "":
            if vtp_pruning_value == "enable" and vtp_mode_value == "server":
                vtp_commands_list.append("vtp pruning")
            elif vtp_pruning_value == "enable" and (vtp_mode_value == "client" or vtp_mode_value == "transparent"):
                mgbx.showinfo("Error", "Cannot modify pruning unless in VTP server mode")
            elif vtp_pruning_value == "disable" or vtp_pruning_value == "":
                pass
            else:
                mgbx.showinfo("Error", "Please select correct VTP-pruning value")

        # print(vtp_commands_list)
        conn.add_commands(vtp_commands_list)
    else:
        mgbx.showinfo("Error", "VTP domain-name & mode must not be empty!")