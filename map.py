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

countries=nor.append([uk,ice]).reset_index()
raster=gpd.read_file(csh+'layer_565.shp')

patches=raster[["LOKREF","geometry"]].rename(columns={"LOKREF" : "patch"})

rr = raster.dissolve(by='HAVOMR')
rr['patches']=rr.index

def projectionChange(inp,set=False):
    if set==False:
        return inp.to_crs({'init': 'epsg:4326'})
    if set==True:
        return inp.to_crs({'init': 'epsg:3574'})

def setPrj(val=False):
    global patches,countries,raster
    raster=projectionChange(raster,val)
    patches=projectionChange(patches,val)
    countries=projectionChange(countries,val)

def mapShowL(inp,cc,ccc='Set3',ent="testL"):
    fig, ax = plt.subplots(figsize=(16,9))
    inp.plot(ax=ax,column=cc,cmap=ccc)
    countries.plot(ax=ax, color='white', edgecolor='black',alpha=0.3)
    for i in rr.index:
        plt.annotate(i,xy=(rr.geometry[i].centroid.x,rr.geometry[i].centroid.y),size=1)
    fig=figsize=(1000,1000)
    ax.axis('scaled')
    plt.savefig(str(ent)+".png",dpi=1080)
    plt.show();

def mapShow(inp):
    fig, ax = plt.subplots(figsize=(16,9))
    inp.plot(ax=ax,color='pink', edgecolor='grey',alpha=0.5)
    countries.plot(ax=ax, color='white', edgecolor='black',alpha=0.3)
    for i in inp.index:
        plt.annotate(patches.patch[i],xy=(patches.geometry[i].centroid.x,patches.geometry[i].centroid.y),size=1)
    fig=figsize=(1000,1000)
    ax.axis('scaled')
    plt.show();

def mapShowSave(inp,ent="test"):
    fig, ax = plt.subplots(figsize=(16,9))
    inp.plot(ax=ax,color='pink', edgecolor='grey',alpha=0.5)
    countries.plot(ax=ax, color='white', edgecolor='black',alpha=0.3)
    for i in inp.index:
        plt.annotate(patches.patch[i],xy=(patches.geometry[i].centroid.x,patches.geometry[i].centroid.y),size=1)
    fig=figsize=(1000,1000)
    ax.axis('scaled')
    plt.savefig(str(ent)+".png",dpi=1080)
    plt.show();

def plain_map():
    countries.plot()

def main():
    plain_map()
    setPrj()

if __name__ == "__main__":
    main()
