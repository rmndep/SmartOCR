import pytesseract
import cv2

def extract_text_from_image(image_path):
    """
    Improved OCR with preprocessing
    """

    # Read image
    image = cv2.imread(image_path)

    # Resize (improves small text)
    image = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Remove noise
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Thresholding (B/W)
    _, thresh = cv2.threshold(gray, 0, 255,
                               cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # OCR configuration
    custom_config = r'--oem 3 --psm 6'

    text = pytesseract.image_to_string(
    thresh,
    config=custom_config,
    lang='eng+hin'
)



    return text
