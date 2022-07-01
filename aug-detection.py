import cv2
import albumentations as A
import numpy as np
from utils import plot_examples
from PIL import Image

image = cv2.imread("images/cju0qkwl35piu0993l0dewei2.jpg")
mask = Image.open("masks/cju0qkwl35piu0993l0dewei2.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
bboxes = [[38, 5, 430, 338]]
SIZE=448
# Pascal_voc (x_min, y_min, x_max, y_max), YOLO, COCO

transform = A.Compose(
    [
        A.Resize(width=SIZE, height=SIZE),
        
        A.Rotate(limit=40, p=0.9, border_mode=cv2.BORDER_CONSTANT),
        A.HorizontalFlip(p=0.5),
        A.VerticalFlip(p=0.1),
        A.RGBShift(r_shift_limit=25, g_shift_limit=25, b_shift_limit=25, p=0.9),
        A.OneOf([
            A.Blur(blur_limit=3, p=0.5),
            A.ColorJitter(p=0.5),
        ], p=1.0),
    ], bbox_params=A.BboxParams(format="pascal_voc", min_area=2048,
                                min_visibility=0.3, label_fields=[])
)

images_list = [image]
saved_bboxes = [bboxes[0]]

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[2])/2.0
    y = (box[1] + box[3])/2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


for i in range(4):
    augmentations = transform(image=image, bboxes=bboxes)
    augmented_img = augmentations["image"]

    if len(augmentations["bboxes"]) == 0:
        continue

    images_list.append(augmented_img)
    print(augmentations["bboxes"][0])
    box = augmentations["bboxes"][0]
    size=[SIZE, SIZE]
    print(convert(size, box))
    saved_bboxes.append(augmentations["bboxes"][0])

plot_examples(images_list, saved_bboxes)


# def convert(size, box):
#     dw = 1./size[0]
#     dh = 1./size[1]
#     x = (box[0] + box[1])/2.0
#     y = (box[2] + box[3])/2.0
#     w = box[1] - box[0]
#     h = box[3] - box[2]
#     x = x*dw
#     w = w*dw
#     y = y*dh
#     h = h*dh
#     return (x,y,w,h)

# im=Image.open(img_path)
# w= int(im.size[0])
# h= int(im.size[1])


# print(xmin, xmax, ymin, ymax) #define your x,y coordinates
# b = (xmin, xmax, ymin, ymax)
# bb = convert((w,h), b)