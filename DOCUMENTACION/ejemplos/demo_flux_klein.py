"""Genera un workflow API Klein sin iniciar ComfyUI ni descargar pesos."""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
from comfy_design_client import workflow,DEFAULT_MODEL
out=Path(__file__).resolve().parent/'demo_flux_klein_api.json'
graph=workflow('Virgin of the Pillar, full body on her column','Escala de grises',DEFAULT_MODEL,768,768,steps=4,circular=True,seed=43)
out.write_text(json.dumps(graph,indent=2),encoding='utf-8')
assert graph['2']['inputs']['device']=='cpu'
print(out)
