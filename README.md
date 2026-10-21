# March Madness Predictor

> One-sentence pitch goes here once Phase 1 works.

<!-- TODO: add a screenshot or GIF of the dashboard here -->

## What it does

TODO: 2–3 sentences. What does the project predict, and what makes it different?

## Architecture

TODO: add a diagram once the streaming pipeline exists (Phase 2).

| Part | Folder | Status |
|------|--------|--------|
| 1. Historical ingestion | `ingestion/load_historical.py` | ⬜ |
| 2. Database schema | `db/schema.sql` | ⬜ |
| 3. Transformations | `transforms/` | ⬜ |
| 4. Ratings engine | `models/ratings.py` | ⬜ |
| 5. Game prediction model | `models/game_predictor.py` | ⬜ |
| 6. Tournament simulator | `simulation/bracket_sim.py` | ⬜ |
| 7. Live producer | `ingestion/live_producer.py` | ⬜ |
| 8. Stream consumer | `streaming/consumer.py` | ⬜ |
| 9. Live win probability | `models/win_probability.py` | ⬜ |
| 10. Replay mode | `streaming/replay.py` | ⬜ |
| 11. Orchestration | `orchestration/` | ⬜ |
| 12. Dashboard | `app/streamlit_app.py` | ⬜ |
| 13. Infra and CI | `docker-compose.yml`, `.github/` | ⬜ |

## Results

TODO: backtest numbers (accuracy, Brier score, log loss) vs. a "higher seed wins" baseline.

## How to run it

TODO: setup steps someone else could follow from a fresh clone.

## What I learned

TODO: fill in as you go. This section is great interview material.

## What's next

TODO
