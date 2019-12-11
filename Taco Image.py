from PIL import Image, ImageFont, ImageDraw     #The pillow libraries used to create the image
image = Image.open('jason-leung-tZq8NkZ3T8k-unsplash.jpg')      #This is the image that will be edited

img_draw = ImageDraw.Draw(image)    #I use the Draw library to create the text from the font library on the image.

font = ImageFont.truetype('DejaVuSans.ttf', 500)    #This is the font and the size of the font
img_draw.text([350, 20], 'Random Taco Cookbook', fill='blue', font=font)
image.thumbnail((800, 800))

image.show()

image.save('Omega Taco.jpg')