"""Demostración offline de contador, ETA y STOP; no controla hardware."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
from mark_time_estimate import MarkTimeEstimate
from mark_pass_counter import PassCounter
clock=[0.]
groups=[(0,[[(0,0),(100,0)]],2,10.,25.,30.),(0,[[(0,0),(10,0)]],1,10.,10.,30.)]
eta=MarkTimeEstimate(groups,lambda:clock[0])
counter=PassCounter([(1,2,'grabado'),(1,1,'limpieza')])
print(counter.text());print(eta.text())
clock[0]=30.;eta.confirm_block();counter.confirm_block()
print(counter.text());print(eta.text())
clock[0]=31.;eta.stop()
print(counter.text(stopped=True));print(eta.text())
assert eta.percent<100
