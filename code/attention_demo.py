import numpy as np

words = ["I", "love", "AI"]

# Random attention scores
attention = np.array([
    [0.2, 0.5, 0.3],
    [0.1, 0.7, 0.2],
    [0.4, 0.3, 0.3]
])

print("Words:")
print(words)

print("\nAttention Scores:")
print(attention)

for i, word in enumerate(words):
    print(f"\nWhile processing '{word}' the model pays attention to:")
    for j, other in enumerate(words):
        print(f"{other}: {attention[i][j]:.2f}")
