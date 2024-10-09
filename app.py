import tkinter as tk
from tkinter import ttk, messagebox
from data_service import DataService

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("MySQL GUI")
        self.master.geometry("600x400")

        # Input fields for database connection
        self.host_var = tk.StringVar()
        self.user_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.database_var = tk.StringVar()

        tk.Label(master, text="Host:").pack(pady=5) # Kotak input host
        tk.Entry(master, textvariable=self.host_var).pack(pady=5)

        tk.Label(master, text="User:").pack(pady=5) # Kotak input user
        tk.Entry(master, textvariable=self.user_var).pack(pady=5)

        tk.Label(master, text="Password:").pack(pady=5) # Kotak input password
        tk.Entry(master, textvariable=self.password_var, show='*').pack(pady=5)

        tk.Label(master, text="Database:").pack(pady=5) # Kotak input nama Database
        tk.Entry(master, textvariable=self.database_var).pack(pady=5)

        # Create a button to fetch data
        fetch_button = tk.Button(master, text="Fetch Data", command=self.fetch_data)
        fetch_button.pack(pady=10)

        # Create a tree view to display data
        self.columns = ("Radam", "Fazil", "Fino", "Ario")
        self.tree = ttk.Treeview(master, columns=self.columns, show='headings')
        for col in self.columns:
            self.tree.heading(col, text=col)

        # Hide the treeview initially
        self.tree.pack_forget()

    def fetch_data(self):
        # Get user input for database connection
        host = self.host_var.get()
        user = self.user_var.get()
        password = self.password_var.get()
        database = self.database_var.get()

        # Initialize DataService
        data_service = DataService(host, user, password, database)

        try:
            records = data_service.get_records()

            # Clear the treeview
            for row in self.tree.get_children():
                self.tree.delete(row)

            # Insert data into the treeview
            for record in records:
                self.tree.insert("", tk.END, values=record)

            # Show the treeview only if there are records
            if records:
                self.tree.pack(expand=True, fill='both')
            else:
                messagebox.showinfo("No Data", "No records found.")

        except Exception as err:
            messagebox.showerror("Error", str(err))


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()