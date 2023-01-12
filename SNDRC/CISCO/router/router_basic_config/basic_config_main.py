from tkinter import ttk
from CISCO.router.router_main_frames import *
from .basic_config_functions import *

def basicConfig():
    notebook = ttk.Notebook(right_main_frame)
    notebook.pack(expand=True, fill=tk.BOTH)

    # create frames
    user_frame = tk.Frame(notebook)
    ssh_main_frame = tk.Frame(notebook)
    system_frame = tk.Frame(notebook)

    user_frame.pack(fill='both', expand=True)
    ssh_main_frame.pack(fill='both', expand=True)
    system_frame.pack(fill='both', expand=True)

    # add frames to notebook
    notebook.add(user_frame, text='User')
    notebook.add(ssh_main_frame, text='SSH')
    notebook.add(system_frame, text='System')

    # ADDUSER Section
    adduser_frame = tk.LabelFrame(user_frame, text="Add User")
    adduser_frame.pack(fill=tk.X, padx=20, pady=15)

    # adduser label section
    name_label = tk.Label(adduser_frame, text="Username: ")
    password_label = tk.Label(adduser_frame, text="Password: ")
    type_label = tk.Label(adduser_frame, text="Type of password")
    privilige_label = tk.Label(adduser_frame, text="Privilige Level:")

    name_label.grid(row=0, column=0)
    password_label.grid(row=0, column=1)
    type_label.grid(row=0, column=2)
    privilige_label.grid(row=0, column=3)

    # Entries Section
    new_name_value = tk.StringVar()
    password_value = tk.StringVar()
    type_value = tk.StringVar()
    privilige_value = tk.StringVar()

    name_entry = tk.Entry(adduser_frame, textvariable=new_name_value)
    password_entry = tk.Entry(adduser_frame, textvariable=password_value)
    type_combobox = ttk.Combobox(adduser_frame, values=["Plain text", "Cipher"], textvariable=type_value)
    privilige_entry = tk.Entry(adduser_frame, textvariable=privilige_value)

    name_entry.grid(row=1, column=0, padx=20)
    password_entry.grid(row=1, column=1, padx=20)
    type_combobox.grid(row=1, column=2, padx=20)
    privilige_entry.grid(row=1, column=3, padx=20)

    # Buttons Section
    cmd_button = tk.Button(adduser_frame, text="Commands", width=12)
    useradd_run_button = tk.Button(adduser_frame, text="Execute", width=12, command=lambda: user_add_config(new_name_value, password_value, type_value, privilige_value))

    cmd_button.grid(row=2, column=0, padx=20, pady=15, sticky=tk.W)
    useradd_run_button.grid(row=2, column=3, padx=20, sticky=tk.E)

    # Remove username section

    removeuser_info_frame = tk.LabelFrame(user_frame, text="Remove User")
    removeuser_info_frame.pack(fill=tk.X, padx=20, pady=15, ipadx=10, ipady=10)

    name_label = tk.Label(removeuser_info_frame, text="Username: ")
    name_label.grid(row=0, column=0, padx=20, ipady=15)

    name_rmv_value = tk.StringVar()
    name_rmv_entry = tk.Entry(removeuser_info_frame, textvariable=name_rmv_value)
    name_rmv_entry.grid(row=0, column=1, padx=10)

    # Buttons Section
    user_rmv_run_button = tk.Button(removeuser_info_frame, text="Execute", width=12, command=lambda: user_rmv_config(name_rmv_value.get()))
    user_rmv_run_button.grid(row=0, column=3, padx=20, sticky=tk.E)

    # Commands_display_frame = LabelFrame(user_frame, text="Commands")
    # Commands_display_frame.pack(expand=TRUE, fill=BOTH, padx=20, pady=15, ipadx=10, ipady=10)
    # name_value = StringVar()
    # name_entry = Entry(Commands_display_frame, width=50)
    # name_entry.pack(side=LEFT, expand=True, fill=BOTH)

    # data_display_frame = LabelFrame(user_frame, text="Database")
    # data_display_frame.pack(side=RIGHT, fill=BOTH, padx=20, pady=15, ipadx=10, ipady=10)
    # name_value = StringVar()
    # data_entry = Entry(data_display_frame, width=50)
    # data_entry.pack(side=RIGHT, expand=True, fill=BOTH)

    # =============================================================
    # System Section
    system_save_frame = tk.LabelFrame(system_frame, text="SAVE")
    system_save_frame.pack(fill=tk.X, padx=20, pady=15)

    # Save label section
    save_label = tk.Label(system_save_frame, text="To write running Config in Startup Config: ")
    save_label.grid(row=0, column=0)

    # Save Buttons Section
    save_button = tk.Button(system_save_frame, text="Save", width=12, command=lambda: device_save())
    save_button.grid(row=0, column=1, padx=20, pady=10, sticky=tk.E)

    # Backup label section
    system_backup_frame = tk.LabelFrame(system_frame, text="BACKUP")
    system_backup_frame.pack(fill=tk.X, padx=20, pady=15)

    save_label = tk.Label(system_backup_frame, text="To Backup Device Configuration in your Local System: ")
    save_label.grid(row=0, column=0)

    # Backup Buttons Section
    backup_button = tk.Button(system_backup_frame, text="Download", width=12, command=lambda: device_backup())
    backup_button.grid(row=0, column=1, padx=20, pady=10, sticky=tk.E)

    # =============================================================
    # SSH Section
    ssh_frame = tk.LabelFrame(ssh_main_frame, text="Configure SSH:")
    ssh_frame.pack(fill=tk.X, padx=20, pady=15)

    # Save label section
    ssh_domain_label = tk.Label(ssh_frame, text="IP domain-name: ")
    ssh_version_label = tk.Label(ssh_frame, text="SSH Version : ")

    ssh_domain_label.grid(row=0, column=0)
    ssh_version_label.grid(row=0, column=2)

    # Entries Section
    ssh_domain_value = tk.StringVar()
    ssh_version_value = tk.StringVar()

    domain_entry = tk.Entry(ssh_frame, textvariable=ssh_domain_value)
    ssh_version_combobox = ttk.Combobox(ssh_frame, values=["1", "2"], textvariable=ssh_version_value)

    domain_entry.grid(row=0, column=1, padx=20)
    ssh_version_combobox.grid(row=0, column=3, padx=20)

    # Buttons Section
    ssh_cmd_button = tk.Button(ssh_frame, text="Commands", width=12)
    ssh_run_button = tk.Button(ssh_frame, text="Execute", width=12, command=lambda: ssh_config(ssh_domain_value, ssh_version_value))

    ssh_cmd_button.grid(row=2, column=0, padx=20, pady=15, sticky=tk.W)
    ssh_run_button.grid(row=2, column=3, padx=20, sticky=tk.E)
