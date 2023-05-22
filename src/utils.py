from PIL import Image



def remove_transparency(im, bg_colour=(255, 255, 255)):
    '''reomve alpha channel or convert black and white image to RGB'''
    
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
        alpha = im.convert('RGBA').split()[-1]
        bg = Image.new("RGB", im.size, bg_colour)
        bg.paste(im, mask=alpha)
        return bg
    elif im.mode == 'P':
        bg = Image.new("RGB", im.size, bg_colour)
        bg.paste(im)
        return bg
    else:
        return im