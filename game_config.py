import os

image_size = 128
screen_size = 512
tile_in_line = 4
total_tiles = 16
margin = 4
assets_dir = 'assests'

assests_files = [x for x in os.listdir(assets_dir) if x[-3:].lower() == 'png']

assert len(assests_files) == 8