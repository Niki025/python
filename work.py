import tkinter as tk
from tkinter import filedialog


def get_excel_file_path():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx;*.xls")])

    return file_path


if __name__ == "__main__":
    excel_file_path = get_excel_file_path()
    if excel_file_path:
        print("Selected Excel file path:", excel_file_path)
    else:
        print("No file selected.")
