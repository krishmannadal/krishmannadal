# Evidence audit

23 October 2026. The profile is positioned as a third-year AIML student seeking paid remote internships, not an inflated senior/research title. Personal details and graduation date are user-provided. Technical statements are grounded in the repositories below.

## Inspected source snapshots

| Repository | Default branch at audit | Source head |
| --- | --- | --- |
| mini-r1 | main | 4fa163f6eae9b6b85003971549fd67d4d0ba0718 |
| StemLab | main | 18b7b49 (full ID retained in git history) |
| Nullius | master | 46e358c |
| traffic-rl-twin | main | c89c913 |
| UNSUPERVISED_ASTRONOMY | main | 819b0a6 |
| portfolio | main | cc24225 |
| AmanGound2237/Wecode | main | e1f5db7 |

All source trees were cloned for code/configuration/history inspection. Public repositories beyond the named projects were considered; the portfolio was documented but not selected as a pin. Empty/practice/private repositories were not advertised as public evidence.

## Main corrections

| Finding | Source evidence | Presentation decision |
| --- | --- | --- |
| Mini-R1 replay claims overstate causal isolation | `configs/task22b_replay_only.yaml`, `configs/task23_90_10.yaml`, `configs/task23_75_25.yaml`, Task 23 report | Show composition and share together. G/H match composition; F differs in both. No claim that composition dominates dose or 25% is globally optimal. |
| Historical benchmark padding is imperfect | `src/evaluation.py`, Task 22 report, inference documentation | Preserve recorded numbers with limits; do not call every number a proven conservative lower bound. |
| H is released but absent from the web registry | `web/server.py`, release v1.0.0 | Link H's Python walkthrough and explain the UI mismatch. Do not offer a working H UI demo. |
| Release lists only H and G | GitHub release API | Remove claims that base/Task20 weights are already downloadable. State reproduction's missing prerequisites. |
| StemLab has two editions and accumulated claims | `web/src`, `web/build.mjs`, `package.json`, Netlify config, `VALIDATION.md` | Focus the web README; link Python setup. Separate source, historical developer checks, new local tests and current production observations. |
| WeCode labels execution success ACCEPTED | `src/app/api/run/route.ts`, `src/lib/runner.ts` | Explain it is not a correctness judge. No hidden-test claim. |
| WeCode setup has stale variables/runner instructions | session/chat/paper routes, `.env.example`, seed code | Use actual source variable names; flag module-load Gemini key and admin seed issue. |
| WeCode contributions are collaborative | Eight commits under Krishmannadal; initial platform/migration commits under Aman Gound | Cite representative changes; do not claim sole ownership. |
| Traffic media is empty and wait-time table lacks run output | Empty `docs/*` assets; evaluation source and tracked tree | Remove demo promise, unsupported metric table and unsupported MIT/production-grade claims. |
| Traffic evaluator always builds EmergencyEnv | `training/evaluate.py` | Warn about observation/action compatibility and accumulated-wait metric units; no new result. |
| Astronomy metrics/Colab link are unsupported placeholders | README, generator, trainer, pipeline, tracked tree | Remove headline metrics and placeholder URL; link real notebook and qualify synthetic examples. |
| Astronomy validation augmentation/checkpoint fallbacks | trainer shares dataset; pipeline falls back to random weights | Explicit limitations and a realistic validation roadmap. |
| Portfolio default README and conflicting content | `src/data/projects.ts`, `src/data/skills.ts`, metadata, current deployment | Replace framework boilerplate; list content discrepancies. Do not silently edit application behavior. |

## Live observations

- StemLab landing loaded; selecting the synthetic demo opened account creation. No authentication or studio processing was completed during this audit. The screenshot is the actual public landing page.
- WeCode `/sing-in` showed 404. The app's `/sign-in` route loaded; the public `/problems` catalog displayed database-backed problem listings. A screenshot records that catalog. Authenticated submissions and the external runner were not certified by this audit.
- The portfolio deployment loaded. Several displayed research claims conflict with the source; those remain a separate page-content backlog.

## Scientific status

No new model was trained, no benchmark was rerun on released weights, no publications/users/metrics were invented, and no human annotation or personal contribution was fabricated. Source code establishes implementation paths; successful unit tests establish the covered behavior under their fixtures; neither establishes production readiness or scientific generalization. Historical reports remain the archival record and may retain older interpretations; the refreshed README qualifies their use.
