import tkinter.messagebox as mgbx

def ip_checking(user_ip):
    result = []
    user_ip = user_ip.split(".")
    if len(user_ip) == 4:  # check no. of octats of IP
        # if int(user_ip[3]) == 0:  # check last octat of IP
        #     # for Network address
        #     mgbx.showinfo("Caution", "It is a Network address")
        # else:
        for octat in user_ip:  # loop each octat of IP
            if octat.isnumeric():  # check octat not contain any invalid syntax
                if int(octat) >= 0 and int(octat) <= 255:  # check each octat validity
                    result.append("True")
                else:
                    mgbx.showinfo("Selection", f"Error! {octat} is not a valid octat")
                    break  # break the loop in case of issue
            else:
                mgbx.showinfo("Selection", "Entered IPv4 Address is not valid")
                break
    else:
        mgbx.showinfo("Wrong Input", f"""Please Check your entered IPv4 Address\nno. of Valid Octat of IPv4 is 4 but you entered {len(user_ip)}""")

    if len(result) == 4:
        if result[0] and result[1] and result[2] and result[3] == "True":
            return "IP_Pass"
    else:
        return "IP_Fail"



def get_subnetmask(userValue):
    subnet_mask = {"1": "128.0.0.0", "2": "192.0.0.0", "3": "224.0.0.0", "4": "240.0.0.0", "5": "248.0.0.0",
                   "6": "252.0.0.0", "7": "254.0.0.0", "8": "255.0.0.0", "9": "255.128.0.0", "10": "255.192.0.0",
                   "11": "255.224.0.0", "12": "255.240.0.0", "13": "255.248.0.0", "14": "255.252.0.0",
                   "15": "255.254.0.0", "16": "255.255.0.0", "17": "255.255.128.0", "18": "255.255.192.0",
                   "19": "255.255.224.0", "20": "255.255.240.0", "21": "255.255.248.0", "22": "255.255.252.0",
                   "23": "255.255.254.0", "24": "255.255.255.0", "25": "255.255.255.128", "26": "255.255.255.192",
                   "27": "255.255.255.224", "28": "255.255.255.240", "29": "255.255.255.248", "30": "255.255.255.252",
                   "31": "255.255.255.254", "32": "255.255.255.255"}
    return subnet_mask[userValue]


def prefix_checking(user_prefix):
    if 0 < int(user_prefix) <= 32:
        return "Pass"
    else:
        mgbx.showinfo("Error", "Prefix length must be in the 1-32 range")