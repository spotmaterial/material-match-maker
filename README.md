# Spot Material · Match (prototype)

**index.html (v3, 30 Oct):** starts with a few words ("soft fabric for a café chair"), then up to 3 questions chosen from the tags that best split the materials found (plain wording in table `match_labels`, questions in `match_questions`; untick `ask` / `enabled` to hide one). Then the swipe deck and matches as below. Uses the Edge Function `match` (words → meaning, then `match_next_question`, `match_deck_words`, `match_suggest_words`).

**Looks (30 Oct):** after the words, a grid of generic material "looks" (studio-lit spheres in `looks/`, drawn procedurally with Three.js (no product photos; renderer kept outside the repo)) narrows the search; chosen looks count strongly in the ranking. Which grades belong to which look comes from editable rules in Supabase (`match_look_rules`; after editing run `select match_build_looks();`).

**classic.html:** the earlier tick-box start.

Designers set a short brief, then swipe through standard materials (Spot Material's own photos): right = suits my design, left = doesn't (optional reason), "Not sure" = skip. The deck learns from each swipe. After 4 suitable and 10 swipes it's "a match": the page suggests innovations and standard materials not yet seen, each with the reason (brief fit, and which suitable material it resembles).

Separate from the EU material-intelligence project. Reads from Supabase through read-only functions `match_deck` and `match_suggest`, records swipes with `log_swipe` (table `swipe_events`). Material photos: Spot Material (copied into Storage by the `copy-match-images` Edge Function, listed in `match_images`). Innovation images belong to the companies named.
