import pymel.core as pm
import OpenMaya as om




class Pyletool:
    """
    Tool thtat takes 3 selected bones with an ik solver 
    and placed a locator where the polevector imfluent object must be.
    """
    def __init__(self):
        """Initialize data, including basic UI"""
        pass
    def retrieve(self):
        """Retrieve data from the selected objects"""
        selection = pm.ls(sl=True, type ='joint')
        if not len(selection) == 3:
            raise ValueError("Selection must be of lengh 3")
        else:
            self.objects = selection
    def calcPos(self):
        if not self.objects:
            raise AttributeError("None objects have been selected")
        else:
            #Querry positions
            dataA = pm.xform(self.objects[0],q=True,ws=True,t=True)
            dataB = pm.xform(self.objects[1],q=True,ws=True,t=True)
            dataC = pm.xform(self.objects[2],q=True,ws=True,t=True)
            #Inicializate joints vectors throug position querry
            vA = om.MVector(dataA[0],dataA[1],dataA[2])
            vB = om.MVector(dataB[0],dataB[1],dataB[2])
            vC = om.MVector(dataC[0],dataC[1],dataC[2])
            #Vector calculation
            size = vC - vA
            halfsize = size * .5
            halfpos = vA + halfsize
            returnpos = (vB + halfpos) * 2
            return returnpos
            
    def doit(self):
        """Place a locator over the correct coordinates"""
        self.retrieve()
        pos = self.calcPos()
        self.loc = pm.spaceLocator(name='pyle_locator1')
        pm.setAttr(self.loc+'.translate', pos)
        
        
class PyleUI:
    def __init__(self):
        if pm.window('pyleUI', ex=True):
            self.w = pm.window('pyleUI', q=True)
            pm.showWindow(self.w)
        else:
            self.w = pm.window('pyleUI', t='Pyle_Vector', h=300,w=300)
            pm.columnLayout(adjustableColumn=True)
            pm.text(label='SELECT 3 JOINTS PARENT->CHILDREN ORIENTATION',align='center',rs=True)
            self.button = pm.button(label='DoIt', command = 'pyletool.doit()')
            pm.showWindow(self.w)
    
    
###Copy for shelve button
pyletool = Pyletool
pyleui = PyleUI
###Copy for shelve button
    
    
    
    
    
    
    
    
    
    
    