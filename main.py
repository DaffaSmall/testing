import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import ttk
import locale

# Set the locale to Indonesian
locale.setlocale(locale.LC_ALL, 'id_ID')


# Define constants for items and their prices
ITEMS = {
    "Tisu": 15,
    "Buku": 25,
    "Sayuran": 30,
    "plastik botol": -100,
    "Pembungkus makanan": -70,
    "mainan plastik": -50,
    "perabot/peralatan plastik": -30
}

class RecyclingGame:
    def __init__(self):
        self.point = 0
        self.uang = 0
        self.pilih = []
        self.create_widgets()

    def create_widgets(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("e-Waste Reduction")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
    
        # Create the style for the ttk widgets
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 14))
        style.configure("TButton", font=("Helvetica", 12), width=25)
    
        # Create the widgets
        self.uang_label = ttk.Label(self.root, text=f"Total Uang akumulasi: {self.uang}")        
        self.point_label = ttk.Label(self.root, text=f"Total Point: {self.point}")
        self.pilih_label = ttk.Label(self.root, text=f"Pilih: {self.pilih}")
        self.items_frame = ttk.Frame(self.root)
        self.reset_button = ttk.Button(self.root, text="Reset", command=self.reset_game)
    
        # Pack the widgets
        self.uang_label.pack(side="top", fill="x", pady=(10, 0))
        self.point_label.pack(side="top", fill="x", pady=(10, 0))
        self.pilih_label.pack(side="top", fill="x", pady=(10, 0))
        self.items_frame.pack(side="top", fill="both", expand=True, padx=10, pady=(20, 0))
        self.reset_button.pack(side="bottom", pady=(0, 10))
    
        # Populate the list of items
        for item_num, item_name in enumerate(ITEMS):
            item_frame = ttk.Frame(self.items_frame)
            item_frame.pack(side="top", fill="x", pady=5)
    
            item_label = ttk.Label(item_frame, text=f"{item_name}", width=20)
            item_label.pack(side="left")
    
            quantity_label = ttk.Label(item_frame, text="Qty:")
            quantity_label.pack(side="left", padx=10)
    
            self.quantity_var = tk.StringVar()
            self.quantity_var.set("1")
    
            quantity_box = ttk.Combobox(item_frame, values=[x for x in range(500)], textvariable=self.quantity_var, state="readonly", width=5)
            quantity_box.pack(side="left", padx=20)

            self.price_label = ttk.Label(item_frame, text=f"Point: {ITEMS[item_name] * int(self.quantity_var.get())}", width=10)
            self.price_label.pack(side="left",fill="y", padx=10)

            item_button = ttk.Button(item_frame, text="Recycle", command=lambda i=item_name, q=self.quantity_var: self.recycle_item(i, int(q.get())), width=10)
            item_button.pack(side="right")
    
        self.items_frame.pack_propagate(False)

    def reset_game(self):
        # Reset point, money earned, and selected items
        self.point = 0
        self.uang = 0
        self.pilih = []

        # Update labels
        self.uang_label.config(text=f"Total Uang akumulasi: {self.uang}")
        self.point_label.config(text=f"Total Point: {self.point}")
        self.pilih_label.config(text=f"Pilih: {self.pilih}")

    def recycle_item(self, item_name, quantity):
        # Update point and selected items
        self.point += ITEMS[item_name] * quantity
        if not all(value in self.pilih for value in [item_name]):
            self.pilih.append(item_name)
        self.uang = locale.currency(self.point * 200, grouping=True)

        # Update labels
        self.uang_label.config(text=f"Total Uang akumulasi: {self.uang}")
        self.point_label.config(text=f"Total Point: {self.point}")
        self.price_label.config(text=f"Point: {ITEMS[item_name] * int(self.quantity_var.get())}")
        self.pilih_label.config(text=f"Pilih: {self.pilih}")

        # Show message box
        mbox.showinfo("Recycling Success", f"Terimakasih sudah ngericycle {quantity} {item_name}\nPoint ditambah/dikurang: {ITEMS[item_name] * quantity}")

    def run(self):
        # Start the main loop
        self.root.mainloop()

if __name__ == "__main__":
    game = RecyclingGame()
    game.run()
