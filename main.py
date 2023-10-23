import qrcode
from tkinter import Tk, Label, Button, Entry, filedialog

def generate_qr():
    data = url_entry.get()
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        img.save(file_path)

app = Tk()
app.title("QR Code Generator")

url_label = Label(app, text="Enter URL:")
url_label.pack(pady=10)

url_entry = Entry(app)
url_entry.pack(pady=10, padx=10, fill="both")

generate_button = Button(app, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=20)

app.mainloop()
