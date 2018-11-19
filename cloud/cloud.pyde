'''
Draw a cloud in the centre of the screen
'''

def setup():
    size(640, 360)
    background('#7a95c1')
    noStroke()
    noLoop()
    
def draw():
    drawCloud("#edeff2", 100, 200)
    drawCloud("#d4d5d6", 350, 100)
    drawCloud("#dee3e8", 450, 150)
    
def drawCloud(colour, xloc, yloc):
    noStroke()
    ellipse(xloc, yloc, 50, 50)
    ellipse(xloc+30, yloc, 50, 50)
    ellipse(xloc+10, yloc-20, 50, 50)

            
