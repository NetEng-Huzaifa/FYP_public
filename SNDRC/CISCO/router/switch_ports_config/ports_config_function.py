from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
from tkinter import messagebox as mgbx


def access_config(ports_interface_value, ports_mode_value, access_ports_type_value, access_ports_vlan_value):
    if access_ports_type_value != "" and access_ports_vlan_value != "":
        if access_ports_type_value == "data":
            access_cmd_list = [f"int {ports_interface_value}", f"switchport mode {ports_mode_value}", f"switchport access vlan {access_ports_vlan_value}"]
        elif access_ports_type_value == "voice":
            access_cmd_list = [f"int {ports_interface_value}", f"switchport mode {ports_mode_value}", f"switchport {access_ports_type_value} vlan {access_ports_vlan_value}"]
        else:
            mgbx.showinfo("Error", "Please select correct type of Traffic")
        print(access_cmd_list)
        conn.add_commands(access_cmd_list)
    else:
        mgbx.showinfo("Error", "Please Fill all fields")

