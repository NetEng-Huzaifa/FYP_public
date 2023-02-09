# from tkinter import messagebox as mgbx
from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
from CISCO.router.subnetmask_selection import get_subnetmask


def dhcpServerDisable_config(dhcpServerDisable_pool_name_value):
    dhcp_off = f"no ip dhcp pool {dhcpServerDisable_pool_name_value}"
    print(dhcp_off)
def dhcpServer_config(dhcpServer_pool_name_value, dhcpServer_pool_ip_value, dhcpServer_pool_prefixLength_value, dhcpServer_exclude_from_value, dhcpServer_exclude_to_value, dhcpServer_gateway_value):
    dhcp_on = [f"ip dhcp excluded-address {dhcpServer_exclude_from_value} {dhcpServer_exclude_to_value}",
               f"ip dhcp pool {dhcpServer_pool_name_value}",
               f"network {dhcpServer_pool_ip_value} {get_subnetmask(dhcpServer_pool_prefixLength_value)}",
               f"default-router {dhcpServer_gateway_value}",
               f"exit"]
    print(dhcp_on)
    conn.add_commands(dhcp_on)
