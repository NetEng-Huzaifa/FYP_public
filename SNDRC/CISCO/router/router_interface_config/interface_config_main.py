from tkinter import ttk
from CISCO.router.router_main_frames import *
from .interface_config_functions import *
from CISCO.router.access_cisco_router.access_cisco_router_ssh import *
import re
from CISCO.router.get_info_from_device import interface_info


def interface():
    notebook = ttk.Notebook(right_main_frame)
    notebook.pack(expand=True, anchor=tk.N, fill=tk.X)
    # create frames
    interface_main_frame = tk.Frame(notebook)

    interface_main_frame.pack(fill='both', expand=True)

    # add frames to notebook
    notebook.add(interface_main_frame, text='Interface Config')

    # =============================Interface Config Section================================
    # ===========> interface section
    interface_frame = tk.LabelFrame(interface_main_frame, text="INTERFACE ")
    interface_frame.pack(fill=tk.X, padx=20, pady=15)
    # label section
    interface_label = tk.Label(interface_frame, text="Interface(port)")
    interface_state_label = tk.Label(interface_frame, text="State")
    interface_duplex_label = tk.Label(interface_frame, text="Duplex")
    interface_description_label = tk.Label(interface_frame, text="Description")
    interface_keepalive_label = tk.Label(interface_frame, text="Keepalive(0-32767) sec")

    interface_label.grid(row=1, column=1)
    interface_state_label.grid(row=1, column=2)
    interface_duplex_label.grid(row=1, column=3)
    interface_description_label.grid(row=1, column=4)
    interface_keepalive_label.grid(row=1, column=5)
    # Entries Section
    interface_value = tk.StringVar()
    interface_state_value = tk.StringVar()
    interface_duplex_value = tk.StringVar()
    interface_description_value = tk.StringVar()
    interface_keepalive_value = tk.StringVar()

    interface_entry = ttk.Combobox(interface_frame, values = re.findall(r"^[A-Za-z].+?[\d/.]+", conn.get_info_from_router("sh ip int br"), re.MULTILINE), textvariable = interface_value)
    interface_state_entry = ttk.Combobox(interface_frame, values = ["UP", "Shutdown"], textvariable = interface_state_value)
    interface_duplex_entry = ttk.Combobox(interface_frame, values = ["Half", "Full", "Auto"], textvariable = interface_duplex_value)
    interface_description_entry = tk.Entry(interface_frame, textvariable=interface_description_value)
    interface_keepalive_entry = tk.Entry(interface_frame, textvariable=interface_keepalive_value)

    interface_entry.grid(row=2, column=1, padx=20, pady=10)
    interface_state_entry.grid(row=2, column=2, padx=20, pady=10)
    interface_duplex_entry.grid(row=2, column=3, padx=20, pady=10)
    interface_description_entry.grid(row=2, column=4, padx=20, pady=10)
    interface_keepalive_entry.grid(row=2, column=5, padx=20, pady=10)

    # Buttons Section
    interface_run_button = tk.Button(interface_frame, text="Execute", width=12, command=lambda: interface_config(hostname_value))

    interface_run_button.grid(row=3, column=3, padx=20, pady=10, sticky=tk.E)

    # ===========> Serial interface section
    interface_serial_frame = tk.LabelFrame(interface_main_frame, text="SERIAL INTERFACE ")
    interface_serial_frame.pack(fill=tk.X, padx=20, pady=15)
    # label section
    interface_serial_label = tk.Label(interface_serial_frame, text="Interface(port)")
    interface_serial_encapsulation_label = tk.Label(interface_serial_frame, text="Encapsulation")
    interface_serial_clockRate_label = tk.Label(interface_serial_frame, text="ClockRate (bps)")
    # interface_serial_description_label = tk.Label(interface_serial_frame, text="Description")

    interface_serial_label.grid(row=1, column=1)
    interface_serial_encapsulation_label.grid(row=1, column=2)
    interface_serial_clockRate_label.grid(row=1, column=3)
    # interface_serial_description_label.grid(row=1, column=4)
    # Entries Section
    interface_serial_value = tk.StringVar()
    interface_serial_encapsulation_value = tk.StringVar()
    interface_serial_clockRate_value = tk.StringVar()
    # interface_serial_description_value = tk.StringVar()

    interface_serial_entry = ttk.Combobox(interface_serial_frame, values = interface_info, textvariable = interface_serial_value)
    interface_serial_encapsulation_entry = ttk.Combobox(interface_serial_frame, values = ["HDLC", "PPP"], textvariable = interface_serial_encapsulation_value)
    interface_serial_clockRate_entry = ttk.Combobox(interface_serial_frame, values = ["1200", "2400", "4800", "9600", "14400", "19200", "28800", "38400", "56000", "64000", "128000", "2015232"], textvariable = interface_serial_clockRate_value)
    # interface_serial_description_entry = tk.Entry(interface_serial_frame, textvariable=interface_serial_description_value)

    interface_serial_entry.grid(row=2, column=1, padx=20, pady=10)
    interface_serial_encapsulation_entry.grid(row=2, column=2, padx=20, pady=10)
    interface_serial_clockRate_entry.grid(row=2, column=3, padx=20, pady=10)
    # interface_serial_description_entry.grid(row=2, column=4, padx=20, pady=10)

    # Buttons Section
    interface_serial_run_button = tk.Button(interface_serial_frame, text="Execute", width=12, command=lambda: interface_config(hostname_value))

    interface_serial_run_button.grid(row=3, column=3, padx=20, pady=10, sticky=tk.E)


    # ===========> Default interface section
    defaultInterface_frame = tk.LabelFrame(interface_main_frame, text="DEFAULT INTERFACE ")
    defaultInterface_frame.pack(fill=tk.X, padx=20, pady=15)
    # label section
    defaultInterface_label = tk.Label(defaultInterface_frame, text="Interface(port) : ")

    defaultInterface_label.grid(row=0, column=0)
    # Entries Section
    defaultInterface_value = tk.StringVar()

    defaultInterface_entry = ttk.Combobox(defaultInterface_frame, values = interface_info, textvariable = defaultInterface_value)

    defaultInterface_entry.grid(row=0, column=1, padx=20, pady=10)
    # Buttons Section
    interface_run_button = tk.Button(defaultInterface_frame, text="Execute", width=12, command=lambda: interface_config(hostname_value))

    interface_run_button.grid(row=2, column=3, padx=20, pady=10, sticky=tk.E)
