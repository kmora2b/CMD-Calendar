"""This is a multi line comment"""
from time import sleep, strftime
NAME = "Kim"
calendar = {
  
}

def welcome():
  print "Welcome " + NAME + "\nThe calendar is now opening..."
  sleep(1)
  print "Today is: " + strftime("%A %B %d, %Y")
  print "Current time: " + strftime("%H: %M: %S")
  print "What would you like to do?"
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Type a letter:\n A: Add \n U: Update \n V: View \n D: Delete \n X: Exit\n")
    if user_choice.lower() == "v":
      if len(calendar.keys()) < 1:
        print "Calendar is empty"
      else:
        print calendar
    elif user_choice.lower() == "u":
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Update successful! "
      print calendar
    elif user_choice.lower() == "a":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
        print "Invalid date was entered "
        try_again = raw_input("Try again? Y for Yes, N for No: ").lower()
        if try_again == "y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print "Event successfully added "
    elif user_choice.lower() == "d":
      if len(calendar.keys()) < 1:
        print "Calendar is empty "
      else:
        event = raw_input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del (calendar[date])
            print "Event has been deleted "
            print calendar
          else:
            print "Incorrect event"
    elif user_choice.lower() == "x":
      start = False
    else:
      print "Invalid command "
      return;
      

start_calendar()
  
