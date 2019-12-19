from PIL import Image, ImageFont, ImageDraw     # The pillow libraries used to create the image
image = Image.open('jason-leung-tZq8NkZ3T8k-unsplash.jpg')      # This is the image that will be edited

img_draw = ImageDraw.Draw(image)    # I use the Draw library to create the text from the font library on the image.

font = ImageFont.truetype('DejaVuSans.ttf', 500)    # This is the font and the size of the font
img_draw.text([350, 20], 'Random Taco Cookbook', fill='blue', font=font) # This is the font
image.thumbnail((500, 800)) # This adjusts the size of the image while keeping that aspect ratio

image.show() # This allows the image to show and view the modifications

image.save('Omega Taco.jpg') # Saves the image and creates a new taco image: an Omega Taco image :)
