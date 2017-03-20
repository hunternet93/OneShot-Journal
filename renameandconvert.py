import os
for filename in os.listdir('images'): os.system("convert images/{} -alpha on -transparent '#00ff00' images/{}.png".format(filename, filename[-6:-4].lower()))
