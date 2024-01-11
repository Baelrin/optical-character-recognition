import easyocr
import torch


def is_text_present(image_path):
    """
    Check if there's any text present in the given image.

    Args:
    image_path (str): The file path to the image to be analyzed.

    Returns:
    bool: True if text is found, False otherwise.
    """
    # Initialize the OCR reader for the English language using the GPU if available
    reader = easyocr.Reader(['en'], gpu=torch.cuda.is_available())
    # Use OCR to read text from the image
    result = reader.readtext(image_path, detail=0)
    # Check if the list of strings is non-empty
    return bool(result)


# Test the function with an example image file, taking into account GPU availability
print(is_text_present('images/1.png'))
