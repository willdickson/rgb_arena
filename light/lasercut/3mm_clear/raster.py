from __future__ import print_function
import sys
import os
from py2gcode import gcode_cmd
from py2gcode import cnc_laser

dxfFileName = sys.argv[1]

layerList = ['raster']

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
param = {
        'fileName'    :  dxfFileName,
        'layers'      :  layerList,
        'dxfTypes'    :  ['CIRCLE','LINE','ARC'],
        'laserPower'  :  200,
        'feedRate'    :  400,
        'convertArcs' :  True,
        'startCond'   : 'minX',
        'direction'   : 'ccw',
        'ptEquivTol'  :  0.4e-3,
        }

vectorCut = cnc_laser.VectorCut(param)
prog.add(vectorCut)

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)

baseName, ext = os.path.splitext(dxfFileName)
ngcFileName = 'raster_{0}.ngc'.format(baseName)
print(ngcFileName)
prog.write(ngcFileName)
