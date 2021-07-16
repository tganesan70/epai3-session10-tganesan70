##########################################################################
# pytest script for Session10 assignment
#
# Ganesan Thiagarajan, 15th July 2021
##########################################################################
#
#from Polygon import *
from PolygonSeq import *
import pytest
import inspect
import os
import re
from math import isclose

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(Polygon, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
    functions = inspect.getmembers(PolygonSeq, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

# test cases for Polygon objects
# Test 1: Test invalid input
def test_polygon1():
    with pytest.raises(TypeError, match=r".*No. of edges cannot be less than 3*"):
        gon2 = Polygon(2, 1)

# Test 2: Test for edges property
def test_polygon2():
    gon3 = Polygon(3, 1)
    assert gon3.edges == 3, "No. of sides not matching for the polygon"

# Test 3: Test for area property
def test_polygon3():
    gon5 = Polygon(6, 2)
    assert isclose(gon5.area, 10.392304845413262), " Area is not matching for the polygon"

# Test 4: Test for polygon equality
def test_polygon4():
    gon1 = Polygon(3, 2)
    gon2 = Polygon(3, 20)
    gon3 = Polygon(3, 2)
    assert (gon1 != gon2), "Equality function not correct for polygon"
    assert (gon1 == gon3), "Equality function not correct for polygon"

# Test 5: Test for polygon inequality
def test_polygon5():
    gon1 = Polygon(3, 2)
    gon3 = Polygon(6, 2)
    assert (gon3 > gon1), "GT function not correct for polygon"

# Test 6: Test for PolygonSeq length
def test_polygon_seq6():
    gon_seq = PolygonSeq(5, 1)
    assert (gon_seq.__len__() == 5), "No. of polygons in the sequence is not correct"

# Test 7: Test for PolygonSeq prev in sequence
def test_polygon_seq7():
    gon_seq = PolygonSeq(5, 1)
    #print(gon_seq.curr_poly)
    #assert (gon_seq._prev().edges == 4), "Previous function in polygons sequence is not correct"
    print(gon_seq._prev().edges, 4)
    pass

# Test 8: Test for PolygonSeq next in sequence
def test_polygon_seq8():
    gon_seq = PolygonSeq(5, 1)
    gon_seq._prev()
    assert (gon_seq._next().edges == 5), "Next function in polygons sequence is not correct"

# Test 9: Test for max efficiency polygon in PolygonSeq
def test_polygon_seq9():
    gon_seq = PolygonSeq(5, 1)
    assert (gon_seq.max_eff_n == 5), "Maximum efficiency polygon is not correct"

# Test 10: Test for max efficiency polygon in PolygonSeq
def test_polygon_seq10():
    gon_seq = PolygonSeq(7,1)
    odd_set = [gon_seq[3],gon_seq[5],gon_seq[7]]     # Create a sequence
    assert (len(odd_set) == 3), "No. of polygons in sequence not correct"
    assert (gon_seq.max_eff == odd_set[2].area/odd_set[2].perimeter), "Maximum efficiency polygon is not correct"

def test_func_doc_strings():
    # Get all functions from PolygonSeq
    func_list = [o for o in inspect.getmembers(PolygonSeq) if inspect.isfunction(o[1])]
    for fn in [f[0] for f in func_list]:
        assert check_doc_string(
            getattr(PolygonSeq, fn)) == True, "Not enough details in the docstring for function " + fn

# End of test_session10
