import matplotlib.pyplot as plt
import sys
import os
import numpy as np
import pandas as pd
import geopandas as gpd

acc_dir=os.path.dirname(os.path.realpath(__file__))

csh=acc_dir+'/contries_shape/'
nor=gpd.read_file(csh+'gadm36_NOR_shp/gadm36_NOR_0.shp')
uk=gpd.read_file(csh+'gadm36_GBR_shp/gadm36_GBR_0.shp')
ice=gpd.read_file(csh+'gadm36_ISL_shp/gadm36_ISL_0.shp')

abutter=nor.append([uk,ice]).reset_index()

def countries():
    return abutter


def main():
    countries()
main()
