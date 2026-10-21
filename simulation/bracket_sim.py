"""Part 6: Tournament simulator.

Goal: play the whole tournament thousands of times using your model's
probabilities, then count how often each team reaches each round.

TODO:
  1. Represent a bracket: which seeds play each other, and who the winners
     face next.
  2. Simulate one tournament: for each game, draw a random number and
     compare it to the win probability.
  3. Repeat 10,000 times and tally results per team per round.
  4. Backtest: run it on past tournaments and compare to what happened.
  5. 2027: support the new 76-team format with its expanded Opening Round.

Questions to answer before you code:
  - Why simulate instead of just advancing the favorite in every game?
  - How will you make results reproducible? (hint: random seeds)
"""
