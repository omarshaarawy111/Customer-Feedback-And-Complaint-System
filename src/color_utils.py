import colorsys
import matplotlib.colors as mc

def adjust_color_lightness(color, amount=0.5):
    try:
        c = mc.cnames[color] if color in mc.cnames else color
        c = colorsys.rgb_to_hls(*mc.to_rgb(c))
        return colorsys.hls_to_rgb(c[0], max(0, min(1, amount * c[1])), c[2])
    except:
        return color

def rgb_to_hex(rgb):
    return '#' + ''.join([f'{int(x*255):02x}' for x in rgb])

def generate_color_palette(base_color, num_colors=15):
    colors = [base_color]
    for i in range(1, num_colors):
        lightness_factor = 1.0 - (i * 0.06)
        new_color = adjust_color_lightness(base_color, lightness_factor)
        colors.append(rgb_to_hex(new_color))
    return colors

