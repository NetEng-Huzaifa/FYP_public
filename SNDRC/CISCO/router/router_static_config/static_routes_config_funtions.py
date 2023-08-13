from tkinter import messagebox as mgbx
from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
from CISCO.router.helper import get_subnetmask, ip_checking, prefix_checking

def staticRoute_config(static_network_value, static_prefixLength_value, static_gateway_value):
    if static_network_value and static_prefixLength_value and static_gateway_value:
        if (ip_checking(static_network_value) == ip_checking(static_gateway_value) == "IP_Pass") and prefix_checking(static_prefixLength_value) == "Pass":
            conn.add_commands([f"ip route {static_network_value} {get_subnetmask(static_prefixLength_value)} {static_gateway_value}"])
    else:
        mgbx.showinfo("Error", " ALL Fields are Required")
def staticDefault_config(static_default_gateway_value):
    if static_default_gateway_value:
        if ip_checking(static_default_gateway_value) == "IP_Pass":
            staticDefault = [f"ip route 0.0.0.0 0.0.0.0 {static_default_gateway_value}"]
            # print(staticDefault)
            conn.add_commands(staticDefault)
    else:
        mgbx.showinfo("Error", "Field is Required")
