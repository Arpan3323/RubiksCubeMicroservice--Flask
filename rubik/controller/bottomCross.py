from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomCross(theCube: Cube) -> str:
    
    cubeList = theCube.get()
    daisyPetals = 4
    rotation = ''       
       
    #If bottom cross exists return no rotations   
    if verifyBottomCrossExists(cubeList):
        rotation += ''
        return rotation
    
    topEdges = [cubeList[UTM], cubeList[UML], cubeList[UMR], cubeList[UBM]]
    sideEdges = [cubeList[FTM], cubeList[RTM], cubeList[BTM], cubeList[LTM]]
    
    #checking if top-daisy exists and side edges are aligned
    daisyEdge = topEdges.count(cubeList[DMM])
    topDaisyFound = daisyEdge == daisyPetals
    
    #check if side edges are aligned on top
    sideEdgesAlignedOnTop = (sideEdges == [cubeList[FMM], cubeList[RMM], cubeList[BMM], cubeList[LMM]])
        
        
    #check if top daisy exists but side edges are not aligned
    if (topDaisyFound == True) and (sideEdgesAlignedOnTop == False):
        return _daisyFormation(theCube)
        
    #checks if daisy exists and side edges are aligned
    if (topDaisyFound == True) and (sideEdgesAlignedOnTop == True):
        rotation += 'FFRRBBLL'
        theCube.rotate(rotation)
        return rotation
    
    
    if (topDaisyFound == False):
        return _daisyFormation(theCube)
        

#return true if the bottom cross exists otherwise return false
def verifyBottomCrossExists(cubeList):
    return (cubeList[DML] == cubeList[DMM] and cubeList[DTM] == cubeList[DMM] 
            and cubeList[DBM] == cubeList[DMM] and cubeList[DMR] == cubeList[DMM] 
            and cubeList[LMM] == cubeList[LBM] and cubeList[FMM] == cubeList[FBM]
            and cubeList[RMM] == cubeList[RBM] and cubeList[BMM] == cubeList[BBM])
    

#forms a daisy on top and aligns the side face edges with the daisy and rotates it
def _daisyFormation(theCube):
    
    rotation = ''
    
    #specific rotations for each daisy petal
    bottomPetalRotation = ''
    rightPetalRotation = ''
    topPetalRotation = ''
    leftPetalRotation = ''
    
    #Rotations that will be used to orient missing petals to UBM position, initially empty so they do not get added at the end if not performed
    algorithmRotationOne = ''
    algorithmRotationTwo = ''
    algorithmRotationThree = ''
    
    cubeList = theCube.get()
    topEdges = [cubeList[UBM], cubeList[UMR], cubeList[UTM], cubeList[UML]]
    
    #counting petals daisy petals on the incoming cube
    daisyPetals = topEdges.count(cubeList[DMM])
    
    
    cubeList, bottomPetalRotation, algorithmRotationOne, rightPetalRotation, algorithmRotationTwo, topPetalRotation, algorithmRotationThree, leftPetalRotation = _algorithmToFormDaisy(theCube, bottomPetalRotation, 
                                     rightPetalRotation, topPetalRotation, 
                                     leftPetalRotation, algorithmRotationOne, 
                                     algorithmRotationTwo, algorithmRotationThree, 
                                     cubeList, topEdges, daisyPetals)
    
    rotation += bottomPetalRotation + algorithmRotationOne + \
    rightPetalRotation + algorithmRotationTwo + \
    topPetalRotation + algorithmRotationThree + \
    leftPetalRotation 
                
    #after daisy is formed on top, side edges will be aligned and rotated to form bottom cross
    rotation += _alignSideEdgesToBottomCross(theCube, cubeList)

    return rotation

