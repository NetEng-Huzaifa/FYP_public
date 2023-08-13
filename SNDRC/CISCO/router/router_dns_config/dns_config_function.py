from tkinter import messagebox as mgbx
from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
from CISCO.router.helper import ip_checking


def dns_service_off():
    conn.add_commands("no ip domain lookup")
    mgbx.showinfo("Success", "DNS Services disabled")

dns_list = ["ip domain lookup", "ip dns server"]
def dnsServer_add_config(dnsServer_pool_name_value, dnsServer_pool_ip_value):
    if dnsServer_pool_name_value and dnsServer_pool_ip_value:
        if ip_checking(dnsServer_pool_ip_value) == "IP_Pass":
            if f"ip host {dnsServer_pool_name_value} {dnsServer_pool_ip_value}" not in dns_list:
                dns_list.append(f"ip host {dnsServer_pool_name_value} {dnsServer_pool_ip_value}")
            else:
                mgbx.showinfo("Error", "Entry already exists!")
    else:
        mgbx.showinfo("Error", "Both fields are Required")

def dnsServer_run_config():
    if len(dns_list) == 2:
        mgbx.showinfo("Error", "Add the entry to run DNS")
    else:
        # print(dns_list)
        conn.add_commands(dns_list)
        mgbx.showinfo("Success", "DNS Services Enabled Successfully!")


def dnsClient_config(dnsClient_ServerIP_primary_value, dnsClient_ServerIP_secondary_value):
    dns_client_list = ["ip domain lookup"]
    if dnsClient_ServerIP_primary_value != "" and dnsClient_ServerIP_secondary_value != "":
        dns_client_list.append(f"ip name-server {dnsClient_ServerIP_primary_value} {dnsClient_ServerIP_secondary_value}")
        # print(dns_client_list)
        conn.add_commands(dns_client_list)
        mgbx.showinfo("Success", f"Executed Successfully!")
    elif dnsClient_ServerIP_primary_value == "" and dnsClient_ServerIP_secondary_value == "":
        mgbx.showinfo("Error!", "Atleast primary field is Required")
    elif dnsClient_ServerIP_primary_value != "" and dnsClient_ServerIP_secondary_value == "":
        dns_client_list.append(f"ip name-server {dnsClient_ServerIP_primary_value}")
        # print(dns_client_list)
        conn.add_commands(dns_client_list)
        mgbx.showinfo("Success", f"Executed Successfully!")
    elif dnsClient_ServerIP_primary_value == "" and dnsClient_ServerIP_secondary_value != "":
        mgbx.showinfo("Error!", "Primary field is Required")



