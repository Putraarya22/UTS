import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def fetch_data():
    try:
        # Connect to the database
        conn = mysql.connector.connect(
            host='127.0.0.1',         # Adjust if the database is not on the local machine
            user='root',     # Replace with your MySQL username
            password='',  # Replace with your MySQL password
            database='nyoba'          # Your database name
        )

        cursor = conn.cursor()
        
        # Execute the query
        cursor.execute("SELECT * FROM `db 2`")  # Note the backticks around table name containing spaces

        # Fetch all results
        records = cursor.fetchall()

        # Clear the treeview
        for row in tree.get_children():
            tree.delete(row)

        # Insert data into the treeview
        for record in records:
            tree.insert("", tk.END, values=record)

        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))

# Create the main application window
app = tk.Tk()
app.title("MySQL GUI")
app.geometry("600x400")

# Create a button to fetch data
fetch_button = tk.Button(app, text="Fetch Data", command=fetch_data)
fetch_button.pack(pady=10)

# Create a tree view to display the data
columns = ("Radam", "Fazil", "Fino", "Ario")
tree = ttk.Treeview(app, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)

tree.pack(expand=True, fill='both')

# Start the GUI event loop
app.mainloop()