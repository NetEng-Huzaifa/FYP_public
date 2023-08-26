from tkinter import ttk
from CISCO.router.router_main_frames import *
from .ethchannel_config_functions import *
from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
import re
from CISCO.router.get_info_from_device import interface_info, vlan_info

def eth_channel():
    notebook = ttk.Notebook(right_main_frame)
    notebook.pack(expand=True, anchor=tk.N, fill=tk.X)
    # create frames
    interface_pap_main_frame = tk.Frame(notebook)
    interface_chap_main_frame = tk.Frame(notebook)

    interface_pap_main_frame.pack(fill='both', expand=True)
    interface_chap_main_frame.pack(fill='both', expand=True)

    # add frames to notebook
    notebook.add(interface_pap_main_frame, text='PAP')
    notebook.add(interface_chap_main_frame, text='CHAP')



