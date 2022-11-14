import cv2
import numpy
src="images/0f42a3aeef3cb8bb9ecfeb08f68de466.jpg" #insert your image path
scaling = 50
# scaling value of the image size
def imagetotext(src,scaling=100):
    ima = cv2.imread(src)
    siz = numpy.shape(ima)
    o_hight = siz[0]
    o_width = siz[1]
    hight = int(o_hight * scaling / 100)
    width = int(o_width * scaling / 100)
    print(hight, width)
    for i in range(int(hight / 4) + 1):
        for j in range(int(width / 2) + 1):
            s = ""
            for k in range(4):
                for l in range(2):
                    x=int(((i * 4) + k)*100/scaling)
                    y=int(((j * 2) + l)*100/scaling)
                    if x < o_hight and y < o_width and sum(ima[x][y]) / 3 > 127:
                        s = s + "1"
                    else:
                        s = s + "0"
            s = s[0] + s[2] + s[4] + s[1] + s[3] + s[5] + s[6] + s[7]
            s = int(s, 2)
            if s == 0:
                print(chr(10241), end="")
            else:
                print(chr(10240 + s), end="")
        print("")

# .........................................................................................>
# if image is not black and white and has color below code some times may work better..

# def imagetotext(src,scaling):
#     ima = cv2.imread(src)
#     siz = numpy.shape(ima)
#     hight = siz[0]
#     width = siz[1]
#     hight = int(hight * scaling / 100)
#     width = int(width * scaling / 100)
#     ima = cv2.resize(ima, (width, hight))
#     # for i in ima:
#     #     print(i)
#     # print(hight, width)
#     for i in range(int(hight / 4) + 1):
#         for j in range(int(width / 2) + 1):
#             s = ""
#             for k in range(4):
#                 for l in range(2):
#                     if (i * 4) + k < hight and (j * 2) + l < width and sum(ima[(i * 4) + k][(j * 2) + l]) / 3 < 127:
#                         s = s + "1"
#                     else:
#                         s = s + "0"
#             s = s[0] + s[2] + s[4] + s[1] + s[3] + s[5] + s[6] + s[7]
#             s = int(s, 2)
#             if s == 0:
#                 print(chr(10241), end="")
#             else:
#                 print(chr(10240 + s), end="")
#         print("")


imagetotext(src,25)
