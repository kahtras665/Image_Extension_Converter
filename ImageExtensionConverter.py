from PIL import Image
imageName_extension= input("Enter image along with its extension- ")
convertedImageName_convertedExtension= input("Enter converted image name along with its converted extension- ")
img= Image.open(imageName_extension) # opening the original file before conversion
img.save(convertedImageName_convertedExtension) # saving the image file after conversion
print("Successfully saved!")