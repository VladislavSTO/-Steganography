import cv2
from path import Path
from qrcodegenerator import gen_qr_code
import numpy as np


# text = "Тут могла быть ваша реклама"
# path_to_download = Path().joinpath("cat.png")  # Путь до фона qr кода
# path_to_save = Path().joinpath("catWithQR.png")  # Куда сохранять результат и под каким именем (обязательно в png)

# gen_qr_code(text, path_to_download, path_to_save)

def changeValue(value):
    if (value < 255):
        value += 1
    else:
        value -= 1
    return value

def writeText(pixel, elem):
    (b, g, r) = pixel
    if(b % 2 == 0):
        if(int(elem) == 0):
            pass
        else:
            b = changeValue(b)
    else:
        if (int(elem) == 1):
            pass
        else:
            b = changeValue(b)
    return (b, g, r)

def writeQRCode(writablePixel, sourcePixel):
    (b_writable, g_writable, r_writable) = writablePixel
    if (sourcePixel == 0):
        if( g_writable % 2 == 0):
            pass
        else:
            g_writable = changeValue(g_writable)
    else:
        if (g_writable % 2 != 0):
            pass
        else:
            g_writable = changeValue(g_writable)
    return (b_writable, g_writable, r_writable)


def shifr(img_file, text, download_path, save_path, path_to_res):
    path_to_download = Path().joinpath(download_path)  # Путь до фона qr кода
    path_to_save = Path().joinpath(save_path)  # Куда сохранять результат и под каким именем (обязательно в png)

    gen_qr_code("Здесь могла быть ваша реклама", path_to_download, path_to_save)
    # img = cv2.imread('newtext.png')
    img = cv2.imread(img_file)
    width = img.shape[1]
    height = img.shape[0]
    try:
        canals = img.shape[2]
    except:
        canals = 2
    # print("Высота:"+str(img.shape[0]))
    # print("Ширина:" + str(img.shape[1]))
    # print("Количество каналов:" + str(img.shape[2]))
    # text = input('Введите скрываемый текст: ')
    # if(len(text) >= width * height):
    #     print('Слишком много текста')
    #     return
    binaryText = ''.join(format(c, 'b').zfill(8) for c in bytearray(text, "utf-8"))
    # imgWithQRCode = cv2.imread('catWithQR.png', cv2.IMREAD_GRAYSCALE)
    imgWithQRCode = cv2.imread(save_path, cv2.IMREAD_GRAYSCALE)

    # # define a threshold, 128 is the middle of black and white in grey scale
    thresh = 128
    img_binary = cv2.threshold(imgWithQRCode, thresh, 255, cv2.THRESH_BINARY)[1]
    dsize = (width, height)
    output = cv2.resize(img_binary, dsize, interpolation = cv2.INTER_AREA)
    for i in range (height):
        for j in range (width):
            if(i * j + j < len(binaryText)):
                img[i, j] = writeText(img[i, j], binaryText[i * j + j])
            img[i, j] = writeQRCode(img[i, j], output[i, j])

    # cv2.imwrite('result.png', img)
    cv2.imwrite(path_to_res, img)

def findShifr(path_to_res, length = -1):
    bitText = []
    # imgWithShifr = cv2.imread('result.png')
    imgWithShifr = cv2.imread(path_to_res)
    height = imgWithShifr.shape[0]
    width = imgWithShifr.shape[1]
    try:
        canals = imgWithShifr.shape[2]
    except:
        canals = 2
    binarryImage = np.zeros((height, width), np.uint8)
    for i in range (height):
        for j in range (width):
            (b, g, r) = imgWithShifr[i,j]
            if (b % 2 == 0):
                bitText.append(0)
            else:
                bitText.append(1)
            if (g % 2 == 0):
                binarryImage[i, j] = 0
            else:
                binarryImage[i, j] = 255
    resultText =''
    k = 0
    if length == -1:
        length = len(bitText)
    else:
        length = 8 * length
    while k < length:
        bukva = 0
        for j in range(8):
            bukva += bitText[k] * (2**(7 - j))
            k+=1
        resultText += chr(bukva)

    with open("hiddentext.txt", "w", encoding="utf-8") as file:
        file.write(resultText)
    cv2.imwrite('hiddencode.png', binarryImage)


# shifr()
# findShifr()
