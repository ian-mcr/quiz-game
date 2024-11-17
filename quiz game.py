import pgzrun
WIDTH=800
HEIGHT=700
TITLE="quiz game"
allquestions=[]
question=[]
total=11
timer=50
number=0

ryme=Rect(0,0,800,100)
rane=Rect(75,510,225,170)
rene=Rect(350,510,225,170)
rine=Rect(75,300,225,170)
rume=Rect(350,300,225,170)
line=Rect(75,130,500,140)
square=Rect(600,130,150,140)
lane=Rect(600,300,150,380)
def draw():
  
   screen.draw.filled_rect(ryme,"black")
   screen.draw.filled_rect(rane,"orange")
   screen.draw.filled_rect(rene,"orange")
   screen.draw.filled_rect(rine,"orange")
   screen.draw.filled_rect(rume,"orange")
   screen.draw.filled_rect(line,"white")
   screen.draw.filled_rect(square,"blue")
   screen.draw.filled_rect(lane,"green")

   screen.draw.textbox("welcome to quiz",ryme,color="white")
   screen.draw.textbox("1",rine,color="black")
   screen.draw.textbox("2",rume,color="black")
   screen.draw.textbox("3",rane,color="black")
   screen.draw.textbox("4",rene,color="black")
   screen.draw.textbox("question",line,color="black")
   screen.draw.textbox("Time",square,color="white")
   screen.draw.textbox("skip",lane,color="black")

def move_marquee():
   ryme.x=ryme.x+1
   if ryme.x>WIDTH:
      ryme.x=0

def on_mouse_down(pos):
   pass

def correct_answer():
   pass

def game_over():
   pass

def skip_question():
   pass

def update_time_left():
   pass


def read_question_file():
  file=open("questions.txt","r")
  allquestions=file.readlines()
  total=len(allquestions)
  print(allquestions[number])
  file.close()

def update():
   move_marquee()
   
read_question_file()

pgzrun.go()