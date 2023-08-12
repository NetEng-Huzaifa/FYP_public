from tkinter import messagebox as mgbx
from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
from CISCO.router.helper import ip_checking
import re

rip_run_commands = ["router rip"]
eigrp_run_commands = []
ospf_run_commands = []
network_add = []

def rip_add_net_config(rip_add_net_label_value, rip_add_net_value):
    if rip_add_net_label_value == "1":
        if ip_checking(rip_add_net_value) == "IP_Pass":
            if f"network {rip_add_net_value}" not in network_add:
                network_add.append(f"network {rip_add_net_value}")
            else:
                mgbx.showinfo("Info", "Given Address already Exists!")
    elif rip_add_net_value and rip_add_net_label_value == "0":
        mgbx.showinfo("Error", "Please Mark check on Network Address to add network Addresses")

def rip_run_config(rip_ver_2_value, rip_dir_con_int_value, rip_dir_con_lopbak_int_value, rip_add_net_label_value, rip_add_net_value):
    rip_run_commands.clear()
    if rip_dir_con_int_value == rip_dir_con_lopbak_int_value == rip_add_net_label_value == "0":
        mgbx.showinfo("Error", "Please select a desired option to Advertise Routes in RIP")
    else:
        if f"router rip" not in rip_run_commands:
            rip_run_commands.clear()
            rip_run_commands.insert(0, f"router rip")


    if rip_ver_2_value == "1":
        if "version 2" not in rip_run_commands:
            rip_run_commands[1:1] = ["version 2", "no auto-summary"]
    else:
        if "version 2" in rip_run_commands:
            item_to_remove = ["version 2", "no auto-summary"]
            for item in item_to_remove:
                rip_run_commands.remove(item)

    if rip_add_net_label_value == "0":
        if rip_dir_con_int_value == "1" and rip_dir_con_lopbak_int_value == "1":
            mgbx.showinfo("Error", "You cannot select both 2nd and 3rd option at the same time.")
        elif rip_dir_con_int_value == "1":
            lines = re.findall(r".*\d*.\d*.\d*.\d*/32 is directly connected.*", conn.get_info_from_router("sh ip route"), re.MULTILINE)
            data_without_spaces = '\n'.join([line for line in lines if "Loopback" not in line]).replace(" ", "")
            ip = re.findall(r"\d*\.\d*\.\d*\.\d*", data_without_spaces, re.MULTILINE)
            for line in ip:
                network_ip_addresses = 'network ' + line
                if network_ip_addresses not in rip_run_commands:
                    rip_run_commands.append(network_ip_addresses)
            conn.add_commands(rip_run_commands)
            network_add.clear()
        elif rip_dir_con_lopbak_int_value == "1":
            lines = re.findall(r"^L\d*.\d*.\d*.\d*.*isdirectlyconnected", conn.get_info_from_router("sh ip route").replace(" ", ""), re.MULTILINE)
            for line in lines:
                ip = re.findall(r"\d*\.\d*\.\d*\.\d*", line, re.MULTILINE)
                network_ip_addresses = 'network ' + str(ip).strip("[]'")
                if network_ip_addresses not in rip_run_commands:
                    rip_run_commands.append(network_ip_addresses)
            conn.add_commands(rip_run_commands)
            network_add.clear()
    else:
        if rip_dir_con_int_value == "1" or rip_dir_con_lopbak_int_value == "1":
            mgbx.showinfo("Error", "Please uncheck on Network Address manually to use Auto add functionality")
        elif rip_add_net_label_value == "1":
            if network_add:
                for address in network_add:
                    if address not in rip_run_commands:
                        rip_run_commands.append(address)
                conn.add_commands(rip_run_commands)
                network_add.clear()
            else:
                mgbx.showinfo("Error", "Please enter addresses first to add manually")




