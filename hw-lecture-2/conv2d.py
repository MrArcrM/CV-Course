
import numpy as np

def medianBlur(img, kernel, padding_way, padding_size):
    kernel = np.array(kernel)
    k_h, k_w = kernel.shape
    img = np.array(img)
    h, w = img.shape
    if padding_way.lower() == 'zero':
        new_img = np.zeros((h + 2*padding_size, w + 2*padding_size))
        new_img[padding_size : h+padding_size, padding_size : w+padding_size] = img

    if padding_way.lower() == 'replica':
        new_img = np.zeros((h + 2*padding_size, w + 2*padding_size))
        new_img[padding_size : h+padding_size, padding_size : w+padding_size] = img
        # up
        new_img[0 : padding_size, padding_size : w+padding_size] = img[0, 0:w]
        # left
        new_img[padding_size : h+padding_size, 0 : padding_size] = \
            np.tile(img[0:h, 0][:, np.newaxis], (padding_size,))
        # down
        new_img[padding_size:h+padding_size, padding_size:w+padding_size] = img[h-1, 0:w]
        # right
        new_img[padding_size:h+padding_size, w+padding_size:w+padding_size*2] = \
            np.tile(img[0:h, w-1][:, np.newaxis], (padding_size,))
        # leftup
        new_img[0:padding_size, 0:padding_size] = img[0,0]
        # rightup
        new_img[0:padding_size, w+padding_size:w+padding_size*2] = img[0,w-1]
        # leftdown
        new_img[h+padding_size:h+padding_size*2, 0:padding_size] = img[h-1,0]
        # rightdown
        new_img[h+padding_size:h+padding_size*2, w+padding_size:w+padding_size*2] = img[h-1, w-1]

    new_h = h + 3 - k_h
    new_w = w + 3 - k_w

    median_img = np.zeros((new_h, new_w))
    for i in range(new_h):
        for j in range(new_w):
            median_img[i, j] = int(np.median(new_img[i+padding_size-k_h//2 : i+padding_size+k_h//2,
                                             j+padding_size-k_w//2 : j+padding_size+k_w//2]))

    print('Median_img is: \n', median_img)

a = [[1,2,3],[3,4,4],[7,8,9]]
b = np.array(a)
print("median kernel shape is: ",b.shape)
medianBlur(a,b,'replica',1)








