from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk

root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir='/Users/macbook/Downloads', title='Select an Image:')


# print(filename)


def add_watermark(image, wm_text):
    # Creates the Image object
    opened_image = Image.open(image)

    # Get Image size
    image_width, image_height = opened_image.size

    # Draw on Image
    draw = ImageDraw.Draw(opened_image)

    # Specify a font size
    font_size = int(image_width / 8)

    # For Windows, change font type to 'arial'
    font = ImageFont.truetype('Arial.ttf', font_size)

    # Coordinates for where we want the image
    x, y = int(image_width / 2), int(image_height / 2)

    # Add the watermark
    draw.text((x, y), wm_text, font=font, fill='#FFF', stroke_width=5, stroke_fill='#222', anchor='ms')

    # Show the new image
    opened_image.show()


add_watermark(filename, 'website.com')
