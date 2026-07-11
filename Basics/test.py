from Func import hello
from Func import square
import sys

# if len(sys.argv)==2:
#     hello(sys.argv[1])
    
    
def test_hello():
    assert hello("kalpana") == "hello, kalpana"

#To run this you ned to run // pip install pytest  -- to install pytest

def test_square():
    assert square(2) == 4
    assert square(-3)==9
    assert square(1)==1