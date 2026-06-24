# Week 4

This week I started learning about Transformers. Before this, I only knew that models like ChatGPT are based on the Transformer architecture. I never really understood why Transformers became so popular or what makes them different from older models.

## Why Transformers?

Earlier models like RNNs processed one word after another. This worked well for short sentences but became slow for longer ones. It was also difficult for them to remember information from words that appeared much earlier in the sentence.

Transformers solve this problem by processing all the tokens together instead of one by one. This makes training much faster and also helps the model capture long-range relationships between words.

---

## Self Attention

The most important concept this week was **Self Attention**.

The basic idea is that while processing a word, the model looks at the other words in the sentence to decide which ones are more important.

For example,

```
The animal didn't cross the road because it was tired.
```

Here, the word **"it"** refers to **"animal"**.

Using self attention, the model can focus more on the correct word instead of treating every word equally.

I found this idea easy to understand, even though the calculations behind it are still a little confusing.

---

## Query, Key and Value

While studying self attention, I came across three new terms:

- Query (Q)
- Key (K)
- Value (V)

Each token is converted into these three vectors.

The Query of one token is compared with the Keys of all the other tokens to calculate attention scores. These scores decide how much importance each token should receive.

I understand the purpose of Query, Key and Value, but I still need to study the matrix calculations in more detail.

---

## Transformer Block

A transformer is made by stacking multiple transformer blocks one after another.

A transformer block mainly contains:

- Multi Head Attention
- Feed Forward Network
- Layer Normalization
- Residual Connections

Each block helps the model learn better representations of the input before passing it to the next block.

---

## Overall Pipeline

By the end of this week, I got a rough idea of how all the concepts from the previous weeks fit together.

```
Input Text
      ↓
Tokenizer
      ↓
Token IDs
      ↓
Embeddings
      ↓
Transformer Layers
      ↓
Prediction
```

Earlier, I was learning each topic separately. Seeing the complete flow made it easier to understand why tokenization, embeddings and transformers are all needed.

---

## My Notes

This was probably the most interesting week so far because I finally started learning about the architecture used in modern language models.

I understood the intuition behind self attention, but I still need to practice the mathematical part, especially how the attention scores are calculated using Query, Key and Value.

Overall, I now have a much better picture of how text moves through a language model before the next token is predicted.
