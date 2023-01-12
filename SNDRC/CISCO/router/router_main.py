from CISCO.router.router_basic_config.basic_config_main import *


def Hide_indicate():
    basic_config_button.config(bg="#373737")
    interfaces_button.config(bg="#373737")
    # button3.config(bg="green")
    pass
def delete_pages():
    for frame in right_main_frame.winfo_children():
        frame.destroy()
def indicate(button, page):
    Hide_indicate()
    button.config(bg="#ffb837")
    delete_pages()
    page()


basic_config_button = tk.Button(left_button_frame, text="Basic Config", width=12, command=lambda:indicate(basic_config_button, basicConfig))
basic_config_button.grid(padx=2, pady=1)
interfaces_button = tk.Button(left_button_frame, text="Interfaces", width=12, command=lambda:indicate(interfaces_button, Interfaces))
interfaces_button.grid(padx=2, pady=1)
# button3 = Button(left_button_frame, text="Routing", width=12, command=lambda:indicate(button3, Home))
# button3.grid(padx=2, pady=1)
# button4 = Button(left_button_frame, text="Interfaces", width=12, command=lambda:indicate(button4, Home))
# button4.grid(padx=2, pady=1)


router_root.mainloop()





