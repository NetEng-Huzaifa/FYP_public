from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
import re

interface_info = re.findall(r"^[A-Za-z].+?[\d/.]+", conn.get_info_from_router("sh ip int br"), re.MULTILINE)
# interface_info = ["fa0/1", "e3/0"]

vlan_info = re.findall(r"^[\d]+", conn.get_info_from_router("sh vlan br"), re.MULTILINE)
# vlan_info = [1, 3, 5, 6]