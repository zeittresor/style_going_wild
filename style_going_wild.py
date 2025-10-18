#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generate Style to wildcard files from a CSV

CSV format (header optional, fields may be quoted):
    data1,data2,data3
    foo,"positive style","negative style"
    ...

The script opens a file‑chooser dialog, reads the selected CSV and creates
two files in a subfolder called `Generated_Styles`:

    Generated_Styles/prompt_styles.txt   – one line per entry in column data2
    Generated_Styles/negativ_styles.txt – one line per entry in column data3

Created by gpt-oss:20b for github.com/zeittresor

"""

import csv
import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox

# ---------------------------------------------------------------------------

class CSVGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Style CSV → Wildcard Files")
        self.geometry("485x180")
        self.resizable(False, False)

        # ----- GUI Widgets ---------------------------------------------------
        # 1. Label / Entry for the CSV path (read‑only)
        self.csv_path_var = tk.StringVar()
        csv_frame = ttk.Frame(self, padding=(10, 10))
        csv_frame.pack(fill=tk.X)

        ttk.Label(csv_frame, text="Selected CSV:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(csv_frame, textvariable=self.csv_path_var, width=50, state='readonly').grid(
            row=0, column=1, sticky=tk.W, padx=5
        )
        ttk.Button(csv_frame, text="Browse…", command=self.select_csv).grid(row=0, column=2, sticky=tk.W)

        # 2. Generate button
        btn_frame = ttk.Frame(self, padding=(10, 0))
        btn_frame.pack(fill=tk.X)
        ttk.Button(btn_frame, text="Generate", command=self.generate_styles).pack()

        # 3. Status / Info label
        self.status_var = tk.StringVar()
        ttk.Label(self, textvariable=self.status_var, foreground="blue").pack(pady=5)

    # -----------------------------------------------------------------------
    def select_csv(self):
        """Open file dialog and store selected CSV path."""
        file_path = filedialog.askopenfilename(
            title="Select CSV file",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
        )
        if file_path:
            self.csv_path_var.set(file_path)
            self.status_var.set("")

    # -----------------------------------------------------------------------
    def generate_styles(self):
        """Read CSV and write two style files."""
        csv_file = self.csv_path_var.get()
        if not csv_file:
            messagebox.showwarning("No CSV selected", "Select a CSV-File.")
            return

        # Destination folder
        dest_dir = Path("Generated_Styles")
        dest_dir.mkdir(exist_ok=True)

        # Output files
        prompt_file = dest_dir / "prompt_styles.txt"
        negative_file = dest_dir / "negativ_styles.txt"

        try:
            with open(csv_file, newline="", encoding="utf-8") as f_in, \
                 prompt_file.open("w", encoding="utf-8") as pf_out, \
                 negative_file.open("w", encoding="utf-8") as nf_out:

                reader = csv.reader(f_in)
                # Try to skip a header if it exists
                first_row = next(reader, None)
                if first_row is None:
                    raise ValueError("CSV is empty.")
                # Detect header by looking for non‑numeric values in the first column
                has_header = not all(cell.isdigit() for cell in first_row)

                if has_header:
                    # header exists – skip it
                    pass
                else:
                    # no header – treat first_row as data
                    pf_out.write(first_row[1] + "\n")
                    nf_out.write(first_row[2] + "\n")

                # Process remaining rows
                for row in reader:
                    # Defensive: skip incomplete rows
                    if len(row) < 3:
                        continue
                    pf_out.write(row[1] + "\n")
                    nf_out.write(row[2] + "\n")

            self.status_var.set(f"✅ Files created in '{dest_dir}'.")
        except Exception as exc:
            messagebox.showerror("Error while generating", f"Error:\n{exc}")

# ---------------------------------------------------------------------------

def main():
    app = CSVGeneratorApp()
    app.mainloop()

if __name__ == "__main__":
    main()
