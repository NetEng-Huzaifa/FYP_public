from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
from tkinter import messagebox as mgbx
from CISCO.router.subnetmask_selection import get_subnetmask as gsm

def ipAddress_config(ip_interface_value, ipAddress_value, ip_prefixLength_value, ip_priority_value):
    ipAddress_command_list = []
    if ip_interface_value != "":
        ipAddress_command_list.append(f"interface {ip_interface_value}")
        ipAddress_command_list.append(f"no switchport")
        # ipAddress and prefix length section
        if ipAddress_value != "":
            if ip_prefixLength_value != "":
                if int(ip_prefixLength_value) > 0 and int(ip_prefixLength_value) < 33:
                    # priority section
                    if ip_priority_value == "" or ip_priority_value == "primary":
                        var = f"ip address {ipAddress_value} {gsm(ip_prefixLength_value)}"
                        ipAddress_command_list.append(var)
                    elif ip_priority_value == "Secondary":
                        var = f"ip address {ipAddress_value} {gsm(ip_prefixLength_value)} Secondary"
                        ipAddress_command_list.append(var)
                    else:
                        mgbx.showinfo("Error", "Please select correct value")
                else:
                    mgbx.showinfo("Error", "Please select the prefix length from 1 to 32")
            else:
                mgbx.showinfo("Error", "Please select the prefix length")
        else:
            mgbx.showinfo("Error", "Please Enter an IP address")

        print(ipAddress_command_list)
        conn.add_commands(ipAddress_command_list)
    else:
        mgbx.showinfo("Error", "Please select the interface first")
