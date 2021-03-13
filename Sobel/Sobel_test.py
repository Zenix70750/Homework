import cv2 as cv
def test():
    src = cv.imread("/home/yeeder/index3.jpg")
    src = cv.GaussianBlur(src, (3, 3), 0)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    grad_x = cv.Sobel(gray, -1, 1, 0, ksize=3)
    grad_y = cv.Sobel(gray, -1, 0, 1, ksize=3)
    
    grad  = cv.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)
    
    cv.imshow("origin",src)
    cv.imshow("grad",grad)
    cv.waitKey()
    
test()