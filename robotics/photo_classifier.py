from PIL import Image
import pytesseract

def extract_info_from_image(image_path):
    # Open the image
    image = Image.open(image_path)

    # Extract text using pytesseract
    extracted_text = pytesseract.image_to_string(image)

    # Print the extracted text
    print("Extracted Text:")
    print(extracted_text)

    # Additional information can be extracted here (e.g., objects, colors, etc.)

if __name__ == "__main__":
    image_path = "./test.JPG"
    extract_info_from_image(image_path)
