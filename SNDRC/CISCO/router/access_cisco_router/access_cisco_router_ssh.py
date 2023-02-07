from netmiko import ConnectHandler
from tkinter import messagebox as mgbx
import os

#this section will comment out when start execution of login page or ssh page
# for i in range(1, 4):
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
            print(self.ssh.find_prompt())
        except Exception as e:
            mgbx.showinfo("Error!", f"{e}")
    # def reset_mode(self):
    #     if self.ssh.config_mode():
    #         self.ssh.exit_config_mode()
    def add_commands(self, commands):
        # print(self.ssh.find_prompt())
        # self.reset_mode()
        # print(self.ssh.find_prompt())
        # self.ssh.config_mode()
        # print(self.ssh.find_prompt())
        # self.ssh.send_command(commands)
        self.ssh.send_config_set(commands)
        # print(self.ssh.find_prompt())
        # self.ssh.exit_config_mode()
        # print(self.ssh.find_prompt())
        # self.reset_mode()
    def ssh_config_device(self ):
        pass
    def save_device_commands(self):
        # self.ssh.send_command("copy run start", read_timeout=1)
        # self.ssh.send_command("yes")
        self.ssh.save_config()
    def backup_device_commands(self):
        self.ssh.send_command("terminal length 0\n")
        result = self.ssh.send_command("show running-config")
        with open(f"{info[0]}_backup.txt", "w") as f:
            f.write(result)
            # print(result)
    def reset_device_commands(self):
        output = self.ssh.send_command_timing(
            command_string="wr erase",
            strip_prompt=False,
            strip_command=False
        )
        if "confirm" in output:
            output += self.ssh.send_command_timing(
                command_string="y",
                strip_prompt=False,
                strip_command=False
            )
        # self.ssh.disconnect()
        # print()
        # print(output)
        # print()
    def reload_device_commands(self):
        # self.ssh.send_command("reload", read_timeout=1)
        # self.ssh.send_command("y", read_timeout=1)
        output = self.ssh.send_command_timing(
            command_string="reload",
            strip_prompt=False,
            strip_command=False
        )
        if "Save?" in output:
            output += self.ssh.send_command_timing(
                command_string="no",
                strip_prompt=False,
                strip_command=False
            )
        if "confirm" in output:
            output += self.ssh.send_command_timing(
                command_string="y",
                strip_prompt=False,
                strip_command=False
            )
    def get_info_from_router(self, command):
        self.ssh.send_command("terminal length 0\n")
        return self.ssh.send_command(command)

conn = SshDevice()
# conn.backup_device_commands()
# conn.reset_device_commands()
# conn.reload_device_commands()
# conn.backup_device_commands()