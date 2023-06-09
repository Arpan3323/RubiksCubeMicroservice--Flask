'''
Created on Mar 9, 2023

@author: Arpan Srivastava
'''
import unittest
import rubik.controller.bottomLayer as bl
import rubik.controller.bottomCross as bc
import rubik.controller.upFaceCross as ufc
import rubik.controller.upFaceSurface as ufs
import rubik.controller.upperLayer as ul
import rubik.controller.middleLayer as ml
import rubik.model.cube as cube
from rubik.model.constants import *
from rubik.view.solve import solve

#Analysis of bottomLayer.py: 
#    A file that consists of components that will form a bottom layer on the incoming cube 
#    returns the rotations needed to solve bottom layer as well as the cube (as a list)
#    after performing the returned rotations on it
#    
#    input:
#        receives the cube string as a Cube class object (converts it into a list)
#    outputs:
#        Checks if Cube already has bottom layer solved, if yes, then returns '' rotations
#        if bottom layer is not solved, returns the rotations needed and the rotated cube with bottom layer solved
#
#Happy path tests:
#    test 100: checks the rotations returned if bottom layer is solved
#
#    test 101: checks if bottom cross exists on incoming cube
#    
#    test 102: checks the returned cube after aligning the top layer adjacent corner piece with side face 
#              that has the correct center piece
#    
#    test 103: checks the returned cube after performing left trigger on front face
#     
#    test 104: checks the returned cube after rotating a piece in the top layer to bottom
#
#    test 105: checks the returned cube after performing right trigger on front face
#
#    test 106: checks the returned cube after rotating two top layer corner pieces to bottom
#
#    test 107: checks the returned cube after rotating a single corner piece from top face to bottom
#
#    test 108: checks the returned cube after rotating multiple corner pieces from top face to bottom
#    
#    test 109: checks the returned cube after rotating a corner piece in bottom layer to top face and
#              then to bottom
#
#    test 110: checks the returned cube when 4 top layer pieces are sent to bottom and during the process
#              of rotation a piece is sent to top face
#
#    test 111: checks the returned cube after rotating three bottom layer pieces to top face and then to
#              bottom
#
#    test 112: checks the returned cube after rotating an incoming cube that only has bottom cross. Full
#              bottom layer solve
#
#    test 113: checks if solve.py also includes the rotations returned by bottomLayer.py
#
#    test 114: rotated a cube that leaves a corner piece on top face that was supposed to go to bottom 
#    
#    test 115: rotated a cube that leaves a corner piece in bottom layer that was supposed to go to bottom
#
#    test 116: rotated a cube that leaves two corner pieces in top layer. This is an acceptance test that failed
#    
#Sad path:
#    all sad path scenarios (ways in which the customer can break solve bottom layer and recieve an error)
#    have been captured in solve.py and were tested in solveTest.py



