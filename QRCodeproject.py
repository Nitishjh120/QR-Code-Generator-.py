import qrcode
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox


def generate_qr_code():
    data = entry_data.get()
    if not data:
        messagebox.showerror("Error", "Please enter data to generate QR Code.")
        return

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill="black", back_color="white")
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
    )
    if save_path:
        qr_img.save(save_path)
        messagebox.showinfo("Success", f"QR Code saved successfully at {save_path}!")


# GUI setup
root = Tk()
root.title("QR Code Generator")

Label(root, text="Enter Data:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_data = Entry(root, width=40, font=("Arial", 12))
entry_data.grid(row=0, column=1, padx=10, pady=10)

Button(root, text="Generate QR Code", command=generate_qr_code, bg="blue", fg="white", font=("Arial", 12)).grid(
    row=1, column=0, columnspan=2, pady=10
)

root.mainloop()
