from PIL import Image
def hide_message(image_path, message, output_path):
    image = Image.open(image_path)
    image = image.convert("RGB")
    pixels = image.load()
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'

    if len(binary_message) > image.width * image.height:
        raise ValueError("Message is too long to hide in this image.")

    message_index = 0
    for y in range(image.height):
        for x in range(image.width):
            if message_index < len(binary_message):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary_message[message_index])
                message_index += 1
                pixels[x, y] = (r, g, b)
            else:
                break
    image.save(output_path)
    print(f"Message hidden in {output_path} successfully!")
message = "Hi whatsup!! Did you decrypt it?"
hide_message("inputy.jpeg", message, "decryptit.png")
