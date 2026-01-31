"""
File: mirror_lake.py
Name:Roger141
----------------------------------
This program reads the image “mt-rainier.jpg” and generates a 
new image that creates a mirror-lake effect by placing an 
inverted copy of the original image beneath it.
"""


from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:str
    :return:Simpleimage
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width,img.height*2)
    for y in range(img.height):
        for x in range(img.width):
            # b_img.set_rgb(x,y,imgP.red,imgP.green,imgP.blue)
            imgP = img.get_pixel(x,y)
            bP1 = b_img.get_pixel(x,y)
            bP1.red = imgP.red
            bP1.green = imgP.green
            bP1.blue = imgP.blue
            # b_img.set_rgb(x,b_img.height-1-y,imgP.red,imgP.green,imgP.blue)
            bP2 = b_img.get_pixel(x, b_img.height-1-y)
            bP2.red = imgP.red
            bP2.green = imgP.green
            bP2.blue = imgP.blue
    return b_img


def main():
    """
    Display the original image and the reflected mirror image.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
