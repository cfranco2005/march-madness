"""Part 5: Game prediction model.

Goal: given two teams, output the probability that each one wins.

TODO:
  1. Baseline first: "the higher seed always wins." Every model must beat this.
  2. Build features for each matchup (rating difference, seed difference, ...).
  3. Train on past seasons, test on seasons the model has never seen.
     Never test on data you trained on.
  4. Score with accuracy, Brier score, and log loss.
  5. Check calibration: when the model says 70%, does that team win about
     70% of the time?

Questions to answer before you code:
  - Why is log loss a better scorecard than accuracy for this project?
  - Why must you split train/test by season rather than randomly?
"""
