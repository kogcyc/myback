class SimpleIndex:
	def __init__(self):
		self.index = {}
	def add_document(self, document_id, content):
		self.index[document_id] = content
	def search(self, query):
		results = []
		for doc_id, content in self.index.items():
			if query.lower() in content.lower():
				results.append(doc_id)
		return results

import json

my_dict = {"key1": "This is a sample document.", "key2": "This is a another document.", "key3": "Another sample example document."}
json_data = json.dumps(my_dict, indent=2)  # The indent parameter is optional and used for pretty formatting

print(json_data)

with open('output_file.json', 'w') as file:
	file.write(json_data)

with open('output_file.json', 'r') as file:
	loaded_data = json.load(file)


index = SimpleIndex()
for key in loaded_data:
	index.add_document(key, loaded_data[key])

search_query = "sample"
results = index.search(search_query)
for result in results:
	print(result)