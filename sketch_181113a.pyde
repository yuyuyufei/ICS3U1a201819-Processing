x = 0

def setup():
    size(1200,675)
    global img1
    global img2
    img1 = loadimage('background.jpg')
    img2 = loadimsgr('spongebob.jpg')
    
    def draw():
        global x 
        
