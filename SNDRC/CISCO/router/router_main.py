from CISCO.router.router_basic_config.basic_config_main import *
from CISCO.router.router_interface_config.interface_config_main import *
from CISCO.router.router_ip_address_config.ip_address_main import *
from CISCO.router.router_dhcp_config.dhcp_config_main import *
from CISCO.router.router_dns_config.dns_config_main import *
from CISCO.router.router_static_config.static_routes_config_main import *
from CISCO.router.router_dynamic_config.dynamic_routing_config_main import *
from CISCO.router.router_acl_config.acl_config_main import *
from CISCO.router.switch_vlan_config.vlan_config_main import *
from CISCO.router.switch_vtp_config.vtp_config_main import *
from CISCO.router.switch_ports_config.ports_config_main import *


def hide_indicate():
    basic_config_button.config(bg="#d5d5d5", fg="black")
    interface_config_button.config(bg="#d5d5d5", fg="black")
    ipAddress_config_button.config(bg="#d5d5d5", fg="black")
    dhcp_config_button.config(bg="#d5d5d5", fg="black")
    dns_config_button.config(bg="#d5d5d5", fg="black")
    static_routing_config_button.config(bg="#d5d5d5", fg="black")
    dynamic_routing_config_button.config(bg="#d5d5d5", fg="black")
    acl_config_button.config(bg="#d5d5d5", fg="black")
    vlan_config_button.config(bg="#d5d5d5", fg="black")
    vtp_config_button.config(bg="#d5d5d5", fg="black")
    ports_config_button.config(bg="#d5d5d5", fg="black")


def delete_pages():
    for frame in right_main_frame.winfo_children():
        frame.destroy()
def indicate(button, page):
    hide_indicate()
    button.config(bg="#373737", fg="#d5d5d5")
    delete_pages()
    page()


basic_config_button = tk.Button(left_button_frame, text="Basic Config", font= ("Arial", 12), bg="#d5d5d5", width=13, command=lambda:indicate(basic_config_button, basicConfig))
basic_config_button.grid()
interface_config_button = tk.Button(left_button_frame, text="Interfaces", font= ("Arial", 12), bg="#d5d5d5", width=13, command=lambda:indicate(interface_config_button, interface))
interface_config_button.grid()
ipAddress_config_button = tk.Button(left_button_frame, text="IP address", font= ("Arial", 12), bg="#d5d5d5", width=13, command=lambda:indicate(ipAddress_config_button, ip_address))
ipAddress_config_button.grid()
dhcp_config_button = tk.Button(left_button_frame, text="DHCP", font= ("Arial", 12), bg="#d5d5d5", width=13, command=lambda:indicate(dhcp_config_button, dhcp))
dhcp_config_button.grid()
dns_config_button = tk.Button(left_button_frame, text="DNS", font= ("Arial", 12), bg="#d5d5d5", width=13, command=lambda:indicate(dns_config_button, dns))
dns_config_button.grid()
static_routing_config_button = tk.Button(left_button_frame, text="Static Route", font=("Arial", 12), bg="#d5d5d5", width=13, command=lambda: indicate(static_routing_config_button, static_routing))
static_routing_config_button.grid()
dynamic_routing_config_button = tk.Button(left_button_frame, text="Routing Protocol", font=("Arial", 12), bg="#d5d5d5", width=13, command=lambda: indicate(dynamic_routing_config_button, dynamic_routing))
dynamic_routing_config_button.grid()
acl_config_button = tk.Button(left_button_frame, text="ACL", font=("Arial", 12), bg="#d5d5d5", width=13, command=lambda: indicate(acl_config_button, acl))
acl_config_button.grid()
vlan_config_button = tk.Button(left_button_frame, text="VLAN", font=("Arial", 12), bg="#d5d5d5", width=13, command=lambda: indicate(vlan_config_button, vlan))
vlan_config_button.grid()
vtp_config_button = tk.Button(left_button_frame, text="VTP", font=("Arial", 12), bg="#d5d5d5", width=13, command=lambda: indicate(vtp_config_button, vtp))
vtp_config_button.grid()
ports_config_button = tk.Button(left_button_frame, text="Ports", font=("Arial", 12), bg="#d5d5d5", width=13, command=lambda: indicate(ports_config_button, ports))
ports_config_button.grid()



indicate(basic_config_button, basicConfig)
router_root.mainloop()





