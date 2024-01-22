#export MAGGIK=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
#sk-78LKW50e5lMcHLiNmlRXT3BlbkFJO9wTjEW6OXj7kUxbKOBVimport os

import sys
import re
from openai import OpenAI
client = OpenAI(api_key='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')
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": f"{sys.argv[1]}"}
  ]
)
con_tent = completion.choices[0].message.content

# Define a regular expression pattern to match code blocks
#code_pattern = r'```(?:[^`]+|`(?!``))+```'

# Use re.findall to find all occurrences of the code pattern in the string
#code_blocks = re.findall(code_pattern, con_tent)

# Print the extracted code blocks
#for code_block in code_blocks:
    #print(code_block)

#print(con_tent)

code_pattern = r'(?:[^`]+|`(?!``))+'
code_blocks = re.findall(code_pattern, con_tent, re.DOTALL)
for code_block in code_blocks:
  print(code_block)