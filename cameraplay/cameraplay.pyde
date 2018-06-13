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
#----------------
nC = 72
mCircles=[]
cr = 12
vw = 1280
vh = 720
#----------------
def setup():
    size(1280, 720)
    for x in range(nC):
        mCircles.append(movingcircle())
        mCircles[x].setpos(random(width),random(height))
    global video
    # global vw
    # global vh
    video = Capture(this,width, height)
    video.start()
    global f
    f = createFont("Helvetica", 36, True) 
#----------------
def draw():
    loadPixels()
    global video
    # global vw
    # global vh
#----------------
    video.loadPixels()
    #background(255)
    rt = 0
    gt = 0
    bt = 0
    c = 0
    cr = map(mouseX, 0, width, 4, 24)
    for x in range(nC):
       # mCircles[x].display()
        mCircles[x].move()
    for y in xrange(0,height,cr):
        for x in xrange(0,width,cr):
            c+=1
            loc = x + y*width
            r = red(video.pixels[loc])
            rt+=r
            g = green(video.pixels[loc])
            gt+=g
            b = blue(video.pixels[loc])
            bt +=b
            fill(r,g,b,125)
            noStroke()
            ellipse(x,y,cr,cr)

    fill(0)
    textFont(f,36)
    noStroke()
   # rect(0,740,width,40)
    fill(255)
    s = "r:" + str(int(bt/c)) + " g: " + str(int(gt/c)) +" b: " + str(int(bt/c)) 
    #s = str(bt/c)
    text(s,30,600)
#----------------
def captureEvent(c):
    c.read()
