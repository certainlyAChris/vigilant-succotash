import json
import sys

sys.path.insert(0, "function_calling_fun")

from accessing_time import get_time_date

time_date = get_time_date()

print(json.dumps({"time_and_date": time_date}))