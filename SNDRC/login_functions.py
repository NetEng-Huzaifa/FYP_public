import subprocess
import tkinter.messagebox as mgbx
# from login_main import root
from telnetlib import Telnet

def ip_checking(user_ip):
    result = []
    user_ip = user_ip.split(".")
    # print(user_ip)
    if len(user_ip) == 4:  # check no. of octats of IP
        if int(user_ip[3]) == 0:  # check last octat of IP
            # for Network address
            mgbx.showinfo("Caution", "It is a Network address")
        else:
            for octat in user_ip:  # loop each octat of IP
                if octat.isnumeric():  # check octat not contain any invalid syntax
                    if int(octat) >= 0 and int(octat) <= 255:  # check each octat validity
                        result.append("True")
                    else:
                        mgbx.showinfo("Selection", f"Error! {octat} is not a valid octat")
                        break  # break down the loop in case of issue
                else:
                    mgbx.showinfo("Selection", "Entered IPv4 Address is not valid")
                    break
    else:
        mgbx.showinfo("Wrong Input", f"""Please Check your entered IPv4 Address\nno. of Valid Octat of IPv4 is 4 but you entered {len(user_ip)}""")
    if result[0] and result[1] and result[2] and result[3] == "True":
    # if result[:] == "True":
        return "IP_Pass"
    else:
        return "IP_Fail"

def selection_device(vendor, device):
    if vendor == "Cisco":
        if device == "Router":
            return f"{vendor} {device}"
        elif device == "Switch":
            return f"{vendor} {device}"
        else:
            mgbx.showinfo("Selection", f"Please select {vendor} device")
    elif vendor == "Huawei":
        if device == "Router":
            return f"{vendor} {device}"
        elif device == "Switch":
            return f"{vendor} {device}"
        else:
            mgbx.showinfo("Selection", f"Please select given {vendor} device")
    else:
        mgbx.showinfo("Selection", f"Please select given other {vendor} devices")

def pre_telnet_device(ip, user, pwd):
    try:
        telnet = Telnet(ip, timeout=5)
        # telnet.open(ip)

        telnet.read_until(b'sername')
        # print(telnet.read_until(b'sername').decode())
        telnet.write(user.encode('ascii') + b'\n')

        telnet.read_until(b'assword')
        telnet.write(pwd.encode('ascii') + b'\n')

        telnet.read_until(b'>', timeout=5)
        telnet.write(b'exit\n')
        return "Successful"
    except Exception as e:
        mgbx.showinfo("Access Denied", f"{e}")

def Add_button_press():
    pass


