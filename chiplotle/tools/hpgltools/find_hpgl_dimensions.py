from chiplotle.hpgl.abstract.hpgl import _HPGL
from chiplotle.hpgl.compound.container import Container
from chiplotle.hpgl.compound.hpglcontainer import HPGLContainer


def find_hpgl_dimensions(hpgl):
   '''
   returns [[minX, minY], [maxX, maxY]] found in hpgl object
   '''
   
   maxX = -100000.0
   minX = 100000.0
   maxY = -100000.0
   minY = 100000.0

   if isinstance(hpgl, (list, tuple, Container, HPGLContainer)):
      for command in hpgl:
         if hasattr(command, 'xy') and len(command.xy) > 0: 
            xy = command.xy
        
            x = xy[0][0]
            y = xy[0][1]
        
            if x > maxX:
               maxX = x
         
            if x < minX:
               minX = x
        
            if y > maxY:
               maxY = y
        
            if y < minY:
               minY = y
      return [[minX, minY], [maxX, maxY]]
   else:
      return None
      
      

