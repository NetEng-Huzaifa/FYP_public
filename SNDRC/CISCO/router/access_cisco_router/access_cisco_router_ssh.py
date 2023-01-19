from netmiko import ConnectHandler
from tkinter import messagebox as mgbx
import os

#this section will comment out when start execution of login page or ssh page
# for i in range(1, 2):
#     os.chdir("..")
print(os.getcwd())
with open("login_info.txt", "r") as f:
    var = f.readline()
    info = var.split(",")
cisco_router = {
    'device_type': 'cisco_ios',
    'host': info[0],
    'username': info[1],
    'password': info[2],
    'secret': info[3],
    'port': 22
}
class SshDevice:
    def __init__(self):
        try:
            self.ssh = ConnectHandler(**cisco_router)
            self.ssh.enable()
        except Exception as e:
            mgbx.showinfo("Error!", f"{e}")
    def reset_mode(self):
        if self.ssh.config_mode():
            self.ssh.exit_config_mode()
    def add_commands(self, commands):
        self.reset_mode()
        self.ssh.config_mode()
        self.ssh.send_command(commands)
        self.ssh.exit_config_mode()

    def save_device_commands(self):
        self.ssh.send_command("copy run start", read_timeout=1)
        self.ssh.send_command("yes")
    def backup_device_commands(self):
        self.ssh.send_command("terminal length 0\n")
        result = self.ssh.send_command("show running-config")
        with open(f"{info[0]}_backup.txt", "w") as f:
            f.write(result)
            # print(result)
    def reset_device_commands(self):
        self.ssh.send_command("write erase", read_timeout=1)
        self.ssh.send_command("y", read_timeout=1)
    def reload_device_commands(self):
        self.ssh.send_command("reload", read_timeout=1)
        self.ssh.send_command("y", read_timeout=1)
    def get_info_from_router(self, command):
        self.reset_mode()
        self.ssh.send_command("terminal length 0\n")
        return self.ssh.send_command(command)


conn = SshDevice()
