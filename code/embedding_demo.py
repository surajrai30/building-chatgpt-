import numpy as np

vocabulary = {
    "i": 0,
    "love": 1,
    "ai": 2,
    "learning": 3
}

embedding_dimension = 4

embedding_matrix = np.random.rand(
    len(vocabulary),
    embedding_dimension
)

print("Embedding Matrix:\n")
print(embedding_matrix)

word = "ai"

print("\nEmbedding for", word)
print(embedding_matrix[vocabulary[word]])
