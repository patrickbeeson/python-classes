from datetime import datetime, timedelta

weeks = timedelta(weeks=2)
hours = timedelta(hours=1)
minutes = timedelta(minutes=100)
seconds = timedelta(seconds=1000)
composite = timedelta(hours=1, minutes=30)

now = datetime.now()
print(now)
print(now + weeks)
print(now + hours)
print(now + minutes)
print(now + seconds)
print(now + composite)