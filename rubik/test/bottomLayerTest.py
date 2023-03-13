'''
Created on Mar 9, 2023

@author: Arpan Srivastava
'''
import unittest
import rubik.controller.bottomLayer as bl
import rubik.model.cube as cube
from rubik.model.constants import *


class BottomLayerTest(unittest.TestCase):


    def test100_bottomLayer_checkIfBottomLayerIsSolved(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotation = bl.solveBottomLayer(theCube)
        self.assertEquals(actualRotation, '')
        
    def test101_bottomLayer_createABottomCrossIfItDoesNotExist(self):
        encodedCube = 'orobbggyowyrorwgrywryggrbywbowgoobwyrwgwyogybrbybwbrgo'
        expectedCube = 'gggobgwbbrbbrrgyrgwrbygyrgwybyboygoboyrryooowowrwwwowy'
        theCube = cube.Cube(encodedCube)
        actualRotatedCube = ''.join(bl.alignToBottomCross(theCube))
        self.assertEquals(actualRotatedCube, expectedCube)
        
    def test102_bottomLayer_alignTopLayerPieceWithCenter(self):
        encodedCube = 'gybygggggwryooboooggoybbbbrbbrrrrbrryyooygyorwwwwwwyww'
        expectedCube = 'ggoygggggbbroobooogybybbbbrwryrrrbrrroygyooyywwwwwwyww'
        theCube = cube.Cube(encodedCube)
        actualRotatedCube = ''.join(bl.alignTopLayerPieceWithCenter(list(encodedCube))[0])
        self.assertEquals(actualRotatedCube, expectedCube)
        
    def test103_cube_leftTriggerWhenPieceAlignedWithCenterIsLocatedOnFTL(self):
        encodedCube = 'gryygyoggbobroyoooyyrbbrbbbggwgrgrryyoooybrbrgwwwwwwww'
        expectedCube = 'ogyogyggggryroyoooborbbrbbbggygryrrrybroybbyowwwwwwwww'
        theCube = cube.Cube(encodedCube)
        pieceAlignedWithCenterLocation = FTL
        actualRotatedCube = ''.join(theCube.leftTrigger(pieceAlignedWithCenterLocation)[0])
        self.assertEquals(actualRotatedCube, expectedCube)
        
    def test104_bottomLayer_rotateOneTopLayerPieceToBottom(self):
        encodedCube = 'oryogygggbowroyooorgobbybbrygygryyrrgrboybbbrwwwwwwgww'
        expectedCube = 'ggoogygggygyroyoooboobbrbbbbyrbryrrrybrgyoyrgwwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotatedCube = ''.join(bl.rotateTopLayerPieceToBottom(list(encodedCube))[0])
        self.assertEquals(actualRotatedCube, expectedCube)
        
    def test105_cube_rightTriggerWhenPieceAlignedWithCenterIsLocatedOnFTR(self):
        encodedCube = 'gggygbgggwobyoryooyryybobbbbbryrgrrrrbooygyrowwowwwwww'
        expectedCube = 'yyrygbgggyobroroooybrybobbbggoyrgrrryooryggbbwwwwwwwww'
        theCube = cube.Cube(encodedCube)
        pieceAlignedWithCenterLocation = FTR
        actualRotatedCube = ''.join(theCube.rightTrigger(pieceAlignedWithCenterLocation)[0])
        self.assertEquals(actualRotatedCube, expectedCube)
        
    def test106_bottomLayer_rotateTwoTopLayerPieceToBottom(self):
        #encodedCube = 'wygrgbygbwyooogoorwgwybobbggybgrbyrrrrbryorbogwywwwowy'
        encodedCube = 'wgboggbgyrbwrobgoogyorbbbbbyygyrgrrygrroyooyyowrwwwwww'
        expectedCube = 'ogbygogggryrbobooogrorbbbbbbogyrrrrrygygyoyyywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotatedCube = ''.join(bl.rotateTopLayerPieceToBottom(list(encodedCube))[0])
        self.assertEquals(actualRotatedCube, expectedCube)
        
    ''' This test does not work anymore as the method it was testing has advanced to its next stage
    def test107_bottomLayer_rotateOnePieceFromTopFaceToSideFace(self):
        encodedCube = 'byrygygggbrgboboooyborbobbobrygrggrryoryygrowwwwwwwyww'
        expectedCube = 'yyyygygggggbbobooowbrrbybbyyrgrrgbrrborgyoroowwwwwwoww'
        theCube = cube.Cube(encodedCube)
        actualRotatedCube = ''.join(bl.rotatePieceFromTopFaceToSideFace(list(encodedCube))[0])
        self.assertEquals(actualRotatedCube, expectedCube)'''
        
    def test107_bottomLayer_rotateOnePieceFromTopFaceToBottom(self):
        encodedCube = 'bryygygggbyrbobooobrgrbobboybogrggrrrgwoyoyyrwwwwwwyww'
        expectedCube = 'yyyygygggggobobooobrrrbgbbbgbrrrgrrryyyoyoboowwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotatedCube = ''.join(bl.solveBottomLayer(theCube)[0])
        self.assertEquals(actualRotatedCube, expectedCube)
        
    def test108_bottomLayer_rotateMultiplePiecesFromTopFaceToBottom(self):
        encodedCube = 'ogobgyoggyrgboooobrowybyybyrybrrogrbbgwgybwrgywwwwwrwr'
        expectedCube = 'yyoogygggyyobobooobggobrbbbygrbrgrrrryyryrbogwwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotatedCube = ''.join(bl.solveBottomLayer(theCube)[0])
        self.assertEquals(actualRotatedCube, expectedCube)
        
    def test108_bottomLayer_rotateOneBottomLayerPieceToTopFace(self):
        encodedCube = 'rgwogywgrbogboywobwoyrbyybgobygrgyrgbyorybgrorwbwwwowr'
        expectedCube = 'gggygroggrybgobooorogrbybbbybyorgrrbrbyyyroowywwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotatedCube = ''.join(bl.solveBottomLayer(theCube)[0])
        self.assertEquals(actualRotatedCube, expectedCube)
    
        
        
        
        
        
