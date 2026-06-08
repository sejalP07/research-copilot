from app.services.retrieval_service import (
    search_documents
)

results = search_documents(
    "What is Artificial Intelligence?"
)

print(results)