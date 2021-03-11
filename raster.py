import matplotlib.pyplot as plt
import sys
import os
import numpy as np
import pandas as pd
import geopandas as gpd

acc_dir=os.path.dirname(os.path.realpath(__file__))

csh=acc_dir+'/contries_shape/'
raster=gpd.read_file(csh+'layer_565.shp')

def raster():
    return raster

def main():
    raster()
main()
