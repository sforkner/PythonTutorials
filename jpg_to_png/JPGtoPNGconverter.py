import sys
import os
from PIL import Image

# grab first snd second arguments
JPGfolder = sys.argv[1]
PNGfolder = sys.argv[2]

# check if newimages/ exists, if not create it
if not os.path.exists(PNGfolder):
    os.makedirs(PNGfolder)

# loop through  JPGfolder
for filename in os.listdir(JPGfolder):
    img = Image.open(f'{JPGfolder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{PNGfolder}{clean_name}.png', 'png')
    print(f'Done {clean_name}')

print(" All Done")



