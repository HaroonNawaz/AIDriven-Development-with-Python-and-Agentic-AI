---
# What is LLM - Advanced Flashcards

Application scenarios, problem-solving, and synthesis for real-world understanding.

---

## Card 1: Evaluating LLM Appropriateness

**Q: You have a problem. Walk through how you would decide if an LLM-based solution is appropriate.**

A: 1) Does it involve language understanding/generation? (If no, unlikely suitable) 2) How critical is factual accuracy? (Hallucination risk) 3) Is real-time information needed? (Knowledge cutoff issue) 4) Can outputs be easily verified? (Determines feasibility) 5) What's cost of failure? (Determines need for safeguards) Use these to evaluate suitability. Example: LLM good for creative writing (no accuracy critical); bad for medical diagnosis without verification.

**Application**: Evaluation framework for any potential LLM use

**Decision Factors**: Language component, accuracy needs, verification feasibility, failure cost

**Memory Aid**: Five-factor decision framework

**Difficulty**: 3 (Hard)

---

## Card 2: Designing Safe LLM Systems

**Q: Design safeguards for an LLM-based customer support system. What could go wrong, and how would you prevent it?**

A: Risks and mitigations: 1) Financial errors (claiming non-existent refunds) → Hardcode policies, require human confirmation 2) Revealing confidential info → Filter sensitive data access 3) Inconsistent information → Provide consistent knowledge sources 4) Making impossible promises → Limit scope to predefined categories 5) Hallucinated facts → Escalate novel questions to humans. Additional: implement confidence scoring, have humans review novel requests, log conversations for improvement.

**Real-World Application**: Building trustworthy AI systems

**Key Principle**: Defense in depth (multiple safeguards, not relying on one)

**Memory Aid**: Multiple layers of protection against different failure modes

**Difficulty**: 3 (Hard)

---

## Card 3: Comparing Model Selection

**Q: When would you choose a small, specialized fine-tuned model over a large general-purpose model, and why?**

A: Choose small specialized model when: 1) Domain specific (medical, legal, technical) where fine-tuned model outperforms general 2) Resource constraints (cost, latency, on-device deployment) 3) Performance on narrow task is critical 4) Privacy matters (smaller models, more control). General model better when: 1) Task diverse/cross-domain 2) Reasoning across domains needed 3) Resources abundant. Example: Medical diagnosis → specialized model; General Q&A → large general model.

**Trade-offs**: Specialization vs Generality, Cost vs Performance

**Decision Criteria**: Task specificity, resources, performance requirements

**Memory Aid**: Specialized for specific domains, general for diverse tasks

**Difficulty**: 3 (Hard)

---

## Card 4: Prompt Engineering Strategy

**Q: Develop a prompt strategy to get better code generation from an LLM. What makes prompts effective?**

A: Effective prompts: 1) Provide context (programming language, framework, style) 2) Show examples of desired format 3) Specify constraints (performance, security, simplicity) 4) Request step-by-step reasoning 5) Ask for multiple approaches then select best. Example: Instead of "Write a function", say "Write a Python function that sorts a list in O(n) time, uses no extra space, with example usage." Ineffective prompts: vague requirements, no context, no examples.

**Key Insight**: Detailed prompts significantly improve output quality

**In-Context Learning**: Examples in prompt teach the model expected format

**Memory Aid**: Context + Examples + Constraints = Better outputs

**Difficulty**: 3 (Hard)

---

## Card 5: Detecting and Mitigating Hallucination

**Q: An LLM generated a confident claim about a recent scientific discovery. How would you verify accuracy and prevent future hallucinations?**

A: Verification: 1) Check claim against reliable sources (peer-reviewed papers, official sources) 2) Verify if recent enough (check knowledge cutoff) 3) Look for consistency with known facts 4) Note if LLM expressed uncertainty. Prevention: 1) Use retrieval augmentation (provide recent papers) 2) Ask model to cite sources 3) Request step-by-step reasoning (easier to spot errors) 4) Fine-tune on high-quality verified data 5) Implement confidence scoring, flag low-confidence outputs for human review.

**Practical Process**: Verify + Prevent strategy

**Tool**: Retrieval augmentation especially effective for recent information

**Memory Aid**: Verify when critical; prevent with retrieval & fine-tuning

**Difficulty**: 3 (Hard)

---

## Card 6: Adapting LLMs to Specialized Domains

**Q: You need an LLM for medical diagnosis suggestions. What approaches could adapt a general LLM for this specialized domain?**

A: Options: 1) Prompting: Include medical knowledge in prompts, request reasoning 2) Retrieval augmentation: Provide relevant medical literature to model 3) Fine-tuning: Train on medical data if sufficient labeled data available 4) Smaller specialized model: If resources allow, fine-tune small model specifically for medical domain 5) Hybrid: Combine LLM with medical database/knowledge system. Best approach depends on: accuracy requirements (high = fine-tuning), data availability, resources, regulatory requirements. Medical domain requires high accuracy → suggests hybrid or specialized approach, not pure prompting.

