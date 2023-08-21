import tkinter as tk
from .access_cisco_router.access_cisco_router_ssh import conn

#temporary import will delete when complete
# import os
# for i in range(1, 3):
#     os.chdir("..")
# print(os.getcwd())

with open("Files/login_info.txt", "r") as f:
    var = f.readline()
    info = var.split(",")

router_root = tk.Tk()
router_root.title(f"SRCND_[{conn.get_hostname()}{info[0]}]")
# WxH
router_root.geometry(f"{router_root.winfo_screenwidth()}x{router_root.winfo_screenwidth()}")
# router_root.geometry("1330x800")
# router_root.geometry()


left_button_frame = tk.Frame(router_root)
left_button_frame.pack(anchor=tk.W, fill=tk.Y, side=tk.LEFT)

label1 = tk.Label(left_button_frame, text=f"{info[4]}", font= ("Algerian", 20), fg="#d5d5d5", borderwidth=3, relief="sunken", bg="#373737")
label1.grid(padx=2, pady=1, ipadx=22)

right_main_frame = tk.Frame(router_root, borderwidth=5, relief="groove", bg="#373737")
right_main_frame.pack(expand=True, fill=tk.BOTH)


