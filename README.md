# AI Agent Error Detection Lag Capstone

## Research Question

How many steps typically pass between the decisive error in an AI-agent
trajectory and the earliest point at which that error becomes detectable?

## Dataset

This project investigates failure traces from the Who&When and/or
TraceElephant benchmark.

## Goal

The goal is to measure detection lag: the number of steps between an
annotated decisive error and the earliest point where signals of that
failure become detectable.

## Sources

**Dataset**: https://huggingface.co/datasets/Kevin355/Who_and_When

**Paper** : Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems (https://arxiv.org/abs/2505.00212)

## Repository Structure

- `data/` - raw and processed data (not committed to Git)
- `src/` - reusable Python scripts
- `notebooks/` - exploratory analysis
- `figures/` - generated plots
- `NOTES.md` - dataset provenance and observations
- `PROFILE.md` - exploratory profile
