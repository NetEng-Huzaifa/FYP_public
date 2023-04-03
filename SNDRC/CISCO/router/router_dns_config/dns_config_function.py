from tkinter import messagebox as mgbx
from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
# from CISCO.router.subnetmask_selection import get_subnetmask


def dns_service_off():
    conn.add_commands("no ip domain lookup")

dns_list = ["ip domain lookup", "ip dns server"]
def dnsServer_add_config(dnsServer_pool_name_value, dnsServer_pool_ip_value):
    if dnsServer_pool_name_value and dnsServer_pool_ip_value != "":
        dns_list.append(f"ip host {dnsServer_pool_name_value} {dnsServer_pool_ip_value}")
    else:
        mgbx.showinfo("Error!", "Both fields are Required")
def dnsServer_run_config():
    print(dns_list)
    conn.add_commands(dns_list)



def dnsClient_config(dnsClient_ServerIP_primary_value, dnsClient_ServerIP_secondary_value):
    dns_client_list = ["ip domain lookup"]
    if dnsClient_ServerIP_primary_value != "" and dnsClient_ServerIP_secondary_value != "":
        dns_client_list.append(f"ip name-server {dnsClient_ServerIP_primary_value} {dnsClient_ServerIP_secondary_value}")
        print(dns_client_list)
        conn.add_commands(dns_client_list)
    elif dnsClient_ServerIP_primary_value == "" and dnsClient_ServerIP_secondary_value == "":
        mgbx.showinfo("Error!", "Atleast primary field is Required")
    elif dnsClient_ServerIP_primary_value != "" and dnsClient_ServerIP_secondary_value == "":
        dns_client_list.append(f"ip name-server {dnsClient_ServerIP_primary_value}")
        print(dns_client_list)
        conn.add_commands(dns_client_list)
    elif dnsClient_ServerIP_primary_value == "" and dnsClient_ServerIP_secondary_value != "":
        mgbx.showinfo("Error!", "Primary field is Required")



