import tkinter as tk
from tkinter import filedialog, messagebox
import bibtexparser

# Function to load .bib file and return BibDatabase object
def load_bib_file(file_path):
    with open(file_path, 'r') as bib_file:
        bib_database = bibtexparser.load(bib_file)
    return bib_database

# Function to remove duplicate entries from BibDatabase object
def remove_duplicates(bib_database):
    unique_entries = []
    seen_titles = set()  # To track titles

    for entry in bib_database.entries:
        title = entry.get('title', '').lower().strip()
        if title not in seen_titles:
            unique_entries.append(entry)
            seen_titles.add(title)
    
    return unique_entries

# Function to save the non-redundant .bib file
def save_bib_file(entries, output_file):
    db = bibtexparser.bibdatabase.BibDatabase()
    db.entries = entries
    
    writer = bibtexparser.bwriter.BibTexWriter()
    with open(output_file, 'w') as bib_file:
        bib_file.write(writer.write(db))

# Function to process input and output files
def process_bib_file(input_file, output_file):
    try:
        bib_database = load_bib_file(input_file)
        unique_entries = remove_duplicates(bib_database)
        save_bib_file(unique_entries, output_file)
        messagebox.showinfo("Success", f"Non-redundant bibliography saved to {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI Application
def create_app():
    # Create the main window
    root = tk.Tk()
    root.title("Bib Cleaner Tool")
    
    # Input file selection
    def select_input_file():
        file_path = filedialog.askopenfilename(filetypes=[("BibTeX files", "*.bib")])
        input_file_var.set(file_path)
    
    # Output file selection
    def select_output_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".bib", filetypes=[("BibTeX files", "*.bib")])
        output_file_var.set(file_path)
    
    # UI elements
    input_file_var = tk.StringVar()
    output_file_var = tk.StringVar()
    
    tk.Label(root, text="Select Input .bib File:").grid(row=0, column=0, padx=10, pady=10)
    tk.Entry(root, textvariable=input_file_var, width=50).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(root, text="Browse", command=select_input_file).grid(row=0, column=2, padx=10, pady=10)
    
    tk.Label(root, text="Select Output .bib File:").grid(row=1, column=0, padx=10, pady=10)
    tk.Entry(root, textvariable=output_file_var, width=50).grid(row=1, column=1, padx=10, pady=10)
    tk.Button(root, text="Save As", command=select_output_file).grid(row=1, column=2, padx=10, pady=10)
    
    tk.Button(root, text="Clean .bib File", command=lambda: process_bib_file(input_file_var.get(), output_file_var.get())).grid(row=2, column=1, pady=20)
    
    root.mainloop()

# Run the app
if __name__ == "__main__":
    create_app()
