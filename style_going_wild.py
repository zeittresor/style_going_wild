#!/usr/bin/env python3
# Created using gpt-oss:20b for github.com/zeittresor

import csv
import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class CSVGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSV → Style Files")
        self.geometry("525x200")
        self.resizable(False, False)
        self.csv_path_var = tk.StringVar()
        frame_csv = ttk.Frame(self, padding=(10, 10))
        frame_csv.pack(fill=tk.X)
        ttk.Label(frame_csv, text="Selected CSV:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(frame_csv, textvariable=self.csv_path_var,
                  width=55, state='readonly').grid(row=0, column=1, sticky=tk.W, padx=5)
        ttk.Button(frame_csv, text="Browse…", command=self.select_csv).grid(row=0, column=2, sticky=tk.W)
        self.correct_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(self, text="Correct lines", variable=self.correct_var).pack(anchor=tk.W, padx=15, pady=(0, 5))
        self.integrated_var = tk.BooleanVar(value=True)
        self.integrated_cb = ttk.Checkbutton(self, text="Include integrated styles", variable=self.integrated_var)
        self.integrated_cb.pack(anchor=tk.W, padx=15)
        ttk.Button(self, text="Generate", command=self.generate_styles).pack(pady=5)
        self.status_var = tk.StringVar()
        ttk.Label(self, textvariable=self.status_var, foreground="blue").pack(pady=(5, 0))

    def select_csv(self):
        file_path = filedialog.askopenfilename(
            title="Select CSV file",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if file_path:
            self.csv_path_var.set(file_path)
            self.status_var.set("")
            integ_path = Path(file_path).parent / "styles_integrated.csv"
            if integ_path.exists():
                self.integrated_cb.config(state=tk.NORMAL)
            else:
                self.integrated_cb.config(state=tk.DISABLED)
                self.integrated_var.set(False)

    def generate_styles(self):
        csv_file = self.csv_path_var.get()
        if not csv_file:
            messagebox.showwarning("No CSV selected", "Please select a CSV file first.")
            return
        dest_dir = Path("Generated_Styles")
        dest_dir.mkdir(exist_ok=True)
        prompt_file = dest_dir / "01-prompt_styles.txt"
        negative_file = dest_dir / "02-negativ_styles.txt"
        integ_prompt_file = dest_dir / "03-prompt_integrated_styles.txt"
        integ_negative_file = dest_dir / "04-negativ_integrated_styles.txt"
        try:
            with open(csv_file, newline="", encoding="utf-8") as f_in, \
                 prompt_file.open("w", encoding="utf-8") as pf_out, \
                 negative_file.open("w", encoding="utf-8") as nf_out:
                reader = csv.reader(f_in)
                first_row = next(reader, None)
                if first_row is None:
                    raise ValueError("CSV file is empty.")
                has_header = not all(cell.strip().isdigit() for cell in first_row)
                if not has_header:
                    pf_out.write(first_row[1] + "\n")
                    nf_out.write(first_row[2] + "\n")
                for row in reader:
                    if len(row) < 3:
                        continue
                    pf_out.write(row[1] + "\n")
                    nf_out.write(row[2] + "\n")
            total_open = 0
            total_close = 0
            if self.correct_var.get():
                open_c, close_c = self.correct_file(prompt_file)
                total_open += open_c
                total_close += close_c
                self.clean_file(prompt_file)
                open_c, close_c = self.correct_file(negative_file)
                total_open += open_c
                total_close += close_c
                self.clean_file(negative_file)
            if self.integrated_var.get():
                integ_path = Path(csv_file).parent / "styles_integrated.csv"
                with open(integ_path, newline="", encoding="utf-8") as f_in, \
                     integ_prompt_file.open("w", encoding="utf-8") as pf_out, \
                     integ_negative_file.open("w", encoding="utf-8") as nf_out:
                    reader = csv.reader(f_in)
                    first_row = next(reader, None)
                    if first_row is None:
                        raise ValueError("Integrated CSV is empty.")
                    has_header = not all(cell.strip().isdigit() for cell in first_row)
                    if not has_header:
                        pf_out.write(first_row[1] + "\n")
                        nf_out.write(first_row[2] + "\n")
                    for row in reader:
                        if len(row) < 3:
                            continue
                        pf_out.write(row[1] + "\n")
                        nf_out.write(row[2] + "\n")
                if self.correct_var.get():
                    open_c, close_c = self.correct_file(integ_prompt_file)
                    total_open += open_c
                    total_close += close_c
                    self.clean_file(integ_prompt_file)
                    open_c, close_c = self.correct_file(integ_negative_file)
                    total_open += open_c
                    total_close += close_c
                    self.clean_file(integ_negative_file)
            status_msg = f"Files created in '{dest_dir}'. Corrections: {total_open} openings, {total_close} closings."
            self.status_var.set(status_msg)
        except Exception as exc:
            messagebox.showerror("Error", f"An error occurred:\n{exc}")

    @staticmethod
    def correct_file(file_path: Path):
        open_to_close = {"(": ")", "[": "]", "{": "}"}
        close_to_open = {v: k for k, v in open_to_close.items()}
        openings_added = 0
        closings_added = 0
        lines = file_path.read_text(encoding="utf-8").splitlines()
        corrected = []
        for line in lines:
            stack = []
            openings_needed = []
            for ch in line:
                if ch in open_to_close:
                    stack.append(ch)
                elif ch in close_to_open:
                    if stack and open_to_close[stack[-1]] == ch:
                        stack.pop()
                    else:
                        openings_needed.append(close_to_open[ch])
            closings_needed = [open_to_close[ch] for ch in reversed(stack)]
            openings_added += len(openings_needed)
            closings_added += len(closings_needed)
            corrected.append("".join(openings_needed) + line + "".join(closings_needed))
        file_path.write_text("\n".join(corrected) + ("\n" if corrected else ""), encoding="utf-8")
        return openings_added, closings_added

    @staticmethod
    def clean_file(file_path: Path):
        lines = file_path.read_text(encoding="utf-8").splitlines()
        seen = set()
        cleaned = []
        for line in lines:
            stripped = line.strip()
            if stripped and stripped not in seen:
                seen.add(stripped)
                cleaned.append(line)
        file_path.write_text("\n".join(cleaned) + ("\n" if cleaned else ""), encoding="utf-8")

def main():
    app = CSVGeneratorApp()
    app.mainloop()

if __name__ == "__main__":
    main()
