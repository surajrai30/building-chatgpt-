text = "I love learning about language models."

tokens = text.lower().split()

print("Original Text:")
print(text)

print("\nTokens:")
print(tokens)

# Create a simple vocabulary
vocab = {}

for token in tokens:
    if token not in vocab:
        vocab[token] = len(vocab)

print("\nVocabulary:")
print(vocab)

token_ids = [vocab[token] for token in tokens]

print("\nToken IDs:")
print(token_ids)
