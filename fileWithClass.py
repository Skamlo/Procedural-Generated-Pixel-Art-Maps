import numpy as np
from PIL import Image
from perlin_noise import PerlinNoise
import math

class mapGenerator:
    sea = {'base': ['img/sea/sea.png', 0.85],
           'waves': ['img/sea/sea_waves.png', 0.1],
           'rock': ['img/sea/sea_rock.png', 0.05],
           '0': ['img/sea/sea.png', 0.85],
           '1': ['img/sea/sea_waves.png', 0.1],
           '2': ['img/sea/sea_rock.png', 0.05]}
    sea_beach = {'left': 'img/sea_beach/sea_beach_left.png',
                 'top': 'img/sea_beach/sea_beach_top.png',
                 'right': 'img/sea_beach/sea_beach_right.png',
                 'bottom': 'img/sea_beach/sea_beach_bottom.png',
                 'left_top': 'img/sea_beach/sea_beach_left_top.png',
                 'right_top': 'img/sea_beach/sea_beach_right_top.png',
                 'right_bottom': 'img/sea_beach/sea_beach_right_bottom.png',
                 'left_bottom': 'img/sea_beach/sea_beach_left_bottom.png',
                 'corner_left_top': 'img/sea_beach/sea_beach_corner_left_top.png',
                 'corner_right_top': 'img/sea_beach/sea_beach_corner_right_top.png',
                 'corner_right_bottom': 'img/sea_beach/sea_beach_corner_right_bottom.png',
                 'corner_left_bottom': 'img/sea_beach/sea_beach_corner_left_bottom.png'}
    beach = {'base': ['img/beach/beach.png', 0.95],
             'rock': ['img/beach/beach_rock.png', 0.05],
             '0': ['img/beach/beach.png', 0.95],
             '1': ['img/beach/beach_rock.png', 0.05]}
    beach_meadow = {'left': 'img/beach_meadow/beach_meadow_left.png',
                    'top': 'img/beach_meadow/beach_meadow_top.png',
                    'right': 'img/beach_meadow/beach_meadow_right.png',
                    'bottom': 'img/beach_meadow/beach_meadow_bottom.png',
                    'left_top': 'img/beach_meadow/beach_meadow_left_top.png',
                    'right_top': 'img/beach_meadow/beach_meadow_right_top.png',
                    'right_bottom': 'img/beach_meadow/beach_meadow_right_bottom.png',
                    'left_bottom': 'img/beach_meadow/beach_meadow_left_bottom.png',
                    'corner_left_top': 'img/beach_meadow/beach_meadow_corner_left_top.png',
                    'corner_right_top': 'img/beach_meadow/beach_meadow_corner_right_top.png',
                    'corner_right_bottom': 'img/beach_meadow/beach_meadow_corner_right_bottom.png',
                    'corner_left_bottom': 'img/beach_meadow/beach_meadow_corner_left_bottom.png'}
    meadow = {'base': ['img/meadow/meadow.png', 0.7],
              'birch_1': ['img/meadow/meadow_birch_1.png', 0.025],
              'birch_2': ['img/meadow/meadow_birch_2.png', 0.025],
              'flowers_1': ['img/meadow/meadow_flowers_1.png', 0.05],
              'flowers_2': ['img/meadow/meadow_flowers_2.png', 0.05],
              'flowers_3': ['img/meadow/meadow_flowers_3.png', 0.05],
              'home_1': ['img/meadow/meadow_home_1.png', 0.0125],
              'home_2': ['img/meadow/meadow_home_2.png', 0.0125],
              'oak_1': ['img/meadow/meadow_oak_1.png', 0.025],
              'oak_2': ['img/meadow/meadow_oak_2.png', 0.025],
              'rock': ['img/meadow/meadow_rock.png', 0.025],
              '0': ['img/meadow/meadow.png', 0.7],
              '1': ['img/meadow/meadow_birch_1.png', 0.025],
              '2': ['img/meadow/meadow_birch_2.png', 0.025],
              '3': ['img/meadow/meadow_flowers_1.png', 0.05],
              '4': ['img/meadow/meadow_flowers_2.png', 0.05],
              '5': ['img/meadow/meadow_flowers_3.png', 0.05],
              '6': ['img/meadow/meadow_home_1.png', 0.0125],
              '7': ['img/meadow/meadow_home_2.png', 0.0125],
              '8': ['img/meadow/meadow_oak_1.png', 0.025],
              '9': ['img/meadow/meadow_oak_2.png', 0.025],
              '10': ['img/meadow/meadow_rock.png', 0.025]}
    meadow_hill = {'left': 'img/meadow_hill/meadow_hill_left.png',
                   'top': 'img/meadow_hill/meadow_hill_top.png',
                   'right': 'img/meadow_hill/meadow_hill_right.png',
                   'bottom': 'img/meadow_hill/meadow_hill_bottom.png',
                   'left_top': 'img/meadow_hill/meadow_hill_left_top.png',
                   'right_top': 'img/meadow_hill/meadow_hill_right_top.png',
                   'right_bottom': 'img/meadow_hill/meadow_hill_right_bottom.png',
                   'left_bottom': 'img/meadow_hill/meadow_hill_left_bottom.png',
                   'corner_left_top': 'img/meadow_hill/meadow_hill_corner_left_top.png',
                   'corner_right_top': 'img/meadow_hill/meadow_hill_corner_right_top.png',
                   'corner_right_bottom': 'img/meadow_hill/meadow_hill_corner_right_bottom.png',
                   'corner_left_bottom': 'img/meadow_hill/meadow_hill_corner_left_bottom.png'}
    hill = {'base': ['img/hill/hill.png', 0.9],
            'rock': ['img/hill/hill_rock.png', 0.05],
            'home_1': ['img/hill/hill_home_1.png', 0.025],
            'home_2': ['img/hill/hill_home_2.png', 0.025],
            '0': ['img/hill/hill.png', 0.9],
            '1': ['img/hill/hill_rock.png', 0.05],
            '2': ['img/hill/hill_home_1.png', 0.025],
            '3': ['img/hill/hill_home_2.png', 0.025]}
    hill_mountain = {'left': 'img/hill_mountain/hill_mountain_left.png',
                     'top': 'img/hill_mountain/hill_mountain_top.png',
                     'right': 'img/hill_mountain/hill_mountain_right.png',
                     'bottom': 'img/hill_mountain/hill_mountain_bottom.png',
                     'left_top': 'img/hill_mountain/hill_mountain_left_top.png',
                     'right_top': 'img/hill_mountain/hill_mountain_right_top.png',
                     'right_bottom': 'img/hill_mountain/hill_mountain_right_bottom.png',
                     'left_bottom': 'img/hill_mountain/hill_mountain_left_bottom.png',
                     'corner_left_top': 'img/hill_mountain/hill_mountain_corner_left_top.png',
                     'corner_right_top': 'img/hill_mountain/hill_mountain_corner_right_top.png',
                     'corner_right_bottom': 'img/hill_mountain/hill_mountain_corner_right_bottom.png',
                     'corner_left_bottom': 'img/hill_mountain/hill_mountain_corner_left_bottom.png'}
    mountain = {'base': ['img/mountain/mountain.png', 0.9],
                'rock': ['img/mountain/mountain_rock.png', 0.09],
                'flag': ['img/mountain/mountain_flag.png', 0.01],
                '0': ['img/mountain/mountain.png', 0.9],
                '1': ['img/mountain/mountain_rock.png', 0.09],
                '2': ['img/mountain/mountain_flag.png', 0.01]}

    biomsList = [sea, sea_beach, beach, beach_meadow, meadow, meadow_hill, hill, hill_mountain, mountain]

    forest = {'base': 'img/forest/forest.png',
              'base_alpha': 'img/forest/forest_alpha.png',
              'background': 'img/forest/forest_background.png',
              'left': 'img/forest/forest_left.png',
              'top': 'img/forest/forest_top.png',
              'right': 'img/forest/forest_right.png',
              'bottom': 'img/forest/forest_bottom.png',
              'left_top': 'img/forest/forest_left_top.png',
              'right_top': 'img/forest/forest_right_top.png',
              'right_bottom': 'img/forest/forest_right_bottom.png',
              'left_bottom': 'img/forest/forest_left_bottom.png',
              'corner_left_top': 'img/forest/forest_corner_left_top.png',
              'corner_right_top': 'img/forest/forest_corner_right_top.png',
              'corner_right_bottom': 'img/forest/forest_corner_right_bottom.png',
              'corner_left_bottom': 'img/forest/forest_corner_left_bottom.png'}
    hill_forest = {'base': 'img/hill_forest/hill_forest.png',
                   'base_alpha': 'img/hill_forest/hill_forest_alpha.png',
                   'background': 'img/hill_forest/hill_forest_background.png',
                   'left': 'img/hill_forest/hill_forest_left.png',
                   'top': 'img/hill_forest/hill_forest_top.png',
                   'right': 'img/hill_forest/hill_forest_right.png',
                   'bottom': 'img/hill_forest/hill_forest_bottom.png',
                   'left_top': 'img/hill_forest/hill_forest_left_top.png',
                   'right_top': 'img/hill_forest/hill_forest_right_top.png',
                   'right_bottom': 'img/hill_forest/hill_forest_right_bottom.png',
                   'left_bottom': 'img/hill_forest/hill_forest_left_bottom.png',
                   'corner_left_top': 'img/hill_forest/hill_forest_corner_left_top.png',
                   'corner_right_top': 'img/hill_forest/hill_forest_corner_right_top.png',
                   'corner_right_bottom': 'img/hill_forest/hill_forest_corner_right_bottom.png',
                   'corner_left_bottom': 'img/hill_forest/hill_forest_corner_left_bottom.png'}

    xSegments = 20
    ySegments = 20
    pixelsPerSegment = 8

    @staticmethod

    def __minMaxScaler(array:np.ndarray) -> np.ndarray:
        arMin = array.min()
        arMax = array.max()
        array = (array - arMin) / (arMax - arMin)
        return array

    def __expandImage(array:np.ndarray, fillValue:int=0) -> np.ndarray:
        newArray = np.full((array.shape[0]+2, array.shape[1]+2), fillValue)
        for x in range(array.shape[0]):
            for y in range(array.shape[1]):
                newArray[x+1][y+1] = array[x][y]

        return newArray

    def __heightMapGenerator(array:np.ndarray,
        sea_beach:float=0.2, beach_meadow:float=0.3, meadow_hill:float=0.6, hill_mountain:float=0.8) -> np.ndarray:
        for x in range(array.shape[0]):
            for y in range(array.shape[1]):
                if array[x][y] < sea_beach:
                    array[x][y] = 0
                elif array[x][y] >= sea_beach and array[x][y] < beach_meadow:
                    array[x][y] = 1
                elif array[x][y] >= beach_meadow and array[x][y] < meadow_hill:
                    array[x][y] = 2
                elif array[x][y] >= meadow_hill and array[x][y] < hill_mountain:
                    array[x][y] = 3
                else:
                    array[x][y] = 4

        return array

    def __heightStandardizer(heightMap:np.ndarray) -> np.ndarray:
        heightMap = mapGenerator.__expandImage(heightMap)

        for height in range(4, -1, -1):
            for x in range(1, heightMap.shape[0]-1):
                for y in range(1, heightMap.shape[1]-1):
                    if heightMap[x][y] == height:
                        # flattening
                        if heightMap[x][y] - heightMap[x-1][y-1] == 2:
                            heightMap[x-1][y-1] = height - 1
                        if heightMap[x][y] - heightMap[x-1][y] == 2:
                            heightMap[x-1][y] = height - 1
                        if heightMap[x][y] - heightMap[x-1][y+1] == 2:
                            heightMap[x-1][y+1] = height - 1
                        if heightMap[x][y] - heightMap[x][y+1] == 2:
                            heightMap[x][y+1] = height - 1
                        if heightMap[x][y] - heightMap[x+1][y+1] == 2:
                            heightMap[x+1][y+1] = height - 1
                        if heightMap[x][y] - heightMap[x+1][y] == 2:
                            heightMap[x+1][y] = height - 1
                        if heightMap[x][y] - heightMap[x+1][y-1] == 2:
                            heightMap[x+1][y-1] = height - 1
                        if heightMap[x][y] - heightMap[x][y-1] == 2:
                            heightMap[x][y-1] = height - 1

                        # smoothing edges
                        counter = 0
                        if heightMap[x+1][y] < heightMap[x][y]:
                            counter += 1
                        if heightMap[x-1][y] < heightMap[x][y]:
                            counter += 1
                        if heightMap[x][y+1] < heightMap[x][y]:
                            counter += 1
                        if heightMap[x][y-1] < heightMap[x][y]:
                            counter += 1

                        if counter >= 3:
                            heightMap[x][y] = height - 1

        heightMap = heightMap[1:-1, 1:-1]
        return heightMap

    def __forestBinarizer(array:np.ndarray, split_point:float=0.5) -> np.ndarray:
        array = mapGenerator.__minMaxScaler(array)
        for x in range(array.shape[0]):
            for y in range(array.shape[1]):
                if array[x][y] >= split_point:
                    array[x][y] = 1
                else:
                    array[x][y] = 0

        return array

    def __biomGenerator(heightMap:np.ndarray, forestMap:np.ndarray) -> np.ndarray:
        biomMap = np.zeros(heightMap.shape)
        for x in range(heightMap.shape[0]):
            for y in range(heightMap.shape[1]):
                if heightMap[x][y] == 0:
                    biomMap[x][y] = 0
                elif heightMap[x][y] == 1:
                    biomMap[x][y] = 1
                elif heightMap[x][y] == 2:
                    if forestMap[x][y] == 0:
                        biomMap[x][y] = 2
                    else:
                        biomMap[x][y] = 3
                elif heightMap[x][y] == 3:
                    if forestMap[x][y] == 0:
                        biomMap[x][y] = 4
                    else:
                        biomMap[x][y] = 5
                elif heightMap[x][y] == 4:
                    biomMap[x][y] = 6

        return biomMap

    def __biomStandardizer(biomMap:np.ndarray) -> np.ndarray:
        biomMap = mapGenerator.__expandImage(biomMap, fillValue=3)
        for x in range(biomMap.shape[0]-1):
            for y in range(biomMap.shape[1]-1):
                if biomMap[x][y] == 3 or biomMap[x][y] == 5:
                    LT = biomMap[x-1][y-1]
                    T  = biomMap[x-1][y]
                    RT = biomMap[x-1][y+1]
                    R  = biomMap[x][y+1]
                    RB = biomMap[x+1][y+1]
                    B  = biomMap[x+1][y]
                    LB = biomMap[x+1][y-1]
                    L  = biomMap[x][y-1]

                    if   (L == 3 or L == 5 or L == 6) and (LT == 3 or LT == 5 or LT == 6) and (T == 3 or T == 5 or T == 6):
                        pass
                    elif (T == 3 or T == 5 or T == 6) and (RT == 3 or RT == 5 or RT == 6) and (R == 3 or R == 5 or R == 6):
                        pass
                    elif (R == 3 or R == 5 or R == 6) and (RB == 3 or RB == 5 or RB == 6) and (B == 3 or B == 5 or B == 6):
                        pass
                    elif (B == 3 or B == 5 or B == 6) and (LB == 3 or LB == 5 or LB == 6) and (L == 3 or L == 5 or L == 6):
                        pass
                    else:
                        if biomMap[x][y] == 3:
                            biomMap[x][y] = 2
                        else:
                            biomMap[x][y] = 4

        biomMap = biomMap[1:-1, 1:-1]
        return biomMap

    def __heightMapEdgesGenerator(heightMap:np.ndarray) -> np.ndarray:
        heightMap = mapGenerator.__expandImage(heightMap, fillValue=4)
        
        for height in range(4, -1, -1):
            for x in range(1, heightMap.shape[0]-1):
                for y in range(1, heightMap.shape[1]-1):
                    if heightMap[x][y] == height:
                        isLess = False
                        if heightMap[x-1][y-1] < height:
                            isLess = True
                        if heightMap[x-1][y] < height:
                            isLess = True
                        if heightMap[x-1][y+1] < height:
                            isLess = True
                        if heightMap[x][y+1] < height:
                            isLess = True
                        if heightMap[x+1][y+1] < height:
                            isLess = True
                        if heightMap[x+1][y] < height:
                            isLess = True
                        if heightMap[x+1][y-1] < height:
                            isLess = True
                        if heightMap[x][y-1] < height:
                            isLess = True

                        if isLess == True:
                            heightMap[x][y] = height * 2 - 1
                        else:
                            heightMap[x][y] = height * 2

        heightMap = heightMap[1:-1, 1:-1]
        return heightMap

    def __forestMapLimitedStandardizer(forestMapLimited:np.ndarray) -> np.ndarray:
        forestMapLimited = mapGenerator.__expandImage(forestMapLimited, fillValue=1)
        for x in range(1, forestMapLimited.shape[0]-1):
            for y in range(1, forestMapLimited.shape[1]-1):
                if forestMapLimited[x][y] != 0:
                    if forestMapLimited[x][y-1] != 0 and forestMapLimited[x-1][y] != 0:
                        pass
                    elif forestMapLimited[x-1][y] != 0 and forestMapLimited[x][y+1] != 0:
                        pass 
                    elif forestMapLimited[x][y+1] != 0 and forestMapLimited[x+1][y] != 0:
                        pass 
                    elif forestMapLimited[x+1][y] != 0 and forestMapLimited[x][y-1] != 0:
                        pass
                    else:
                        forestMapLimited[x][y] = 0
        
        return forestMapLimited[1:-1, 1:-1]

    def __forestMapLimitedGenerator(biomMap:np.ndarray, forestMap:np.ndarray) -> np.ndarray:
        forestMapLimited = np.zeros_like(biomMap)
        forestMapLimited = mapGenerator.__expandImage(forestMapLimited, fillValue=1)
        biomMap = mapGenerator.__expandImage(biomMap, fillValue=1)
        for x in range(1, forestMapLimited.shape[0]-1):
            for y in range(1, forestMapLimited.shape[1]-1):
                if biomMap[x][y] == 3:
                    forestMapLimited[x][y] = 1
                elif biomMap[x][y] == 5:
                    forestMapLimited[x][y] = 2
                elif biomMap[x][y] == 6 and forestMap[x-1][y-1] == 1:
                    isFife = False
                    if biomMap[x-1][y-1] == 5:
                        isFife = True
                    if biomMap[x-1][y] == 5:
                        isFife = True
                    if biomMap[x-1][y+1] == 5:
                        isFife = True
                    if biomMap[x][y+1] == 5:
                        isFife = True
                    if biomMap[x+1][y+1] == 5:
                        isFife = True
                    if biomMap[x+1][y] == 5:
                        isFife = True
                    if biomMap[x+1][y-1] == 5:
                        isFife = True
                    if biomMap[x][y-1] == 5:
                        isFife = True

                    if isFife == True:
                        forestMapLimited[x][y] = 2
            
        forestMapLimited = forestMapLimited[1:-1, 1:-1]
        forestMapLimited = mapGenerator.__forestMapLimitedStandardizer(mapGenerator.__forestMapLimitedStandardizer(forestMapLimited))
        return forestMapLimited

    def __forestMapEdgesGenerator(forestMapLimited:np.ndarray, heightMapEdges:np.ndarray) -> np.ndarray:
        forestMapEdges = np.zeros_like(forestMapLimited)
        forestMapLimited = mapGenerator.__expandImage(forestMapLimited, fillValue=1)
        for forest in range(1, 3):
            for x in range(1, forestMapLimited.shape[0]-1):
                for y in range(1, forestMapLimited.shape[1]-1):
                    if forestMapLimited[x][y] == forest:
                        isZero = False
                        if forestMapLimited[x-1][y-1] == 0:
                            isZero = True
                        if forestMapLimited[x-1][y] == 0:
                            isZero = True
                        if forestMapLimited[x-1][y+1] == 0:
                            isZero = True
                        if forestMapLimited[x][y+1] == 0:
                            isZero = True
                        if forestMapLimited[x+1][y+1] == 0:
                            isZero = True
                        if forestMapLimited[x+1][y] == 0:
                            isZero = True
                        if forestMapLimited[x+1][y-1] == 0:
                            isZero = True
                        if forestMapLimited[x][y-1] == 0:
                            isZero = True

                        if isZero == True:
                            forestMapEdges[x-1][y-1] = forest * 2 - 1
                        else:
                            if heightMapEdges[x-1][y-1] % 2 == 1:
                                forestMapEdges[x-1][y-1] = forest * 2 - 1
                            else:
                                forestMapEdges[x-1][y-1] = forest * 2

        return forestMapEdges

    def __pasteAset(image:Image, y:int, x:int, asetPath:str, withAlpha:bool=False) -> None:
        imgToPaste = Image.open(asetPath)

        if withAlpha == False:
            image.paste(imgToPaste, (y*8, x*8))
        else:
            image.paste(imgToPaste, (y*8, x*8), imgToPaste)

    def __biomMapAsetsGenerator(heightMapEdges:np.ndarray, seed:int=int(np.random.random() * 4294967296)) -> Image:
        image = np.zeros((mapGenerator.ySegments * 8, mapGenerator.xSegments * 8, 3))
        image = image.astype('uint8')
        image = Image.fromarray(image)

        for i, biom in enumerate(mapGenerator.biomsList):
            if i % 2 == 1: # edges
                heightMapEdges = mapGenerator.__expandImage(heightMapEdges, fillValue=i)
                hm = heightMapEdges

                for x in range(1, heightMapEdges.shape[0]-1):
                    for y in range(1, heightMapEdges.shape[1]-1):
                        if hm[x][y] == i:
                            if   hm[x-1][y] == hm[x][y] and hm[x+1][y] == hm[x][y] and hm[x][y-1] < hm[x][y]: # left
                                mapGenerator.__pasteAset(image, y-1, x-1, biom['left'])
                            elif hm[x][y+1] == hm[x][y] and hm[x][y-1] == hm[x][y] and hm[x-1][y] < hm[x][y]: # top
                                mapGenerator.__pasteAset(image, y-1, x-1, biom['top'])
                            elif hm[x+1][y] == hm[x][y] and hm[x-1][y] == hm[x][y] and hm[x][y+1] < hm[x][y]: # right
                                mapGenerator.__pasteAset(image, y-1, x-1, biom['right'])
                            elif hm[x][y-1] == hm[x][y] and hm[x][y+1] == hm[x][y] and hm[x+1][y] < hm[x][y]: # bottom
                                mapGenerator.__pasteAset(image, y-1, x-1, biom['bottom'])
                            elif hm[x][y+1] == hm[x][y] and hm[x+1][y] == hm[x][y] and hm[x][y-1] < hm[x][y] and hm[x-1][y] < hm[x][y]: # left_top
                                mapGenerator.__pasteAset(image, y-1, x-1, biom['left_top'])
                            elif hm[x][y-1] == hm[x][y] and hm[x+1][y] == hm[x][y] and hm[x-1][y] < hm[x][y] and hm[x][y+1] < hm[x][y]: # right_top
                                mapGenerator.__pasteAset(image, y-1, x-1, biom['right_top'])
                            elif hm[x][y-1] == hm[x][y] and hm[x-1][y] == hm[x][y] and hm[x][y+1] < hm[x][y] and hm[x+1][y] < hm[x][y]: # right_bottom
                                mapGenerator.__pasteAset(image, y-1, x-1, biom['right_bottom'])
                            elif hm[x-1][y] == hm[x][y] and hm[x][y+1] == hm[x][y] and hm[x+1][y] < hm[x][y] and hm[x][y-1] < hm[x][y]: # left_bottom
                                mapGenerator.__pasteAset(image, y-1, x-1, biom['left_bottom'])
                            elif hm[x-1][y-1] < hm[x][y] and hm[x-1][y] == hm[x][y] and hm[x][y-1] == hm[x][y]: # corner_left_top
                                mapGenerator.__pasteAset(image, y-1, x-1, biom['corner_left_top'])
                            elif hm[x-1][y+1] < hm[x][y] and hm[x-1][y] == hm[x][y] and hm[x][y+1] == hm[x][y]: # corner_right_top
                                mapGenerator.__pasteAset(image, y-1, x-1, biom['corner_right_top'])
                            elif hm[x+1][y+1] < hm[x][y] and hm[x+1][y] == hm[x][y] and hm[x][y+1] == hm[x][y]: # corner_right_bottom
                                mapGenerator.__pasteAset(image, y-1, x-1, biom['corner_right_bottom'])
                            elif hm[x+1][y-1] < hm[x][y] and hm[x+1][y] == hm[x][y] and hm[x][y-1] == hm[x][y]: # corner_left_bottom
                                mapGenerator.__pasteAset(image, y-1, x-1, biom['corner_left_bottom'])

                heightMapEdges = heightMapEdges[1:-1, 1:-1]
            else: # solid
                numberOfAsets = int(len(list(biom))/2)
                intervalsList = np.zeros((numberOfAsets, 2))
                # making interval list
                for j in range(numberOfAsets):
                    intervalsList[j][1] = biom[str(j)][1] + intervalsList[j][0]
                    if j < numberOfAsets-1:
                        intervalsList[j+1][0] = intervalsList[j][1]

                for x in range(heightMapEdges.shape[0]):
                    for y in range(heightMapEdges.shape[1]):
                        if heightMapEdges[x][y] == i:
                            # generate random number
                            np.random.seed(seed)
                            randValue = np.random.random()
                            seed=int(np.random.random() * 4294967296)

                            asetID = 0
                            for j in range(numberOfAsets):
                                if randValue >= intervalsList[j][0] and randValue <= intervalsList[j][1]:
                                    asetID = j
                                    break

                            mapGenerator.__pasteAset(image, y, x, biom[str(asetID)][0])

        return image

    def __pasteAsetBackground(image:Image, x:int, y:int, heightMapEdges:np.ndarray, aset:str, background:str) -> None:
        if heightMapEdges[x][y] == 4 or heightMapEdges[x][y] == 6:
            mapGenerator.__pasteAset(image, y-1, x-1, background)
            mapGenerator.__pasteAset(image, y-1, x-1, aset, withAlpha=True)
        else:
            mapGenerator.__pasteAset(image, y-1, x-1, aset, withAlpha=True)

    def __pasteAsetForestEdges(image:Image, x:int, y:int, forestMapEdges:np.ndarray,
        heightMapEdges:np.ndarray, forestList:dict, currentIterator:int) -> None:
        saveSpots = np.ones((3, 3))

        if forestMapEdges[x-1][y-1] < currentIterator: # left_top
            saveSpots[0][0] = 0
        if forestMapEdges[x-1][y] < currentIterator: # top
            saveSpots[0][0] = 0
            saveSpots[0][1] = 0
            saveSpots[0][2] = 0
        if forestMapEdges[x-1][y+1] < currentIterator: # right_top
            saveSpots[0][2] = 0
        if forestMapEdges[x][y+1] < currentIterator: # right
            saveSpots[0][2] = 0
            saveSpots[1][2] = 0
            saveSpots[2][2] = 0
        if forestMapEdges[x+1][y+1] < currentIterator: # right_bottom
            saveSpots[2][2] = 0
        if forestMapEdges[x+1][y] < currentIterator: # bottom
            saveSpots[2][0] = 0
            saveSpots[2][1] = 0
            saveSpots[2][2] = 0
        if forestMapEdges[x+1][y-1] < currentIterator: # left_bottom
            saveSpots[2][0] = 0
        if forestMapEdges[x][y-1] < currentIterator: # left
            saveSpots[0][0] = 0
            saveSpots[1][0] = 0
            saveSpots[2][0] = 0

        if saveSpots[0][0] == 0 and saveSpots[2][0] == 0: # left
            saveSpots[1][0] = 0
        if saveSpots[0][0] == 0 and saveSpots[0][2] == 0: # top
            saveSpots[0][1] = 0
        if saveSpots[0][2] == 0 and saveSpots[2][2] == 0: # right
            saveSpots[1][2] = 0
        if saveSpots[2][0] == 0 and saveSpots[2][2] == 0: # bottom
            saveSpots[2][1] = 0

        if saveSpots.sum() == 9: # solid
            mapGenerator.__pasteAsetBackground(image, x, y, heightMapEdges, forestList['base_alpha'], forestList['background'])
        elif saveSpots.sum() == 8 and saveSpots[0][0] == 0: # corner_right_bottom
            mapGenerator.__pasteAsetBackground(image, x, y, heightMapEdges, forestList['corner_right_bottom'], forestList['background'])
        elif saveSpots.sum() == 8 and saveSpots[0][2] == 0: # corner_left_bottom
            mapGenerator.__pasteAsetBackground(image, x, y, heightMapEdges, forestList['corner_left_bottom'], forestList['background'])
        elif saveSpots.sum() == 8 and saveSpots[2][2] == 0: # corner_left_top
            mapGenerator.__pasteAsetBackground(image, x, y, heightMapEdges, forestList['corner_left_top'], forestList['background'])
        elif saveSpots.sum() == 8 and saveSpots[2][0] == 0: # corner_right_top
            mapGenerator.__pasteAsetBackground(image, x, y, heightMapEdges, forestList['corner_right_top'], forestList['background'])
        elif saveSpots.sum() == 6 and saveSpots[1][0] == 0: # right
            mapGenerator.__pasteAsetBackground(image, x, y, heightMapEdges, forestList['right'], forestList['background'])
        elif saveSpots.sum() == 6 and saveSpots[0][1] == 0: # bottom
            mapGenerator.__pasteAsetBackground(image, x, y, heightMapEdges, forestList['bottom'], forestList['background'])
        elif saveSpots.sum() == 6 and saveSpots[1][2] == 0: # left
            mapGenerator.__pasteAsetBackground(image, x, y, heightMapEdges, forestList['left'], forestList['background'])
        elif saveSpots.sum() == 6 and saveSpots[2][1] == 0: # top
            mapGenerator.__pasteAsetBackground(image, x, y, heightMapEdges, forestList['top'], forestList['background'])
        elif saveSpots.sum() == 4 and saveSpots[0][0] == 1: # left_top
            mapGenerator.__pasteAsetBackground(image, x, y, heightMapEdges, forestList['left_top'], forestList['background'])
        elif saveSpots.sum() == 4 and saveSpots[0][2] == 1: # right_top
            mapGenerator.__pasteAsetBackground(image, x, y, heightMapEdges, forestList['right_top'], forestList['background'])
        elif saveSpots.sum() == 4 and saveSpots[2][2] == 1: # right_bottom
            mapGenerator.__pasteAsetBackground(image, x, y, heightMapEdges, forestList['right_bottom'], forestList['background'])
        elif saveSpots.sum() == 4 and saveSpots[2][0] == 1: # left_bottom
            mapGenerator.__pasteAsetBackground(image, x, y, heightMapEdges, forestList['left_bottom'], forestList['background'])
        elif saveSpots.sum() == 7 and saveSpots[0][0] == 0 and saveSpots[2][2] == 0: # diagonal right /
            mapGenerator.__pasteAsetBackground(image, x, y, heightMapEdges, forestList['left_bottom'], forestList['background'])
            mapGenerator.__pasteAset(image, y-1, x-1, forestList['right_top'], withAlpha=True)
        elif saveSpots.sum() == 7 and saveSpots[2][0] == 0 and saveSpots[0][2] == 0: # diagonal left \
            mapGenerator.__pasteAsetBackground(image, x, y, heightMapEdges, forestList['left_top'], forestList['background'])
            mapGenerator.__pasteAset(image, y-1, x-1, forestList['right_bottom'], withAlpha=True)

    def __pasteAsetFrontier(image:Image, x:int, y:int, forestMapEdges:np.ndarray,
        heightMapEdges:np.ndarray, forestList:dict, hillForestList:dict) -> None:
        hm = heightMapEdges
        fm = forestMapEdges
        
        heightMapShape = np.zeros((2, 2)) # 1 is hill_forest, 0 is forest
        forestMapShape = np.zeros((2, 2))


        #heightMapShape calculating
        if   hm[x-1][y] == hm[x][y] and hm[x+1][y] == hm[x][y] and hm[x][y-1] < hm[x][y]: # right
            heightMapShape[0][1] = 1
            heightMapShape[1][1] = 1
        elif hm[x][y+1] == hm[x][y] and hm[x][y-1] == hm[x][y] and hm[x-1][y] < hm[x][y]: # bottom
            heightMapShape[1][0] = 1
            heightMapShape[1][1] = 1
        elif hm[x+1][y] == hm[x][y] and hm[x-1][y] == hm[x][y] and hm[x][y+1] < hm[x][y]: # left
            heightMapShape[0][0] = 1
            heightMapShape[1][0] = 1
        elif hm[x][y-1] == hm[x][y] and hm[x][y+1] == hm[x][y] and hm[x+1][y] < hm[x][y]: # top
            heightMapShape[0][0] = 1
            heightMapShape[0][1] = 1
        elif hm[x][y+1] == hm[x][y] and hm[x+1][y] == hm[x][y] and hm[x][y-1] < hm[x][y] and hm[x-1][y] < hm[x][y]: # right_bottom
            heightMapShape[1][1] = 1
        elif hm[x][y-1] == hm[x][y] and hm[x+1][y] == hm[x][y] and hm[x-1][y] < hm[x][y] and hm[x][y+1] < hm[x][y]: # left_bottom
            heightMapShape[1][0] = 1
        elif hm[x][y-1] == hm[x][y] and hm[x-1][y] == hm[x][y] and hm[x][y+1] < hm[x][y] and hm[x+1][y] < hm[x][y]: # left_top
            heightMapShape[0][0] = 1
        elif hm[x-1][y] == hm[x][y] and hm[x][y+1] == hm[x][y] and hm[x+1][y] < hm[x][y] and hm[x][y-1] < hm[x][y]: # right_top
            heightMapShape[0][1] = 1
        elif hm[x-1][y-1] < hm[x][y] and hm[x-1][y] == hm[x][y] and hm[x][y-1] == hm[x][y]: # corner_right_bottom
            heightMapShape[0][1] = 1
            heightMapShape[1][0] = 1
            heightMapShape[1][1] = 1
        elif hm[x-1][y+1] < hm[x][y] and hm[x-1][y] == hm[x][y] and hm[x][y+1] == hm[x][y]: # corner_left_bottom
            heightMapShape[0][0] = 1
            heightMapShape[1][0] = 1
            heightMapShape[1][1] = 1
        elif hm[x+1][y+1] < hm[x][y] and hm[x+1][y] == hm[x][y] and hm[x][y+1] == hm[x][y]: # corner_left_top
            heightMapShape[0][0] = 1
            heightMapShape[0][1] = 1
            heightMapShape[1][0] = 1
        elif hm[x+1][y-1] < hm[x][y] and hm[x+1][y] == hm[x][y] and hm[x][y-1] == hm[x][y]: # corner_right_top
            heightMapShape[0][0] = 1
            heightMapShape[0][1] = 1
            heightMapShape[1][1] = 1


        # forestMapShape calculating
        saveSpots = np.ones((3, 3))

        if forestMapEdges[x-1][y-1] == 0: # left_top
            saveSpots[0][0] = 0
        if forestMapEdges[x-1][y] == 0: # top
            saveSpots[0][0] = 0
            saveSpots[0][1] = 0
            saveSpots[0][2] = 0
        if forestMapEdges[x-1][y+1] == 0: # right_top
            saveSpots[0][2] = 0
        if forestMapEdges[x][y+1] == 0: # right
            saveSpots[0][2] = 0
            saveSpots[1][2] = 0
            saveSpots[2][2] = 0
        if forestMapEdges[x+1][y+1] == 0: # right_bottom
            saveSpots[2][2] = 0
        if forestMapEdges[x+1][y] == 0: # bottom
            saveSpots[2][0] = 0
            saveSpots[2][1] = 0
            saveSpots[2][2] = 0
        if forestMapEdges[x+1][y-1] == 0: # left_bottom
            saveSpots[2][0] = 0
        if forestMapEdges[x][y-1] == 0: # left
            saveSpots[0][0] = 0
            saveSpots[1][0] = 0
            saveSpots[2][0] = 0

        if saveSpots[0][0] == 0 and saveSpots[2][0] == 0: # left
            saveSpots[1][0] = 0
        if saveSpots[0][0] == 0 and saveSpots[0][2] == 0: # top
            saveSpots[0][1] = 0
        if saveSpots[0][2] == 0 and saveSpots[2][2] == 0: # right
            saveSpots[1][2] = 0
        if saveSpots[2][0] == 0 and saveSpots[2][2] == 0: # bottom
            saveSpots[2][1] = 0

        if saveSpots.sum() == 9: # solid
            forestMapShape[0][0] = 1
            forestMapShape[0][1] = 1
            forestMapShape[1][0] = 1
            forestMapShape[1][1] = 1
        elif saveSpots.sum() == 8 and saveSpots[0][0] == 0: # corner_right_bottom
            forestMapShape[0][1] = 1
            forestMapShape[1][0] = 1
            forestMapShape[1][1] = 1
        elif saveSpots.sum() == 8 and saveSpots[0][2] == 0: # corner_left_bottom
            forestMapShape[0][0] = 1
            forestMapShape[1][0] = 1
            forestMapShape[1][1] = 1
        elif saveSpots.sum() == 8 and saveSpots[2][2] == 0: # corner_left_top
            forestMapShape[0][0] = 1
            forestMapShape[0][1] = 1
            forestMapShape[1][0] = 1
        elif saveSpots.sum() == 8 and saveSpots[2][0] == 0: # corner_right_top
            forestMapShape[0][0] = 1
            forestMapShape[0][1] = 1
            forestMapShape[1][1] = 1
        elif saveSpots.sum() == 6 and saveSpots[1][0] == 0: # right
            forestMapShape[0][1] = 1
            forestMapShape[1][1] = 1
        elif saveSpots.sum() == 6 and saveSpots[0][1] == 0: # bottom
            forestMapShape[1][0] = 1
            forestMapShape[1][1] = 1
        elif saveSpots.sum() == 6 and saveSpots[1][2] == 0: # left
            forestMapShape[0][0] = 1
            forestMapShape[1][0] = 1
        elif saveSpots.sum() == 6 and saveSpots[2][1] == 0: # top
            forestMapShape[0][0] = 1
            forestMapShape[0][1] = 1
        elif saveSpots.sum() == 4 and saveSpots[0][0] == 1: # left_top
            forestMapShape[0][0] = 1
        elif saveSpots.sum() == 4 and saveSpots[0][2] == 1: # right_top
            forestMapShape[0][1] = 1
        elif saveSpots.sum() == 4 and saveSpots[2][2] == 1: # right_bottom
            forestMapShape[1][1] = 1
        elif saveSpots.sum() == 4 and saveSpots[2][0] == 1: # left_bottom
            forestMapShape[1][0] = 1
        elif saveSpots.sum() == 7 and saveSpots[0][0] == 0 and saveSpots[2][2] == 0: # diagonal right /
            forestMapShape[0][1] = 1
            forestMapShape[1][0] = 1
        elif saveSpots.sum() == 7 and saveSpots[2][0] == 0 and saveSpots[0][2] == 0: # diagonal left \
            forestMapShape[0][0] = 1
            forestMapShape[1][1] = 1

        # calculating forestToPasteShape
        forestToPasteShape = np.zeros((2, 2))
        if forestMapShape[0][0] == 1 and heightMapShape[0][0] == 0:
            forestToPasteShape[0][0] = 1
        if forestMapShape[0][1] == 1 and heightMapShape[0][1] == 0:
            forestToPasteShape[0][1] = 1
        if forestMapShape[1][0] == 1 and heightMapShape[1][0] == 0:
            forestToPasteShape[1][0] = 1
        if forestMapShape[1][1] == 1 and heightMapShape[1][1] == 0:
            forestToPasteShape[1][1] = 1


        # paste forest asets
        if forestToPasteShape[1][0] == 1 and forestToPasteShape[0][0] == 1 and forestToPasteShape[0][1] == 1: # corner_left_top
            mapGenerator.__pasteAset(image, y-1, x-1, forestList['corner_left_top'], withAlpha=True)
        elif forestToPasteShape[0][0] == 1 and forestToPasteShape[0][1] == 1 and forestToPasteShape[1][1] == 1: # corner_right_top
            mapGenerator.__pasteAset(image, y-1, x-1, forestList['corner_right_top'], withAlpha=True)
        elif forestToPasteShape[0][1] == 1 and forestToPasteShape[1][1] == 1 and forestToPasteShape[1][0] == 1: # corner_right_bottom
            mapGenerator.__pasteAset(image, y-1, x-1, forestList['corner_right_bottom'], withAlpha=True)
        elif forestToPasteShape[1][1] == 1 and forestToPasteShape[1][0] == 1 and forestToPasteShape[0][0] == 1: # corner_left_bottom
            mapGenerator.__pasteAset(image, y-1, x-1, forestList['corner_left_bottom'], withAlpha=True)
        elif forestToPasteShape[0][0] == 1 and forestToPasteShape[1][0] == 1: # left
            mapGenerator.__pasteAset(image, y-1, x-1, forestList['left'], withAlpha=True)
        elif forestToPasteShape[0][0] == 1 and forestToPasteShape[0][1] == 1: # top
            mapGenerator.__pasteAset(image, y-1, x-1, forestList['top'], withAlpha=True)
        elif forestToPasteShape[0][1] == 1 and forestToPasteShape[1][1] == 1: # right
            mapGenerator.__pasteAset(image, y-1, x-1, forestList['right'], withAlpha=True)
        elif forestToPasteShape[1][0] == 1 and forestToPasteShape[1][1] == 1: # bottom
            mapGenerator.__pasteAset(image, y-1, x-1, forestList['bottom'], withAlpha=True)
        elif forestToPasteShape[0][0] == 1: # left_top
            mapGenerator.__pasteAset(image, y-1, x-1, forestList['left_top'], withAlpha=True)
        elif forestToPasteShape[0][1] == 1: # right_top
            mapGenerator.__pasteAset(image, y-1, x-1, forestList['right_top'], withAlpha=True)
        elif forestToPasteShape[1][1] == 1: # right_bottom
            mapGenerator.__pasteAset(image, y-1, x-1, forestList['right_bottom'], withAlpha=True)
        elif forestToPasteShape[1][0] == 1: # left_bottom
            mapGenerator.__pasteAset(image, y-1, x-1, forestList['left_bottom'], withAlpha=True)


        # calculating hillForestToPasteShape
        hillForestToPasteShape = np.zeros((2, 2))
        if forestMapShape[0][0] == 1 and heightMapShape[0][0] == 1:
            hillForestToPasteShape[0][0] = 1
        if forestMapShape[0][1] == 1 and heightMapShape[0][1] == 1:
            hillForestToPasteShape[0][1] = 1
        if forestMapShape[1][0] == 1 and heightMapShape[1][0] == 1:
            hillForestToPasteShape[1][0] = 1
        if forestMapShape[1][1] == 1 and heightMapShape[1][1] == 1:
            hillForestToPasteShape[1][1] = 1


        # paste hill_forest asets
        if hillForestToPasteShape[1][0] == 1 and hillForestToPasteShape[0][0] == 1 and hillForestToPasteShape[0][1] == 1: # corner_left_top
            mapGenerator.__pasteAset(image, y-1, x-1, hillForestList['corner_left_top'], withAlpha=True)
        elif hillForestToPasteShape[0][0] == 1 and hillForestToPasteShape[0][1] == 1 and hillForestToPasteShape[1][1] == 1: # corner_right_top
            mapGenerator.__pasteAset(image, y-1, x-1, hillForestList['corner_right_top'], withAlpha=True)
        elif hillForestToPasteShape[0][1] == 1 and hillForestToPasteShape[1][1] == 1 and hillForestToPasteShape[1][0] == 1: # corner_right_bottom
            mapGenerator.__pasteAset(image, y-1, x-1, hillForestList['corner_right_bottom'], withAlpha=True)
        elif hillForestToPasteShape[1][1] == 1 and hillForestToPasteShape[1][0] == 1 and hillForestToPasteShape[0][0] == 1: # corner_left_bottom
            mapGenerator.__pasteAset(image, y-1, x-1, hillForestList['corner_left_bottom'], withAlpha=True)
        elif hillForestToPasteShape[0][0] == 1 and hillForestToPasteShape[1][0] == 1: # left
            mapGenerator.__pasteAset(image, y-1, x-1, hillForestList['left'], withAlpha=True)
        elif hillForestToPasteShape[0][0] == 1 and hillForestToPasteShape[0][1] == 1: # top
            mapGenerator.__pasteAset(image, y-1, x-1, hillForestList['top'], withAlpha=True)
        elif hillForestToPasteShape[0][1] == 1 and hillForestToPasteShape[1][1] == 1: # right
            mapGenerator.__pasteAset(image, y-1, x-1, hillForestList['right'], withAlpha=True)
        elif hillForestToPasteShape[1][0] == 1 and hillForestToPasteShape[1][1] == 1: # bottom
            mapGenerator.__pasteAset(image, y-1, x-1, hillForestList['bottom'], withAlpha=True)
        elif hillForestToPasteShape[0][0] == 1: # left_top
            mapGenerator.__pasteAset(image, y-1, x-1, hillForestList['left_top'], withAlpha=True)
        elif hillForestToPasteShape[0][1] == 1: # right_top
            mapGenerator.__pasteAset(image, y-1, x-1, hillForestList['right_top'], withAlpha=True)
        elif hillForestToPasteShape[1][1] == 1: # right_bottom
            mapGenerator.__pasteAset(image, y-1, x-1, hillForestList['right_bottom'], withAlpha=True)
        elif hillForestToPasteShape[1][0] == 1: # left_bottom
            mapGenerator.__pasteAset(image, y-1, x-1, hillForestList['left_bottom'], withAlpha=True)

    def __forestMapAsetsGenerator(image:Image, forestMapEdges:np.ndarray, heightMapEdges:np.ndarray) -> Image:
        image = image.copy()
        for i in range(1, 5):
            if i % 2 == 1: # edges
                forestMapEdges = mapGenerator.__expandImage(forestMapEdges, fillValue=i)
                heightMapEdges = mapGenerator.__expandImage(heightMapEdges, fillValue=5)
                fm = forestMapEdges

                if i == 1: # forest
                    for x in range(1, forestMapEdges.shape[0]-1):
                        for y in range(1, forestMapEdges.shape[1]-1):
                            if forestMapEdges[x][y] == 1:
                                mapGenerator.__pasteAsetForestEdges(image, x, y, forestMapEdges, heightMapEdges, mapGenerator.forest, i)

                elif i == 3: # hill_forest
                    for x in range(1, forestMapEdges.shape[0]-1):
                        for y in range(1, forestMapEdges.shape[1]-1):
                            if forestMapEdges[x][y] == 3:
                                isForestNearby = False
                                if forestMapEdges[x-1][y-1] == 1 or forestMapEdges[x-1][y-1] == 2:
                                    isForestNearby = True
                                if forestMapEdges[x-1][y] == 1 or forestMapEdges[x-1][y] == 2:
                                    isForestNearby = True
                                if forestMapEdges[x-1][y+1] == 1 or forestMapEdges[x-1][y+1] == 2:
                                    isForestNearby = True
                                if forestMapEdges[x][y+1] == 1 or forestMapEdges[x][y+1] == 2:
                                    isForestNearby = True
                                if forestMapEdges[x+1][y+1] == 1 or forestMapEdges[x+1][y+1] == 2:
                                    isForestNearby = True
                                if forestMapEdges[x+1][y] == 1 or forestMapEdges[x+1][y] == 2:
                                    isForestNearby = True
                                if forestMapEdges[x+1][y-1] == 1 or forestMapEdges[x+1][y-1] == 2:
                                    isForestNearby = True
                                if forestMapEdges[x][y-1] == 1 or forestMapEdges[x][y-1] == 2:
                                    isForestNearby = True

                                if isForestNearby == True: # forests frontier
                                    mapGenerator.__pasteAsetFrontier(image, x, y, forestMapEdges, heightMapEdges, mapGenerator.forest, mapGenerator.hill_forest)
                                else: # hill forest edges
                                    if heightMapEdges[x][y] >= 7 or heightMapEdges[x][y] <= 5:
                                        mapGenerator.__pasteAsetForestEdges(image, x, y, forestMapEdges, heightMapEdges, mapGenerator.hill_forest, i)
                                    else:
                                        mapGenerator.__pasteAset(image, y-1, x-1, mapGenerator.hill_forest['background'])
                                        mapGenerator.__pasteAsetForestEdges(image, x, y, forestMapEdges, heightMapEdges, mapGenerator.hill_forest, i)

                forestMapEdges = forestMapEdges[1:-1, 1:-1]
                heightMapEdges = heightMapEdges[1:-1, 1:-1]
            else: # solid
                for x in range(forestMapEdges.shape[0]):
                    for y in range(forestMapEdges.shape[1]):
                        if forestMapEdges[x][y] == i:
                            if heightMapEdges[x][y] % 2 == 1: # edges
                                if i == 2:
                                    mapGenerator.__pasteAset(image, y, x, mapGenerator.forest['base_alpha'], withAlpha=True)
                                elif i == 4:
                                    mapGenerator.__pasteAset(image, y, x, mapGenerator.hill_forest['base_alpha'], withAlpha=True)
                            else: # solid
                                if i == 2:
                                    mapGenerator.__pasteAset(image, y, x, mapGenerator.forest['base'])
                                elif i == 4:
                                    mapGenerator.__pasteAset(image, y, x, mapGenerator.hill_forest['base'])

        return image

    def __resizeImage(image:Image) -> Image:
        imageResized = np.zeros((mapGenerator.ySegments * mapGenerator.pixelsPerSegment,
                                 mapGenerator.xSegments * mapGenerator.pixelsPerSegment, 3))
        pixSize = int(mapGenerator.pixelsPerSegment / 8)
        image = np.array(image)

        for x in range(mapGenerator.ySegments * 8):
            for y in range(mapGenerator.xSegments * 8):
                for xpic in range(pixSize):
                    for ypic in range(pixSize):
                        imageResized[x*pixSize + xpic][y*pixSize + ypic][0] = int(image[x][y][0])
                        imageResized[x*pixSize + xpic][y*pixSize + ypic][1] = int(image[x][y][1])
                        imageResized[x*pixSize + xpic][y*pixSize + ypic][2] = int(image[x][y][2])

        return Image.fromarray(imageResized.astype('uint8'))

    def generate(size:list=(20, 20), pixelsPerSegment:int=8, biomSizeMultiplayer:float=1, forestSizeMultiplayer:float=1,
                 forestDensity:float=0.5, heightIndicator:float=0.5, seed:int=None) -> Image:
        """
        ## Parameters
        
        `size`: list, default: (20, 20)

        `pixelsPerSegment`: int, default: 8

        `biomSizeMultiplayer`: float, default: 1.0

        `forestSizeMultiplayer`: float, default: 1.0

        `forestDensity`: float, default: 0.5

        `heightIndicator`: float, default: 0.5

        `seed`: int, default: None


        output: `Image` from Pillow
        """

        # input values walidation
        if pixelsPerSegment < 8:
            pixelsPerSegment = 8
        pixelsPerSegment = pixelsPerSegment / 8
        pixelsPerSegment = math.floor(pixelsPerSegment)
        pixelsPerSegment = int(pixelsPerSegment*8)
        mapGenerator.pixelsPerSegment = pixelsPerSegment

        if size[0] < 1:
            size[0] = 1
        if size[1] < 1:
            size[1] = 1
        mapGenerator.xSegments = size[1]
        mapGenerator.ySegments = size[0]

        if forestDensity < 0:
            forestDensity = 0
        elif forestDensity > 1:
            forestDensity = 1
        forestDensity = 1 - forestDensity

        if heightIndicator < 0:
            heightIndicator = 0
        elif heightIndicator > 1:
            heightIndicator = 1
        splitPoints = np.array([0.4, 0.5, 0.8, 0.95])
        difference = np.array([0.3, 0.3, 0.45, 0.2])
        difference = difference * heightIndicator
        splitPoints = splitPoints - difference

        heightOctaves = (((mapGenerator.xSegments + mapGenerator.ySegments) / 2) / 28.571) * (1/biomSizeMultiplayer)
        forestOctaves = (((mapGenerator.xSegments + mapGenerator.ySegments) / 2) / 5) * (1/forestSizeMultiplayer)

        if seed == None:
            seed = int(np.random.random() * 4294967296)

        # heightMap
        noise = PerlinNoise(octaves=heightOctaves, seed=seed)
        w = mapGenerator.xSegments
        h = mapGenerator.ySegments
        if h > w:
            indicator = h / w
            heightMap = [[noise([x/h, (y/w)/indicator]) for y in range(w)] for x in range(h)]
        else:
            indicator = w / h
            heightMap = [[noise([(x/h)/indicator, y/w]) for y in range(w)] for x in range(h)]
        heightMap = mapGenerator.__minMaxScaler(np.array(heightMap))
        heightMap = mapGenerator.__heightMapGenerator(heightMap,
            sea_beach=splitPoints[0], beach_meadow=splitPoints[1], meadow_hill=splitPoints[2], hill_mountain=splitPoints[3])
        heightMap = mapGenerator.__heightStandardizer(heightMap)

        # forestMap
        noise = PerlinNoise(octaves=forestOctaves, seed=seed+1)
        if h > w:
            indicator = h / w
            forestMap = [[noise([x/h, (y/w)/indicator]) for y in range(w)] for x in range(h)]
        else:
            indicator = w / h
            forestMap = [[noise([(x/h)/indicator, y/w]) for y in range(w)] for x in range(h)]
        forestMap = mapGenerator.__forestBinarizer(np.array(forestMap), split_point=forestDensity)

        # biomMap
        biomMap = mapGenerator.__biomGenerator(heightMap, forestMap)
        biomMap = mapGenerator.__biomStandardizer(biomMap)

        # heightMapEdges
        heightMapEdges = mapGenerator.__heightMapEdgesGenerator(heightMap)

        # forestMapEdges
        forestMapEdges = mapGenerator.__forestMapEdgesGenerator(mapGenerator.__forestMapLimitedGenerator(biomMap, forestMap), heightMapEdges)

        # image
        image = mapGenerator.__biomMapAsetsGenerator(heightMapEdges, seed=seed)
        image = mapGenerator.__forestMapAsetsGenerator(image, forestMapEdges, heightMapEdges)

        # resize image
        if mapGenerator.pixelsPerSegment != 8:
            image = mapGenerator.__resizeImage(image)

        return image
