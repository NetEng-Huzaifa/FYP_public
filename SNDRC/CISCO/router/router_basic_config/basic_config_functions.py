from tkinter import messagebox as mgbx
from CISCO.router.access_cisco_router.access_cisco_router_ssh import *

# ==============================System Section===============================
def hostname_config(hostname_value):
    if hostname_value:
        hostname = f"hostname {hostname_value}"
        # print(hostname)
        conn.add_commands(hostname)
        exit()
    else:
        mgbx.showinfo("Error", "All fields are required")
def enablePass_config(enablePass_value, enablePass_type_value):
    def runCmds_enablePass(type_value):
        enable_password = f"enable {type_value} {enablePass_value}"
        # print(enable_password)
        conn.add_commands(enable_password)

    if enablePass_value and enablePass_type_value:
        if enablePass_type_value == "Plain text":
            type_value = "password"
            runCmds_enablePass(type_value)
        elif enablePass_type_value == "Cipher":
            type_value = "secret"
            runCmds_enablePass(type_value)
        else:
            mgbx.showinfo("Error", "Please select \"Cipher\" or \"Plain text\"")
    else:
        mgbx.showinfo("Error", "Both fields are required")


def motd_config(motd_value):
    if motd_value:
        motd = f"banner motd %{motd_value.get()}%"
        # print(motd)
        conn.add_commands(motd)
    else:
        mgbx.showinfo("Error", "It is a required field")


def clockSet_config(clock_hour_value, clock_min_value, clock_sec_value, clock_date_value, clock_month_value, clock_year_value):
    def clockSet_run_config(clock_hour_value, clock_min_value, clock_sec_value, clock_date_value, clock_month_value, clock_year_value):
        clockSet_cmd = f"clock set {clock_hour_value}:{clock_min_value}:{clock_sec_value} {clock_date_value} {clock_month_value} {clock_year_value}"
        # print(clockSet_cmd)
        conn.clock_cmd(clockSet_cmd)
    def clock_month_name(clock_month_value):
        months = {"1":"Jan", "2":"Feb", "3":"Mar", "4":"Apr", "5":"May", "6":"Jun", "7":"July", "8":"Aug", "9":"Sep", "10":"Oct", "11":"Nov", "12":"Dec", }
        return months[clock_month_value]

    def clockset_range_checking(clock_hour_value, clock_min_value, clock_sec_value, clock_date_value, clock_month_value, clock_year_value):
        # print(clock_hour_value, clock_min_value, clock_sec_value, clock_date_value, clock_month_value, clock_year_value)
        if int(clock_hour_value) < 25 and int(clock_hour_value) >= 1:
            if int(clock_min_value) <= 60 and int(clock_min_value) >=1:
                if int(clock_sec_value) <= 60 and int(clock_sec_value) >= 1:
                    if int(clock_date_value) <= 31 and int(clock_date_value) >= 1:
                        if int(clock_month_value) <= 12 and int(clock_month_value) >= 1:
                            if len(clock_year_value) == 4:
                                clockSet_run_config(clock_hour_value, clock_min_value, clock_sec_value, clock_date_value, clock_month_name(clock_month_value), clock_year_value)
                            else:
                                mgbx.showinfo("ClockSet Error!", "Please! Enter correct Year i.e 2023")
                        else:
                            mgbx.showinfo("ClockSet Error!", "Please! Enter correct Month in the range 1-12")
                    else:
                        mgbx.showinfo("ClockSet Error!", "Please! Enter correct Date in the range 1-31")
                else:
                    mgbx.showinfo("ClockSet Error!", "Please! Enter correct Second in the range 1-60")
            else:
                mgbx.showinfo("ClockSet Error!", "Please! Enter correct Minute in the range 1-60")
        else:
            mgbx.showinfo("ClockSet Error!", "Please! Enter correct hour in the range 1-24")
    def clockset_numeric_checking():
        userValue_list = [clock_hour_value, clock_min_value, clock_sec_value, clock_date_value, clock_month_value, clock_year_value]
        list_result = []
        for items in userValue_list:
            if items.isnumeric():
                list_result.append(items)
            elif items == "":
                mgbx.showinfo("ClockSet Error!", "please fill all the fields")
                break
            else:
                mgbx.showinfo("ClockSet Error!", f"please! replace \"{items}\" with correct numeric value ")
                break
        if len(list_result) == 6:
            clockset_range_checking(clock_hour_value, clock_min_value, clock_sec_value, clock_date_value, clock_month_value, clock_year_value)


    clockset_numeric_checking()