def _algorithmToFormDaisy(theCube, bottomPetalRotation, 
                          rightPetalRotation, topPetalRotation, 
                          leftPetalRotation, algorithmRotationOne, 
                          algorithmRotationTwo, algorithmRotationThree, 
                          cubeList, topEdges, daisyPetals):
    
    #Checking if UBM petal is missing
    if daisyPetals <= 3 and topEdges[0] != cubeList[DMM]:
        bottomPetalRotation += _alignDaisyBottomEdge(cubeList)
        cubeList = list(theCube.rotate(bottomPetalRotation))
        
        #updating top edges and the count of daisy petals 
        topEdges = [cubeList[UBM], cubeList[UMR], cubeList[UTM], cubeList[UML]]
        daisyPetals = topEdges.count(cubeList[DMM])
    
    #Checking if UMR petal is missing
    if daisyPetals <= 3 and topEdges[1] != cubeList[DMM]:
        #rotating U to get missing petal from UMR to UBM
        algorithmRotationOne += 'U'
        cubeList = list(theCube.rotate('U'))
        
        #After placing the missing petal in UBM spot again running it through the method that aligns bottom petal
        rightPetalRotation += _alignDaisyBottomEdge(cubeList)
        cubeList = list(theCube.rotate(rightPetalRotation))
        
        #updating top edges and the count of daisy petals 
        topEdges = [cubeList[UBM], cubeList[UMR], cubeList[UTM], cubeList[UML]]
        daisyPetals = topEdges.count(cubeList[DMM])
    
    #Checking if UTM petal is missing    
    if daisyPetals <= 3 and topEdges[2] != cubeList[DMM]:
        #rotating UU to get missing petal from UTM to UBM
        algorithmRotationTwo += 'UU'
        cubeList = list(theCube.rotate('UU'))
        
        #After placing the missing petal in UBM spot again running it through the method that aligns bottom petal
        topPetalRotation += _alignDaisyBottomEdge(cubeList)
        cubeList = list(theCube.rotate(topPetalRotation))
        
        #updating top edges and the count of daisy petals 
        topEdges = [cubeList[UBM], cubeList[UMR], cubeList[UTM], cubeList[UML]]
        daisyPetals = topEdges.count(cubeList[DMM])
        
    #Checking if UML is missing, if not, check if UMR is missing
    if daisyPetals <= 3:
        #rotating u to get missing petal from UML to UBM
        if topEdges[3] != cubeList[DMM]:
            algorithmRotationThree += 'u'
            cubeList = list(theCube.rotate('u'))
        
        #rotating U to get missing petal from UMR to UBM
        elif topEdges[1] != cubeList[DMM]:
            algorithmRotationThree += 'U'
            cubeList = list(theCube.rotate('U'))
        
        
        
        #After placing the missing petal in UBM spot again running it through the method that aligns bottom petal
        leftPetalRotation += _alignDaisyBottomEdge(cubeList)
        cubeList = list(theCube.rotate(leftPetalRotation))
    return cubeList, bottomPetalRotation, algorithmRotationOne, rightPetalRotation, algorithmRotationTwo, topPetalRotation, algorithmRotationThree, leftPetalRotation

