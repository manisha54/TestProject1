'''
  Building the car game ::
  CAR GAME:
        > help
          start - to start the car
          stop - to stop the car
          quit - to exit
        > asd
          I don't understand this
        > start
          Car started... Ready to go!!
        > stop
          Car stopped..
        > quit
'''
command=""
started=0 #false
#while command != "quit"
while True:
    command=input(">").lower()
    if command =="start":
        if started:
            print("car is already started !!")
        else:
            started=1 #true
            print("car started !!...")
    elif command=="stop":
        if not started:
            print("car is already stopped !!")
        else:
            started=0#false
            print("car stopped !!...")
    elif command == "help":
        print("""
start=to start a car
stop=to stop a car
quit=exit
        """)
    elif command=='quit':
        break
    else:
        print("sorry,i don't understand that !!")




