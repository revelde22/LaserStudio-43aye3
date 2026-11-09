"""Mezcla artística offline; no ejecuta el láser ni descarga modelos."""
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(root / 'work'))
from depth_map_tools import prepare_depth_map
folder = Path(__file__).resolve().parent
output = folder / 'demo_relieve_artistico.png'
prepare_depth_map(folder / 'demo_grises.png', folder / 'demo_grises.png',
                  output, gamma=1.0, remove_white=True,
                  circular=True, detail_weight=0.60)
print(output)
