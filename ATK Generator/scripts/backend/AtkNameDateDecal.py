from cgitb import text
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

class Decal:
    """
    Renders ATK on instantiation
    """

    # ! Decal will be rendered on instantiation, no need to call additional functions!
    # * Constructor
    def __init__(self, name, date, img_dir_out, font_dir, font_size, custom_img_dir_in) -> None:
        
        self.img_dir_out = str(Path(img_dir_out).resolve())

        # ? Instantiates a new black image texture to draw on.
        self.img = Image.new(mode="RGB", size=(4096, 4096))
        self.draw = ImageDraw.Draw(self.img)
        self.draw.rectangle([(0, 0), self.img.size], fill=(0, 0, 0))

        # ? Whether the decal will be rendered using a custom image texture or rendered using text and font
        if custom_img_dir_in:
            # * render using custom image texture
            self.custom_img_dir_in: str = str(Path(custom_img_dir_in).resolve())

        else:
            # * render using custom text and font
            self.text_location = (0, 0)
            self.text: str = f"{name} {date}"
            self.font_dir: str = str(Path(font_dir).resolve())
            self.font_size: int = font_size  # ! When string is too long the font will shrink
            self.font = ImageFont.truetype(self.font_dir, self.font_size)

            # * call the drawing of the text
            self.render_atk_decal_text()

        # * save and update decal
        self.img.save(self.img_dir_out)
        
    # * Render decal image texture using text rendered using a font
    def render_atk_decal_text(self) -> None:
        """
        Render decal image texture using text rendered using a font
        """

        self.fix_x_trans()  # fixes negative x trans due to font

        # if text doesnt fit, make it fit image width
        if self.check_outofbounds():
            # Fit text
            self.text_fit_width()
            # text_location = center_align(img, draw, text_location, txt, font)

        # if it fits do not scale text, just center it
        # center align
        else:
            self.center_align()

        self.font = ImageFont.truetype(self.font_dir, self.font_size)
        print(self.draw.multiline_textbbox(self.text_location, text=self.text, align='center', font=self.font))
        self.draw.multiline_text(self.text_location, text=self.text, align='center', font=self.font, fill=(256, 256, 256), spacing=56)


    # * Render decal image texture using custom image
    def render_atk_decal_image(self) -> None:
        """
        Creates decal texture for atk test.
        """
        # Relative paths to aboslute paths
        self.img_dir_out = str(Path(self.img_dir_out).resolve())
        font_dir = str(Path(font_dir).resolve())

        img = Image.new(mode="RGB", size=(4096, 4096))
        draw = ImageDraw.Draw(img)

        # Reset image
        draw.rectangle([(0, 0), img.size], fill=(0, 0, 0))

        # Psuedocode
        """
        - take custom signature and make it into a PIL image.
        - find identfy the region where the text is
            - Use transparancy or maybe a certain color with a threshold.
        - scale the custom signature to an equivalent size of the font text
            - 
        """

        return None
        
    # * Helper methods, I want then to have 
    def text_fit_width(self):
        while 1:

            if self.draw.multiline_textbbox(self.text_location, text=self.text, align='center', font=self.font)[2] > self.img.size[0]:
                self.font_size -= 1
                self.font = ImageFont.truetype(self.font_dir, self.font_size)

            elif self.draw.multiline_textbbox(self.img_dir_out, text=self.text, align='center', font=self.font)[0] < 0:
                self.text_location = (self.text_location[0] + 1, self.text_location[1])
                self.font = ImageFont.truetype(self.font_dir, self.font_size)

            else:
                if self.draw.multiline_textbbox(self.text_location, text=self.text, align='center', font=self.font)[2] < self.img.size[0]:
                    self.font_size -= 1
                    self.font = ImageFont.truetype(self.font_dir, self.font_size)
                break

    def check_outofbounds(self) -> bool:
        """
        Checks if text is out of bounds of the picture
        """
        dimension = self.draw.multiline_textbbox(self.text_location, text=self.text, align='center', font=self.font)
        
        if dimension[2] > self.img.size[0] or dimension[0] < 0:
            return True

        return False


    def fix_x_trans(self):
        """
        Corrects for negative position of font
        """
        # Get Spacing
        self.text_location = list(self.text_location)
        spacings = self.draw.multiline_textbbox(self.text_location, text=self.text, align='center', font=self.font)
        x_trans = abs(spacings[0])

        self.text_location[0] += x_trans
        self.text_location = tuple(self.text_location)


    def center_align(self):
        """
        Aligns text to the center
        """
        
        # Get Spacing
        self.text_location = list(self.text_location)
        spacings = self.draw.multiline_textbbox(self.text_location, text=self.text, align='center', font=self.font)
        x_trans = (spacings[0] + (self.img.size[0] - spacings[2])) / 2

        self.text_location[0] += x_trans
        self.text_location = tuple(self.text_location)

# Testing Decal 
name = "Austin M."
date = '8-09-22'
img_dir_out = 'assets/atk_materials/atk_decal.png'
font_dir = 'assets/fonts/en/SkitserFineliner.ttf'
font_size = 300
custom_img_dir_in = ""


decal = Decal(name, date, img_dir_out, font_dir, font_size, custom_img_dir_in)




