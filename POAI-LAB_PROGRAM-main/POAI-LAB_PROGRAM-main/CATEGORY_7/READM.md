# EXPERIMENT 7 – CONSTRAINT SATISFACTION PROBLEMS

## Aim
To study and solve Constraint Satisfaction Problems using Python.

## Introduction
A Constraint Satisfaction Problem (CSP) is a problem in which values must be assigned to variables while satisfying a set of constraints.

A CSP contains three main components:

1. Variables – Items whose values must be assigned.
2. Domains – Possible values for each variable.
3. Constraints – Rules that restrict the possible assignments.

## 1. Map Coloring Problem

Map Coloring is a CSP where different regions of a map must be assigned colors such that neighboring regions have different colors.

**Example:** Coloring a map using Red, Green and Blue.

**Working:**
1. Identify all regions.
2. Assign available colors to each region.
3. Check neighboring regions.
4. Ensure adjacent regions have different colors.
5. Backtrack if a constraint is violated.

**Objective:** Color all regions without conflicts.

## 2. Crypt-Arithmetic Problem

Crypt-Arithmetic is a mathematical puzzle in which letters represent digits.

**Example:**

SEND + MORE = MONEY

Each letter represents a unique digit from 0 to 9.

**Rules:**
- Each letter must have a different digit.
- The first letter of a number cannot be zero.
- The arithmetic equation must be correct.

**Working:**
1. Identify the letters.
2. Assign unique digits.
3. Check the arithmetic equation.
4. Reject assignments that violate constraints.
5. Find the valid solution.

## 3. Local Search for CSP

Local Search is an optimization-based method for solving CSPs.

It starts with an initial assignment and tries to reduce the number of constraint violations.

**Working:**
1. Generate an initial assignment.
2. Check the constraints.
3. Identify violated constraints.
4. Change variable values to reduce conflicts.
5. Repeat until all constraints are satisfied or a stopping condition is reached.

**Example:** Solving the Eight Queens Problem by reducing attacking queen pairs.

## Comparison

| Problem | Objective |
|---|---|
| Map Coloring | Adjacent regions must have different colors |
| Crypt-Arithmetic | Find unique digits satisfying an equation |
| Local Search | Reduce constraint violations |

## Result
Map Coloring, Crypt-Arithmetic and Local Search techniques for Constraint Satisfaction Problems were studied and implemented successfully.
