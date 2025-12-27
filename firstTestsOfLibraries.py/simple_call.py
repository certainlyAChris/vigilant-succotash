from openai import OpenAI

client = OpenAI()


response = client.responses.create(
    model="gpt-5-nano",
    input="hello, this is a test of me calling the API",
    
)

print(response.output_text)