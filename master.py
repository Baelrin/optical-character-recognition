import easyocr


def is_text_present(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)
    return len(result) > 0


print(is_text_present('images/1.png'))
