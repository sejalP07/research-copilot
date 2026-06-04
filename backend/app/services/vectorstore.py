from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

VECTORSTORE_PATH = "data/vectorstore"


def create_vectorstore(chunks):
    vectorstore = FAISS.from_texts(
        texts=chunks,
        embedding=embedding_model
    )

    vectorstore.save_local(
        VECTORSTORE_PATH
    )

    return vectorstore


def load_vectorstore():
    return FAISS.load_local(
        VECTORSTORE_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )


def retrieve_documents(
    query: str,
    k: int = 3
):
    vectorstore = load_vectorstore()

    docs = vectorstore.similarity_search(
        query,
        k=k
    )

    return docs