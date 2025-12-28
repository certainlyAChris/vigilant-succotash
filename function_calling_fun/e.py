import accessing_time
import json
time_and_date = accessing_time.get_time_date()
t = json.dumps({
                   "time_and_date_string": time_and_date
              })
print(t)