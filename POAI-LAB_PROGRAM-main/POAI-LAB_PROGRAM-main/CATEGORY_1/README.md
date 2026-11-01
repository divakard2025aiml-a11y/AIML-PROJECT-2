# AI Course II – Intelligent Agents

This repository contains Python implementations of four fundamental Intelligent Agent architectures as part of the **AI Course II Practical Lab**. Each agent demonstrates a different approach to decision-making in Artificial Intelligence using real-world examples.

---

## 📌 Intelligent Agents

An **Intelligent Agent** is a system that perceives its environment through sensors, processes the information, and performs actions through actuators to achieve specific objectives.

---

# 1. Simple Reflex Agent

## Definition

A **Simple Reflex Agent** selects actions based only on the current percept (current input). It does not store previous information or consider future consequences. The agent follows predefined condition-action rules.

### Example Used
**Smoke Detector System**

### Working

- Detects whether smoke is present.
- If smoke is detected, the alarm is turned ON.
- If no smoke is detected, the alarm remains OFF.
- The decision is made solely based on the current sensor reading.

### Real-World Applications

- Fire Alarm Systems
- Automatic Door Sensors
- Motion Detection Lights

---

# 2. Model-Based Agent

## Definition

A **Model-Based Agent** maintains an internal model (memory) of the environment. It uses both the current percept and previously stored information to make decisions.

### Example Used
**Parking Gate Management System**

### Working

- Stores the number of available parking slots.
- Updates the slot count whenever a vehicle enters or exits.
- Opens or closes the gate based on parking availability.
- Prevents vehicles from entering when the parking lot is full.

### Real-World Applications

- Smart Parking Systems
- Warehouse Inventory Management
- Smart Building Access Control

---

# 3. Goal-Based Agent

## Definition

A **Goal-Based Agent** makes decisions based on achieving a predefined goal. It evaluates possible actions and selects the one that helps reach the desired objective.

### Example Used
**Smart Irrigation System**

### Goal

Maintain optimal soil moisture while conserving water.

### Working

- If soil is dry, the irrigation system turns ON.
- If soil is wet, the irrigation system remains OFF.
- If rain is detected, irrigation is stopped to save water.
- The system continuously works toward maintaining healthy soil conditions.

### Real-World Applications

- Smart Agriculture
- Automated Greenhouses
- Precision Farming

---

# 4. Utility-Based Agent

## Definition

A **Utility-Based Agent** selects the action that provides the highest utility (maximum benefit or satisfaction). Instead of simply reaching a goal, it compares multiple options and chooses the best one.

### Example Used
**Music Recommendation System**

### Working

- Considers the user's mood and preferences.
- Evaluates different music genres.
- Recommends the songs with the highest utility (best match).
- Improves user satisfaction by selecting the most suitable recommendation.

### Real-World Applications

- Spotify Music Recommendation
- Netflix Movie Recommendation
- Amazon Product Recommendation
- YouTube Video Recommendation

---

# Project Structure

```
AI-Course-II-Intelligent-Agents
│
├── simple_reflex_agent.py
├── model_based_agent.py
├── goal_based_agent.py
├── utility_based_agent.py
├── README.md

```

---

# Technologies Used

- Python 3
- VS Code
- Git
- GitHub

---

# How to Run

Clone the repository:

```bash
git clone https://github.com/bhavanasudhakar29/AI-Course-II-Intelligent-Agents.git
```

Navigate to the project folder:

```bash
cd AI-Course-II-Intelligent-Agents
```

Run any program:

```bash
python simple_reflex_agent.py
```

```bash
python model_based_agent.py
```

```bash
python goal_based_agent.py
```

```bash
python utility_based_agent.py
```

---

# Learning Outcomes

After completing this practical, you will understand:

- Simple Reflex Agent Architecture
- Model-Based Agent Architecture
- Goal-Based Agent Architecture
- Utility-Based Agent Architecture
- Real-world applications of Intelligent Agents
- Python implementation of AI agent concepts

---

## Author

**Bhavana S**
**Devisri S**
**Gayathri D**

B.Tech Artificial Intelligence and Machine learning

Rajalakshmi Engineering college

AI Course II Practical Lab
