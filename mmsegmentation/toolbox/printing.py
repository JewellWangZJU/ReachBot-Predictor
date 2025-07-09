from toolbox import color

def print_color(text, c="white"):
    color_code = getattr(color, c, color.white)
    print(color_code + text + color.reset)

def warn(text):
    print_color("WARNING: " + text, c="red")
