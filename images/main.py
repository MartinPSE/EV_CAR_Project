import project
from datetime import datetime, timedelta

start = datetime.now()
project.checkplate('e5.jpg')
print(datetime.now() - start )
