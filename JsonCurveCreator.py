import os
import json
from tkinter import Tk



TemplateCurveBegin = '''Begin Object Class=/Script/CurveEditor.CurveEditorCopyBuffer Name="CurveEditorCopyBuffer"
   Begin Object Class=/Script/CurveEditor.CurveEditorCopyableCurveKeys Name="CurveEditorCopyableCurveKeys"'''

TemplateKeyPositions = "      KeyPositions({index})=(InputValue={time},OutputValue={value})"

TemplateKeyAttributes = "      KeyAttributes({index})=(bHasInterpMode=True)"

TemplateCurveEnd = '''   End Object
   Curves(0)=/Script/CurveEditor.CurveEditorCopyableCurveKeys'"CurveEditorCopyableCurveKeys"'
End Object'''





def clear():
    os.system('cls' if os.name=='nt' else 'clear')



def addToClipBoard(text):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)
    r.update()



def CreateCurve(input):
    KeyPositions = ""
    KeyAttributes =""
    TempIndex = 0

    Input_JSON = json.loads(input)

    for JsonValue in Input_JSON:
        KeyPositions += TemplateKeyPositions.format(index = TempIndex, time = JsonValue["Time"], value = JsonValue["Value"]) + "\r"
        KeyAttributes += TemplateKeyAttributes.format(index = TempIndex) + "\r"

        TempIndex += 1

    KeyPositions = KeyPositions[:len(KeyPositions) -1]
    KeyAttributes = KeyAttributes[:len(KeyAttributes) -1]

    return(str(TemplateCurveBegin + "\r" + KeyPositions + "\r" + KeyAttributes + "\r" + TemplateCurveEnd))





clear()

while True:
    print("Paste Curve Json(minified): ")

    try:
        addToClipBoard(CreateCurve(input()))

        print("Curve added to clipboard.")
    
    except:
        clear()
        
        print("Failed, wrong input.")