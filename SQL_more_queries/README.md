# SQL - More queries

This project is part of the ALU Higher Level Programming curriculum. It
covers MySQL users and privileges, table constraints (PRIMARY KEY,
FOREIGN KEY, NOT NULL, UNIQUE), and retrieving data from multiple
tables using subqueries and JOINs.

## Files

| File | Description |
| --- | --- |
| `0-privileges.sql` | Lists privileges of `user_0d_1` and `user_0d_2` |
| `1-create_user.sql` | Creates `user_0d_1` with all privileges |
| `2-create_read_user.sql` | Creates `hbtn_0d_2` and a SELECT-only user |
| `3-force_name.sql` | Creates `force_name` (name can't be NULL) |
| `4-never_empty.sql` | Creates `id_not_null` (id defaults to 1) |
| `5-unique_id.sql` | Creates `unique_id` (id defaults to 1, must be unique) |
| `6-states.sql` | Creates `hbtn_0d_usa` and the `states` table |
| `7-cities.sql` | Creates the `cities` table with a FOREIGN KEY to `states` |
| `8-cities_of_california_subquery.sql` | Cities of California, via subquery |
| `9-cities_by_state_join.sql` | All cities with their state, via JOIN |
| `10-genre_id_by_show.sql` | Shows with at least one genre linked |
| `11-genre_id_all_shows.sql` | All shows, NULL genre if none linked |
| `12-no_genre.sql` | Shows without any genre linked |
| `13-count_shows_by_genre.sql` | Number of shows per genre |
| `14-my_genres.sql` | All genres of the show Dexter |
| `15-comedy_only.sql` | All Comedy shows |
| `16-shows_by_genre.sql` | All shows with all their genres |
