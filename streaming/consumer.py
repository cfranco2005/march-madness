"""Part 8: Stream consumer (Phase 2).

Goal: read play events from Kafka, process them, and store them.

TODO:
  1. Subscribe to the topic your producer (Part 7) writes to.
  2. For each event, update the game state (score, time remaining, possession).
  3. Call the win probability model (Part 9) and store the result.
  4. Write events and probabilities to TimescaleDB.

Questions to answer before you code:
  - What happens if the same event arrives twice? How do you avoid
    double-counting it?
  - If the consumer restarts, how does it know where it left off?
"""
