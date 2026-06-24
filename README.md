# Building a ChatGPT-like Bot

## Overview

This repository contains my work and learning notes for the Summer of Code (SOC) project **Building a ChatGPT-like Bot**. The goal of this project is to understand how modern Large Language Models (LLMs) work and gradually build the different components involved in such systems instead of directly using existing libraries.

The project is divided into weekly milestones. During the first four weeks, I mainly focused on understanding the basic concepts that are required before actually building a language model. Rather than jumping directly into transformer architectures, I first revised Python, learned some useful data science libraries, studied neural networks, and then moved towards tokenization, embeddings, attention, and transformers.

The repository mainly contains notes that I wrote while studying the resources provided during the SOC. Some topics are still new to me, so these notes reflect my current understanding rather than complete documentation.

---

# Week 1

The first week was mostly a revision of Python along with learning a few important libraries that are commonly used while working with machine learning projects.

The libraries that I explored were:

- NumPy
- Pandas
- Matplotlib

Although I had used Python before, I had very little experience with these libraries. NumPy helped me understand how numerical computations are performed efficiently using arrays instead of Python lists. Pandas introduced me to handling tabular datasets, filtering rows, selecting columns, and reading CSV files. Matplotlib was useful for plotting simple graphs and visualizing data.

Apart from these libraries, I also started reading about Large Language Models.

One thing that surprised me was that language models do not actually understand language in the way humans do. Instead, they learn statistical patterns from huge amounts of text and use those patterns to predict what token should come next.

This idea looked very simple at first, but I later realized that almost every part of an LLM is built around improving this next-token prediction process.

---

# Week 2

The second week introduced the basics of neural networks.

Before this week, I only had a rough idea that neural networks are inspired by the human brain. After studying the resources, I understood that a neural network is actually a mathematical model made up of layers of neurons connected through weights.

Some of the concepts I studied include:

- Perceptron
- Weights and Biases
- Activation Functions
- Forward Propagation
- Loss Functions
- Gradient Descent
- Backpropagation

Initially, I found it difficult to understand why activation functions are needed. Later I learned that without them, stacking multiple linear layers would still behave like a single linear transformation. Activation functions introduce non-linearity, allowing the network to learn much more complicated relationships.

Gradient descent was another important concept. Instead of manually changing parameters, the model computes gradients and updates its weights in a direction that reduces the loss. Although I understand the intuition, I still need more practice with the mathematical derivation.

---

# Week 3

After understanding neural networks, I started learning about how text is represented inside language models.

The first concept was tokenization.

Computers cannot directly process text. Every sentence first has to be divided into smaller units called tokens.

For example,

```
I love machine learning.
```

can become

```
["I", "love", "machine", "learning", "."]
```

Depending on the tokenizer, a single word may also be divided into multiple subwords.

After tokenization, each token is converted into an integer ID.

However, integer IDs alone do not contain any semantic meaning.

This is where embeddings become important.

Embeddings represent every token as a vector containing multiple numerical values. During training, these vectors are adjusted so that tokens appearing in similar contexts become closer in the embedding space.

Although I understood why embeddings are required, I am still curious about how these vectors gradually learn meaningful relationships during training.

---

# Week 4

This week introduced transformers and the attention mechanism.

Earlier sequence models processed words one after another. This made training slower and also caused difficulty when sentences became very long.

Transformers solve this problem differently.

Every token is allowed to interact with every other token using a mechanism called self-attention.

Instead of remembering information sequentially, the model calculates which words are more important for predicting the next token.

The transformer architecture also contains several additional components such as positional encoding, feed-forward layers, residual connections, and layer normalization.

I now have a general understanding of how these components are arranged, although the mathematical details behind Query, Key, and Value vectors are still slightly confusing.

Another concept introduced during this week was the overall training pipeline of an LLM.

The complete flow can be summarized as:

```
Input Text
      ↓
Tokenizer
      ↓
Token IDs
      ↓
Embeddings
      ↓
Positional Encoding
      ↓
Transformer Layers
      ↓
Linear Layer
      ↓
Softmax
      ↓
Next Token Prediction
      ↓
Loss Calculation
      ↓
Backpropagation
      ↓
Parameter Update
```

Studying this pipeline helped me connect the topics from previous weeks together. Earlier I learned each component separately, but this week I understood where each component fits inside the complete model.

---

# Current Progress

After completing the first four weeks, I have developed a basic understanding of how language models process text before generating responses.

I understand the motivation behind tokenization, embeddings, neural networks, attention, and transformers at a conceptual level. There are still several mathematical details that I need to study more carefully, especially attention score computation and the training process.

I have also written a few small Python programs to experiment with some of these concepts. These programs are not intended to be complete implementations but rather small exercises to reinforce my understanding.

---

# Future Work

The next phase of the SOC project shifts from understanding concepts to implementing them.

In Week 5, I will start learning PyTorch, which is one of the most commonly used deep learning frameworks. Until now, most of the concepts I studied were theoretical or explained using simple examples. Learning PyTorch will help me implement neural networks more efficiently and understand how automatic differentiation and model training work in practice.

After that, the main focus will be the final project. The goal is to build a small ChatGPT-like language model by combining the concepts covered in the previous weeks. This will include implementing the different components involved in the model, preparing a dataset, training the model, and generating text from it. I expect this part to be more challenging because it combines everything learned so far.

If time permits, I also plan to explore the optional topics mentioned in the roadmap. These include understanding pretrained language models, learning the basics of instruction fine-tuning, and seeing how pretrained models can be adapted for different tasks. I am also interested in trying to build a simple web interface so that the model can be interacted with more easily.

At this stage, my focus is on understanding each concept properly while gradually moving towards implementing a complete language model by the end of the project.
