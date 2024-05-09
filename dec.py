import marshal

def decode_file(encoded_file):
    with open(encoded_file, 'rb') as f:
        encoded_data = f.read()

    # Assuming the encoded data starts with the header and the bytecode
    header_size = 8  # Size of the header in bytes
    bytecode = encoded_data[header_size:]

    try:
        # Unmarshal the bytecode to obtain the code object
        code_obj = marshal.loads(bytecode)
        exec(code_obj)  # Execute the code object
    except Exception as e:
        print("Error decoding and executing the encoded file:", e)

# Usage
if __name__ == "__main__":
    encoded_file = "/sdcard/Download/test_enc.py"
    decode_file(encoded_file)
