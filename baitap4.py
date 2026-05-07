import tkinter as tk
from tkinter import messagebox  # Thêm thư viện để hiện popup
import datetime                  # Thêm thư viện để lấy thời gian

def xu_ly_du_lieu():
    # 1. Lấy dữ liệu từ ô nhập
    mssv = o_nhap_ma_sv.get()
    ho_ten = o_nhap_ho_ten.get()
    
    # Lấy thời gian hiện tại
    thoi_gian = datetime.datetime.now().strftime("%H:%M:%S - %d/%m/%Y")
    
    # 2. Ràng buộc dữ liệu (Validation)
    # Kiểm tra trống
    if not mssv or not ho_ten:
        messagebox.showwarning("Cảnh báo", "Đừng để trống thông tin nhé!")
        return

    # Kiểm tra MSSV phải là số
    if not mssv.isdigit():
        messagebox.showerror("Lỗi nhập liệu", "MSSV phải là chữ số, sếp kiểm tra lại giúp!")
        nhan_ket_qua.config(text="Lỗi: MSSV không hợp lệ", fg="red")
        return

    # 3. Nếu mọi thứ ổn, xử lý tiếp
    # In ra Terminal kèm thời gian
    print(f"[{thoi_gian}] Dữ liệu nhận được: MSSV: {mssv} - Họ tên: {ho_ten}")
    
    # Cập nhật Label kết quả
    nhan_ket_qua.config(text=f"Chào sinh viên: {ho_ten} ({mssv})", fg="blue")
    
    # 4. Xóa trắng ô nhập sau khi thành công
    o_nhap_ma_sv.delete(0, tk.END)
    o_nhap_ho_ten.delete(0, tk.END)
    
    # Hiện thông báo thành công
    messagebox.showinfo("Thành công", "Đã ghi nhận thông tin điểm danh!")

# --- PHẦN GIAO DIỆN ---
root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("400x350")
root.columnconfigure(1, weight=1)

tk.Label(root, text="Mã sinh viên:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
o_nhap_ma_sv = tk.Entry(root)
o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Họ và tên:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
o_nhap_ho_ten = tk.Entry(root)
o_nhap_ho_ten.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

nut_xac_nhan = tk.Button(root, text="Xác nhận điểm danh", command=xu_ly_du_lieu)
nut_xac_nhan.grid(row=2, column=0, columnspan=2, pady=10)

nhan_ket_qua = tk.Label(root, text="Chưa có dữ liệu", font=("Arial", 10, "italic"))
nhan_ket_qua.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()