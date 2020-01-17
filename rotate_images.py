# http://automatetheboringstuff.com/2e/chapter10/
# http://automatetheboringstuff.com/2e/chapter19/
# https://www.daveperrett.com/articles/2012/07/28/exif-orientation-handling-is-a-ghetto/
# https://stackoverflow.com/questions/4764932/in-python-how-do-i-read-the-exif-data-for-an-image

import os
from PIL import Image
from PIL import ExifTags

# key: orientation, value: degrees (counterclockwise)
rotation = {1:0, 2:0, 3:180, 4:180, 5:270, 6:270, 7:90, 8:90}

for image in os.listdir('.'):
    if image == 'rotate_images.py' or image == 'rotate_images.bat':
        continue
    curr_img = Image.open(image)
    orientation = curr_img._getexif()[274] # get image orientation
    if orienation == 1:
        continue
    # flip first, then rotate for certain orientations
    if orientation in [2, 4, 5, 7]:
        if orientation % 2 == 0:
            curr_img.transpose(Image.FLIP_LEFT_RIGHT).rotate(rotation[orientation], expand=True).save(image)
        else:
            curr_img.transpose(Image.FLIP_TOP_BOTTOM).rotate(rotation[orientation], expand=True).save(image)
    else:
        curr_img.rotate(rotation[orientation], expand=True).save(image)

