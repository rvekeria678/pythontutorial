# Flipping an Image

# Description: Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image. To flip an image horizontally means that each row of the image is reversed. For example, flipping [1,1,0] horizontally results in [0,1,1]. To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0,1,1] results in [1,0,0].

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]
            for b in range(len(image[i])):
                image[i][b] = image[i][b] ^ 1
        return image

s = Solution()

image = [[1,1,0],[1,0,1],[0,0,0]]

print(s.flipAndInvertImage(image))

image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

print(s.flipAndInvertImage(image))



