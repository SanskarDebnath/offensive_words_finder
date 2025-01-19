from PIL import Image
def retrieve_message(image_path):
    image = Image.open(image_path)
    pixels = image.load()
    binary_message = ""
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]
            binary_message += str(r & 1)
    binary_chars = [binary_message[i:i + 8] for i in range(0, len(binary_message), 8)]
    message = ""
    for binary_char in binary_chars:
        if binary_char == "11111110":
            break
        message += chr(int(binary_char, 2))

    print("Hidden message retrieved:", message)
    return message

retrieve_message("decryptit.png")
