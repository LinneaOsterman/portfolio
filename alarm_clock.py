class Clock:
    # Initialize the clock with the given hours, minutes, and seconds
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    # Set the clock to a specific time
    def set_clock(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    # Simulate the ticking of the clock, advancing the time by one second
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
            if self.minutes == 60:
                self.hours += 1
                self.minutes = 0
                if self.hours == 24:
                    self.hours = 0
                    
    # Get the current time in HH:MM:SS format
    def get_time(self):
        return f"Time is {self.hours:02}:{self.minutes:02}:{self.seconds:02}"

# Inherit from the Clock class to create an Alarmclock subclass
class Alarmclock(Clock):
    # Initialize the alarm clock with the given hours, minutes, and seconds
    # Set additional attributes for alarm hours, alarm minutes, and alarm seconds
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.alarm_hours = 0
        self.alarm_minutes = 0
        
    # Set the alarm time
    def set_alarm(self, alarm_hours, alarm_minutes):
        self.alarm_hours = alarm_hours
        self.alarm_minutes = alarm_minutes
        self.alarm_seconds = 0

    # Get the current alarm time in HH:MM:SS format
    def get_alarm(self):
        return f"Alarm is set to {self.alarmHours:02}:{self.alarmMinutes:02}:{self.alarmSeconds:02}"

# Create an instance of Alarmclock and test the functionality    
alarm = Alarmclock(12,0,0)
print(alarm.get_time())
alarm.set_clock(6,50,0)
print(alarm.get_time())
alarm.set_alarm(7,0)
print(alarm.get_alarm())

# Continuously tick the alarm clock until the alarm time is reached
while True:
    alarm.tick()
    # Check if the current time matches the alarm time
    if alarm.hours == alarm.alarm_hours and alarm.minutes == alarm.alarm_minutes and alarm.seconds == alarm.alarm_seconds:
        print(alarm.get_time())
        print("Wake up!")
        break
