from rembg import remove
from PIL import Image
import cv2
input_path = 'input.jpg' 
output_path = 'output.png' 
input = Image.open(input_path)
output = remove(input) 
output.save(output_path) # save 