# Building a ChatGPT-like Bot

This repository contains my notes and small practice programs for the Summer of Code (SOC) project **Building a ChatGPT-like Bot**.

I joined this project because I wanted to understand how language models like ChatGPT work internally. Before starting, I only had a basic idea that these models were based on deep learning. Through the first four weeks, I learned about the concepts that form the foundation of modern language models.

The repository mainly contains the notes I made while following the recommended resources. I have tried to write everything in simple words so that I can revise the concepts later.

## Weekly Progress

### Week 1

The first week was mainly a revision of Python and a few libraries like NumPy, Pandas and Matplotlib. Along with that, I got introduced to Large Language Models and learned that they generate text by predicting one token at a time.

### Week 2

This week focused on Neural Networks. I learned about perceptrons, weights, bias, activation functions, forward propagation, loss functions, gradient descent and backpropagation. Some mathematical parts are still new to me, but I now understand the basic learning process.

### Week 3

This week was about how text is prepared before it reaches the model. I learned about tokenization, token IDs, embeddings and vocabulary. I found embeddings particularly interesting because they help represent the meaning of words instead of just assigning numbers.

### Week 4

This week introduced the Transformer architecture and the attention mechanism. I learned why transformers perform better than older sequence models and got a basic idea of how self attention works. I also looked at the overall pipeline of a language model from input text to prediction.

## Repository Structure

```
Building-ChatGPT-Like-Bot/

│── README.md
│── requirements.txt
│
├── notes/
│     ├── week1.md
│     ├── week2.md
│     ├── week3.md
│     └── week4.md
│
├── code/
│     ├── numpy_practice.py
│     ├── tokenizer_demo.py
│     ├── embedding_demo.py
│     └── attention_demo.py
│
└── images/
      ├── llm_pipeline.png
      └── transformer_architecture.png
```

## Current Status

At this stage, I have mainly focused on understanding the concepts covered in the first four weeks. The code included in this repository is only for practice and to better understand the topics. I have not built the complete language model yet.

## Future Work

The next part of the project will focus on learning PyTorch and then using the concepts studied so far to build a simple ChatGPT-like model. I also plan to explore the optional topics later in the roadmap if time permits.
