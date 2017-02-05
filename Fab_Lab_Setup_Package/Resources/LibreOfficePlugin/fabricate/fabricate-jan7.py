#Author: Edward Baafi
#Edited By: David Solomon
#04-16-2015
#Embedded OpenOffice Epilog Printing - Finally (and nowhere near enough)
#1-07-2006

#FABUNTU - check if openoffice running before unopkg  

import uno, unohelper, os
from com.sun.star.task import XJobExecutor
from com.sun.star.awt import XActionListener
from com.sun.star.awt import FontDescriptor
from com.sun.star.beans import PropertyValue

#Cancel Button Listener
class CancelButtonListener(XActionListener, unohelper.Base):
  
    def __init__(self, dialog):
        self.dialog = dialog

    def disposing(self):
        pass
# close dialog box
    def actionPerformed(self, event):
        self.dialog.endExecute()

# Fabricate Button Listener 
class FabricateButtonListener(XActionListener, unohelper.Base):
  
    def __init__(self, top, xMinModel, bedHeightModel, powerModel, speedModel, rateModel, dialog):
        self.top = top
        self.documentModel = top.documentModel
        self.xMinModel = xMinModel
        self.bedHeightModel = bedHeightModel
        self.powerModel = powerModel
        self.speedModel = speedModel
        self.rateModel = rateModel
        self.dialog = dialog

    def disposing(self):
        pass

    def actionPerformed(self, event):
        global docURL
        global docTitle
        #get values for xmin and bedheight
        xMin = self.xMinModel.Value
        bedHeight = self.bedHeightModel.Value
        power = self.powerModel.Value
        speed = self.speedModel.Value
        rate = self.rateModel.Value
        # close dialog box
        self.dialog.endExecute()

 
        # prepare and export as eps
  
        exportProperty=PropertyValue()
   
        exportProperty.Name="FilterName"
     
        exportProperty.Value="draw_eps_Export"
     
        self.documentModel.storeToURL("file:///usr/local/bin/fabscripts/tmp/tmp.eps",(exportProperty,)) 
        
        
        #convert to dxf
        try:
            print (os.system("pstoedit -f dxf /usr/local/bin/fabscripts/tmp/tmp.eps /usr/local/bin/fabscripts/tmp/tmp.dxf"))
        # get doc title from URL 
        
            for propertyVal in self.documentModel.getArgs():
                if propertyVal.Name == 'URL':
                    docURL = propertyVal.Value
            #get filename from path
                    docTitle = os.path.split(docURL)[1]
                    break

        # or get doc title from title  
            else:
                for propertyVal in self.documentModel.getArgs():
                    if propertyVal.Name == 'Title':
                        docTitle = propertyVal.Value
                        break

         # or doc title is unknown
                else:     
                    docTitle = 'unknown' 

            print ("***************************")
            print ("jobname: " + docTitle)
            print ("***************************")
        
    #Process in cam
        
            os.system("python /usr/local/bin/fabscripts/tmp/cam.py -i /usr/local/bin/fabscripts/tmp/tmp.dxf -x " +str(xMin) + " -h " + str(bedHeight) + " -o /usr/local/bin/fabscripts/tmp/tmp.epi -e "+str(power)+" -s "+str(speed)+" -a "+str(rate)+" -j " + docTitle +" -w")
        except Exception as e:
            print ('No ed baafi, I, David Solomon, caught the error: ' , str(e))
            print ('Here is it: ' , str(e.message))

#Send to laser
        try:
            os.system("python /usr/local/bin/fabscripts/laser.py /usr/local/bin/fabscripts/tmp/tmp.epi")
        except Exception as e:
            print ('Here is it: ' , str(e.message))

       
#Remove temp files
	
        os.system("rm /usr/local/bin/fabscripts/tmp/tmp.eps")
        os.system("rm /usr/local/bin/fabscripts/tmp/tmp.dxf")
        os.system("rm /usr/local/bin/fabscripts/tmp/tmp.epi")
	
def createNumericField(dialogModel, xPosition, yPosition, width, height, name, value, maxValue, minValue, decimalAccuracy):
    numericModel = dialogModel.createInstance("com.sun.star.awt.UnoControlNumericFieldModel")
    numericModel.PositionX = xPosition
    numericModel.PositionY = yPosition
    numericModel.Width = width
    numericModel.Height = height
    numericModel.Name = name
    numericModel.Value = value
    numericModel.ValueMax = maxValue
    numericModel.ValueMin = minValue
    numericModel.DecimalAccuracy = decimalAccuracy
    return numericModel


def createButton(dialogModel, xPosition, yPosition, width, height, name, tabIndex, label):
    buttonModel = dialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")
    buttonModel.PositionX = xPosition
    buttonModel.PositionY = yPosition
    buttonModel.Width = width
    buttonModel.Height = height
    buttonModel.Name = name
    buttonModel.TabIndex = tabIndex
    buttonModel.Label = label
    return buttonModel

def createFixedText(dialogModel, xPosition, yPosition, width, height, name, label, fontWeight):
    labelModel = dialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")
    labelModel.PositionX = xPosition
    labelModel.PositionY = yPosition
    labelModel.Width = width
    labelModel.Height = height
    labelModel.Name = name
    labelModel.Label = label
    #create font descriptor if not regular font
    if fontWeight == "bold":
       fontDescStruct = FontDescriptor()
       fontDescStruct.Weight = 150.0000 #Bold
       labelModel.FontDescriptor = fontDescStruct
    return labelModel

 
