from netmiko import ConnectHandler
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
        self.ssh = ConnectHandler(**cisco_router)
        self.ssh.enable()
    def add_commands(self, commands):
        self.ssh.config_mode()
        self.ssh.send_command(commands)
        self.ssh.exit_config_mode()

    # same issue with this function
    def save_device_commands(self):
        result = self.ssh.send_command("copy run start")
        result = self.ssh.send_command("yes")
        print(result)
        # self.ssh.send_command("\n")
        # self.telnet.read_until(b'Overwrite the previous NVRAM configuration?[confirm]', 0.3)
        # self.telnet.write(b'\n')
    def backup_device_commands(self):
        self.ssh.send_command("terminal length 0\n")
        result = self.ssh.send_command("show running-config")
        print(result)
    # issue in this function
    def reset_device_commands(self):
        # self.ssh.send_command("write erase")
        # self.ssh.send_command("y", expect_string="[confirm]")
        # result = self.ssh.send_command("y",expect_string="Erasing the nvram filesystem will remove all configuration files! Continue? [confirm]",delay_factor=1)
        # result = self.ssh.send_command("show running-config")
        # print(result)
        pass
    def get_info_from_router(self, command):
        self.ssh.send_command("terminal length 0\n")
        return self.ssh.send_command(command)
        # self.telnet.write(command.encode('ascii') + b'\n')
        # all = self.telnet.read_very_eager().decode('utf-8')
        # print(all)
        # self.telnet.write(b'end\n')
        # self.telnet.write(b'exit\n')

    def enable(self):
        self.ssh.enable()
        result = self.ssh.send_command('show run')
        return result

conn = SshDevice()
# result = c1.enable()
# print(result)