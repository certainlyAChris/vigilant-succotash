# Import Libraries
from sys import argv
from openai import OpenAI
import json

# Import tools
from accessing_time import get_time_date

# Import helper functions
from adjust_model_params_with_args import prompt_params

class toolConverse:
    """Defines the conversation between the user and model, and contains the main event loop. Supports tools."""
    def __init__(self, model_params):

        # Intialize OpenAI client and conversation
        self.client = OpenAI()
        self.conversation = self.client.conversations.create()

        # Define model parameters
        self.instructions = model_params.get("instructions")
        self.developerCommand = model_params.get("developerCommand")
        self.reasoningEffort = model_params.get("reasoningEffort")

        # Load tools_list
        with open(r"function_calling_fun\tools_list.json", 'r') as tools_list_json_file:
            self.tools_list = json.load(tools_list_json_file)['tools_list']

        # Define input_list
        self.input_list = []
        if self.developerCommand:
                self.input_list.append({
                    "role": "developer",
                    "content": self.developerCommand
                })

    def _get_prompt_and_make_list(self):
            """Get a prompt from the user and add it to the input list"""
            user_prompt = input("\nprompt: ")
            if user_prompt=="quit":
                return False
            
            self.input_list.append({
                "role": "user",
                "content": user_prompt
            })

            #print("final input: ")
            #print(self.input_list)

            return True
    
    def _make_request_to_model(self):
        """Make request to model, inputting model, input_list, reasoningEffort, tools, and conversation"""
        response = self.client.responses.create(
                
            model="gpt-5-nano",

            input=self.input_list,

            reasoning={"effort": self.reasoningEffort},

            tools=self.tools_list,

            conversation=self.conversation.id
        )
        return response
         
    def _time_date_call(self, id):
         """Calls the time_date function and appends the ouptut to input list, then requests the model again."""
         time_and_date = get_time_date()
         
         # Generates a dictionary containing the output of the function call 
         function_call_output = {
              "type": "function_call_output",
              "call_id": id,
              "output": json.dumps({
                   "time_and_date_string": time_and_date
              })
            
         }

         # Adds function_call_output to input_list
         self.input_list.append(function_call_output)
         #print("input to model after function call")
         #print(self.input_list)
         
         # Makes second request to the model
         response2 = self._make_request_to_model()
         return response2

    def exec(self):
        """Main event loop."""
        while (True):
            
            # Get a prompt from the user and add it to the input list, breaking if prompt == 'quit'
            continue_conversation = self._get_prompt_and_make_list()
            if not(continue_conversation):
                break

            # Request for reponse
            response = self._make_request_to_model()

            # Check if function call is requested. If so, check name to see which function it was
            for item in response.output:
                # Check if function call was get_time_date
                if item.type == "function_call" and item.name == "get_time_date":

                    call_id = getattr(item, "call_id", None)
                    if call_id is None:
                        # fallback just for safety/debugging (but usually call_id exists)
                        call_id = getattr(item, "id", None)
                    response2 = self._time_date_call(call_id)
                    print(response2.output_text)
                    break
            else:
                print(response.output_text)

            # Reset input_list
            self.input_list = []
            if self.developerCommand:
                    self.input_list.append({
                        "role": "developer",
                        "content": self.developerCommand
                    })

# Define model variables form sys.arg args and store in dict model_params
model_params = prompt_params()

# create conversation with functions instance and execute
funConvo = toolConverse(model_params)
funConvo.exec()