import tkinter as tk

#temporary import will delete when complete
# import os
# for i in range(1, 3):
#     os.chdir("..")
# print(os.getcwd())

with open("login_info.txt", "r") as f:
    var = f.readline()
    info = var.split(",")

router_root = tk.Tk()
router_root.title(f"SNDRC_{info[4].upper()}_{info[0]}")
router_root.geometry("1330x800")


# top_frame = Frame(root, borderwidth=5, relief="groove")
# top_frame.pack(anchor=N, fill=X, side=TOP)
# labeltop = Label(top_frame, text="ROUTER").pack()

left_button_frame = tk.Frame(router_root)
left_button_frame.pack(anchor=tk.W, fill=tk.Y, side=tk.LEFT)

label1 = tk.Label(left_button_frame, text=f"{info[5]}", font= ("Algerian", 20), fg="#373737")
label1.grid(padx=2, pady=1)

right_main_frame = tk.Frame(router_root, borderwidth=5, relief="groove", bg="#373737")
right_main_frame.pack(expand=True, fill=tk.BOTH)


