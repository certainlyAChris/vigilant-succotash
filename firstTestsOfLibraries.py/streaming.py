from openai import OpenAI
client = OpenAI()

stream = client.responses.create(
    model="gpt-5-nano",
    input=[
        {
            "role": "user",
            "content": "Say 'Give me a good explanation of the enistein field equations",
        },
    ],
    stream=True,
)
try:
    for event in stream:
        if event.type == "response.output_text.delta":
            print(event.delta, end="")
except:
    pass