add_library('video')
video = None
class movingcircle(object):
    def __init__(self):
        self.c = color(random(255),random(255),random(255),100)
        self.xp = random(100)
        self.yp = random(100)
        self.es = random(10,90)
        self.vc = PVector(random(-10,10), random(-10,10))
    def setpos(self,x,y):
        self.xp = x
        self.yp = y
    def display(self):
        strokeWeight(1)
        stroke(255,255,255)
        noStroke()
        fill(self.c)
        ellipse(self.xp,self.yp,self.es,self.es)
    
    def move(self):
        self.xp += self.vc.x
        self.yp += self.vc.y
        
        if (self.xp>width):
            self.xp = 0
        if (self.xp<0):
            self.xp=width
        if (self.yp>height):
            self.yp = 0
        if (self.yp<0):
            self.yp=height
nC = 72
mCircles=[]
cr = 12
vw = 1280
vh = 720
def setup():
    size(1280, 780)
    for x in range(nC):
        mCircles.append(movingcircle())
        mCircles[x].setpos(random(width),random(height))
    global video
    global vw
    global vh
    video = Capture(this,vw, vh)
    video.start()
    global f
    f = createFont("Helvetica", 28, True) 

def draw():
    loadPixels()
    global video
    global vw
    global vh
#
    video.loadPixels()
    cr = map(mouseX, 0, width, 6, 24)
    for x in range(nC):
       # mCircles[x].display()
        mCircles[x].move()
    for y in xrange(0,vh,cr):
        for x in xrange(0,vw,cr):
            loc = x + y*width
            r = red(video.pixels[loc])
            g = green(video.pixels[loc])
            b = blue(video.pixels[loc])
            fill(r,g,b,125)
            noStroke()
            ellipse(x,y,cr,cr)
    strokeWeight(10)
    stroke(0)
    line(0,vh,width,vh)
    textFont(f,26)
    
    text("Hello Strings!",10,740)

def captureEvent(c):
    c.read()