class BottomLayerTest(unittest.TestCase):


    def test100_bottomLayer_checkIfBottomLayerIsSolved(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotation = bl.solveBottomLayer(theCube)[1]
        self.assertEquals(actualRotation, '')
        
    def test101_bottomLayer_createABottomCrossIfItDoesNotExist(self):
        encodedCube = 'orobbggyowyrorwgrywryggrbywbowgoobwyrwgwyogybrbybwbrgo'
        theCube = cube.Cube(encodedCube)
        actualRotatedCube = ''.join(bl._alignToBottomCross(theCube))
        verifyBottomCross = bc.verifyBottomCrossExists(list(actualRotatedCube))
        self.assertTrue(verifyBottomCross)
        
    def test102_bottomLayer_alignTopLayerPieceWithCenter(self):
        encodedCube = 'gybygggggwryooboooggoybbbbrbbrrrrbrryyooygyorwwwwwwyww'
        expectedCube = 'ggoygggggbbroobooogybybbbbrwryrrrbrrroygyooyywwwwwwyww'
        theCube = cube.Cube(encodedCube)
        actualRotatedCube = ''.join(bl._alignTopLayerPieceWithCenter(list(encodedCube))[0])
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
        actualRotatedCube = ''.join(bl._rotateTopLayerPieceToBottom(list(encodedCube))[0])
        self.assertEquals(actualRotatedCube, expectedCube)
        
    def test105_cube_rightTriggerWhenPieceAlignedWithCenterIsLocatedOnFTR(self):
        encodedCube = 'gggygbgggwobyoryooyryybobbbbbryrgrrrrbooygyrowwowwwwww'
        expectedCube = 'yyrygbgggyobroroooybrybobbbggoyrgrrryooryggbbwwwwwwwww'
        theCube = cube.Cube(encodedCube)
        pieceAlignedWithCenterLocation = FTR
        actualRotatedCube = ''.join(theCube.rightTrigger(pieceAlignedWithCenterLocation)[0])
        self.assertEquals(actualRotatedCube, expectedCube)
        
    def test106_bottomLayer_rotateTwoTopLayerPieceToBottom(self):
        encodedCube = 'wgboggbgyrbwrobgoogyorbbbbbyygyrgrrygrroyooyyowrwwwwww'
        expectedCube = 'ogbygogggryrbobooogrorbbbbbbogyrrrrrygygyoyyywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotatedCube = ''.join(bl._rotateTopLayerPieceToBottom(list(encodedCube))[0])
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
        #expectedCube = 'yyyygygggggobobooobrrrbgbbbgbrrrgrrryyyoyoboowwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotatedCube = ''.join(bl.solveBottomLayer(theCube)[0])
        verifyBottomLayer = bl.verifyBottomLayerExists(list(actualRotatedCube))
        self.assertTrue(verifyBottomLayer)
        #self.assertEquals(actualRotatedCube, expectedCube)
        
    def test108_bottomLayer_rotateMultiplePiecesFromTopFaceToBottom(self):
        encodedCube = 'ogobgyoggyrgboooobrowybyybyrybrrogrbbgwgybwrgywwwwwrwr'
        expectedCube = 'yyoogygggyyobobooobggobrbbbygrbrgrrrryyryrbogwwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotatedCube = ''.join(bl.solveBottomLayer(theCube)[0])
        self.assertEquals(actualRotatedCube, expectedCube)
        
    '''This test does not work anymore as the method it was testing has advanced to its next stage
    def test108_bottomLayer_rotateOneBottomLayerPieceToTopFace(self):
        encodedCube = 'rgwogywgrbogboywobwoyrbyybgobygrgyrgbyorybgrorwbwwwowr'
        expectedCube = 'gggygroggrybgobooorogrbybbbybyorgrrbrbyyyroowywwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotatedCube = ''.join(bl.solveBottomLayer(theCube)[0])
        self.assertEquals(actualRotatedCube, expectedCube)'''
        
    def test109_bottomLayer_rotateOneBottomLayerPieceToTopFaceAndThenToBottom(self):
        encodedCube = 'bogogywgrwoyboywobobyrbyybgrgwgrgyrggrbryyoborwbwwwowr'
        expectedCube = 'booygrgggygygobooooygrbybbbybyorrrrrrgbyyorbgwwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotatedCube = ''.join(bl.solveBottomLayer(theCube)[0])
        verifyBottomLayer = bl.verifyBottomLayerExists(list(actualRotatedCube))
        self.assertTrue(verifyBottomLayer)
        
    def test110_bottomLayer_rotatingCubeWithAllPiecesInTopLayerWhereRotationsSendAPieceTopFace(self):
        encodedCube = 'wygrgbygbwyooogoorwgwybobbggybgrbyrrrrbryorbogwywwwowy'
        expectedCube = 'byobgrgggbbyyoboooggyybobbbrgyyrorrrgrooyrrgywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        rotationsReturned = bl.solveBottomLayer(theCube)[1]
        actualRotatedCube = theCube.rotate(rotationsReturned)
        self.assertEquals(actualRotatedCube, expectedCube)
        
    def test111_bottomLayer_rotatingThreeBottomLayerPieceToTopFaceAndThenToBottom(self):
        encodedCube = 'roorgywgryrygoogowryyybrbbwogbgrbgrbbbgoyyybgowwwwwowr'
        expectedCube = 'yyyrgggggrgooobooobybobbbbbryorryrrrygyoyrgbgwwwwwwwww'
        theCube = cube.Cube(encodedCube)
        rotationsReturned = bl.solveBottomLayer(theCube)[1]
        actualRotatedCube = theCube.rotate(rotationsReturned)
        verifyBottomLayer = bl.verifyBottomLayerExists(list(actualRotatedCube))
        self.assertTrue(verifyBottomLayer)
        
    def test112_bottomLayer_aCubeWithOnlyBottomCross(self):
        parms = {}
        encodedCube = 'ryrgggggrwyboogboyoboybbobybywrrrgrwyowryobbgowywwwrwg'
        expectedCube = 'yyyygrgggboogoyoooyrygbbbbboygorrrrrbbgoygrbrwwwwwwwww'
        theCube = cube.Cube(encodedCube)
        rotationsReturned = bl.solveBottomLayer(theCube)[1]
        actualRotatedCube = theCube.rotate(rotationsReturned)
        verifyBottomLayer = bl.verifyBottomLayerExists(list(actualRotatedCube))
        self.assertTrue(verifyBottomLayer)
        
        
    def test113_solve_checkingSolveReturnsBottomLayerRotaions(self):
        parms = {}
        parms['cube'] = 'ryrgggggrwyboogboyoboybbobybywrrrgrwyowryobbgowywwwrwg'
        result = solve(parms)
        encodedCube = 'ryrgggggrwyboogboyoboybbobybywrrrgrwyowryobbgowywwwrwg'
        theCube = cube.Cube(encodedCube)
        bottomCross = ''
        bottomLayer = bl.solveBottomLayer(theCube)[1] 
        middleLayer = ml.solveMiddleLayer(theCube)[1]
        upCross = ufc.solveUpCross(theCube)[1]
        upSurface = ufs.solveUpSurface(theCube)[1]
        upLayer = ul.solveUpperLayer(theCube)[1]
        rotations = bottomCross + bottomLayer + middleLayer + upCross + upSurface + upLayer
        self.assertEqual(rotations, result['solution'])
        self.assertEqual('ok', result['status'])
        
    def test114_bottomLayer_rotatingCubeThatWillLeaveTopFaceWithOneCornerAfterEveryhtingElseIsAligned(self):
        parms = {}
        encodedCube = 'yyyrggbggroooobwoogbrybrbbybobgryorrwrwbyyoggywrwwwgww'
        expectedCube = 'ggybgogggrgyyobooobroybbbbbbyyorrrrryyrgyoorgwwwwwwwww'
        theCube = cube.Cube(encodedCube)
        rotationsReturned = bl.solveBottomLayer(theCube)[1]
        actualRotatedCube = theCube.rotate(rotationsReturned)
        verifyBottomLayer = bl.verifyBottomLayerExists(list(actualRotatedCube))
        self.assertTrue(verifyBottomLayer)
        
    def test115_bottomLayer_rotatingCubeThatWillLeaveBottomLayerWithOneCornerAfterEveryhtingElseIsAligned(self):
        parms = {}
        encodedCube = 'oowggyygorgrgoygobwbrrbowbrgbwbrrbroyrgyyogybbwywwwywo'
        expectedCube = 'yyyogbgggbbbroyoooyyyobgbbbryorrgrrrggoryogbrwwwwwwwww'
        theCube = cube.Cube(encodedCube)
        rotationsReturned = bl.solveBottomLayer(theCube)[1]
        actualRotatedCube = theCube.rotate(rotationsReturned)
        verifyBottomLayer = bl.verifyBottomLayerExists(list(actualRotatedCube))
        self.assertTrue(verifyBottomLayer)
        
    def test116_bottomLayer_rotatingCubeThatWillLeaveTopLayerWithTwoCornersAfterEveryhtingElseIsAligned(self):
        encodedCube = 'j8388vv9v8jj993j3v7j79v7338888873j733vv9379j99j9vjv777'
        #expectedCube = 'yyyogbgggbbbroyoooyyyobgbbbryorrgrrrggoryogbrwwwwwwwww'
        theCube = cube.Cube(encodedCube)
        rotationsReturned = bl.solveBottomLayer(theCube)[1]
        actualRotatedCube = theCube.rotate(rotationsReturned)
        verifyBottomLayer = bl.verifyBottomLayerExists(list(actualRotatedCube))
        self.assertTrue(verifyBottomLayer)
        
    def test117_bottomLayer_FailedCustomerAcceptanceTest_ExceptionThrownForStringConcatenation(self):
        encodedCube = 'S4qwSSx4SxqSw499xxqx4xxq4qxw9q49xw9qS44SwS9S49wwwqq99w'
        theCube = cube.Cube(encodedCube)
        rotations = bl.solveBottomLayer(theCube)[1]
        rotatedCube = theCube.rotate(rotations)
        verifyBottomLayer = bl.verifyBottomLayerExists(list(rotatedCube))
        self.assertTrue(verifyBottomLayer)
        
        