def _alignSideEdgesToBottomCross(theCube, cubeList):
    rotationsToAlignSideEdges = ''
    
    #front face  
    while (cubeList[UBM] != cubeList[DMM]):
        rotationsToAlignSideEdges += 'U'
        cubeList = list(theCube.rotate('U'))
    while(cubeList[FTM] != cubeList[FMM]):
        rotationsToAlignSideEdges += 'U'
        cubeList = list(theCube.rotate('U'))
    if (cubeList[FTM] == cubeList[FMM]):
        rotationsToAlignSideEdges += 'FF'
        cubeList = list(theCube.rotate('FF'))
    
    #right face
    while (cubeList[UMR] != cubeList[DMM]):
        rotationsToAlignSideEdges += 'U'
        cubeList = list(theCube.rotate('U'))
    while(cubeList[RTM] != cubeList[RMM]):
        rotationsToAlignSideEdges += 'U'
        cubeList = list(theCube.rotate('U'))
    if (cubeList[RTM] == cubeList[RMM]):
        rotationsToAlignSideEdges += 'RR'
        cubeList = list(theCube.rotate('RR'))
    
    #back face
    while (cubeList[UTM] != cubeList[DMM]):
        rotationsToAlignSideEdges += 'U'
        cubeList = list(theCube.rotate('U'))
    while(cubeList[BTM] != cubeList[BMM]):
        rotationsToAlignSideEdges += 'U'
        cubeList = list(theCube.rotate('U'))

    if (cubeList[UTM] != cubeList[DMM]):
        rotationsToAlignSideEdges += 'U'
        cubeList = list(theCube.rotate('U'))
        
    if (cubeList[BTM] == cubeList[BMM]):
        rotationsToAlignSideEdges += 'BB'
        cubeList = list(theCube.rotate('BB'))
    
    #left face
    while (cubeList[UML] != cubeList[DMM]):
        rotationsToAlignSideEdges += 'U'
        cubeList = list(theCube.rotate('U'))
    while(cubeList[LTM] != cubeList[LMM]):
        rotationsToAlignSideEdges += 'U'
        cubeList = list(theCube.rotate('U'))
    if (cubeList[LTM] == cubeList[LMM]):
        rotationsToAlignSideEdges += 'LL'
        cubeList = list(theCube.rotate('LL'))
    
    return rotationsToAlignSideEdges

#this method does not perform any rotations on the cube but returns the rotation 
def _alignDaisyBottomEdge(cubeList):
    rotation = ''
    edgeLocation = _locateNeededEdge(cubeList)
            
    edgeRotations = {
        cubeList[FTM]: 'FuRU',
        cubeList[FML]: 'Ulu',
        cubeList[FMR]: 'uRU',
        cubeList[FBM]: 'fuRU',
        cubeList[RTM]: 'rf',
        cubeList[RML]: 'f',
        cubeList[RMR]: 'uRRUf',
        cubeList[RBM]: 'uRUf',
        cubeList[BTM]: 'BULu',
        cubeList[BML]: 'urU',
        cubeList[BMR]: 'ULu',
        cubeList[BBM]: 'UUbuLu',
        cubeList[LTM]: 'LF',
        cubeList[LML]: 'UUbUU',
        cubeList[LMR]: 'F',
        cubeList[LBM]: 'ULUbUU',
        cubeList[DTM]: 'FF',
        cubeList[DML]: 'ULLu',
        cubeList[DMR]: 'uRRU',
        cubeList[DBM]: 'UUBBUU',
    }

    if edgeLocation[0] in edgeRotations:
        rotation += edgeRotations[edgeLocation[0]]

    return rotation

def _locateNeededEdge(cubeList):
    edgeLocation = []
    
    faceEdges = [(cubeList[FTM], cubeList[FML], cubeList[FMR], cubeList[FBM], 'F'), 
                (cubeList[RTM], cubeList[RML], cubeList[RMR], cubeList[RBM], 'R'),
                (cubeList[BTM], cubeList[BML], cubeList[BMR], cubeList[BBM], 'B'),
                (cubeList[LTM], cubeList[LML], cubeList[LMR], cubeList[LBM], 'L'),
                (cubeList[DTM], cubeList[DML], cubeList[DMR], cubeList[DBM], 'D')]
    
    for edge in faceEdges:
        if (edge[0] == cubeList[DMM]) and len(edgeLocation) == 0:
            edgeFace = edge[4]
            edgeLocation.append(edge[0])
            
        elif (edge[1] == cubeList[DMM]) and len(edgeLocation) == 0:
            edgeFace = edge[4]
            edgeLocation.append(edge[1]) 
            
        elif (edge[2] == cubeList[DMM]) and len(edgeLocation) == 0:
            edgeFace = edge[4]
            edgeLocation.append(edge[2]) 

        elif (edge[3] == cubeList[DMM]) and len(edgeLocation) == 0:
            edgeFace = edge[4]
            edgeLocation.append(edge[3])
    return edgeLocation
         
    
    