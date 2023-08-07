from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
from tkinter import messagebox as mgbx


def access_config(ports_interface_value, ports_mode_value, access_ports_type_value, access_ports_vlan_value):
    if access_ports_type_value and access_ports_vlan_value:
        if access_ports_type_value in ["data", "voice"]:
            conn.add_commands([f"int {ports_interface_value}", f"switchport mode {ports_mode_value}", f"switchport access vlan {access_ports_vlan_value}"])
        elif access_ports_type_value in "voice":
            conn.add_commands([f"int {ports_interface_value}", f"switchport mode {ports_mode_value}", f"switchport {access_ports_type_value} vlan {access_ports_vlan_value}"])
        else:
            mgbx.showinfo("Error", "Please select correct type of Traffic")
    else:
        mgbx.showinfo("Error", "Please Fill all fields")


def trunk_config(ports_interface_value , ports_mode_value, trunk_ports_allowed_vlan_value, trunk_ports_allowed_vlan_add_entry, current_vlans):
    trunk_config_commands = [f"int {ports_interface_value}", "switchport trunk encapsulation dot1q", f"switchport mode {ports_mode_value}"]

    if trunk_ports_allowed_vlan_value and trunk_ports_allowed_vlan_add_entry:
        mgbx.showinfo("Error", "Please select one of them at a time")
    elif trunk_ports_allowed_vlan_value or trunk_ports_allowed_vlan_add_entry:
        if trunk_ports_allowed_vlan_add_entry:
            total_vlan = set(current_vlans)
            trunk_ports_allowed_vlan_add_entry_set = set(trunk_ports_allowed_vlan_add_entry.split(","))
            trunk_ports_allowed_vlan_add_entry = ','.join(trunk_ports_allowed_vlan_add_entry_set)
            is_subset = set(trunk_ports_allowed_vlan_add_entry_set).issubset(total_vlan)
            if is_subset:
                trunk_config_commands.append(f"switchport trunk allowed vlan add {trunk_ports_allowed_vlan_add_entry}")
                conn.add_commands(trunk_config_commands)
            else:
                mgbx.showinfo("Error", "All Selected VLANs must be created on switch")
        else:
            trunk_config_commands.append(f"switchport trunk allowed vlan {trunk_ports_allowed_vlan_value}")
            conn.add_commands(trunk_config_commands)
    else:
        conn.add_commands(trunk_config_commands)


def dynamic_config(ports_interface_value, ports_mode_value, dynamic_ports_np_value):
    if dynamic_ports_np_value:
        if dynamic_ports_np_value in ["desirable", "auto"]:
            # print([f"int {ports_interface_value}", f"switchport mode {ports_mode_value} {dynamic_ports_np_value}"])
            conn.add_commands([f"int {ports_interface_value}", f"switchport mode {ports_mode_value} {dynamic_ports_np_value}"])
        else:
            mgbx.showinfo("Error", "Please select correct negotiation parameter")
    else:
        mgbx.showinfo("Error", "Please Fill all fields")

