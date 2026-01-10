---
# What is LLM - Basic Flashcards
## 📚 Foundational Knowledge Level 1

Foundational definitions, facts, and terminology for memorization and foundational recall.

*✨ Visual Flashcard Format - Flip to reveal answers*

---

## 🎯 Card 1: LLM Definition | ⭐ ESSENTIAL

```
┌─────────────────────────────────────────────────────┐
│                    FRONT SIDE                       │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ❓ What is a Large Language Model (LLM)?          │
│                                                     │
│  [FLIP TO REVEAL ANSWER]                          │
│                                                     │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│                    BACK SIDE                        │
├─────────────────────────────────────────────────────┤
│                                                     │
│  💡 An AI model trained on massive text data to    │
│  understand and generate human language.           │
│                                                     │
│  🔧 Uses neural networks (transformer             │
│  architecture) and predicts next token.           │
│                                                     │
│  📌 Memory Aid:                                     │
│  LLM = Large + Learning + Model                   │
│                                                     │
│  📚 Examples: ChatGPT, GPT-4, Claude, LLaMA       │
│                                                     │
│  🔗 Related: Cards 3, 6, 14                        │
│  ⭐ Difficulty: ★☆☆ EASY                          │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 🎯 Card 2: What is a Token | ⭐ ESSENTIAL

```
┌─────────────────────────────────────────────────────┐
│                    FRONT SIDE                       │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ❓ What is a "token" in LLMs?                     │
│                                                     │
│  [FLIP TO REVEAL ANSWER]                          │
│                                                     │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│                    BACK SIDE                        │
├─────────────────────────────────────────────────────┤
│                                                     │
│  💡 The smallest unit of text an LLM processes.   │
│                                                     │
│  📊 Can be:                                         │
│  • Word: "hello"                                   │
│  • Subword: "hel", "lo"                           │
│  • Character: individual letters                  │
│                                                     │
│  📌 Memory Aid:                                     │
│  Token = Text broken into tiny pieces              │
│                                                     │
│  📝 Example:                                        │
│  "Hello world" → ["Hello", "world"] OR            │
│                → ["Hel", "lo", "wor", "ld"]      │
│                                                     │
│  🔗 Related: Cards 1, 6, 16                        │
│  ⭐ Difficulty: ★☆☆ EASY                          │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 🎯 Card 3: Transformer Architecture | ⭐ ESSENTIAL

