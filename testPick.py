import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime

# Kết nối tới cơ sở dữ liệu
conn = sqlite3.connect('upcase.db')
c = conn.cursor()

# Tạo bảng nếu chưa tồn tại


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Datetime Picker Application")

# Hàm lưu dữ liệu vào cơ sở dữ liệu
def save_data():
    name = name_entry.get()
    profession = profession_entry.get()
    company = company_entry.get()
    status = status_entry.get()
    birthday = birthday_entry.get_date().strftime('%Y-%m-%d')
    
    # Chèn dữ liệu vào bảng
    c.execute("UPDATE Profile SET name = ?, profession = ?, company = ?, status = ?, birth = ? WHERE id = 1", 
              (name, profession, company, status, birthday))
    conn.commit()
    messagebox.showinfo("Info", "Data saved successfully!")

# Hàm hiển thị dữ liệu từ cơ sở dữ liệu
def display_data():
    c.execute("SELECT * FROM Profile")
    rows = c.fetchall()
    display_text = ""
    for row in rows:
        display_text += f"ID: {row[0]}, Name: {row[2]}, Profession: {row[3]}, Company: {row[4]}, Status: {row[5]}, Birthday: {row[6]}\n"
    data_display.delete(1.0, tk.END)
    data_display.insert(tk.END, display_text)

# Tạo các nhãn và trường nhập liệu
tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Profession:").grid(row=1, column=0)
profession_entry = tk.Entry(root)
profession_entry.grid(row=1, column=1)

tk.Label(root, text="Company:").grid(row=2, column=0)
company_entry = tk.Entry(root)
company_entry.grid(row=2, column=1)

tk.Label(root, text="Status:").grid(row=3, column=0)
status_entry = tk.Entry(root)
status_entry.grid(row=3, column=1)

tk.Label(root, text="Birthday:").grid(row=4, column=0)
birthday_entry = DateEntry(root, date_pattern='dd-mm-yyyy')
birthday_entry.grid(row=4, column=1)

# Tạo nút lưu và hiển thị dữ liệu
save_button = tk.Button(root, text="Save Data", command=save_data)
save_button.grid(row=5, column=0, pady=10)

display_button = tk.Button(root, text="Display Data", command=display_data)
display_button.grid(row=5, column=1, pady=10)

# Tạo hộp văn bản để hiển thị dữ liệu
data_display = tk.Text(root, height=10, width=50)
data_display.grid(row=6, column=0, columnspan=2, pady=10)

# Chạy ứng dụng
root.mainloop()

# Đóng kết nối cơ sở dữ liệu khi ứng dụng kết thúc
conn.close()
