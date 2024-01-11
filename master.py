import easyocr


def is_text_present(image_path):
    """
    Check if there's any text present in the given image.

    Args:
    image_path (str): The file path to the image to be analyzed.

    Returns:
    bool: True if text is found, False otherwise.
    """
    # Initialize the OCR reader for the English language
    reader = easyocr.Reader(['en'])
    # Use OCR to read text from the image
    result = reader.readtext(image_path)
    # Return True if the result contains any text, False otherwise
    return len(result) > 0


# Test the function with an example image file
print(is_text_present('images/1.png'))
