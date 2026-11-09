"""Llamar install_counter(main) después de crear los menús."""
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMessageBox

def install_counter(main):
    action=QAction('Contar objetos',main)
    action.triggered.connect(lambda:QMessageBox.information(main,'Selección',f'{len(main.selected())} objetos seleccionados'))
    tools=next((a.menu() for a in main.menuBar().actions() if a.menu() and a.text().replace('&','')=='Tools'),None)
    if tools:tools.addAction(action)
    return action
