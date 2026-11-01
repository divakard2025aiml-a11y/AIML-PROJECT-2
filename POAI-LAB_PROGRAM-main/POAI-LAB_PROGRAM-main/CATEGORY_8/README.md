# EXPERIMENT 8 – KNOWLEDGE-BASED SYSTEMS

## Aim
To study and implement Knowledge-Based Systems using facts, rules, forward chaining and backward chaining.

## Introduction
A Knowledge-Based System is an Artificial Intelligence system that stores knowledge and uses reasoning techniques to make decisions or solve problems.

## 1. Knowledge Base

A Knowledge Base is a collection of information used by an intelligent system.

It contains:
- Facts
- Rules

**Example:** Fever is a symptom that may be used in a medical diagnosis system.

## 2. Facts

Facts are statements that are considered true and stored in the knowledge base.

**Example:**
- Patient has fever.
- Patient has cough.
- Patient has headache.

## 3. Rules

Rules represent relationships between facts and conclusions.

They are generally written using IF-THEN statements.

**Example:**

IF a patient has fever AND cough, THEN the patient may have an infection.

## 4. Forward Chaining

Forward Chaining is a data-driven reasoning method. It starts with available facts and applies rules to generate new facts.

**Working:**
1. Collect the initial facts.
2. Check which rules match the facts.
3. Apply the matching rules.
4. Add new conclusions to the knowledge base.
5. Continue until no new facts can be generated.

**Example:** Using symptoms to generate a possible medical diagnosis.

## 5. Backward Chaining

Backward Chaining is a goal-driven reasoning method. It starts with a goal and checks whether the available facts and rules support it.

**Working:**
1. Select a goal to prove.
2. Find a rule that can produce the goal.
3. Check the conditions of that rule.
4. Verify whether the required facts are available.
5. Prove the goal if all conditions are satisfied.

**Example:** Checking whether a patient may have an infection by examining the required symptoms.

## Applications

### Medical Diagnosis
Uses symptoms and medical rules to suggest possible diseases.

### Autonomous Vehicle
Uses knowledge about roads, traffic signals and obstacles to make decisions.

### Industrial Manufacturing
Uses machine conditions and rules to identify possible faults and support maintenance decisions.

## Comparison

| Reasoning Method | Working |
|---|---|
| Forward Chaining | Facts to conclusion |
| Backward Chaining | Goal to supporting facts |

## Result
Knowledge-Based Systems using facts, rules, Forward Chaining and Backward Chaining were studied and implemented successfully.
