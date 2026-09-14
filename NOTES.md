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

The dataset contains failure trajectories/traces from multi-agent runs.

### Labels

Human annotators:

1. The failure-responsible agent
2. The decisive error step
3. A natural-language explanation of the mistake

### Verification Targets

As per the project brief:

- Number of failed multi-agent runs: 184
- Agent attribution baseline: approximately 50%
- Decisive-step attribution baseline: under 15%
