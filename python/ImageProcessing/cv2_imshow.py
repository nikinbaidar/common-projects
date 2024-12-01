# cv2_imshow : local version of colab's imshow API
import cv2

def cv2_imshow(caption, image_path):
    cv2.imshow(caption, image_path)
    # After displaying an image wait until Escape (ASCII 27) is pressed. 
    while cv2.waitKey() != 27:
        continue
    cv2.destroyAllWindows()
    return None



image = cv2.imread("./output.jpg")
cv2_imshow("No ", image)
