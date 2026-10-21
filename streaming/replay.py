"""Part 10: Replay mode (Phase 2).

Goal: send a finished game through the pipeline as if it were live, so you
can demo anytime, even when no games are on.

TODO:
  1. Load all plays for one past game.
  2. Send them to Kafka in order, pausing between plays.
  3. Add a speed setting (real time, 10x, 100x).

Question to answer before you code:
  - Why is it useful that replay mode uses the same Kafka topic as the
    live producer?
"""
