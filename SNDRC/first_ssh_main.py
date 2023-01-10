import tkinter as tk
from tkinter import ttk

root = tk.Tk()
#set width and height of login window
root.geometry("350x360")
root.title("SSH")
# root.resizable(False, False)
#main frame
main_frame = tk.Frame()
main_frame.pack(fill=tk.X)
#SSH Section
ssh_frame = tk.LabelFrame(main_frame, text="Configure SSH:")
ssh_frame.pack(fill=tk.X, padx=20, pady=15)
# Save label section
ssh_domain_label = tk.Label(ssh_frame, text="IP domain-name : ")
ssh_version_label = tk.Label(ssh_frame, text="SSH Version : ")

ssh_domain_label.grid(row=1, column=1)
ssh_version_label.grid(row=2, column=1)

# Entries Section
ssh_domain_value = tk.StringVar()
ssh_version_value = tk.StringVar()

domain_entry = tk.Entry(ssh_frame, textvariable=ssh_domain_value)
ssh_version_combobox = ttk.Combobox(ssh_frame, values=["1", "2"], textvariable=ssh_version_value)

domain_entry.grid(row=1, column=2, padx=20)
ssh_version_combobox.grid(row=2, column=2, padx=20)

# Buttons Section
# ssh_cmd_button = tk.Button(ssh_frame, text="Commands", width=12)
ssh_run_button = tk.Button(ssh_frame, text="Execute", width=12, command=lambda:ssh_config(ssh_domain_value, ssh_version_value))

# ssh_cmd_button.grid(row=3, column=1, padx=20, pady=15,sticky=tk.W)
ssh_run_button.grid(row=3, column=2, padx=20, sticky=tk.E)


root.mainloop()