# import easyocr
# import pyautogui
# from PIL import ImageGrab
# import numpy as np
# import time

# # Initialize the EasyOCR reader
# reader = easyocr.Reader(['en'])  # You can specify other languages as needed

# def find_and_click(text_to_find):
#     # Capture the screen
#     screenshot = ImageGrab.grab()

#     # Convert the screenshot to a NumPy array
#     screenshot_np = np.array(screenshot)

#     # Use EasyOCR to do OCR on the screenshot
#     results = reader.readtext(screenshot_np)

#     # Check if the given text is in the results
#     for (bbox, text, prob) in results:
#         if text_to_find in text:
#             print(f"Found '{text_to_find}' on the screen.")
            
#             # Get the position of the text and click on it
#             x_center = int((bbox[0][0] + bbox[2][0]) / 2)
#             y_center = int((bbox[0][1] + bbox[2][1]) / 2)
#             pyautogui.click(x_center, y_center)
#             return
#     print(f"'{text_to_find}' not found.")
# import easyocr
# import pyautogui
# from PIL import ImageGrab
# import numpy as np
# import time

# # Initialize the EasyOCR reader
# reader = easyocr.Reader(['en'])  # You can specify other languages as needed

# def find_and_click(text_to_find):
#     # Capture the screen
#     screenshot = ImageGrab.grab()

#     # Convert the screenshot to a NumPy array
#     screenshot_np = np.array(screenshot)

#     # Use EasyOCR to do OCR on the screenshot
#     results = reader.readtext(screenshot_np)
#     print('me')
#     # Check if the given text is in the results
#     for (bbox, text, prob) in results:
#         if text_to_find in text:
#             print(f"Found '{text_to_find}' on the screen.")
            
#             # Get the position of the text and click on it
#             x_center = int((bbox[0][0] + bbox[2][0]) / 2)
#             y_center = int((bbox[0][1] + bbox[2][1]) / 2)
#             pyautogui.click(x_center, y_center)
#             return

import pytesseract
import pyautogui
from PIL import ImageGrab
import numpy as np

def find_and_click(text_to_find):
    # Split the search text into individual words
    search_words = text_to_find.lower().split()
    
    # Capture the screen
    screenshot = ImageGrab.grab()

    # Convert the screenshot to a NumPy array
    screenshot_np = np.array(screenshot)

    # Use pytesseract to do OCR on the screenshot
    data = pytesseract.image_to_data(screenshot_np, output_type=pytesseract.Output.DICT)

    # Initialize variables to track matching positions
    found_positions = []
    current_word_index = 0

    # Check each recognized text element
    for i, text in enumerate(data['text']):
        current_text = text.lower().strip()
        if current_text and current_word_index < len(search_words):
            if search_words[current_word_index] in current_text:
                # Store the position of the matched word
                found_positions.append({
                    'x': data['left'][i],
                    'y': data['top'][i],
                    'w': data['width'][i],
                    'h': data['height'][i]
                })
                current_word_index += 1

                # If all words are found
                if current_word_index == len(search_words):
                    # Calculate average position of all found words
                    total_x = sum(pos['x'] + pos['w']//2 for pos in found_positions)
                    total_y = sum(pos['y'] + pos['h']//2 for pos in found_positions)
                    avg_x = total_x // len(found_positions)
                    avg_y = total_y // len(found_positions)

                    print(f"Found '{text_to_find}' on the screen.")
                    pyautogui.click(avg_x, avg_y)
                    return

    print(f"'{text_to_find}' not found.")

# Example usage:
# find_and_click("Blank Documents")  # Will search for "blank" then "documents"