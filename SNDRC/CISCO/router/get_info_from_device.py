from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
import re

interface_info = re.findall(r"^[A-Za-z].+?[\d/.]+", conn.get_info_from_router("sh ip int br"), re.MULTILINE)