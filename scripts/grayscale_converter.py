from PIL import Image


def convert_image(input_image):
    """Gets a PIL image file and returns its grayscale version"""
    # Create a pillow image instance
    img = Image.open(input_image)
    # Convert the pillow image to grayscale
    gray_img = img.convert('L')
    return gray_img
