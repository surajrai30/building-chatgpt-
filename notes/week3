# Week 3

This week I learned how text is converted into a format that a language model can understand. Since computers cannot directly work with words, there are a few steps before the text is given to the model.

## Tokenization

The first step is tokenization.

Tokenization means breaking a sentence into smaller pieces called **tokens**. A token can be a word, a part of a word or even a punctuation mark.

For example,

```
I love playing football.
```

can be split into

```
["I", "love", "playing", "football", "."]
```

Sometimes even a single word is divided into smaller parts.

For example,

```
unbelievable
```

may become

```
["un", "believ", "able"]
```

This depends on the tokenizer being used.

I initially thought every word would be treated as one token, but that is not always true.

---

## Why do we need Tokenization?

A computer cannot understand normal text directly.

Before a sentence is processed, it has to be broken into tokens. Each token is then assigned a unique number called a **Token ID**.

For example,

```
I love AI
```

may become

| Token | Token ID |
|-------|----------|
| I | 15 |
| love | 82 |
| AI | 301 |

These numbers are easier for the model to process.

---

## Embeddings

After learning about token IDs, I had one question.

If every word already has an ID, why do we need embeddings?

The answer is that token IDs are just numbers used to identify words. They don't contain any meaning.

For example,

```
Cat → 15
Dog → 82
Car → 301
```

From these IDs, the model cannot tell that "cat" and "dog" are more similar than "cat" and "car".

This is where embeddings are useful.

An embedding converts every token into a vector of numbers.

These vectors help the model learn relationships between words during training.

Words used in similar contexts usually end up having similar embeddings.

---

## Example

Suppose we have the sentence

```
The cat is sleeping.
```

The steps would be something like this:

```
Sentence
      ↓
Tokenization
      ↓
["The", "cat", "is", "sleeping", "."]
      ↓
Token IDs
      ↓
[25, 41, 13, 208, 5]
      ↓
Embeddings
      ↓
Vectors
```

These vectors are then passed to the neural network.

---

## Vocabulary

Another important term I came across was **Vocabulary**.

The vocabulary is simply the collection of all the tokens that a model knows.

If a token is not present in the vocabulary, the tokenizer usually breaks it into smaller pieces that already exist.

This makes it possible to handle words that the model has never seen before.

---

## My Notes

This week helped me understand why language models cannot directly read text.

I found the idea of tokenization quite simple, but embeddings were a little more interesting because they actually represent the meaning of words instead of just assigning numbers.

One thing I still want to understand better is how these embeddings are learned during training. Right now I know what they do, but I am not completely clear about how they improve over time.
