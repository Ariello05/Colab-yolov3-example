import os

folders = ['images']
path = r'D:\Data\temp\images'

n = 0
# for folder in folders:
for image in os.scandir("./"):
    n += 1
    if image.path == "./rename.py":
        print(image.path)
        continue

    str1 = image.path.split(' ')
    str2 = str1[1].split('.')
    str2[0] = str2[0][1:]
    final = "img" + str2[0] + "." + str2[1]
    print(final)
    os.rename(image.path, os.path.join(path, final))
