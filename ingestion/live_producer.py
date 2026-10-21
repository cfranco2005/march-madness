"""Part 7: Live producer (Phase 2, start in November).

Goal: during live games, fetch new plays every few seconds and send each one
into Kafka as an event.

TODO:
  1. Find a source of live play-by-play and fetch one finished game by hand.
  2. Decide what one "event" looks like (which fields? what format?).
  3. Poll on a loop, and send only plays you haven't sent before.
  4. Handle the source being slow, down, or returning garbage.

Questions to answer before you code:
  - How will you know which plays are new since the last poll?
  - What should happen if the producer crashes mid-game and restarts?
"""
