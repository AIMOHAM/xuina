bg=0
def setup():
    global img
    size(900,900)
    
def draw():
    global img
    # background(255)
    strokeWeight(2)
    line(mouseX,mouseY,pmouseX,pmouseY)
def keyPressed():
    if key == "1":
       background(255)   
        
    
    

        
