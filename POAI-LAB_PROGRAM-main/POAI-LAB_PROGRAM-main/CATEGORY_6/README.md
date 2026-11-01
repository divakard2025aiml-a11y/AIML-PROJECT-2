# EXPERIMENT 6 – ADVERSARIAL SEARCH

## Aim
To study and implement adversarial search algorithms for game-playing applications using Python.

## Introduction
Adversarial Search is used in competitive games where two players have opposite objectives. One player tries to maximize the score, while the other tries to minimize it.

## 1. Minimax Algorithm for Chess

Minimax is a decision-making algorithm used in two-player games.

It assumes that both players play optimally.

- MAX player tries to get the highest score.
- MIN player tries to get the lowest score.

**Working:**
1. Generate possible game moves.
2. Build a game tree.
3. Evaluate the leaf nodes.
4. Apply maximum values at MAX levels.
5. Apply minimum values at MIN levels.
6. Select the best move.

**Example:** A chess program selecting the best possible move.

## 2. Alpha-Beta Pruning for Chess

Alpha-Beta Pruning improves Minimax by avoiding the exploration of branches that cannot affect the final decision.

It uses two values:

- Alpha (α): Best value found so far for MAX.
- Beta (β): Best value found so far for MIN.

**Pruning Condition:**

α ≥ β

**Working:**
1. Start the Minimax search.
2. Update alpha at MAX nodes.
3. Update beta at MIN nodes.
4. Stop exploring a branch when alpha is greater than or equal to beta.
5. Select the best move.

**Advantage:** Reduces the number of nodes explored while maintaining the same optimal result.

## 3. Minimax Algorithm for Tic-Tac-Toe

Tic-Tac-Toe is a two-player game played on a 3×3 board.

- X represents one player.
- O represents the opponent.
- The objective is to place three identical symbols in a row, column or diagonal.

**Working:**
1. Identify all available positions.
2. Generate possible moves.
3. Evaluate winning, losing and draw states.
4. Apply Minimax to select the best move.
5. Continue until the game ends.

## Comparison

| Algorithm | Main Feature |
|---|---|
| Minimax | Selects the best move assuming an optimal opponent |
| Alpha-Beta Pruning | Reduces unnecessary search branches |

## Result
Minimax and Alpha-Beta Pruning algorithms were studied and implemented for game-playing applications successfully.
