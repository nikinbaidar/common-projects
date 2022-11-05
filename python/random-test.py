import numpy as np

def getPSF(image, wanted_depth):
    x, y = image.shape[0],  image.shape[1]
    h, v = wanted_depth[0], wanted_depth[1]

    a = (h - x) // 2
    b = (v - y) // 2

    depth_x = (a, h - a - x)
    depth_y = (b, v -b - y)

    return np.pad(image, pad_width=(depth_x, depth_y))

def addPadding(image, borderType='zero|replicate', depth=(1,1)):
    """ Adding padding to images.
    * Args:
        image
        borderType = (str) zero or replicate
        depth = (int) padding depth
    """
    # h_pad -> x = add columns 
    # v_pad -> y = add rows

    def replicateBorder(image):
        h_pad_left = image[:,0].reshape(-1,1)
        h_pad_right = image[:,-1].reshape(-1,1)
        v_pad_up = np.hstack(([0], image[0,:], [0]))
        v_pad_down = np.hstack(([0], image[-1,:], [0]))
        image = np.hstack((h_pad_left, image, h_pad_right))
        image = np.vstack((v_pad_up, image, v_pad_down))
        return image


image = [[1, 2, 3], [4,5,6], [7,8,9]]
image = np.array(image)

wanted_shape = (23,24)

psf = getPSF(image, wanted_shape)
print(psf.shape)
print(psf)

# (5, 7)
