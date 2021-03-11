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


![png](https://abader.org/nextcloud/s/qjdjFs9QCyrG8ij)



```python
my.setPrj(False)
grid=my.raster
grid["test"]=np.random.uniform(low=0.0, high=1.0, size=len(grid))
my.mapShowL(grid,"test")
```


![png](https://abader.org/nextcloud/s/o5xefgka4QTtwEb)



```python
my.setPrj(True)
grid=my.raster
grid["test"]=np.random.uniform(low=0.0, high=1.0, size=len(grid))
my.mapShowL(grid,"test")
```


![png](https://abader.org/nextcloud/s/dHYDxCCfffaq2y9)
