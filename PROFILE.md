## 1. Dataset Overview

**Dataset:** Who & When  
**Source:** Hugging Face — `Kevin355/Who_and_When`

The Who & When dataset contains traces from multi-agent systems in which an error or failure occurs during a sequence of interactions.

For this project, the dataset will be used to study **detection lag**: how many steps pass between the point where the decisive error occurs and the point where that error becomes detectable from the trace.

---

## 2. Research Question

The main research question is:

> **How long does an error stay invisible after it first occurs?**

Detection lag can be represented as:

```text
Detection Lag = First Detectable Step - Decisive Error Step
```

A lag of `0` means the error is detectable immediately.

A larger lag means the system continues operating for several steps before there is enough evidence to identify the error.

---

## 3. Dataset Categories

The dataset contains two broad categories:

- **Algorithm-Generated**
- **Hand-Crafted**

These traces represent different multi-agent scenarios in which failures have been annotated.

---

## 4. Dataset Files

The raw dataset is stored under:

```text
data/Who&When/
```

The dataset primarily contains JSON files.

Each JSON file represents a trace or task.

The dataset inventory script recursively examines these files and records:

- file path
- file size
- JSON structure
- available fields
- number of records where applicable

---

## 5. Important Fields

Initial inspection shows fields related to the task, conversation trace, and annotated failure.

Fields of particular interest include:

| Field            | Purpose                                     |
| ---------------- | ------------------------------------------- |
| `question`       | Original task or problem                    |
| `question_ID`    | Identifier for the task                     |
| `history`        | Sequence of agent interactions/actions      |
| `ground_truth`   | Expected correct outcome                    |
| `mistake_agent`  | Agent responsible for the annotated mistake |
| `mistake_step`   | Step where the mistake occurred             |
| `mistake_reason` | Explanation of the mistake                  |

These fields may vary slightly between records and should be verified during exploratory analysis.

---

## 6. Unit of Analysis

The primary unit of analysis will be a **trace**.

A trace consists of an ordered sequence of interactions stored in the `history` field.

Each history entry can potentially provide signals indicating whether an earlier error has become visible.

---

## 7. Initial Variables

Variables expected to be useful include:

```text
trace_id
dataset_type
trace_length
mistake_agent
mistake_step
mistake_reason
first_detectable_step
detection_lag
```

Additional features may later be extracted from the trace, such as:

- message length
- contradictions
- failed actions
- anomaly indicators
- explicit correction attempts
- LLM-based suspicion scores

---

## 8. Exploratory Questions

Before building a detection method, the exploratory analysis should answer:

1. How many traces are available?
2. How many traces are Algorithm-Generated versus Hand-Crafted?
3. How long are the traces?
4. At what step do annotated mistakes usually occur?
5. Which agents are most frequently associated with mistakes?
6. What types of mistakes occur?
