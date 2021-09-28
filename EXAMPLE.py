
def main():
    build_house(100, 100, 200, 50)

def build_house(x, y, width, height):
    """рисует дом; (х,у) - позиция; width - ширина; height - высота"""

    build_walls(x, y, width, 2 * height // 3)
    build_roof(x, y, width, height // 3)
    w_height = 2 * height // 9
    w_width = width // 3
    build_window(x + w_width, y + w_height, w_width, w_height)

main()