def eigrp_add_net_config(eigrp_add_net_label_value, eigrp_add_net_value, eigrp_wcm_value):
    if eigrp_add_net_label_value == "1":
        if eigrp_wcm_value and eigrp_add_net_value:
            if ip_checking(eigrp_add_net_value) == "IP_Pass":
                if f"network {eigrp_add_net_value} {eigrp_wcm_value}" not in network_add:
                    network_add.append(f"network {eigrp_add_net_value} {eigrp_wcm_value}")
                else:
                    mgbx.showinfo("Info", "Given Address already Exists!")
        else:
            mgbx.showinfo("Error", "Network Address and WildCardMask must not empty")
    elif (eigrp_add_net_value or eigrp_wcm_value) and eigrp_add_net_label_value == "0":
        mgbx.showinfo("Error", "Please Mark check on Network Address to add network Addresses")

def eigrp_run_config(eigrp_asn_value, eigrp_dir_con_int_value, eigrp_dir_con_lopbak_int_value, eigrp_add_net_label_value):
    eigrp_run_commands.clear()
    if eigrp_asn_value:
        if eigrp_dir_con_int_value == eigrp_dir_con_lopbak_int_value == eigrp_add_net_label_value == "0":
            mgbx.showinfo("Error", "Please select a desired option to Advertise Routes in EIGRP")
        else:
            if f"router eigrp {eigrp_asn_value}" not in eigrp_run_commands:
                eigrp_run_commands.clear()
                eigrp_run_commands.insert(0, f"router eigrp {eigrp_asn_value}")

            if eigrp_add_net_label_value == "0":
                if eigrp_dir_con_int_value == eigrp_dir_con_lopbak_int_value == "1":
                    mgbx.showinfo("Error", "You can select only one check at a time")
                elif eigrp_dir_con_int_value == "1":
                    lines = re.findall(r".*\d*.\d*.\d*.\d*/32 is directly connected.*", conn.get_info_from_router("sh ip route"), re.MULTILINE)
                    data_without_spaces = '\n'.join([line for line in lines if "Loopback" not in line]).replace(" ", "")
                    ip = re.findall(r"\d*\.\d*\.\d*\.\d*", data_without_spaces, re.MULTILINE)
                    for line in ip:
                        network_ip_addresses = 'network ' + line + ' 0.0.0.0'
                        if network_ip_addresses not in eigrp_run_commands:
                            eigrp_run_commands.append(network_ip_addresses)
                    conn.add_commands(eigrp_run_commands)
                    network_add.clear()
                elif eigrp_dir_con_lopbak_int_value == "1":
                    lines = re.findall(r"^L\d*.\d*.\d*.\d*.*isdirectlyconnected", conn.get_info_from_router("sh ip route").replace(" ", ""), re.MULTILINE)
                    for line in lines:
                        ip = re.findall(r"\d*\.\d*\.\d*\.\d*", line, re.MULTILINE)
                        network_ip_addresses = 'network ' + str(ip).strip("[]'") + ' 0.0.0.0'
                        if network_ip_addresses not in eigrp_run_commands:
                            eigrp_run_commands.append(network_ip_addresses)
                    conn.add_commands(eigrp_run_commands)
                    network_add.clear()
            else:
                if eigrp_dir_con_int_value == "1" or eigrp_dir_con_lopbak_int_value == "1":
                    mgbx.showinfo("Error", "Please uncheck on Network Address manually to use Auto add functionality")
                elif eigrp_add_net_label_value == "1":
                    if network_add:
                        for address in network_add:
                            if address not in eigrp_run_commands:
                                eigrp_run_commands.append(address)
                        conn.add_commands(eigrp_run_commands)
                        network_add.clear()
                    else:
                        mgbx.showinfo("Error", "Please enter addresses first to add manually")
    else:
        mgbx.showinfo("Error", "ASN is required")



