#!/usr/bin/env python3
import sys 
from graph import Graph
from pixel import Pixel
from Stackenlichten import *
from algorithm import *
from control import *

def run(argv):
    slc = FadecandySLC();
    graph = Graph("graphs/graph21.txt")
    alg = mainAlgorithm(slc,[AlgRunningLight(True,True,False,"",graph)],"",graph)
    c = SimpleControl(alg);
    c.start()
    
if __name__ == "__main__":
        run(sys.argv[1:])