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
def default_interface_config(defaultInterface_value):
    conn.add_commands(f"default interface {defaultInterface_value}")