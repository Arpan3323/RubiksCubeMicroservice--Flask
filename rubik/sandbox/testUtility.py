import re
from rubik.model.constants import *
from rubik.model.cube import Cube
import random
import itertools



def cubeRotator(cube):
    rotations = ("FfRrBbLlUu")
    rotationList = []
    
    while (cube[DML] != cube[DMM] or cube[DTM] != cube[DMM] or cube[DBM] != cube[DMM] or cube[DMR] != cube[DMM]):
        
        randomRotation = random.sample(rotations, 1)
        cube = (Cube(cube).rotate(randomRotation))
        rotationList.append(randomRotation)
        
    return (rotationList)

cube = 'wbyooyryoorwgbrgwbbbwyrorryoorbgggrygwowywgybboybwgrgw'
result = cubeRotator(cube)
print (''.join(sum(result, [])))

print(''.join(['o', 'o', 'r', 'y', 'b', 'y', 'y', 'g', 'y', 'w', 'r', 'r', 'b', 'r', 'r', 'r', 'r', 'o', 'b', 'b', 'y', 'y', 'g', 'b', 'y', 'b', 'b', 'r', 'y', 'w', 'r', 'o', 'o', 'w', 'o', 'g', 'g', 'w', 'w', 'g', 'y', 'w', 'g', 'w', 'g', 'o', 'w', 'b', 'g', 'w', 'g', 'o', 'o', 'b']))


