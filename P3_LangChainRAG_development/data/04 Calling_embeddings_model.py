from langchain_community.embeddings import DashScopeEmbeddings

# Create the model object; if model is omitted, text-embedding-v1 is used by default
model = DashScopeEmbeddings()

# Do not use invoke or stream
# embed_query, embed_documents
print(model.embed_query("I like you"))
print(
    model.embed_documents(["I like you", "I liek you", "What to eat for dinner"])
)