import pgzrun
WIDTH=800
HEIGHT=700
TITLE="quiz game"
game_over=False
allquestions=[]
question=[]
total=11
score=0
time=20
number=0

ryme=Rect(0,0,800,100)
rane=Rect(75,510,225,170)
rene=Rect(350,510,225,170)
rine=Rect(75,300,225,170)
rume=Rect(350,300,225,170)
line=Rect(75,130,500,140)
square=Rect(600,130,150,140)
lane=Rect(600,300,150,380)
options=[rine,rume,rane,rene]
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
   screen.draw.textbox(question[1],rine,color="black")
   screen.draw.textbox(question[2],rume,color="black")
   screen.draw.textbox(question[3],rane,color="black")
   screen.draw.textbox(question[4],rene,color="black")
   screen.draw.textbox(question[0],line,color="black")
   screen.draw.textbox(str(time),square,color="white")
   screen.draw.textbox("skip",lane,color="black")

def timer():
   global time,game_over
   if time>0:
      time=time-1
   else:
      game_over=True
      gameover()
clock.schedule_interval(timer,1)
def move_marquee():
   ryme.x=ryme.x+1
   if ryme.x>WIDTH:
      ryme.x=0

def on_mouse_down(pos):
   number=1
   for option in options:
      if option.collidepoint(pos):
         if number==int(question[5]):
            correct_answer()
         else:
            skip_question()
      number=number+1
   if lane.collidepoint(pos):
      skip_question()

def correct_answer():
   global score,number,time
   time=20
   score=score+1
   number=number+1
   if number==11:
      gameover()
   else:
      read_next_question()

def gameover():
   global question,time
   question=["GAME OVER.This was your score"+str(score),"-","-","-","-","5"]
   time=0


def skip_question():
   global score,number,time
   time=20
   number=number+1
   if number==11:
      gameover()
   else:
      read_next_question()

def read_question_file():
  global allquestions,total
  file=open("questions.txt","r")
  allquestions=file.readlines()
  total=len(allquestions)
  file.close()

def update():
   move_marquee()
def read_next_question():
   global number,question
   question=allquestions[number].split(",")
   print(question)
read_question_file()
read_next_question()

pgzrun.go()