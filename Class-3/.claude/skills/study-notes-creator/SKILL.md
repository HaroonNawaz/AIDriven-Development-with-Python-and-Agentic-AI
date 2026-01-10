---
name: study-notes-creator
description: Generates comprehensive study notes for lessons and topics with a focus on reinforcement and revision. Creates well-organized notes featuring summaries, highlighted key terms, review questions, and easy-to-read formatting suitable for academic study and exam preparation. Use when the user asks for study notes, learning summaries, revision materials, lesson notes, note-taking, academic study materials, exam preparation materials, or wants to understand a topic for studying and learning reinforcement.
version: "1.0.0"
trigger: |
  - User asks for "study notes" or "lesson notes"
  - User requests "create notes" or "generate notes"
  - User mentions "revision", "exam preparation", or "study materials"
  - User asks to "summarize" content for learning
  - User wants "learning materials" or "educational content"
  - User requests "note-taking" or "note creation"
  - User asks for "revision materials" or "study guide"
tags:
  - education
  - learning
  - notes
  - revision
  - study
  - academic
activation_context:
  - content_type: text/markdown
  - content_type: text/plain
  - user_intent: create_notes
  - user_intent: study_preparation
  - user_intent: learning_materials
tool: text-processing
capability: note-generation
---

# Study Notes Creator

## Overview

The Study Notes Creator skill generates structured, academically rigorous study notes designed for effective learning reinforcement and revision. Each set of notes follows a consistent format optimized for comprehension and retention.

## Core Features

Every set of study notes includes the following components in order:

### 1. Executive Summary (Top)
- Concise overview of the lesson content
- Main learning objectives
- Central concepts at a glance
- Suitable for quick review and contextualization

### 2. Key Terms and Definitions
- Important terminology highlighted and defined
- Concepts presented in logical sequence
- Clear explanations appropriate for academic study
- Essential vocabulary for understanding the topic

### 3. Main Content with Structure
- Organized hierarchically with clear headings
- Logical progression from foundational to advanced concepts
- Supporting examples and explanations
- Visual hierarchy for easy navigation

### 4. Review Questions (End)
- Comprehension check questions
- Critical thinking prompts
- Application-based questions
- Suitable for self-assessment and examination preparation

### 5. Easy-to-Read Formatting
- Consistent typography and spacing
- Strategic use of bold, italics, and lists
- Clear section separation
- Professional academic presentation

## Usage Instructions

### Basic Usage
Provide the following information:
1. **Source Material**: The lesson content, lecture notes, or topic area
2. **Subject Area**: Academic discipline or course context
3. **Learning Level**: Undergraduate, postgraduate, professional, etc.
4. **Focus Areas** (optional): Specific topics or concepts to emphasize

### Example Input Format
```
Subject: Photosynthesis
Level: High School Biology
Source: Chapter 8 of Biology Textbook
Focus: Light-dependent and light-independent reactions
```

## Output Structure

Generated notes will be formatted as follows:

```
# [Topic Title]

## Summary
[Executive summary of the lesson]

## Key Terms
- **Term 1**: Definition
- **Term 2**: Definition
[Additional terms as needed]

## Detailed Content
[Organized sections with appropriate headings]

## Review Questions
1. Question about main concept
2. Question about application
3. Question for critical analysis
[Additional questions as needed]
```

## Best Practices

- Clearly specify the source material (lecture, textbook, article, etc.)
- Indicate the academic level appropriate for your studies
- Mention any specific assessment or examination being prepared for
- Request emphasis on particular concepts if needed
- Specify preferred note length (concise, standard, comprehensive)

## Examples

### Example 1: Biology Lesson
```
Create study notes for photosynthesis
Source: High school biology curriculum
Focus: Both light-dependent and light-independent reactions
Level: 10th grade
```

### Example 2: Historical Topic
```
Generate study notes on the causes of World War I
Source: AP European History course
Learning objectives: Understand political, economic, and military factors
Level: Advanced High School
```

### Example 3: Technical Subject
```
Create revision notes for thermodynamics
Source: University physics course
Focus: First and second laws of thermodynamics
Level: Undergraduate
Emphasis: Problem-solving applications
```

## Quality Standards

All generated notes maintain the following academic standards:

- Accuracy and factual correctness
- Clarity appropriate to the specified learning level
- Comprehensive coverage of essential concepts
- Professional academic tone and formatting
- Appropriate depth and balance of detail
- Proper use of terminology
- Logical organization and flow
