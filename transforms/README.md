# Part 3: Transformations

Goal: turn raw game rows into the tables your models need.

Start with plain `.sql` files here. In Phase 3, convert them into a dbt project.

TODO:
1. `games_long.sql`: reshape so each game appears twice, once from each team's point of view
2. `team_season_stats.sql`: per team, per season: wins, losses, points for/against, average margin
3. Later: possession-based stats (offensive and defensive efficiency, pace)

Question to answer first: why does "one row per team per game" make stats easier to calculate than "one row per game"?
