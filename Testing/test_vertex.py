# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 00:12:42 2022

@author: Srujan
"""
import sys
sys.path.append("../")


from cp_vertex import Vertex
import numpy as np
from cp_utilities import d2r

point = Vertex([2,3,5])

def test_rotation():
    point.rotate(d2r(60), d2r(45), d2r(30), [0,0,0])
    point_r = np.around(point.xyz(), decimals=3)
    expected = np.array([-1.25, 5.84, 1.526])
    assert np.array_equiv(point_r, expected) == True

    
    