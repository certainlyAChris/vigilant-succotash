from sys import argv
from openai import OpenAI
import json

from accessing_time import get_time_date

client = OpenAI()

tools = [
    {
        "type": "function",

        "name": "get_time_date",

        "description": "Get the current time and date. There are no parameters",

        "parameters": {},
        # PARAMETERS NOT NEEDED

        "strict": False,

        #"additionalPorperties": False


    }
]

# A running input list that only includes function call outputs
input_list = []
conversation = client.conversations.create()


def prompt_params():
    global instructions
    global reasoningEffort
    global developerCommand

    if len(argv)<2:
        instructions = ""
    else:
        instructions = argv[1]

    if len(argv)<3:
        reasoningEffort = "medium"
    else:
        reasoningEffort = argv[3]

    if len(argv)<4:
        developerCommand = ""
    else:
        developerCommand = argv[3]

prompt_params()



prompt = ""
time_date = "unknown"

while (True):

    prompt = input("\nprompt: ")
    if prompt=="quit":
        break



    # Start a fresh input list for each prompt, but you can keep conversation context if needed
    input_list = []
    if developerCommand:
        input_list.append({
            "role": "developer",
            "content": developerCommand
        })
    input_list.append({
        "role": "user",
        "content": prompt
    })

    print("final input: ")
    print(input_list)

    response = client.responses.create(
        model="gpt-5-nano",
        input=input_list,
        reasoning={"effort": reasoningEffort},
        tools=tools,
        conversation=conversation.id
    )

    # If a function call is requested, handle it and send the result back
    for item in response.output:
        if item.type == "function_call" and item.name == "get_time_date":
            time_date = get_time_date()
            # Send the function call output as a new message
            function_output = [
                {
                    "role": "user",
                    "content": prompt
                },
                {
                    "type": "function_call_output",
                    "call_id": item.id,
                    "output": json.dumps({
                        "time_and_date": time_date
                    })
                }
            ]
            response2 = client.responses.create(
                model="gpt-5-nano",
                input=function_output,
                reasoning={"effort": reasoningEffort},
                tools=tools,
                conversation=conversation.id
            )
            print(response2.output_text)
            break
    else:
        print(response.output_text)

