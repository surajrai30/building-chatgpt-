# Building a ChatGPT-like Bot

This repository contains my work for the Summer of Code (SOC) project **Building a ChatGPT-like Bot**.

The main goal of this project is to understand how modern language models work by learning the concepts step by step instead of directly using existing models. These notes are based on the first four weeks of the SOC roadmap. I have written them in my own words so that I can revise the topics later.

Along with the notes, I have also added a few small Python programs that helped me understand concepts like tokenization, embeddings and attention.

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
└── code/
      ├── numpy_practice.py
      ├── tokenizer_demo.py
      ├── embedding_demo.py
      └── attention_demo.py
```

## What I Learned

### Week 1

This week was mostly about revising Python and learning libraries like NumPy, Pandas and Matplotlib. I also got introduced to Large Language Models and learned the basic idea of next token prediction.

### Week 2

This week focused on Neural Networks. I learned about perceptrons, weights, bias, activation functions, forward propagation, loss functions, gradient descent and backpropagation. Some parts involving mathematics are still a little confusing, but I understand the overall learning process.

### Week 3

This week was about how text is prepared before it reaches a language model. I learned about tokenization, token IDs, vocabulary and embeddings. It was interesting to see how words are converted into numbers before they are processed by the model.

### Week 4

This week introduced Transformers and the attention mechanism. I learned why transformers are better than older sequence models and got a basic idea of self attention. I also saw how all the concepts from the previous weeks fit together in the overall language model pipeline.

## Current Progress

So far, I have mainly focused on understanding the concepts covered in the first four weeks. The Python files in this repository are small practice programs that helped me understand these topics better. They are not complete implementations of a language model.

## Future Work

The next part of the project will focus on learning PyTorch and then using these concepts to build a simple ChatGPT-like model. I also plan to explore the optional topics mentioned in the SOC roadmap after completing the main project.

## References

The notes in this repository are based on the learning resources provided as part of the SOC project. I have rewritten the concepts in my own words while studying them.
