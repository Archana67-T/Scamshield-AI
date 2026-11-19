!pip install openai
from openai import OpenAI



client = OpenAI(
    api_key=NEXUS_API_KEY,
    base_url="https://nexusapi.navigatelabs.ai"
)
from openai import OpenAI

client = OpenAI(
    api_key=NEXUS_API_KEY,
    base_url="https://nexusapi.navigatelabs.ai"
)

models = client.models.list()

for model in models.data:
    print(model.id)
response = client.chat.completions.create(
    model="nova-micro",
    messages=[
        {"role": "user", "content": "Explain phishing in 2 simple sentences."}
    ],
    temperature=0.2
)

print(response.choices[0].message.content)
