from PIL import Image, ImageDraw



def base_image_gen(x:int, y:int, color=255, fp=None):
    img = Image.new("RGBA", (x, y), color)
    img.show()


if __name__ == "__main__":
    base_image_gen(x=1200, y=680)
    