from CISCO.router.router_basic_config.basic_config_main import *

def interfaces():
    pass

def hide_indicate():
    basic_config_button.config(bg="#d5d5d5", fg="black")
    interfaces_button.config(bg="#d5d5d5", fg="black")
    # button3.config(bg="green")
    pass
def delete_pages():
    for frame in right_main_frame.winfo_children():
        frame.destroy()
def indicate(button, page):
    hide_indicate()
    button.config(bg="#373737", fg="#d5d5d5")
    delete_pages()
    page()


basic_config_button = tk.Button(left_button_frame, text="Basic Config", font= ("Arial", 12), bg="#d5d5d5", width=12, command=lambda:indicate(basic_config_button, basicConfig))
basic_config_button.grid()
interfaces_button = tk.Button(left_button_frame, text="Interfaces", font= ("Arial", 12), bg="#d5d5d5", width=12, command=lambda:indicate(interfaces_button, interfaces))
interfaces_button.grid()
# button3 = Button(left_button_frame, text="Routing", width=12, command=lambda:indicate(button3, Home))
# button3.grid(padx=2, pady=1)
# button4 = Button(left_button_frame, text="Interfaces", width=12, command=lambda:indicate(button4, Home))
# button4.grid(padx=2, pady=1)

indicate(basic_config_button, basicConfig)
router_root.mainloop()





