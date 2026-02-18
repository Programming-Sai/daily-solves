def flipAndInvertImage(image):
    return [[0 if x else 1 for x in image[r]][::-1] for r in range(len(image))]