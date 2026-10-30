# Spot Material · Match (prototype)

Designers set a short brief, then swipe through standard materials (Spot Material's own photos): right = suits my design, left = doesn't (optional reason), "Not sure" = skip. The deck learns from each swipe. After 4 suitable and 10 swipes it's "a match": the page suggests innovations and standard materials not yet seen, each with the reason (brief fit, and which suitable material it resembles).

Separate from the EU material-intelligence project. Reads from Supabase through read-only functions `match_deck` and `match_suggest`, records swipes with `log_swipe` (table `swipe_events`). Material photos: Spot Material (copied into Storage by the `copy-match-images` Edge Function, listed in `match_images`). Innovation images belong to the companies named.
