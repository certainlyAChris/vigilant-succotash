from sys import argv
from openai import OpenAI
import json


with open(r"function_calling_fun\tools_list.json", 'r') as tools_list_json_file:

    tools_list = json.load(tools_list_json_file)

print(tools_list['tools_list'])