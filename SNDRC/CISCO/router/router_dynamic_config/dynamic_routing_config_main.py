from tkinter import ttk
from CISCO.router.router_main_frames import *

def dynamic_routing():
    notebook = ttk.Notebook(right_main_frame)
    notebook.pack(expand=True, anchor=tk.N, fill=tk.X)
    # create frames
    rip_main_frame = tk.Frame(notebook)
    eigrp_main_frame = tk.Frame(notebook)
    ospf_main_frame = tk.Frame(notebook)

    rip_main_frame.pack(fill='both', expand=True)
    eigrp_main_frame.pack(fill='both', expand=True)
    ospf_main_frame.pack(fill='both', expand=True)

    # add frames to notebook
    notebook.add(rip_main_frame, text='RIP')
    notebook.add(eigrp_main_frame, text='EIGRP')
    notebook.add(ospf_main_frame, text='OSPF')

