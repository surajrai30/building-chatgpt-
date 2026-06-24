# Building a ChatGPT-like Bot

## About this Repository

This repository contains my work and notes for the Summer of Code (SOC) project **Building a ChatGPT-like Bot**.

Before joining this project I had used ChatGPT many times but I never really knew what was happening inside it. I knew it was based on machine learning but I had no idea how text is processed or how a model is able to generate meaningful responses.

The goal of this SOC is not to directly use existing language models. Instead, the idea is to understand every important concept step by step and then use that knowledge to build a simple ChatGPT-like model by the end of the project.

Till now I have completed the first four weeks of the roadmap. These weeks mainly focused on building the required foundation before starting the actual implementation.

This repository contains my notes and a few small code examples that I wrote while learning.

---

# Week 1

The first week was mostly a revision of Python and some important libraries that are commonly used in machine learning.

I studied NumPy, Pandas and Matplotlib.

Although I already knew Python, I had not used these libraries properly before. NumPy helped me understand how arrays work and why they are much faster than normal Python lists for numerical computations.

Pandas introduced me to working with datasets. I learned how to read CSV files, access rows and columns and perform some basic operations on data.

Matplotlib was useful for plotting graphs. I practiced creating simple plots to understand how data can be visualized.

Apart from these libraries I also started reading about Large Language Models.

One thing that surprised me was that language models do not actually understand language like humans do. They simply learn patterns from a very large amount of text and predict what token should come next.

This idea looked simple in the beginning but later I realized that almost everything inside an LLM is connected to this next token prediction process.

---

# Week 2

This week was about understanding neural networks.

I had heard terms like neurons and deep learning before but I never knew what they actually meant.

I started with the basic perceptron model and then learned how multiple layers are connected together to form a neural network.

Some of the concepts I studied were:

- Weights
- Bias
- Activation Functions
- Forward Propagation
- Loss Function
- Gradient Descent
- Backpropagation

At first backpropagation looked difficult because there were many mathematical equations. After watching the videos again I understood the main idea. The model makes a prediction, compares it with the correct answer and then updates its weights to reduce the error.

I still need to practice the mathematics behind it but the overall idea is much clearer now.

---

# Week 3

This week introduced concepts that are directly related to language models.

The first topic was tokenization.

Computers cannot understand text directly. Every sentence first needs to be divided into smaller pieces called tokens.

For example,

```
I like playing chess.
```

can become

```
["I", "like", "playing", "chess", "."]
```

Different tokenizers can split text differently. Sometimes even a single word is divided into smaller parts.

After tokenization every token is assigned an integer ID.

I first thought that these IDs were enough for the model but later I learned about embeddings.

Embeddings convert every token into a vector.

These vectors help the model learn relationships between words. For example, words that appear in similar contexts usually end up having similar vector representations.

I understood why embeddings are needed but I still want to learn more about how these vectors are updated during training.

---

# Week 4

This week I started learning about transformers and attention.

Before this I only knew that ChatGPT is based on transformers. I never knew why transformers became so popular.

The attention mechanism allows every word in a sentence to look at other words while making a prediction.

For example, consider the sentence

```
The boy picked up the ball because it was on the ground.
```

Here the word "it" refers to the ball.

The attention mechanism helps the model understand these kinds of relationships.

I also learned that transformer models process many tokens at the same time instead of reading them one after another. This makes training much faster than older sequence models.

Towards the end of the week I looked at the complete pipeline of a language model.

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

↓

Loss Calculation

↓

Backpropagation

↓

Updated Parameters
```

This was probably the most useful part because it connected many of the topics that I had studied over the previous weeks.

There are still a few things that I find confusing. The Query, Key and Value matrices used in self attention are one example. I understand their purpose but I still need to spend more time understanding the calculations.

---

# Current Understanding

After four weeks I feel that I now understand the basic flow of a language model much better than before.

I know why tokenization is needed, what embeddings do, how neural networks learn and why transformers are used for language models.

I have not built a complete model yet because the implementation part comes later in the roadmap. Right now my focus is on understanding the concepts properly before writing larger programs.

---

# Future Work

The next part of the SOC focuses more on implementation.

In Week 5 I will start learning PyTorch. Till now most of the things I studied were concepts. PyTorch will help me implement these ideas in code and understand how models are trained in practice.

Week 6 is the final project where the goal is to build a simple ChatGPT-like model. This will combine the topics covered in the previous weeks into one project.

The roadmap also includes some optional topics such as exploring pretrained models, instruction fine tuning and building a small web application if time permits.

I am looking forward to implementing these ideas because I think writing the code will help me understand the concepts much better than only reading about them.
