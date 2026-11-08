# Project Notes

## 1. Dataset Provenance

Dataset: Who_and_When
Source: Hugging Face(https://huggingface.co/datasets/Kevin355/Who_and_When)
Version/release: Main Branch
Download date:9/13/2026
License: -
Paper: Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems (https://proceedings.mlr.press/v267/zhang25cq.html)

Citation:
@article{zhang2025agent,
title={Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems},
author={Zhang, Shaokun and Yin, Ming and Zhang, Jieyu and Liu, Jiale and Han, Zhiguang and Zhang, Jingyang and Li, Beibin and Wang, Chi and Wang, Huazheng and Chen, Yiran and others},
journal={arXiv preprint arXiv:2505.00212},
year={2025}
}

The dataset was downloaded directly from the primary source.

## 2. Research Question

How many steps typically pass between the decisive error in an AI-agent
trajectory and the earliest point at which that error becomes detectable?

## 3. Dataset Summary

### Data collection

Who_and_When contains failed multi-agent runs collected from systems solving
research-assistant-style tasks from GAIA and AssistantBench.

The systems include automatically assembled CaptainAgent systems and the
hand-built Magentic-One system.

### Unit of observation

The primary unit of observation is a failed multi-agent execution trajectory (trace).

Each trajectory represents a sequence of interactions or execution steps performed by agents while attempting to complete a task.

These trajectories provide the information needed to investigate:

- Which agent was responsible for a failure.

- At which step the decisive error occurred.

- How errors propagate through subsequent agent interactions.

- When evidence of an error first becomes observable.

### Ground-Truth Annotations

The dataset provides human-annotated failure information, including:

1. **`mistake_agent`:** The agent identified as responsible for the decisive mistake.
2. **`mistake_step`:** The annotated execution step at which the decisive mistake occurred.
3. **Mistake explanation:** A natural-language description explaining the error and its contribution to task failure.

### Verified Targets

As per the project brief, the expected dataset and baseline characteristics are:

| Metric                             |          Expected |
| ---------------------------------- | ----------------: |
| Failed multi-agent runs            |               184 |
| Agent attribution baseline         | Approximately 50% |
| Decisive-step attribution baseline |         Below 15% |

## 4. Dataset Verification

### Objective

The objective of this is to validate the dataset structure, inspect the available ground-truth annotations, and identify inconsistencies that could affect automated failure-attribution evaluation.

### Verification of Results

| Metric                             | Expected            | Phase 1 Finding                               | Status                |
| ---------------------------------- | ------------------- | --------------------------------------------- | --------------------- |
| Number of failed traces            | 184                 | Final count to insert from inventory output   | Pending confirmation  |
| Dataset categories                 | 2                   | Algorithm-Generated and Hand-Crafted          | Verified              |
| Failure-responsible agent label    | Present             | `mistake_agent` identified                    | Verified              |
| Decisive error step label          | Present             | `mistake_step` identified                     | Verified              |
| Natural-language error explanation | Present             | Annotation field identified                   | Verified              |
| Step annotation alignment          | Consistent          | 9 records flagged for further investigation   | Exceptions identified |
| Missing values                     | No target specified | Exact counts to insert from validation output | Pending documentation |
| Number of local files              | No target specified | Exact count to insert from inventory output   | Pending documentation |
