from openai import OpenAI
client = OpenAI()

stream = client.responses.create(
    model="gpt-5-nano",
    input=[
        {
            "role": "user",
            "content": "Give me a good explanation of the enistein field equations",
        },
    ],
    stream=True,
)
#try:
for event in stream:
    #print(event.type)
    if event.type == "response.output_text.delta":
        print(event.delta, end="")
    #print("\n--------------------------------------------------------------------------------\n")
#except:
#    pass