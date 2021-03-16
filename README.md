# aa_map
Plot fishing patches in the north atlantic

```python
import os
import sys
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import aa_map.map as my

```


```python
my.mapShow(my.raster)
```


![png](https://user-images.githubusercontent.com/42641926/111285472-78a4e200-8641-11eb-90f5-0951e5ab2cf9.png)



```python
my.setPrj(False)
grid=my.raster
grid["test"]=np.random.uniform(low=0.0, high=1.0, size=len(grid))
my.mapShowL(grid,"test")
```


![png](https://user-images.githubusercontent.com/42641926/111285477-793d7880-8641-11eb-8bf8-72fe9e8608eb.png)



```python
my.setPrj(True)
grid=my.raster
grid["test"]=np.random.uniform(low=0.0, high=1.0, size=len(grid))
my.mapShowL(grid,"test")
```


![png](https://user-images.githubusercontent.com/42641926/111285480-79d60f00-8641-11eb-8cdc-0afe652fe085.png)
