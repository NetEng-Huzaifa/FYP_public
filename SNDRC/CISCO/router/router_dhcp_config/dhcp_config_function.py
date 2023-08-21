from tkinter import messagebox as mgbx
from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
from CISCO.router.helper import get_subnetmask, ip_checking, prefix_checking


def dhcpServerDisable_config(dhcpServerDisable_pool_name_value):
    if dhcpServerDisable_pool_name_value:
        dhcp_off = f"no ip dhcp pool {dhcpServerDisable_pool_name_value}"
        # print(dhcp_off)
        conn.add_commands(dhcp_off)
    else:
        mgbx.showinfo("Error", "Pool name is required")
def dhcpServer_config(dhcpServer_pool_name_value, dhcpServer_pool_ip_value, dhcpServer_pool_prefixLength_value, dhcpServer_exclude_from_value, dhcpServer_exclude_to_value, dhcpServer_gateway_value):
    if dhcpServer_pool_name_value and dhcpServer_pool_ip_value and dhcpServer_pool_prefixLength_value and dhcpServer_exclude_from_value and dhcpServer_exclude_to_value and dhcpServer_gateway_value:
        # if ip_checking(dhcpServer_pool_ip_value) == ip_checking(dhcpServer_exclude_from_value) == ip_checking(dhcpServer_exclude_to_value) == ip_checking(dhcpServer_gateway_value) == "IP_Pass":
        if prefix_checking(dhcpServer_pool_prefixLength_value) == "Pass":
            dhcp_on = [f"ip dhcp excluded-address {dhcpServer_exclude_from_value} {dhcpServer_exclude_to_value}",
                       f"ip dhcp pool {dhcpServer_pool_name_value}",
                       f"network {dhcpServer_pool_ip_value} {get_subnetmask(dhcpServer_pool_prefixLength_value)}",
                       f"default-router {dhcpServer_gateway_value}",
                       f"exit",
                       f"service dhcp"]
            # print(dhcp_on)
            conn.add_commands(dhcp_on)
    else:
        mgbx.showinfo("Error", "All fields are required")
def dhcpClient_config(dhcpClient_interface_value):
    if dhcpClient_interface_value:
        dhcpClient_on = [f"interface {dhcpClient_interface_value}",
                         f"ip address dhcp"]
        # print(dhcpClient_on)
        conn.add_commands(dhcpClient_on)
    else:
        mgbx.showinfo("Error", "Please select the interface")
