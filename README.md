# Overview

This project explores abstractive text summarization using two advanced transformer models:

- **T5-Small**: A lightweight transformer model suitable for multi-task text generation.
- **Pegasus-XSum**: Optimized for abstractive summarization, capable of capturing contextual nuances.

The models were trained and evaluated on the **Harvard Gigaword Dataset**, a resource for generating concise text summaries from large documents.

---

## Dataset Information

- **Input**: Articles represented in the `document` column.
- **Target**: Corresponding summaries in the `summary` column.
- **Data Split**:
  - **Training Set**: 1,600 samples
  - **Testing Set**: 400 samples

---

## Preprocessing Steps

1. Added a prefix ("`summarize:`") to each document for compatibility with the T5 model.
2. Tokenized input and target sequences, ensuring:
   - Maximum lengths of **1024 tokens** (input) 
   - **128 tokens** (summary).

---

## Models and Training Setup

### Model Descriptions

- **T5-Small**: A smaller version of Google’s T5, built for text-to-text transformations, fine-tuned to generate concise summaries.
- **Pegasus-XSum**: Designed specifically for summarization, leveraging its large-scale pre-training on summarization tasks.

### Training Configuration

- **Framework**: Hugging Face Transformers
- **Batch Size**: 16
- **Learning Rate**: \(2 \times 10^{-5}\)
- **Epochs**: 4
- **Evaluation Metric**: ROUGE (Recall-Oriented Understudy for Gisting Evaluation)

---

## Performance Metrics

### T5-Small Results

- **Training Loss**: 2.50
- **Validation Loss**: 3.15
- **ROUGE-1**: 0.356
- **ROUGE-2**: 0.160
- **ROUGE-L**: 0.3309

### Pegasus-XSum Results

- **Training Loss**: 5.57
- **Validation Loss**: 5.57
- **ROUGE-1**: 0.1185
- **ROUGE-2**: 0.0271
- **ROUGE-L**: 0.1047

## Observations and Key Insights

- **T5-Small** demonstrated better performance, achieving significantly higher ROUGE scores across all metrics.
- **Pegasus-XSum** underperformed, possibly due to a mismatch in dataset size or task-specific optimization requirements.

---

## Deployment and Inference

Both models were deployed for inference using the Hugging Face library. Key steps include:

- Loading models and tokenizers.
- Generating summaries from tokenized input articles.
- Measuring output quality using ROUGE metrics.

---

## Final Remarks

- **T5-Small** proved more suitable for this task, with better loss and evaluation metrics.
  
### Future Directions:

- Experimenting with **larger datasets** for Pegasus-XSum.
- Fine-tuning **hyperparameters** for better convergence.
- Incorporating **beam search** and other decoding techniques for improved summarization quality.
