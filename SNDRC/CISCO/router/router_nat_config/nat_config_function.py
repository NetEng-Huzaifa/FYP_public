from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
from tkinter import messagebox as mgbx
from CISCO.router.helper import ip_checking, get_subnetmask

def snat_config(snat_int_inside_value, snat_int_outside_value, snat_public_ip_value, snat_private_ip_value, interface_info):
    if snat_int_inside_value and snat_int_outside_value and snat_public_ip_value and snat_private_ip_value:
        if (snat_int_inside_value != snat_int_outside_value) and (snat_int_inside_value in interface_info) and (snat_int_outside_value in interface_info):
            if ip_checking(snat_public_ip_value) == "IP_Pass":
                if ip_checking(snat_private_ip_value) == "IP_Pass":
                    conn.add_commands([f"interface {snat_int_inside_value}",
                                       f"ip nat inside",
                                       f"exit",
                                       f"interface {snat_int_outside_value}",
                                       f"ip nat outside",
                                       f"exit",
                                       f"ip nat inside source static {snat_private_ip_value} {snat_public_ip_value}"])
                else:
                    mgbx.showinfo("Error", "Please check your private IP")
            else:
                mgbx.showinfo("Error", "Please check your public IP")
        else:
            mgbx.showinfo("Error", "Inside and outside interfaces must same. And Selected from the given options")
    else:
        mgbx.showinfo("Error", "For Static NAT all fields are required")


def dnat_config(dnat_int_inside_value, dnat_int_outside_value, dnat_set_pool_name_value, dnat_pool_from_value, dnat_pool_to_value, dnat_pool_prefixLength_value, dnat_source_list_value, interface_info):
    if dnat_int_inside_value and dnat_int_outside_value and dnat_set_pool_name_value and dnat_pool_from_value and dnat_pool_to_value and dnat_pool_prefixLength_value and dnat_source_list_value:
        if (dnat_int_inside_value != dnat_int_outside_value) and (dnat_int_inside_value in interface_info) and (dnat_int_outside_value in interface_info):
            if 0 < int(dnat_pool_prefixLength_value) < 31:
                if ip_checking(dnat_pool_from_value) == "IP_Pass":
                    if ip_checking(dnat_pool_to_value) == "IP_Pass":
                        conn.add_commands([f"interface {dnat_int_inside_value}",
                                           f"ip nat inside",
                                           f"exit",
                                           f"interface {dnat_int_outside_value}",
                                           f"ip nat outside",
                                           f"exit",
                                           f"ip nat pool {dnat_set_pool_name_value} {dnat_pool_from_value} {dnat_pool_to_value} netmask {get_subnetmask(dnat_pool_prefixLength_value)}",
                                           f"ip nat inside source list {dnat_source_list_value} pool {dnat_set_pool_name_value}"])
                    else:
                        mgbx.showinfo("Error", "Please check IP provided in \"TO\" field")
                else:
                    mgbx.showinfo("Error", "Please check IP provided in \"From\" field")
            else:
                mgbx.showinfo("Error", "Please check Prefix length field. It must be in range of 1-30")
        else:
            mgbx.showinfo("Error", "Inside and outside interfaces must same. And Selected from the given options")
    else:
        mgbx.showinfo("Error", "For Dynamic NAT all fields are required")


def pat_config(pat_int_inside_value, pat_int_outside_value, pat_set_pool_name_value, pat_pool_from_value, pat_pool_to_value, pat_pool_prefixLength_value, pat_source_list_value, interface_info):
    if pat_int_inside_value and pat_int_outside_value and pat_set_pool_name_value and pat_pool_from_value and pat_pool_to_value and pat_pool_prefixLength_value and pat_source_list_value:
        if (pat_int_inside_value != pat_int_outside_value) and (pat_int_inside_value in interface_info) and (pat_int_outside_value in interface_info):
            if 0 < int(pat_pool_prefixLength_value) < 31:
                if ip_checking(pat_pool_from_value) == "IP_Pass":
                    if ip_checking(pat_pool_to_value) == "IP_Pass":
                        conn.add_commands([f"interface {pat_int_inside_value}",
                                           f"ip nat inside",
                                           f"exit",
                                           f"interface {pat_int_outside_value}",
                                           f"ip nat outside",
                                           f"exit",
                                           f"ip nat pool {pat_set_pool_name_value} {pat_pool_from_value} {pat_pool_to_value} netmask {get_subnetmask(pat_pool_prefixLength_value)}",
                                           f"ip nat inside source list {pat_source_list_value} pool {pat_set_pool_name_value} overload"])
                    else:
                        mgbx.showinfo("Error", "Please check IP provided in \"TO\" field")
                else:
                    mgbx.showinfo("Error", "Please check IP provided in \"From\" field")
            else:
                mgbx.showinfo("Error", "Please check Prefix length field. It must be in range of 1-30")
        else:
            mgbx.showinfo("Error", "Inside and outside interfaces must same. And Selected from the given options")
    else:
        mgbx.showinfo("Error", "For PAT all fields are required")