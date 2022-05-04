#PIL image library
from PIL import Image 

#define ascii list
ASCII_CHARS = ["@", "#", "$","%", "?", "+", "*", ";", ":", ",", "."]

#resize image according to a new width
def resize(image, new_width=300):
    width, height = image.size #specify width and height attributes
    ratio = height/width #aspect ratio
    new_height = new_width * ratio * 0.5 #new height resizes according to ratio
    return image.resize((new_width, int(new_height))) #resizes image according to new width and height
        
#convert image to greyscale with L option
def to_grayscale(image):
    return image.convert("L")

#convert greyscale image to ASCII characters
def pixels_to_ascii(image): 
    pixels = image.getdata() #extracts the pixel values
    characters = ""
    for pixel in pixels:
        characters += ASCII_CHARS[pixel//25]
    return (characters)

#define main sequence
def main(new_width=300):
    #attempt to open image file (with validation)
    path = input("Enter the path name to the image file:\n")
    try:
        image = Image.open(path) #opens image path
    except:
        print(path, "Unable to find image"); 
        return

    #convert image to ascii
    new_image_data = pixels_to_ascii(to_grayscale(resize(image)))

    #format
    pixel_count = len(new_image_data) #return the number of items in a container
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])

    #print result 
    print(ascii_image)

    #Save the result to a file
    with open("ascii_image.txt", "w") as f: #open file with mode as "w" to create a stream from file for writing
        f.write(ascii_image) #writes over ascii image to textfile

#run program
main()