def ospf_add_net_config(ospf_area_value, ospf_add_net_label_value, ospf_add_net_value, ospf_wcm_value):
    if ospf_add_net_label_value == "1":
        if ospf_wcm_value and ospf_add_net_value:
            if ip_checking(ospf_add_net_value) == "IP_Pass":
                if f"network {ospf_add_net_value} {ospf_wcm_value} area {ospf_area_value}" not in network_add:
                    network_add.append(f"network {ospf_add_net_value} {ospf_wcm_value} area {ospf_area_value}")
                    # print(network_add)
                else:
                    mgbx.showinfo("Info", "Given Address already Exists!")
        else:
            mgbx.showinfo("Error", "Network Address and WildCardMask must not empty")
    elif (ospf_add_net_value or ospf_wcm_value) and ospf_add_net_label_value == "0":
        mgbx.showinfo("Error", "Please Mark check on Network Address to add network Addresses")
    else:
        mgbx.showinfo("Error", "First check on Network Address to ADD")


def ospf_run_config(ospf_pid_value, ospf_area_value, ospf_dir_con_int_value, ospf_dir_con_lopbak_int_value, ospf_add_net_label_value):
    ospf_run_commands.clear()
    if ospf_pid_value and ospf_area_value:
        if ospf_dir_con_int_value == ospf_dir_con_lopbak_int_value == ospf_add_net_label_value == "0":
            mgbx.showinfo("Error", "Please select a desired option to Advertise Routes in OSPF")
        else:
            if f"router ospf {ospf_pid_value}" not in ospf_run_commands:
                ospf_run_commands.clear()
                ospf_run_commands.insert(0, f"router ospf {ospf_pid_value}")

            if ospf_add_net_label_value == "0":
                if ospf_dir_con_int_value == ospf_dir_con_lopbak_int_value == "1":
                    mgbx.showinfo("Error", "You can select only one check at a time")
                elif ospf_dir_con_int_value == "1":
                    lines = re.findall(r".*\d*.\d*.\d*.\d*/32 is directly connected.*", conn.get_info_from_router("sh ip route"), re.MULTILINE)
                    data_without_spaces = '\n'.join([line for line in lines if "Loopback" not in line]).replace(" ", "")
                    ip = re.findall(r"\d*\.\d*\.\d*\.\d*", data_without_spaces, re.MULTILINE)
                    for line in ip:
                        network_ip_addresses = 'network ' + line + f' 0.0.0.0 area {ospf_area_value}'
                        if network_ip_addresses not in ospf_run_commands:
                            ospf_run_commands.append(network_ip_addresses)
                    conn.add_commands(ospf_run_commands)
                    network_add.clear()
                elif ospf_dir_con_lopbak_int_value == "1":
                    lines = re.findall(r"^L\d*.\d*.\d*.\d*.*isdirectlyconnected", conn.get_info_from_router("sh ip route").replace(" ", ""), re.MULTILINE)
                    for line in lines:
                        ip = re.findall(r"\d*\.\d*\.\d*\.\d*", line, re.MULTILINE)
                        network_ip_addresses = 'network ' + str(ip).strip("[]'") + f' 0.0.0.0 area {ospf_area_value}'
                        if network_ip_addresses not in ospf_run_commands:
                            ospf_run_commands.append(network_ip_addresses)
                    conn.add_commands(ospf_run_commands)
                    network_add.clear()
            else:
                if ospf_dir_con_int_value == "1" or ospf_dir_con_lopbak_int_value == "1":
                    mgbx.showinfo("Error", "Please uncheck on Network Address manually to use Auto add functionality")
                elif ospf_add_net_label_value == "1":
                    if network_add:
                        for address in network_add:
                            if address not in ospf_run_commands:
                                ospf_run_commands.append(address)
                        conn.add_commands(ospf_run_commands)
                        network_add.clear()
                    else:
                        mgbx.showinfo("Error", "Please enter addresses first to add manually")
    else:
        mgbx.showinfo("Error", "ProcessID and Area is required")