import datetime
import time
from plyer import notification

print("")
ans = input("Do you want to set a reminder? (y/n) : ")
if ans not in ["Y", "y", "Yes", "yes"]:
    print("Thanks for the running the program!")
    exit(0)
print("Please enter date time below in the format of the below given example.")
print("Mistake in format might show unexpected errors.")
print("January 1, 2000 - 1:10 pm")
Tasks = []
Dates_times = []
Reminders = {}
while True:
    task = input("Enter your task please : ")
    date_string = input("Enter your reminder date and time : ")
    inp = datetime.datetime.strptime(date_string, "%B %d, %Y - %I:%M %p")
    Tasks.append(task)
    Dates_times.append(inp)
    t = input("Do you want to register any other schedule? (y/n) : ")
    if t not in ["y", "Y", "Yes", "yes"]:
        break
for i in range(len(Dates_times)):
    Reminders[Dates_times[i]] = Tasks[i]
while len(Reminders) != 0:
    x = datetime.datetime.now()
    y = x.strftime("%d/%m/%Y %H:%M")
    now = datetime.datetime.strptime(y, "%d/%m/%Y %H:%M")
    if now in Reminders.keys():
        rem = Reminders[now]
        notification.notify(
            title = "Reminder for you!",
            message = rem,
            timeout = 3
        )
        del Reminders[now]
    time.sleep(1)
notification.notify(
    title = "Finished!",
    message = "Wow! You have successfully completed all your tasks\nYour Welcome!",
    timeout = 5
)



