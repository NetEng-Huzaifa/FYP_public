from netmiko import ConnectHandler
from tkinter import messagebox as mgbx
# import os

#this section will comment out when start execution of login page or ssh page
# for i in range(1, 4):
#     os.chdir("..")
# print(os.getcwd())
print("Please Wait! Connecting You With your device...")
with open("Files/login_info.txt", "r") as f:
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
            # print(self.ssh.find_prompt())
            print(f"{'='*13} Welcome to \'SRCND\'! {'='*13}\nHere, You can check the output of your commands")
        except Exception as e:
            mgbx.showinfo("Error!", f"{e}")
    def reset_mode(self):
        if self.ssh.config_mode():
            print("before exit", self.ssh.find_prompt())
            self.ssh.exit_config_mode()
            print("after exit", self.ssh.find_prompt())
    def clock_cmd(self, cmd):
        self.ssh.send_command(cmd)
    def add_commands(self, commands):
        # print("1", self.ssh.find_prompt())
        # self.reset_mode()
        # print("2", self.ssh.find_prompt())
        self.ssh.config_mode()
        # print("3", self.ssh.find_prompt())
        # self.ssh.send_command(commands)
        print(self.ssh.send_config_set(commands))
        # print("4", self.ssh.find_prompt())
        # self.ssh.exit_config_mode()
        # print("5", self.ssh.find_prompt())
        # self.reset_mode()
    def get_hostname(self):
        with open("Files/login_info.txt", "a") as f:
            f.write(f",{self.ssh.find_prompt()}")
        with open("Files/login_info.txt", "r") as f:
            var = f.readline()
            info = var.split(",")
            return info[7]
    """
    def ssh_config_device(self, ssh_domain_value, version):
        print(self.ssh.find_prompt())
        self.ssh.send_command(f"ip domain-name {ssh_domain_value}")
        output = self.ssh.send_command_timing(
            command_string = "crypto key generate rsa",
            strip_prompt=False,
            strip_command=False
        )
        print(self.ssh.find_prompt())
        if "You already have RSA keys defined" in output:
            output += self.ssh.send_command_timing(
                command_string="y",
                strip_prompt=False,
                strip_command=False
            )
        print(self.ssh.find_prompt())
        if "How many bits in the modulus" in output:
            output += self.ssh.send_command_timing(
                command_string=f"{version}",
                strip_prompt=False,
                strip_command=False
            )
        print(self.ssh.find_prompt())
        self.ssh.send_config_set(["line vty 0 15", "transport input all", "login local", "exit"])
        print(self.ssh.find_prompt())
        print()
        print(output)
        print()
    """
    """
    def save_device_commands(self):
        try:
            print(self.ssh.find_prompt())
            self.ssh.disconnect()
            print(self.ssh.save_config())
            print(self.ssh.find_prompt())

            mgbx.showinfo("Success", "Configuration Saved Successfully")
        except Exception as e:
            print("exit")
            mgbx.showinfo("Error", "Unable to save the commands! Please Try again")
    """
    def save_device_command_manual(self):
        try:
            output = self.ssh.send_command("write\n", read_timeout=30)
            if "confirm" in output:
                self.ssh.send_command("y\n")
                # print("Save with confirm")
            if "OK" in output:
                # print("Save without confirm")
                mgbx.showinfo("Success", "Configuration Saved Successfully")
        except Exception as e:
            mgbx.showinfo("Error", "Unable to save the commands! Please Try again")

    def backup_device_commands(self):
        try:
            self.ssh.send_command("terminal length 0\n")
            result = self.ssh.send_command("show running-config")
            with open(f"{info[0]}_backup.txt", "w") as f:
                f.write(result)
            mgbx.showinfo("Success", "Backup Completed")
        except Exception as e:
            mgbx.showinfo("Error", "Unable to Backup the device! Please Try again")
    def reset_device_commands(self):
        try:
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
            if "complete" in output:
                mgbx.showinfo("Success", "Device Reset successfully\nNow Reload the device")
        except Exception as e:
            mgbx.showinfo("Error", "Unable to Reset the device! Please Try again")
    def reload_device_commands(self):
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
        print(output)
    def get_info_from_router(self, command):
        self.ssh.send_command("terminal length 0\n")
        return self.ssh.send_command(command)

conn = SshDevice()
conn.get_hostname()
# conn.backup_device_commands()
# conn.reset_device_commands()
# conn.reload_device_commands()
# conn.backup_device_commands()
# conn.save_device_commands()
# conn.save_device_command_manual()