**Real-World Example**: Medical AI requires domain adaptation for safety

**Key Consideration**: Specialization improves accuracy but requires effort

**Memory Aid**: Prompting (easy), Retrieval (medium), Fine-tuning (hard), Specialized (best)

**Difficulty**: 3 (Hard)

---

## Card 7: Evaluating LLM Output Reliability

**Q: You're using an LLM output for decision-making. Create a framework for evaluating when to trust vs verify outputs.**

A: Trust without verification when: 1) Output is verifiable through other means 2) Cost of error is low 3) LLM has high confidence 4) Task is in domain with strong training data 5) Output is internally consistent. Require verification when: 1) High cost of error (medical, legal, financial) 2) Output contains factual claims beyond training cutoff 3) Task requires current information 4) Output is unique/non-standard 5) LLM expressed uncertainty. Process: Evaluate cost of error first (determines how much verification needed), then assess reliability factors.

**Decision Framework**: Cost of error determines verification requirements

**Risk Assessment**: Higher risk = More verification needed

**Memory Aid**: High-cost errors need verification; low-cost allow more trust

**Difficulty**: 3 (Hard)

---

## Card 8: Real-World LLM Application Design

**Q: Design an end-to-end system for using LLM for summarizing lengthy documents. What components are necessary?**

A: Components: 1) Input processing: Extract text from document format (PDF, Word, etc.) 2) Chunking: Split long documents into LLM context-window chunks 3) Summarization: Summarize each chunk 4) Aggregation: Combine chunk summaries into overall summary 5) Refinement: Generate final polished summary 6) Verification: Human review of accuracy 7) Storage: Save summaries with metadata 8) Feedback: Collect user feedback for improvement. Additional: Error handling (corrupted files, encoding issues), performance monitoring, cost tracking.

**System Design**: Multiple components working together

**Key Principle**: LLM is one component; full system includes I/O, processing, verification

**Memory Aid**: Input → Process → Output → Verify → Store → Improve

**Difficulty**: 3 (Hard)

---

## Card 9: Cost-Benefit Analysis of LLM Solutions

**Q: How would you conduct a cost-benefit analysis to decide if LLM solution is worth implementing?**

A: Cost side: 1) API costs (per-token pricing, volume) 2) Infrastructure (servers, GPUs if self-hosted) 3) Development time (integration, testing, refinement) 4) Maintenance (monitoring, updates, error handling) 5) Staff training. Benefit side: 1) Time saved (labor reduction) 2) Quality improvement (better outputs than baseline) 3) Scalability (handling more volume) 4) Revenue increase (new capabilities). ROI calculation: (Benefits - Costs) / Costs. Example: LLM customer support might cost $10k/month but save $50k/month in staff → 5:1 ROI → worthwhile.

**Framework**: Quantify costs and benefits, calculate ROI

**Hidden Costs**: Don't forget development, maintenance, staff training

**Memory Aid**: Full cost accounting including indirect costs

**Difficulty**: 3 (Hard)

---

## Card 10: Ethical Considerations in LLM Deployment

**Q: What ethical issues should you consider when deploying LLM systems, and how would you address them?**

A: Issues: 1) Bias (perpetuating discrimination) → Audit for bias, diverse training data 2) Privacy (training on user data) → Transparent data policies 3) Transparency (users don't know they're using AI) → Disclose AI involvement 4) Harm potential (misuse of outputs) → Limit harmful use cases 5) Misinformation (generating false info) → Implement verification mechanisms 6) Labor displacement (automation of jobs) → Plan workforce transition. Address through: ethical guidelines, user transparency, safety mechanisms, diverse perspectives in design.

**Broader Perspective**: Technical capability ≠ ethical deployment

**Stakeholder Consideration**: Impact on users, workers, society

**Memory Aid**: Bias, Privacy, Transparency, Harm, Misinformation, Labor

**Difficulty**: 3 (Hard)

---

## Study Tips for Advanced Flashcards

1. **Real-World Thinking**: These require practical judgment, not memorization
2. **Design Thinking**: Approach as design problems with multiple valid solutions
3. **Trade-offs**: All solutions involve trade-offs; analyze them
4. **Creativity**: Generate your own solutions, then compare to card answers
5. **Discussion**: Discuss with others; multiple perspectives improve understanding

## Progress Tracking

- [ ] Cards 1-5: Evaluation, design, and selection decisions
- [ ] Cards 6-10: Real-world application and ethical considerations

**Mastery Achieved**: After completing all three levels

**Last Updated**: December 2024
**Difficulty Level**: Advanced (Hard)
**Estimated Study Time**: 2-3 hours for full mastery
