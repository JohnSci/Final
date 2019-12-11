from PIL import Image, ImageFont, ImageDraw
image = Image.open('jason-leung-tZq8NkZ3T8k-unsplash.jpg')

img_draw = ImageDraw.Draw(image)

font = ImageFont.truetype('DejaVuSans.ttf', 500)
img_draw.text([350, 20], 'Random Taco Cookbook', fill='blue', font=font)
image.thumbnail((800, 800))

image.show()

image.save('Omega Taco.jpg')