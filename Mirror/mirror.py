TOP_LEFT = "┏"
TOP_CENTER = "┳"
TOP_RIGHT = "┓"

HORIZONTAL_LINE = "━"
MIDDLE_LEFT = "┣"
MIDDLE_CENTER = "╋"
MIDDLE_RIGHT = "┫"
VERTICAL_LINE = "┃"

BOTTOM_LEFT = "┗"
BOTTOM_CENTER = "┻"
BOTTOM_RIGHT = "┛"

SYMBOL_1 = "▫"  # bagian luar belah ketupat
SYMBOL_2 = " "  # bagian dalam belah ketupat
SYMBOL_3 = "▪"  # garis batas belah ketupat

LIMIT = 15  # membatasi bangun supaya tidak terlalu besar
MULTIPLIER = 2  # pengali sederhana untuk mengatur lebar bangun


def draw_top(size):  # menggambar bagian atas
    print(TOP_LEFT + HORIZONTAL_LINE*size*MULTIPLIER +
          TOP_CENTER + HORIZONTAL_LINE*size*MULTIPLIER + TOP_RIGHT)


def draw_main(size):  # menggambar bagian tengah
    list1 = list(range(0, size + 1))
    list2 = list(range(size - 1, -1, -1))
    for line in (list1+list2):
        if line == size:
            print(MIDDLE_LEFT + HORIZONTAL_LINE*size*MULTIPLIER +
                  MIDDLE_CENTER + HORIZONTAL_LINE*size*MULTIPLIER + MIDDLE_RIGHT)
        else:
            print(VERTICAL_LINE + SYMBOL_1*((size-line)*MULTIPLIER-1) + SYMBOL_3 + SYMBOL_2*line*MULTIPLIER +
                  VERTICAL_LINE + SYMBOL_2*((size-line)*MULTIPLIER-1) + SYMBOL_3 + SYMBOL_1*(line*MULTIPLIER) + VERTICAL_LINE)


def draw_bottom(size):  # menggambar bagian bawah
    print(BOTTOM_LEFT + HORIZONTAL_LINE*size*MULTIPLIER +
          BOTTOM_CENTER + HORIZONTAL_LINE*size*MULTIPLIER + BOTTOM_RIGHT)


def draw_shape(size):  # menggambar bangun
    draw_top(size)
    draw_main(size)
    draw_bottom(size)


def input_size():  # melakukan input
    size = int(input("Input a positive integer: "))
    if (size < 1):
        return 1
    elif (size > LIMIT):
        return LIMIT
    else:
        return size


size = input_size()
draw_shape(size)
