# Number of Cans = ( Wall height * Wall width ) / coverage per can

def paint_calc(height,width,cover):
    print(f"Number of cans: {(height*width)/cover}")


test_height = int(input("Height of wall: "))
test_width = int(input("Width of wall: "))
coverage = int(input("Cover : "))
paint_calc(height=test_height, width=test_width, cover=coverage)