# ==============================User Section===============================

def user_add_config(new_name_value, password_value, type_value, privilige_value):
    def runCmds_usernameAdd(after_type_value, new_privilige_value):
        add_user = f"username {new_name_value} privilege {new_privilige_value} {after_type_value} {password_value}"
        # print(add_user)
        conn.add_commands(add_user)

    if new_name_value and password_value and type_value and privilige_value:
        if str(privilige_value).isnumeric():
            if 0 <= int(privilige_value) <= 15:
                if type_value == "Plain text":
                    runCmds_usernameAdd("password", privilige_value)
                elif type_value == "Cipher":
                    runCmds_usernameAdd("secret", privilige_value)
                else:
                    mgbx.showinfo("Error", "Please select \"Cipher\" or \"Plain text\"")
            else:
                mgbx.showinfo("Caution", "Select Privilige Level between 0 to 15 ")
        else:
            mgbx.showinfo("Caution", "Privilige Level must be numeric")
    else:
        mgbx.showinfo("Error", "All these are Required")

def user_rmv_config(name_rmv_value):
    if name_rmv_value:
        rmv_user = f"no username {name_rmv_value}"
        try:
            # print(rmv_user)
            conn.add_commands(rmv_user)
        except Exception as e:
            mgbx.showinfo("Error", "Unable to complete the task! Please Try again")
    else:
        mgbx.showinfo("Error", "Please Enter username to remove")
# ==============================Device Management Section===============================
def device_save():
    # conn.save_device_commands()
    conn.save_device_command_manual()

def device_backup():
    conn.backup_device_commands()

def device_reset():
    conn.reset_device_commands()
def device_reload():
    conn.reload_device_commands()

# ==============================SSH Section===============================
"""
def ssh_config(ssh_domain_value, ssh_version_value):
    def version_selection(ssh_version_value):
        if ssh_version_value == "1":
            return 600
        elif ssh_version_value == "2":
            return 768
        else:
            mgbx.showinfo("Access Denied", f"Please Enter correct SSH version")
    def ssh_config_error_checking(ssh_domain_value, ssh_version_value):
        if ssh_domain_value and ssh_version_value != "":
            if ssh_version_value.isnumeric():
                if int(ssh_version_value) < 1 or int(ssh_version_value) > 2:
                    mgbx.showinfo("Selection Error!", "Please select given SSH version")
                else:
                    # ssh_run_command = f"ip domain-name {ssh_domain_value}\n crypto key generate rsa\n {version_selection(ssh_version_value)}\n yes \n line vty 0 5\n transport input all\n login local\n exit\n"
                    # print(ssh_run_command)
                    conn.ssh_config_device(ssh_domain_value, version_selection(ssh_version_value))
            else:
                mgbx.showinfo("Caution", "SSH version must be numeric")
        else:
            mgbx.showinfo("Caution", "Please Fill required fields")

    ssh_config_error_checking(ssh_domain_value, ssh_version_value)



"""

    # print(new_name_value)
    # print(password_value)
    # print(after_type_value)
    # print(after_privilige_value)

    # new_name_value = new_name_value.get()
    # password_value = password_value.get()
    # type_value = type_value.get()
    # privilige_value = privilige_value.get()