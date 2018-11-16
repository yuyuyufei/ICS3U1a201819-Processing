x = 0

y = 30

b = 675

f = 675

v = 4

v2 = 7

def setup():
    size(300,168)
    global img1
    global img2
    img1 = loadImage('background.jpeg')
    img2 = loadImage('spongebob.jpeg')
    
def draw():
    global x
    global y
    global f
    global v
    global v2
    
    x += v
    if x >= 300:
        v = -4
    if x <= 0:
        v = 4
    background(img1)
    
    noStroke()
    
    triangle(b, 3*b, 280, 250, 100, 100)
    global b
    if keyPressed:
        if key == 'f' :
            b += 20
        if b >= 168:
            b = 0
    
    rect(y, 100, 50, 50)
    
    if keyPressed:
        if key == 'j' :
            y += 12
        if y >= 168:
            y = 0
    
    ellipse(x, 40, 50, 50)
    
    fill(213, 151, 161)
    
    image(img2, f, 50, 50, 40)
    f += v2
    if f >= 300:
        v2 = -7
    if f <= 0:
        v2 = 7
    
        

            
        
    
   
     
  

   
 


    
    
