# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 02:00:35 2022

@author: Srujan
"""

import sys
sys.path.append("../")


from cp_face import Face
from cp_vertex import Vertex
import numpy as np
from cp_utilities import d2r


p1 = Vertex([1, 3, 0])
p2 = Vertex([1, 3, 9])
p3 = Vertex([6, 3, 9])
p4 = Vertex([6, 3, 0])
face = Face(p1, p2, p3, p4)

def test_area():
    area = face.area()
    expected = 45
    assert area == expected

def test_centroid():
    centroid = np.around(face.find_centroid(), decimals=2)
    expected = np.array([3.5, 3, 4.5])
    assert np.array_equiv(centroid, expected) == True