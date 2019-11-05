from PIL import Image, ImageFilter

img = Image.open('Easter 2012 023.JPG')
img = img.rotate(90)
filtered_img =img.filter(ImageFilter.DETAIL)
filtered_img.save("detail.png", 'png')
filtered_img =img.convert('L')
filtered_img.save("grey.png", 'png')
small_img = img.resize((400, 300))
small_img.save('small.png', 'png')
small_img.thumbnail((100,100))
small_img.save('thumbnail.jpg')
print(img.size)
print(img.mode)
