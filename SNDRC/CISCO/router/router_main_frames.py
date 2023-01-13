import tkinter as tk


router_root = tk.Tk()
router_root.title("SNDRC")
router_root.geometry("1330x800")


# top_frame = Frame(root, borderwidth=5, relief="groove")
# top_frame.pack(anchor=N, fill=X, side=TOP)
# labeltop = Label(top_frame, text="ROUTER").pack()

left_button_frame = tk.Frame(router_root)
left_button_frame.pack(anchor=tk.W, fill=tk.Y, side=tk.LEFT)

label1 = tk.Label(left_button_frame, text="Router", font= ("Algerian", 20), fg="#373737")
label1.grid(padx=2, pady=1)

right_main_frame = tk.Frame(router_root, borderwidth=5, relief="groove", bg="#373737")
right_main_frame.pack(expand=True, fill=tk.BOTH)


