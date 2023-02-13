# from tkinter import messagebox as mgbx
from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
from CISCO.router.subnetmask_selection import get_subnetmask

def staticRoute_config(static_network_value, static_prefixLength_value, static_gateway_value):
    static = [f"ip route {static_network_value} {get_subnetmask(static_prefixLength_value)} {static_gateway_value}"]
    print(static)
    conn.add_commands(static)
def staticDefault_config(static_default_gateway_value):
    staticDefault = [f"ip route 0.0.0.0 0.0.0.0 {static_default_gateway_value}"]
    print(staticDefault)
    conn.add_commands(staticDefault)
