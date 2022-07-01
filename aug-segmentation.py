import cv2
import albumentations as A
import numpy as np
from utils import plot_examples
from PIL import Image

image = Image.open("images/cju0qkwl35piu0993l0dewei2.jpg")
mask = Image.open("masks/cju0qkwl35piu0993l0dewei2.jpg")
mask2 = Image.open("masks/cju0qkwl35piu0993l0dewei2.jpg")

transform = A.Compose(
    [
        A.Resize(width=448, height=448),
        A.RandomCrop(width=440, height=440),
        A.Rotate(limit=40, p=0.9, border_mode=cv2.BORDER_CONSTANT),
        A.HorizontalFlip(p=0.5),
        A.VerticalFlip(p=0.1),
        A.RGBShift(r_shift_limit=25, g_shift_limit=25, b_shift_limit=25, p=0.9),
        A.OneOf([
            A.Blur(blur_limit=3, p=0.5),
            A.ColorJitter(p=0.5),
        ], p=1.0),
    ]
)

images_list = [image,mask]
image = np.array(image)
mask = np.array(mask) # np.asarray(mask), np.array(mask)
mask2 = np.array(mask2)
for i in range(5):
    print(len(images_list))
    augmentations = transform(image=image, masks=[mask])
    augmented_img = augmentations["image"]
    augmented_masks = augmentations["masks"]
    images_list.append(augmented_img)
    images_list.append(augmented_masks[0])
    #images_list.append(augmented_masks[1])
plot_examples(images_list)