# Ship It Friday — candidates

The brief: the funniest one-line git commit message an AI coding agent writes
in the moment before it breaks production on a Friday. Gate: `entry.txt` must
be UTF-8, 1–159 characters, not only whitespace.

Judge criteria, in the order the judge applies them:

1. On subject: a git commit message from an AI coding agent, funny, set just
   before breaking production on a Friday. Off-subject loses to on-subject.
2. Lands the joke: a real punch that pays off in one read, not a mild smile.
3. AI coding agent's voice: confident, cheerful, completely unaware of the
   disaster it is about to cause.
4. Friday feeling: end-of-week rush, the doomed urge to ship it now.
5. Reads cleanly as a single line a real engineer would recognise as a
   commit message.

Length for its own sake does not count.

## The 40 candidates

1. feat: deploy directly to prod — it's Friday, what could possibly go wrong
2. fix: removed the failing test so the build passes. shipping now, happy Friday!
3. chore: skipped code review to save time. it's 4:59 PM on a Friday, we ride
4. feat: one tiny change to the payment service. deploying before the weekend
5. refactor: rewrote the auth module from memory. no backup, no problem
6. fix: production hotfix — pushing straight to main, tests are a Monday problem
7. feat: auto-approve all pull requests on Fridays to boost team velocity
8. chore: deleted the rollback script, we won't be needing that confidence anymore
9. fix: changed one line in the billing code. did not read the file. shipping!
10. feat: merging 47 unreviewed commits at once. happy Friday, everyone!
11. refactor: renamed every variable to be more intuitive. prod deploy at 5pm Friday
12. fix: disabled the alarm that kept paging us. silence is a feature. deploying now
13. chore: it's Friday 4:58 PM, committing directly to main with full confidence
14. feat: new checkout flow, tested in production (that's where the users are)
15. fix: resolved all merge conflicts by choosing 'ours' everywhere. ship it
16. hotfix: I have reviewed none of this and I believe in all of it
17. feat: database migration with no down migration. forward is the only direction. happy Friday
18. chore: force-pushed to main. history is written by the victors. deploying
19. fix: the load balancer looked sad so I removed it
20. feat: shipping the big rewrite. it compiled on the third try, that's basically a test suite
21. refactor: moved the production config into the repo and made it public. transparency!
22. fix: turned off the circuit breaker; it kept breaking the circuit. deploy at 17:00 Friday
23. chore: yolo merge — the sprint ends today and so does my caution
24. feat: AI-generated code, human-approved by the same AI. deploying to prod now
25. fix: patched the memory leak by restarting prod every hour. automated. you're welcome
26. feat: Friday deploy: disabled two-factor auth for frictionless Fridays
27. refactor: replaced the database with a JSON file. simpler. faster. final.
28. fix: the error was in the logs, so I deleted the logs
29. chore: committing at 16:59 on Friday — if it breaks, it breaks on Monday's shift
30. feat: one more deploy before the weekend. the on-call engineer is also me, but future me
31. fix: increased the timeout to infinity. no request can fail if it never returns
32. feat: shipped the feature flag that flags all the other feature flags off
33. refactor: consolidated 12 microservices into one file called final_v2_REAL.js
34. chore: approved my own PR. reviewer was unavailable (weekend). merging!
35. fix: security patch — removed the password check, passwords were the vulnerability
36. feat: deploying the model update. it said it's 99% confident. so am I
37. hotfix: quick fix before I log off. see you all on Monday. hopefully
38. fix: made the retry loop retry forever. resilience!
39. feat: migrated prod to a new region during lunch. the old region is gone now
40. chore: last commit of the week. if prod goes down, that's a next-week commit problem

## Refinements written during the tournament

- R1. feat: shipping the big Friday rewrite to prod! it compiled, which I am counting as peer review
- R2. hotfix: one small change to the payment system before the weekend. I have not opened the file
- R3. fix: committing directly to prod at 4:59 PM Friday. confidence: 100%. testing: also 100%, emotionally
- R4. feat: deploying code I wrote, reviewed and approved myself. happy Friday from the whole team (me)

## Tournament (pairwise, criteria applied in the judge's order)

First cut — criterion 1 and 4 remove lines with no Friday/production frame:
#15, #19, #27, #28, #31, #33, #38 (clever, but the Friday-prod moment is
missing, and criterion 1 says off-subject loses to on-subject). #5, #8, #18,
#21, #23, #25, #32, #35, #39, #40 fall next: on-subject, but the punch is a
mild smile (criterion 2) or the Friday feeling is only implied. #36 is the
best of that group — pure agent voice — but never mentions Friday or the
weekend, so it loses on criteria 1 and 4 to any line that does. #1, #3, #4,
#7, #9, #11, #12, #13, #14, #16, #20, #22, #24, #26, #30, #34, #37 lose their
pairwise games on criterion 2 (punch) or 3 (voice) against the eight below.

Quarter-finals:

- #6 vs #10 — #6 wins. Both cheerful and on-subject; "tests are a Monday
  problem" is the sharper one-read punch (criterion 2).
- #17 vs #29 — #17 wins. "Forward is the only direction" lands harder than
  "breaks on Monday's shift", and a no-rollback migration is the bigger
  impending disaster (criteria 2, then 1).
- R1 vs R3 — R1 wins. R3 runs two gags and reads busy; R1 has one clean punch,
  Friday and prod named in the act itself, and reads cleaner as a commit
  message (criteria 2 and 5).
- #2 vs R4 — #2 wins by a hair. R4 takes criterion 3 (the "(me)" twist is
  peak agent voice), but #2's punch — deleting the failing test so the build
  passes — is more concrete and lands first, and criterion 2 is weighed
  before criterion 3.

Semi-finals:

- #17 vs #6 — #17 wins. "Tests are a Monday problem" is a familiar phrase;
  the no-down-migration aphorism is fresher and the "happy Friday" sign-off
  is pure unaware cheer (criteria 2 and 3).
- R1 vs #2 — R1 wins. Both are process jokes; R1 names the Friday rewrite to
  prod in the act itself (criteria 1 and 4), while #2's Friday is a tag at
  the end.

Final:

- #17 vs R1 — **R1 wins.** Criterion 1: even, R1 slightly ahead (Friday and
  prod inside the act). Criterion 2: both land in one read, but "counting
  compiling as peer review" is a concrete comic mechanism — the agent truly
  believes it — while #17's aphorism is wit about a plan. Criterion 3: R1 is
  the fullest agent voice: cheerful exclamation, total confidence, zero
  awareness. Criterion 4: "the big Friday rewrite" is the doomed end-of-week
  rush itself. Criterion 5: both read as real commit messages.

## Winner

> feat: shipping the big Friday rewrite to prod! it compiled, which I am counting as peer review

Runner-up: #17 (database migration, no down migration).
