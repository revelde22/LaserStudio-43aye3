"""Escala objetivo sintética: no es calibración real de material."""
import sys,json
from pathlib import Path
import numpy as np
from PIL import Image
root=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(root/'work'))
from depth_map_tools import export_mm_map,passes_from_mm
out=Path(__file__).resolve().parent
source=out/'demo_grises.png'
Image.fromarray(np.tile(np.linspace(255,0,256).astype('uint8'),(128,1))).save(source)
count,rate=passes_from_mm(.2,.1,10)
assert count==20
path=export_mm_map(source,.2,.1,10)
meta=json.loads(Path(path).with_suffix('.json').read_text())
with Image.open(path) as image:depth=np.asarray(image,dtype=float)/65535*meta['target_max_mm']
assert depth.min()==0 and abs(depth.max()-.2)<1e-9
print('Objetivo:',depth.min(),'-',depth.max(),'mm; ejemplo:',count,'pasadas')
print(path)
