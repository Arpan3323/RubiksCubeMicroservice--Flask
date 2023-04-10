'''
Created on Apr 10, 2023

@author: Arpan Srivastava
'''
import unittest
import rubik.controller.bottomLayer as bl
import rubik.controller.bottomCross as bc
import rubik.controller.middleLayer as ml
import rubik.controller.upFaceCross as ufc
import rubik.model.cube as cube
from rubik.model.constants import *
from rubik.view.solve import solve

#Happy Path Tests
# test 100: check rotations returned when up face already has a cross
#
# test 101: align the incoming cube to middleLayer configuration if it does not already exist
#
# test 102: if incoming cube does not have top cross, check if it has neighbor edges that match UMM



class upFaceCrossTest(unittest.TestCase):


    def test100_solveUpCross_checkIfUpFaceCrossIsSolved(self):
        encodedCube = 'rgyggggggoogooooooorybbbbbbbbyrrrrrrryyyyygybwwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotation = ufc.solveUpCross(theCube)[1]
        expectedRotations = ''
        self.assertEquals(actualRotation, expectedRotations)

    def test101_solveUpCross_alignToMiddleLayer(self):
        encodedCube = 'wyyoggbgrrrbroogyoobgbbywryogbbrwbgrywwyywrogyowwwrobg'
        expectedCube = 'rbrggggggyogoooooooyobbbbbbbyyrrrrrryrygyygybwwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualCube = ufc._alignMiddleLayer(theCube)
        self.assertEquals(expectedCube, actualCube)
        
    def test102_createTopCross_checkIfThereAreNeighborEdgesOnTopFaceThatMatchUMM(self):
        encodedCube = 'byyggggggryoooooooygbbbbbbbrrorrrrrryygyybyogwwwwwwwww'
        #theCube = cube.Cube(encodedCube)
        checkForNieghbors = ufc._createTopCross(encodedCube)
        self.assertTrue(checkForNieghbors)