def createDialog(top):

    dialogModel = top.createService("com.sun.star.awt.UnoControlDialogModel")
    dialogModel.PositionX = 100
    dialogModel.PositionY = 100
    dialogModel.Width = 220
    dialogModel.Height = 170
    dialogModel.Title = "Fabricate Drawing"


    cancelButtonModel = createButton(dialogModel, 120, 145, 35, 10, "CancelButton", 0, "Cancel")
    fabricateButtonModel = createButton(dialogModel, 165, 145, 40, 10, "FabricateButton", 0, "Fabricate")
    textModel1 = createFixedText(dialogModel, 15, 5, 130, 10, "Text1","Where Printing Will Start", "bold")
    textModel2 = createFixedText(dialogModel, 28, 21, 45, 8, "Text2", "Left Boundary", "standard")
    textModel3 = createFixedText(dialogModel, 110, 21, 45, 8, "Text3", "inches from left", "standard")
    numericModel1 = createNumericField(dialogModel, 85, 21, 20, 9, "Numeric1", 0.1, 22, 0, 2)
    textModel4 = createFixedText(dialogModel, 28, 37, 52, 8, "Text4", "Bottom Boundary", "standard")
    textModel5 = createFixedText(dialogModel, 110, 37, 45, 8, "Text5", "inches from top", "standard")
    numericModel2 = createNumericField(dialogModel, 85, 37, 20, 9, "Numeric2", 10, 11.9, 0.5, 2)
    textModel6 = createFixedText(dialogModel, 15, 65, 130, 10, "Text6", "Laser Cutting Settings", "standard")
    textModel7 = createFixedText(dialogModel, 48, 81, 20, 8, "Text7", "Power:", "standard")
    textModel8 = createFixedText(dialogModel, 97, 81, 45, 8, "Text8" , "%", "standard")
    numericModel3 = createNumericField(dialogModel, 73, 81, 20, 9, "Numeric3", 50, 100, 0, 0)
    textModel9 = createFixedText(dialogModel, 48, 97, 20, 8, "Text9", "Speed:", "standard")
    textModel10 = createFixedText(dialogModel, 97, 97, 45, 8, "Text10", "%", "standard")
    numericModel4 = createNumericField(dialogModel, 73, 97, 20, 9, "Numeric4", 50, 100, 0, 0)
    textModel10 = createFixedText(dialogModel, 97, 97, 45, 8, "Text10", "%", "standard")
    numericModel5 = createNumericField(dialogModel, 140, 81, 20, 9, "Numeric5", 2500, 5000, 10, 0)
    textModel11 = createFixedText(dialogModel, 120, 81, 25, 8, "Text11", "Rate:", "standard")
    
    dialogModel.insertByName("FabricateButton", fabricateButtonModel)
    dialogModel.insertByName("CancelButton", cancelButtonModel)
    dialogModel.insertByName("Text1", textModel1)
    dialogModel.insertByName("Text2", textModel2)
    dialogModel.insertByName("Text3", textModel3)
    dialogModel.insertByName("Text4", textModel4)
    dialogModel.insertByName("Text5", textModel5)
    dialogModel.insertByName("Text6", textModel6)
    dialogModel.insertByName("Text7", textModel7)
    dialogModel.insertByName("Text8", textModel8)
    dialogModel.insertByName("Text9", textModel9)
    dialogModel.insertByName("Text10", textModel10)
    dialogModel.insertByName("Text11", textModel11)
    dialogModel.insertByName("Numeric1", numericModel1)
    dialogModel.insertByName("Numeric2", numericModel2)
    dialogModel.insertByName("Numeric3", numericModel3)
    dialogModel.insertByName("Numeric4", numericModel4)
    dialogModel.insertByName("Numeric5", numericModel5)


    dialog = top.createService("com.sun.star.awt.UnoControlDialog")
    dialog.setModel(dialogModel)

    
    cancelListener = CancelButtonListener(dialog)
    cancelButtonCtrl = dialog.getControl("CancelButton")
    cancelButtonCtrl.addActionListener(cancelListener)

    fabricateListener = FabricateButtonListener(top, numericModel1, numericModel2, numericModel3, numericModel4,numericModel5, dialog)
    fabricateButtonCtrl = dialog.getControl("FabricateButton")
    fabricateButtonCtrl.addActionListener(fabricateListener)
    
    dialog.createPeer(top.createService("com.sun.star.awt.Toolkit"), None)
    dialog.execute()
    dialog.dispose()


# an UNO component fabricate drawing (print to the Epilog Laser..)
# derived from the unohelper.Base class - implements XJobExecutor interface
class Fabricate(unohelper.Base,XJobExecutor):
    def __init__( self, ctx ):

        # store component context
        self.ctx = ctx

    def trigger( self, args ):
        
# get desktop object
        #desktop = self.ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", self.ctx )
        self.desktop = self.createService("com.sun.star.frame.Desktop")
        # get document model (component)
        self.documentModel = self.desktop.getCurrentComponent()
        
	# create dialog box
        createDialog(self)

    def createService(self, cClass):
        return self.ctx.ServiceManager.createInstanceWithContext(cClass, self.ctx)

        


# pythonloader needs ImplementationHelper 
g_ImplementationHelper = unohelper.ImplementationHelper()

g_ImplementationHelper.addImplementation(Fabricate,        # UNO object class
        "fab-lab.comp.pyuno.baafi.fabricate",       # unique implementation name
        ("com.sun.star.task.Job",),)                # Job is only implemented service







