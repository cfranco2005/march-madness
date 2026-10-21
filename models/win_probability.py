"""Part 9: Live win probability (Phase 2).

Goal: during a game, estimate each team's chance of winning after every
possession.

TODO:
  1. Before tip-off, start from the pre-game probability (Part 5).
  2. As the game goes on, shift weight toward the current score margin
     and time remaining.
  3. Train it on historical play-by-play from finished games.

Question to answer before you code:
  - Why is a 5-point lead with 30 seconds left worth more than a 5-point
    lead at halftime, and how should your model capture that?
"""
