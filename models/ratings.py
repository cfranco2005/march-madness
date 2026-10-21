"""Part 4: Ratings engine.

Goal: give every team a number that represents how good it is, updated game
by game.

TODO (in order):
  1. Elo: every team starts at the same rating; after each game, the winner
     gains points and the loser drops by the same amount. Bigger upsets move
     ratings more.
  2. Tune it: what K-factor works best? Should margin of victory matter?
     Should home court be worth extra? Should ratings shrink toward the
     average between seasons?
  3. Later: efficiency-based ratings adjusted for opponent strength.
  4. Phase 3: Bayesian ratings that also report uncertainty.

Questions to answer before you code:
  - What's the formula for the probability that team A beats team B given
    their Elo ratings?
  - How will you check that your ratings are any good? (Part 5 answers this.)
"""