```
┌─────────────────────────────────────────────────────┐
│                    FRONT SIDE                       │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ❓ What is Transformer Architecture?             │
│                                                     │
│  [FLIP TO REVEAL ANSWER]                          │
│                                                     │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│                    BACK SIDE                        │
├─────────────────────────────────────────────────────┤
│                                                     │
│  💡 Neural network design foundation for          │
│  modern LLMs. Introduced in 2017.                 │
│                                                     │
│  🔑 Key Features:                                  │
│  • Attention mechanisms                           │
│  • Parallel processing (not sequential)           │
│  • Handles long-range dependencies                │
│                                                     │
│  📌 Memory Aid:                                     │
│  Transformer = Attention + Parallel processing    │
│                                                     │
│  🚀 Why Important:                                 │
│  Enabled scaling to billions of parameters        │
│                                                     │
│  🔗 Related: Cards 2, 4, 14                        │
│  ⭐ Difficulty: ★☆☆ EASY                          │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## Card 4: Attention Mechanism

**Q: What is the attention mechanism in transformers?**

A: A mathematical technique that allows neural networks to dynamically weigh the importance of different parts of input text when processing information. Lets models focus on relevant information even when it's far from current position.

**Example**: When processing "it", attention identifies what "it" refers to by looking back at previous words

**Memory Aid**: Attention = Model looks around to find what's important

**Related Cards**: Card 3 (Transformer), Card 13 (Long-Range Dependencies)

**Difficulty**: 1 (Easy)

---

## Card 5: Model Parameters

**Q: What are "parameters" in a neural network?**

A: The learned weights and biases within a neural network that determine the model's behavior. Parameters are adjusted during training to improve predictions. Larger parameter counts generally enable greater capability.

**Examples**: GPT-3.5 has ~175 billion parameters; Claude has up to ~100 billion

**Memory Aid**: Parameters = The "knobs" the model learns to adjust for better predictions

**Related Cards**: Card 6 (Model Size), Card 12 (Scaling)

**Difficulty**: 1 (Easy)

---

## Card 6: LLM Training Objective

**Q: What is the primary training objective of language models?**

A: Predict the most likely next token (word) given all previous tokens in a sequence. The model is shown text and learns to predict which token should come next. This simple objective, when scaled, produces sophisticated language understanding.

**Process**: Show "The cat sat on the..." → Model predicts "mat" or similar

**Memory Aid**: Training = Learn to predict what comes next

**Related Cards**: Card 1 (LLM Definition), Card 2 (Token)

**Difficulty**: 1 (Easy)

---

## Card 7: Model Size Range

**Q: What is the typical size range of modern Large Language Models?**

A: Modern LLMs typically contain 7 billion to 540+ billion parameters. Examples: LLaMA-7B (7 billion), GPT-3.5 (~175 billion), GPT-4 (estimated 100B+ parameters), Claude (up to ~100 billion).

**Scale**: 1 billion = 1,000,000,000 parameters

**Memory Aid**: Billions to hundreds of billions parameters = Modern LLM size

**Related Cards**: Card 5 (Parameters), Card 12 (Scaling Laws)

**Difficulty**: 1 (Easy)

---

## Card 8: Training Data Scale

**Q: How much training data (text) are modern LLMs typically trained on?**

A: Modern LLMs are trained on hundreds of billions to trillions of tokens. Typical range: 300 billion to 2+ trillion tokens from diverse sources (books, websites, articles, code repositories).

**Perspective**: 1 trillion tokens ≈ approximately 800+ billion words

**Memory Aid**: Billions to trillions of tokens of text

**Related Cards**: Card 7 (Model Size), Card 11 (Training Data Impact)

**Difficulty**: 1 (Easy)

---

## Card 9: LLM Examples

**Q: Name three examples of Large Language Models.**

A: GPT-4, Claude, LLaMA (also: GPT-3.5, PaLM, Cohere, Anthropic's Claude, OpenAI's GPT models)

**Context**: Developed by different organizations: OpenAI (GPT), Anthropic (Claude), Meta (LLaMA), Google (PaLM)

**Memory Aid**: GPT (OpenAI), Claude (Anthropic), LLaMA (Meta)

**Related Cards**: Card 1 (LLM Definition)

**Difficulty**: 1 (Easy)

---

## Card 10: Inference

**Q: What does "inference" mean in the context of LLMs?**

A: Using a trained model to generate text or make predictions. Inference is different from training; it's when the model generates responses to user prompts after it has already been trained.

**Analogy**: Training = Learning; Inference = Using what you learned

**Memory Aid**: Inference = Using trained model to generate output

**Related Cards**: Card 6 (Training), Card 16 (Training vs Inference)

**Difficulty**: 1 (Easy)

---

## Card 11: Hallucination Definition

**Q: What is "hallucination" in LLMs?**

A: Generation of plausible-sounding but false information. Occurs because LLMs predict tokens based on learned statistical patterns, not by accessing a knowledge database. Model can confidently produce incorrect information.

**Example**: LLM invents a fake fact that sounds reasonable but isn't true

**Memory Aid**: Hallucination = Confident false information

**Related Cards**: Card 19 (Why Hallucination Occurs), Card 20 (Hallucination Prevention)

**Difficulty**: 1 (Easy)

---

## Card 12: Scaling Laws

**Q: What are "scaling laws" in the context of LLMs?**

A: Empirical relationships showing that performance improvements follow predictable patterns with increased model size and training data. Larger models and more data generally lead to better capability.

**Pattern**: Doubling model size or data typically improves performance

**Memory Aid**: Scaling Laws = Bigger usually means better capability

**Related Cards**: Card 5 (Parameters), Card 7 (Model Size), Card 8 (Training Data)

**Difficulty**: 1 (Easy)

---

## Card 13: Emergence Phenomenon

**Q: What does "emergence" mean in large language models?**

A: Appearance of unexpected new capabilities in larger models that don't exist in smaller models. Suggests qualitative differences between small and large models, not just gradual improvements.

**Example**: In-context learning (learning from prompt examples) emerges in models above ~100 billion parameters

**Memory Aid**: Emergence = Surprise new abilities in big models

**Related Cards**: Card 7 (Model Size), Card 12 (Scaling Laws)

**Difficulty**: 1 (Easy)

---

## Card 14: Neural Networks

**Q: What is a neural network?**

A: A computational system inspired by biological neurons. Composed of layers of artificial neurons connected through adjustable weights. Learns patterns by adjusting connection weights through training on data.

**Structure**: Input layer → Hidden layers → Output layer

**Memory Aid**: Neural Network = Interconnected layers of artificial brain-like units

**Related Cards**: Card 3 (Transformer), Card 15 (Deep Learning)

**Difficulty**: 1 (Easy)

---

## Card 15: Context Length

**Q: What is "context length" in LLMs?**

A: The maximum number of tokens an LLM can consider at once when generating responses. Typical modern context lengths range from 2,000 to 100,000+ tokens. Longer context allows model to consider more information.

**Example**: GPT-4 supports up to 128,000 tokens of context

**Memory Aid**: Context Length = How much text the model can "see" at once

**Related Cards**: Card 2 (Token), Card 13 (Long-Range Dependencies)

**Difficulty**: 1 (Easy)

---

## Card 16: Text Tokenization

**Q: What is tokenization?**

A: The process of breaking text into tokens (smaller units). Different tokenization schemes create different token sequences from the same text. Determines how LLMs represent and process language.

**Example**: "hello world" might be 2 tokens ["hello", "world"] or 4 tokens ["hel", "lo", "wor", "ld"]

**Memory Aid**: Tokenization = Splitting text into token units

**Related Cards**: Card 2 (Token), Card 1 (LLM)

**Difficulty**: 1 (Easy)

---

## Card 17: Knowledge Cutoff

**Q: What is a "knowledge cutoff" in LLMs?**

A: The training data completion date. LLMs have no knowledge of events or information after this date since they weren't included in training data. Creates limitation: models don't know about recent events.

**Example**: GPT-3.5 has knowledge cutoff in April 2023; doesn't know about 2024 events

**Memory Aid**: Knowledge Cutoff = Latest date model knows about

**Related Cards**: Card 8 (Training Data), Card 11 (Hallucination)

**Difficulty**: 1 (Easy)

---

## Card 18: Fine-tuning

**Q: What is "fine-tuning" an LLM?**

A: Process of training a pre-trained model on specialized data to adapt it to specific tasks or domains. Uses much less data and computation than original training. Customizes model for particular uses.

**Example**: Fine-tuning GPT on medical texts to create a medical AI assistant

**Memory Aid**: Fine-tuning = Specialized training after general training

**Related Cards**: Card 6 (Training), Card 10 (Inference)

**Difficulty**: 1 (Easy)

---

## Card 19: Pattern Matching vs Understanding

**Q: Do LLMs truly "understand" language?**

A: LLMs don't understand in the human sense—they don't have consciousness. They're sophisticated pattern-matching systems that learned statistical relationships in text. They behave as if they understand, but are fundamentally probabilistic.

**Key Point**: LLMs are pattern matchers, not true understanders

**Memory Aid**: LLMs = Pattern matchers that appear intelligent

**Related Cards**: Card 1 (LLM Definition), Card 11 (Hallucination)

**Difficulty**: 1 (Easy)

---

## Card 20: Transformer Introduction

**Q: When was the transformer architecture introduced?**

A: 2017, in the paper "Attention Is All You Need" by Vaswani and colleagues. This innovation enabled development of modern large language models by allowing efficient parallel processing of text.

**Significance**: This introduced attention mechanisms that power modern LLMs

**Memory Aid**: Transformers = 2017 game-changing architecture

**Related Cards**: Card 3 (Transformer), Card 4 (Attention Mechanism)

**Difficulty**: 1 (Easy)

---

## Study Tips for Basic Flashcards

1. **Memorize exactly**: These terms form your foundation vocabulary
2. **Repeat until automatic**: Review until you can answer without thinking
3. **Create examples**: Make up your own examples for definitions
4. **Use memory aids**: The provided mnemonics are tools for recall
5. **Master before advancing**: Don't move to intermediate until these are solid

## Progress Tracking

- [ ] Card 1-5: Foundational definitions
- [ ] Card 6-10: Training and scale
- [ ] Card 11-15: Key concepts
- [ ] Card 16-20: Additional terminology

**Next Level**: Move to `what-is-llm-intermediate-flashcards.md` after mastering these

**Last Updated**: December 2024
**Difficulty Level**: Foundational (Easy)
**Estimated Study Time**: 2-3 hours for full mastery
