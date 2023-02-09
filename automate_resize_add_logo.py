import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logo_img = Image.open(LOGO_FILENAME)
logo_img = logo_img.resize((100,100))
logo_width, logo_height = logo_img.size

os.makedirs('withlogo', exist_ok=True)

for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue
    
    image = Image.open(filename)
    width, height = image.size
    
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE/width)*height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE/height)*width)
            height = SQUARE_FIT_SIZE
            
        print(f'resizing {filename}...')
        image = image.resize((width, height))
    
    if logo_width*2 < width and logo_height*2 < height:    
        image.paste(logo_img, (width - logo_width, height - logo_height), logo_img)
        image.save(os.path.join('withlogo', filename))