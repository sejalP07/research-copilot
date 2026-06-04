from app.services.vectorstore import retrieve_documents

docs = retrieve_documents(
    "What is Artificial Intelligence?"
)

print("\nRetrieved Documents:\n")

for doc in docs:
    print(doc.page_content)
    print("-" * 50)