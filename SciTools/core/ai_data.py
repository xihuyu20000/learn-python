"""

"""
from openai import OpenAI

client = OpenAI(api_key='QZh5teCkXeFtfNuA3l5XT3BlbkFJ7oouodyWkqJK7zAudlEv')

completion = client.chat.completions.create(model='gpt-3.5-turbo', messages=[{'role':'user', 'content':'中国未来20年的走势'}])
print(completion.choices[0].message)