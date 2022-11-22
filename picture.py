import cv2

def writeText(pixel, elem):
    (b, g, r) = pixel
    if(b % 2 == 0):
        if(int(elem) == 0):
            pass
        else:
            if(b < 255 ):
                b += 1
            else:
                b -= 1
    else:
        if (int(elem) == 1):
            pass
        else:
            if (b < 255):
                b += 1
            else:
                b -= 1
    return (b, g, r)

def shifr():
    img = cv2.imread('newtext.png')
    cv2.imshow('girl', img)
    cv2.waitKey(0)
    width = img.shape[1]
    height = img.shape[0]
    try:
        canals = img.shape[2]
    except:
        canals = 2
    print("Высота:"+str(img.shape[0]))
    print("Ширина:" + str(img.shape[1]))
    print("Количество каналов:" + str(img.shape[2]))
    print('Введите скрываемый текст')
    text = input()
    if(len(text) >= width * height):
        print('Слишком много текста')
        return
    binaryText = ''.join(format(c, 'b').zfill(8) for c in bytearray(text, "utf-8"))
    print(binaryText)
    for i in range (height):
        for j in range (width):
            if(i * j + j >= len(binaryText)):
                break
            img[i, j] = writeText(img[i, j], binaryText[i * j + j])
        if (i * j + j >= len(binaryText)):
            break

    # img[0, 0] = (255, 0, 0)
    # (b, g, r) = img[0, 0]
    # print("Красный: {}, Зелёный: {}, Синий: {}".format(r, g, b))
    cv2.imwrite('newtext1.png', img)

def findShifr():
    bitText = []
    imgWithShifr = cv2.imread('newtext1.png')
    height = imgWithShifr.shape[0]
    width = imgWithShifr.shape[1]
    try:
        canals = imgWithShifr.shape[2]
    except:
        canals = 2
    for i in range (height):
        for j in range (width):
            (b, g, r) = imgWithShifr[i,j]
            if (b % 2 == 0):
                bitText.append(0)
            else:
                bitText.append(1)
    resultText =''
    k = 0
    while k < len(bitText):
        bukva = 0
        for j in range(8):
            bukva += bitText[k] * (2**(7 - j))
            k+=1
        resultText += chr(bukva)

    with open("otus.txt", "w", encoding="utf-8") as file:
        file.write(resultText)



# shifr()
findShifr()
