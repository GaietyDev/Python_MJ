from images import Image

image_list = ['smokey', 'moon', 'EagleNebula']

def noOperation():
    pass

def pointOperation(command, Q, image):
    print("\nProcessing image")
    transform(image, color2gray, Q)
    (_,f) = COMMANDS[command]
    transform(image, f, Q)
    print("Showing processed image")
    print('Close the image to continue')
    image.draw()

def transform(image, function, Q):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            image.setPixel(x,y, function(image.getPixel(x,y), Q))

def passThru(triple, Q):
    return triple

def color2gray(triple, Q):
    (r, g, b) = triple
    r = int(r * 0.299)
    g = int(g * 0.587)
    b = int(b * 0.114)
    lum = r + g + b
    return (lum, lum, lum)

def threshold(triple, Q):
    (r, g, b) = triple
    if r < Q:
        r = 0
        g = 0
        b = 0
    else:
        r = 255
        g = 255
        b = 255
    return (r, g, b)

def contrast(triple, Q):
    (r, g, b) = triple
    xlo = Q[0]
    xhi = Q[1]
    if r < xlo:
        r = 0
        g = 0
        b = 0
    elif r > xhi:
        r = 255
        g = 255
        b = 255
    else:
        r = 255 * (r - xlo)/ (xhi - xlo)
        g = r
        b = r
    return(r, g, b)

def falseColor(triple, Q):
    LUT = [(255,0,0),
           (255,201,14),
           (255,255,0),
           (0,255,0),
           (0,255,255),
           (0,0,255),
           (68,0,255),
           (255,0,255)
           ]
    (r, g, b) = triple
    foundIt = False
    for i in range(len(Q)):
        if r < Q[i]:
            r = LUT[i%len(LUT)][0]
            g = LUT[i%len(LUT)][1]
            b = LUT[i%len(LUT)][2]
            foundIt = True
            break
    if foundIt == False:
        r = LUT[0][0]
        g = LUT[0][1]
        b = LUT[0][2]
    return (r, g, b)

COMMANDS = {0:('QUIT', noOperation),
            1:('Original', noOperation),
            2:('Grayscale', passThru),
            3:('Thresholding', threshold),
            4:('Contrast', contrast),
            5:('False Color', falseColor)}

def printMenu():
    print("Key  Operation")
    print("----------------")
    for key, value in COMMANDS.items():
        print(f" {key} : {value[0]}")
    print("----------------")

def acceptCommand():
    user_input = int(input("Enter the key of an operation: "))
    if user_input in COMMANDS.keys():
        return user_input
    else:
        print("|! INVALD INPUT >>> PLEASE ENTER A VALID KEY !|\n")
        user_input = acceptCommand()
        return user_input

def runCommand(command, image):
    (operation,_) = COMMANDS[command]
    
    if operation == 'Original':
        print('Close the image to continue')
        image.draw()
        
    elif operation == 'Grayscale':
        Q = 0
        pointOperation(command, Q, image)
        
    elif operation == 'Thresholding':
        Q = int(input("Enter threshold: "))
        pointOperation(command, Q, image)
        
    elif operation == 'Contrast':
        xlo = int(input("Enter low limit: "))
        xhi = int(input("Enter high limit: "))
        Q = (xlo, xhi)
        pointOperation(command, Q, image)

    elif operation == 'False Color':
        v = input("Enter equipotential, <enter> when finished: ")
        Q = ()
        while v != "":
            Q = Q + (int(v),)
            v = input("Enter equipotential, <enter> when finished: ")
        pointOperation(command, Q, image)
        

def main():
    # Input Validation
    while True:
        image_name_input = input("Enter the name of the image file: ")
        image_name = image_name_input.strip('.gif')
        if image_name not in image_list:
            print("|! IMAGE NOT FOUND !|\n")
            continue
        
        image_name = image_name + '.gif'
        print(image_name)
        break

    
    try:
        while True:
            image = Image(image_name)
            printMenu()
            command = acceptCommand()
            if command == 0:
                print("\nDone")
                break
            runCommand(command, image)
    except KeyboardInterrupt:
        print("\nProgram Closed")
        
main()
