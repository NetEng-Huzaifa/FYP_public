from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
from tkinter import messagebox as mgbx

def vlan_config(vlan_number_value, vlan_state_value, vlan_name_value):
    vlan_commands_list = []
    def state_name_config():
        if vlan_state_value == "UP":
            vlan_commands_list.append("no shutdown")
        elif vlan_state_value == "Shutdown":
            vlan_commands_list.append("shutdown")
        else:
            pass
        if vlan_name_value != "":
            vlan_commands_list.append(f"name {vlan_name_value}")
        else:
            pass
    if vlan_number_value != "":
        if str(vlan_number_value).isnumeric():
            if int(vlan_number_value) >= 1 and int(vlan_number_value) <= 1001:
                vlan_commands_list.append(f"vlan {vlan_number_value}")
                state_name_config()
            elif int(vlan_number_value) >= 1002 and int(vlan_number_value) <= 1005:
                mgbx.showinfo("Error", "1002 to 1005 are reserved. Don't consider them")
            elif int(vlan_number_value) >= 1006 and int(vlan_number_value) <= 4094:
                mgbx.showinfo("Caution", "Please select VTP mode as transparent otherwise it will not working properly")
                vlan_commands_list.append(f"vlan {vlan_number_value}")
                state_name_config()
            else:
                mgbx.showinfo("Error", "Please select value within a given range")
        else:
            mgbx.showinfo("Error", "Please select numeric value within a given range")

        # print(vlan_commands_list)
        conn.add_commands(vlan_commands_list)
    else:
        mgbx.showinfo("Error", "Please select value within a given range")


