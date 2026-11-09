"""Crear un proyecto y preparar geometría offline; no conecta ni marca."""
import os,sys
from pathlib import Path
os.environ.setdefault('QT_QPA_PLATFORM','offscreen')
root=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(root/'work'))
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QRectF
from PySide6.QtGui import QPainterPath
from comfy_design_ui import DesignDialog
# Evitar preparación IA en esta herramienta offline.
DesignDialog.connect_comfy=lambda self:None
from laser_studio import Main,GItem
from laser_job import from_scene
app=QApplication.instance() or QApplication([])
main=Main();path=QPainterPath();path.addRect(QRectF(45,45,20,20))
item=GItem(path);main.scene.addItem(item)
cut=main.cuts[0];cut.mode='Fill';cut.interval=.05
job=from_scene(main)
assert job.operations and job.operations[0].kind=='Fill'
output=Path(__file__).resolve().parent/'demo_20mm.43laser'
assert main._save(str(output))
print('Operaciones:',len(job.operations),'Campo:',job.bounds)
print('Proyecto guardado:',output)
