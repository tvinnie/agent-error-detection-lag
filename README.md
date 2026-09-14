# AI Agent Error Detection Lag

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

## Repository Structure

- `data/` - raw and processed data (not committed to Git)
- `src/` - reusable Python scripts
- `notebooks/` - exploratory analysis
- `figures/` - generated plots
- `NOTES.md` - dataset provenance and observations
- `PROFILE.md` - exploratory profile
