import tkinter as tk
from tkinter import filedialog
import zlib
import base64
import marshal

def decode_command(encoded_command):
    # Reverse the encoding process
    decoded_b64 = base64.b64decode(encoded_command[::-1])
    decompressed_data = zlib.decompress(decoded_b64[::-1])
    command = marshal.loads(decompressed_data)
    return command

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            encoded_command = file.read().strip()
            decoded_command = decode_command(encoded_command)
            exec(decoded_command)
            result_label.config(text="Command executed successfully.")

# Create the GUI
root = tk.Tk()
root.title("Decoding Tool")

upload_button = tk.Button(root, text="Upload File", command=upload_file)
upload_button.pack(pady=20)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
