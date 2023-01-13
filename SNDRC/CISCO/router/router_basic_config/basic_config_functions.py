from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
def user_add_config(new_name_value, password_value, type_value, privilige_value):
    def type_value_checking():
        if type_value.get() == "Plain text":
            return "password"
        elif type_value.get() == "Cipher":
            return "secret"
        else:
            print("Please select \"Cipher\" or \"Plain text\"")

    def privilige_value_checking():
        if int(privilige_value.get()) >= 0 and int(privilige_value.get()) <= 15:
            # print(f"okey! Level is {privilige_value.get()}")
            return privilige_value.get()
        else:
            print("Select Privilige Level between 0 to 15")

    new_name_value = new_name_value.get()
    new_password_value = password_value.get()
    after_type_value = type_value_checking()
    after_privilige_value = privilige_value_checking()

    def runCmds_usernameAdd():
        add_user = f"username {new_name_value} privilege {after_privilige_value} {after_type_value} {new_password_value}"
        print(add_user)
        # c1 = TelnetCiscoRouter("192.168.33.133","huzaifa","123")
        conn.add_commands(add_user)

    runCmds_usernameAdd()


def user_rmv_config(name_rmv_value):
    rmv_user = f"no username {name_rmv_value}"
    print(rmv_user)
    conn.add_commands(rmv_user)
# =============================================================
#System Section

def device_save():
    conn.save_device_commands()

def device_backup():
    conn.backup_device_commands()

# =============================================================
# SSH Section

def ssh_config(ssh_domain_value, ssh_version_value):
    def version_selection(ssh_version_value):
        if ssh_version_value == "1":
            return 600
        elif ssh_version_value == "2":
            return 768
        else:
            print("Please Enter correct SSH version")

    ssh_run_commands = f"ip domain-name {ssh_domain_value.get()}\n crypto key generate rsa\n {version_selection(ssh_version_value.get())}\n yes \n line vty 0 4\n transport input all\n login local\n exit\n"
    print(ssh_run_commands)
    # scr1 = SshCiscoRouter("192.168.33.133", "huzaifa", "123")
    conn.add_commands(ssh_run_commands)

















    # print(new_name_value)
    # print(password_value)
    # print(after_type_value)
    # print(after_privilige_value)

    # new_name_value = new_name_value.get()
    # password_value = password_value.get()
    # type_value = type_value.get()
    # privilige_value = privilige_value.get()