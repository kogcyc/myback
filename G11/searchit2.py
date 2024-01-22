from lorem.text import TextLorem
lorem = TextLorem(wsep=' ', srange=(450,450))
lorem.sentence()

class SimpleIndex:
    def __init__(self):
        self.index = {}
    def add_document(self, document_id, content):
        self.index[document_id] = content
    def search(self, query1, query2=None):
        results = []
        for doc_id, content in self.index.items():
            if query1.lower() in content.lower() and (query2 is None or query2.lower() in content.lower()):
                results.append(doc_id)
        return results

# Create an instance of SimpleIndex
my_index = SimpleIndex()

# Add documents
my_index.add_document(1, "This is a sample document with string1.")
my_index.add_document(2, "Another document containing string2.")
my_index.add_document(3, "A third document with both string1 and string2.")

# Search for documents containing "string1" without specifying "string2"
results = my_index.search("string1")

# Print the results
print("Documents containing string1:", results)

# Search for documents containing "string1" without specifying "string2"
results = my_index.search("string1","both")

# Print the results
print("Documents containing string1:", results)
