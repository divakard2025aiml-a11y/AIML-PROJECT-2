# EXPERIMENT 9 – UNCERTAINTY-BASED REASONING

## Aim
To study and implement uncertainty-based reasoning techniques using Bayesian Reasoning and Fuzzy Inference Systems.

## Introduction
In real-world situations, information may be incomplete, unclear or uncertain. Uncertainty-based reasoning helps Artificial Intelligence systems make decisions using available information.

## 1. Bayesian Reasoning

Bayesian Reasoning is a probability-based technique used to update the possibility of an event when new evidence becomes available.

It uses Bayes' Theorem.

**Formula:**

P(A|B) = [P(B|A) × P(A)] / P(B)

Where:
- P(A): Prior probability of event A.
- P(B): Probability of evidence B.
- P(B|A): Probability of evidence B when A is true.
- P(A|B): Updated probability of A after observing B.

**Working:**
1. Identify the event.
2. Calculate the prior probability.
3. Collect new evidence.
4. Apply Bayes' Theorem.
5. Calculate the updated probability.

**Example:** Estimating the probability of a disease based on a medical test result.

## 2. Fuzzy Inference System

A Fuzzy Inference System is a reasoning method that uses fuzzy logic to handle vague or imprecise information.

Unlike traditional Boolean logic, which uses only 0 and 1, fuzzy logic allows values between 0 and 1.

**Example:** Temperature can be classified as:
- Low
- Medium
- High

A temperature can belong to more than one fuzzy category with different membership values.

### Main Components

1. Fuzzification – Converts crisp input values into fuzzy values.
2. Rule Base – Contains IF-THEN rules.
3. Inference Engine – Applies the rules.
4. Defuzzification – Converts fuzzy output into a crisp value.

**Example Rule:**

IF temperature is high, THEN fan speed is fast.

## Applications

### Medical Diagnosis
Bayesian reasoning can estimate disease probabilities from test results. Fuzzy logic can represent vague symptoms such as mild, moderate or severe.

### Electric and Autonomous Vehicles
Bayesian reasoning can estimate uncertain road conditions. Fuzzy logic can help represent conditions such as slow, medium or fast speed.

### Smart Manufacturing
Bayesian reasoning can estimate the probability of machine failure. Fuzzy logic can classify machine temperature or vibration as low, medium or high.

## Comparison

| Technique | Main Feature |
|---|---|
| Bayesian Reasoning | Uses probability |
| Fuzzy Inference | Uses degrees of membership |

## Result
Bayesian Reasoning and Fuzzy Inference System techniques were studied and implemented successfully using Python.
