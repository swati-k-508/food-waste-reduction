import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class FoodApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Management System")
        self.root.geometry("1200x700")  # Optimized for fullscreen on laptops
        self.root.configure(bg="#f8f9fa")

        # Define styles
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 14), foreground="#2d3436", background="#f8f9fa")
        self.style.configure("TEntry", font=("Arial", 14))
        self.style.configure("TButton", font=("Arial", 14, "bold"), background="#6c5ce7", foreground="black", padding=10)
        self.style.map("TButton", background=[("active", "#0984e3")])

        # Notebook styles
        self.style.configure("TNotebook", background="#dfe6e9")
        self.style.configure("TNotebook.Tab", font=("Arial", 12, "bold"), background="#81ecec", padding=(15, 10))
        self.style.map("TNotebook.Tab", background=[("selected", "#00cec9")])

        # Main Notebook (Tabs)
        self.notebook = ttk.Notebook(root, style="TNotebook")
        self.notebook.pack(expand=1, fill="both", padx=20, pady=20)

        # Tabs
        self.menu_tab = ttk.Frame(self.notebook, style="TFrame")
        self.ingredient_tab = ttk.Frame(self.notebook, style="TFrame")
        self.comparison_tab = ttk.Frame(self.notebook, style="TFrame")

        self.notebook.add(self.menu_tab, text="Menu Management")
        self.notebook.add(self.ingredient_tab, text="Ingredient Shelf Life")
        self.notebook.add(self.comparison_tab, text="Quantity Comparison")

        # Initialize Tabs
        self.initialize_menu_tab()
        self.initialize_ingredient_tab()
        self.initialize_comparison_tab()

    # MENU MANAGEMENT TAB
    def initialize_menu_tab(self):
        self.menu_items = []

        ttk.Label(self.menu_tab, text="Menu Management", font=("Arial", 20, "bold"), foreground="#d63031").grid(row=0, column=0, columnspan=2, pady=20)

        ttk.Label(self.menu_tab, text="Name:", style="TLabel").grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.menu_name_entry = ttk.Entry(self.menu_tab, style="TEntry", width=30)
        self.menu_name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        ttk.Label(self.menu_tab, text="Price (Rs):", style="TLabel").grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.menu_price_entry = ttk.Entry(self.menu_tab, style="TEntry", width=30)
        self.menu_price_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        ttk.Label(self.menu_tab, text="Category:", style="TLabel").grid(row=3, column=0, padx=20, pady=10, sticky="e")
        self.menu_category_entry = ttk.Entry(self.menu_tab, style="TEntry", width=30)
        self.menu_category_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        ttk.Label(self.menu_tab, text="Availability:", style="TLabel").grid(row=4, column=0, padx=20, pady=10, sticky="e")
        self.menu_availability_entry = ttk.Entry(self.menu_tab, style="TEntry", width=30)
        self.menu_availability_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        ttk.Button(self.menu_tab, text="Add Item", style="TButton", command=self.add_menu_item).grid(row=5, column=0, columnspan=2, pady=20)

        self.menu_listbox = tk.Listbox(self.menu_tab, width=100, height=20, font=("Arial", 12), bg="#ffeaa7", fg="#2d3436")
        self.menu_listbox.grid(row=6, column=0, columnspan=2, padx=20, pady=10)

    def add_menu_item(self):
        name = self.menu_name_entry.get()
        try:
            price = float(self.menu_price_entry.get())
            category = self.menu_category_entry.get()
            availability = self.menu_availability_entry.get()
            self.menu_items.append((name, price, category, availability))
            self.menu_listbox.insert(tk.END, f"{name} - Rs.{price:.2f} | {category} | {availability}")
            self.menu_name_entry.delete(0, tk.END)
            self.menu_price_entry.delete(0, tk.END)
            self.menu_category_entry.delete(0, tk.END)
            self.menu_availability_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid price.")

    # INGREDIENT SHELF LIFE TAB
    def initialize_ingredient_tab(self):
        self.ingredients = []

        ttk.Label(self.ingredient_tab, text="Ingredient Shelf Life", font=("Arial", 20, "bold"), foreground="#0984e3").grid(row=0, column=0, columnspan=2, pady=20)

        ttk.Label(self.ingredient_tab, text="Ingredient Name:", style="TLabel").grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.ingredient_name_entry = ttk.Entry(self.ingredient_tab, style="TEntry", width=30)
        self.ingredient_name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        ttk.Label(self.ingredient_tab, text="Buying Date (YYYY-MM-DD):", style="TLabel").grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.buying_date_entry = ttk.Entry(self.ingredient_tab, style="TEntry", width=30)
        self.buying_date_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        ttk.Label(self.ingredient_tab, text="Ruin Date (YYYY-MM-DD):", style="TLabel").grid(row=3, column=0, padx=20, pady=10, sticky="e")
        self.ruin_date_entry = ttk.Entry(self.ingredient_tab, style="TEntry", width=30)
        self.ruin_date_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        ttk.Button(self.ingredient_tab, text="Add Ingredient", style="TButton", command=self.add_ingredient).grid(row=4, column=0, columnspan=2, pady=20)

        self.ingredient_listbox = tk.Listbox(self.ingredient_tab, width=100, height=20, font=("Arial", 12), bg="#dfe6e9", fg="#2d3436")
        self.ingredient_listbox.grid(row=5, column=0, columnspan=2, padx=20, pady=10)

    def add_ingredient(self):
        name = self.ingredient_name_entry.get()
        buying_date = self.buying_date_entry.get()
        ruin_date = self.ruin_date_entry.get()

        try:
            ruin_date_obj = datetime.strptime(ruin_date, "%Y-%m-%d")
            today = datetime.now()
            warning_period = ruin_date_obj - today

            if warning_period.days <= 3:
                messagebox.showwarning("Expiry Warning", f"Ingredient '{name}' is expiring soon on {ruin_date}!")
            if warning_period.days < 0:
                messagebox.showerror("Expired!", f"Ingredient '{name}' has already expired on {ruin_date}!")

            self.ingredients.append((name, buying_date, ruin_date))
            self.ingredient_listbox.insert(tk.END, f"{name} - {buying_date} to {ruin_date}")
            self.ingredient_name_entry.delete(0, tk.END)
            self.buying_date_entry.delete(0, tk.END)
            self.ruin_date_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Date Format", "Please enter dates in the format YYYY-MM-DD.")

    # QUANTITY COMPARISON TAB
    def initialize_comparison_tab(self):
        self.food_items = []

        ttk.Label(self.comparison_tab, text="Quantity Comparison", font=("Arial", 20, "bold"), foreground="#6c5ce7").grid(row=0, column=0, columnspan=2, pady=20)

        ttk.Label(self.comparison_tab, text="Food Item Name:", style="TLabel").grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.food_name_entry = ttk.Entry(self.comparison_tab, style="TEntry", width=30)
        self.food_name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        ttk.Label(self.comparison_tab, text="Last Year Quantity:", style="TLabel").grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.last_year_quantity_entry = ttk.Entry(self.comparison_tab, style="TEntry", width=30)
        self.last_year_quantity_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        ttk.Label(self.comparison_tab, text="This Year Quantity:", style="TLabel").grid(row=3, column=0, padx=20, pady=10, sticky="e")
        self.this_year_quantity_entry = ttk.Entry(self.comparison_tab, style="TEntry", width=30)
        self.this_year_quantity_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        ttk.Label(self.comparison_tab, text="Cost Per Unit (Rs):", style="TLabel").grid(row=4, column=0, padx=20, pady=10, sticky="e")
        self.cost_per_unit_entry = ttk.Entry(self.comparison_tab, style="TEntry", width=30)
        self.cost_per_unit_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        ttk.Button(self.comparison_tab, text="Add Item", style="TButton", command=self.add_food_item).grid(row=5, column=0, columnspan=2, pady=20)

        self.comparison_listbox = tk.Listbox(self.comparison_tab, width=100, height=20, font=("Arial", 12), bg="#ffeaa7", fg="#2d3436")
        self.comparison_listbox.grid(row=6, column=0, columnspan=2, padx=20, pady=10)

    def add_food_item(self):
        try:
            name = self.food_name_entry.get()
            last_year_qty = float(self.last_year_quantity_entry.get())
            this_year_qty = float(self.this_year_quantity_entry.get())
            cost_per_unit = float(self.cost_per_unit_entry.get())

            difference = this_year_qty - last_year_qty
            profit_or_loss = difference * cost_per_unit

            self.food_items.append((name, last_year_qty, this_year_qty, cost_per_unit))
            self.comparison_listbox.insert(tk.END, f"{name} | Last Year: {last_year_qty:.2f}, This Year: {this_year_qty:.2f}, "
                                           f"Difference: {difference:.2f}, Profit/Loss: Rs.{profit_or_loss:.2f}")

            self.food_name_entry.delete(0, tk.END)
            self.last_year_quantity_entry.delete(0, tk.END)
            self.this_year_quantity_entry.delete(0, tk.END)
            self.cost_per_unit_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numerical values for quantities and cost.")


if __name__ == "__main__":
    root = tk.Tk()
    app = FoodApp(root)
    root.mainloop()
s
