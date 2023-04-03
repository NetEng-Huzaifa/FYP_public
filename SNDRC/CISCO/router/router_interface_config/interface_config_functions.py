from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
from tkinter import messagebox as mgbx

def interface_config(interface_value, interface_state_value, interface_duplex_value, interface_description_value, interface_keepalive_value):
    interface_command_list = []
    if interface_value != "":
        interface_command_list.append(f"interface {interface_value}")
        # state section
        if interface_state_value == "UP":
            interface_command_list.append("no shutdown")
        elif interface_state_value == "Shutdown":
            interface_command_list.append("shutdown")
        elif interface_state_value == "":
            pass
        else:
            mgbx.showinfo("Error", "Please select correct value")
        # duplex section
        if interface_duplex_value == "Half":
            interface_command_list.append("duplex half")
        elif interface_duplex_value == "Full":
            interface_command_list.append("duplex full")
        elif interface_duplex_value == "Auto":
            interface_command_list.append("duplex auto")
        elif interface_duplex_value == "":
            pass
        else:
            mgbx.showinfo("Error", "Please select correct value")
        # description section
        if interface_description_value == "":
            pass
        else:
            interface_command_list.append(f"description {interface_description_value}")
        # keepalive section
        if interface_keepalive_value == "":
            pass
        elif interface_keepalive_value != "":
            if str(interface_keepalive_value).isnumeric():
                if int(interface_keepalive_value) >= 0 and int(interface_keepalive_value) <= 32767:
                    interface_command_list.append(f"keepalive {interface_keepalive_value}")
                else:
                    mgbx.showinfo("Error", "Please select the value between the given range")
            else:
                mgbx.showinfo("Error", "Please select numeric value")

        print(interface_command_list)
        conn.add_commands(interface_command_list)
    else:
        mgbx.showinfo("Error", "Please select the interface first")

def serial_interface_config(interface_serial_value, interface_serial_encapsulation_value, interface_serial_clockRate_value):
    interface_serial_command_list = []
    if interface_serial_value != "":
        interface_serial_command_list.append(f"interface {interface_serial_value}")
        # encapsulation section
        if interface_serial_encapsulation_value == "HDLC":
            interface_serial_command_list.append("encapsulation hdlc")
        elif interface_serial_encapsulation_value == "PPP":
            interface_serial_command_list.append("encapsulation ppp")
        elif interface_serial_encapsulation_value == "":
            pass
        else:
            mgbx.showinfo("Error", "Please select correct value")
        # clockrate section
        if interface_serial_clockRate_value == "":
            pass
        elif interface_serial_clockRate_value != "":
            if str(interface_serial_clockRate_value).isnumeric():
                if int(interface_serial_clockRate_value) >= 1200 and int(interface_serial_clockRate_value) <= 2015232:
                    interface_serial_command_list.append(f"clock rate {interface_serial_clockRate_value}")
                else:
                    mgbx.showinfo("Error", "Please select the value between the given range")
            else:
                mgbx.showinfo("Error", "Please select numeric value")

        print(interface_serial_command_list)
        conn.add_commands(interface_serial_command_list)
    else:
        mgbx.showinfo("Error", "Please select the interface first")
def default_interface_config(defaultInterface_value):
    conn.add_commands(f"default interface {defaultInterface_value}")

def loopbackinterface_config(loopbackInterface_number_value):
    if loopbackInterface_number_value != "":
        if str(loopbackInterface_number_value).isnumeric():
            if int(loopbackInterface_number_value) >= 0 and int(loopbackInterface_number_value) <= 2147483647:
                conn.add_commands(f"interface loopback {loopbackInterface_number_value}")
            else:
                mgbx.showinfo("Error", "Please select the value between the given range")
        else:
            mgbx.showinfo("Error", "Please select numeric value")
    else:
        mgbx.showinfo("Error", "Please select the interface first")

def subinterface_config(subInterface_value, subInterface_number_value, subInterface_vlan_value):
    conn.add_commands([f"interface {subInterface_value}.{subInterface_number_value}",f"encapsulation dot {subInterface_vlan_value}"])

def sv_interface_config(sv_interface_number_value):
    conn.add_commands(f"interface vlan {sv_interface_number_value}")



