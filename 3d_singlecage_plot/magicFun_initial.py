cage = [
    [1, 2, 5, 7, 9, 51, 53, 55, 57, 91, 93, 95, 97, 131, 133, 135, 137, 171, 173, 175, 177, 211, 213, 215, 217, 251,
     253, 255, 257, 291, 293, 295],
    [4, 3, 6, 8, 10, 52, 54, 56, 58, 92, 94, 96, 98, 132, 134, 136, 138, 172, 174, 176, 178, 212, 214, 216, 218, 252,
     254, 256, 258, 292, 294, 296],
    [12, 11, 13, 14, 15, 59, 60, 61, 62, 99, 100, 101, 102, 139, 140, 141, 142, 179, 180, 181, 182, 219, 220, 221, 222,
     259, 260, 261, 262, 297, 298, 299],
    [17, 16, 18, 19, 20, 63, 64, 65, 66, 103, 104, 105, 106, 143, 144, 145, 146, 183, 184, 185, 186, 223, 224, 225, 226,
     263, 264, 265, 266, 300, 301, 302],
    [22, 21, 23, 24, 25, 67, 68, 69, 70, 107, 108, 109, 110, 147, 148, 149, 150, 187, 188, 189, 190, 227, 228, 229, 230,
     267, 268, 269, 270, 303, 304, 305],
    [27, 26, 28, 29, 30, 71, 72, 73, 74, 111, 112, 113, 114, 151, 152, 153, 154, 191, 192, 193, 194, 231, 232, 233, 234,
     271, 272, 273, 274, 306, 307, 308],
    [32, 31, 39, 43, 47, 75, 79, 83, 87, 115, 119, 123, 127, 155, 159, 163, 167, 195, 199, 203, 207, 235, 239, 243, 247,
     275, 279, 283, 287, 309, 313, 317],
    [34, 33, 40, 44, 48, 76, 80, 84, 88, 116, 120, 124, 128, 156, 160, 164, 168, 196, 200, 204, 208, 236, 240, 244, 248,
     276, 280, 284, 288, 310, 314, 318],
    [36, 35, 41, 45, 49, 77, 81, 85, 89, 117, 121, 125, 129, 157, 161, 165, 169, 197, 201, 205, 209, 237, 241, 245, 249,
     277, 281, 285, 289, 311, 315, 319],
    [38, 37, 42, 46, 50, 78, 82, 86, 90, 118, 122, 126, 130, 158, 162, 166, 170, 198, 202, 206, 210, 238, 242, 246, 250,
     278, 282, 286, 290, 312, 316, 320],
]


def drawCageH(nodePosition, handle):
    '''
    :param nodePosition:  a n*3 numpy array. n is the number of node.
    :param handle: the handle to plot the figure.
    :return: plot the horizontal lines.
    '''
    xs = []
    ys = []
    zs = []
    for i in range(0, 10):
        for j in range(0, 32):
            xs.append(nodePosition[cage[i][j]][0])
            ys.append(nodePosition[cage[i][j]][1])
            zs.append(nodePosition[cage[i][j]][2])
        xs.append(nodePosition[cage[i][0]][0])
        ys.append(nodePosition[cage[i][0]][1])
        zs.append(nodePosition[cage[i][0]][2])
        handle.plot(xs, ys, zs, color='grey', alpha=0.8)
        xs = []
        ys = []
        zs = []
    handle.scatter(nodePosition[0][0], nodePosition[0][1], nodePosition[0][2], color='grey', alpha=0.8)


def drawCageV(nodePosition, handle):
    '''
    :param nodePosition: a n*3 numpy array. n is the number of node.
    :param handle: the handle to plot the figure.
    :return: plot the vertical lines.
    '''
    xs = []
    ys = []
    zs = []
    for j in range(0, 32):
        for i in range(0, 10):
            xs.append(nodePosition[cage[i][j]][0])
            ys.append(nodePosition[cage[i][j]][1])
            zs.append(nodePosition[cage[i][j]][2])
        xs.append(nodePosition[0][0])
        ys.append(nodePosition[0][1])
        zs.append(nodePosition[0][2])
        handle.plot(xs, ys, zs, color='grey', alpha=0.8)
        xs = []
        ys = []
        zs = []
