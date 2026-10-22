# Repository presentation plan

Prepared 23 October 2026. Public source, commit history and visible deployment pages were inspected. Private repositories were excluded from public project placement; no repository visibility was changed.

## Recommended pin order

| Order | Repository | Why this slot |
| --- | --- | --- |
| 1 | [mini-r1](https://github.com/krishmannadal/mini-r1) | Strongest research artifact: model implementation, configurations, experiment reports and released weights. Lead with evidence and qualified negative results. |
| 2 | [StemLab](https://github.com/krishmannadal/StemLab) | Practical AI integration and product UI, with a reachable deployed site. Distinguish pretrained inference from model training. |
| 3 | [Nullius](https://github.com/krishmannadal/Nullius) | Direct fit for NLP, evaluation and AI reliability; typed contracts, inspection traces and a gated research workflow. Human evaluation remains pending. |
| 4 | [WeCode](https://github.com/AmanGound2237/Wecode) | Collaborative full-stack evidence and visible contributions: runner migration, editor/math rendering, deployment preparation, paper workspace and tutor. Credit the team. |
| 5 | [traffic-rl-twin](https://github.com/krishmannadal/traffic-rl-twin) | Broadens the profile with simulation, APIs, streaming UI and RL infrastructure. Label it a local prototype pending benchmark reproduction. |
| 6 | [UNSUPERVISED_ASTRONOMY](https://github.com/krishmannadal/UNSUPERVISED_ASTRONOMY) | Adds computer-vision/data workflow evidence. Keep synthetic testing and observational scientific claims separate. |

For application-development applications, move WeCode above Nullius. Keep the portfolio outside the six pins: it is presentation scaffolding and its live copy needs reconciliation with source evidence.

## Repository metadata

The descriptions below are prepared for the corresponding About fields. A blank homepage is intentional when no deployed application is verified.

| Repository | Description | Topics | Homepage |
| --- | --- | --- | --- |
| mini-r1 | 42.1M-parameter PyTorch Transformer with arithmetic-supervision, forgetting and replay experiments. Source, configurations, released weights and qualified results. | pytorch, language-models, evaluation, continual-learning, reproducible-research | Leave blank; release and local inference links belong in the README |
| StemLab | Browser music rehearsal studio integrating pretrained Demucs, a Web Audio mixer, local effects and WAV export. Desktop inference; account required. | audio-processing, source-separation, onnxruntime, web-audio, javascript | https://stemlab-krishmannadal.netlify.app/ |
| Nullius | Claim-verification inspection harness with hybrid retrieval, pairwise NLI, traceable aggregation and a gated annotation workflow. Scientific evaluation pending. | nlp, information-retrieval, fact-checking, fastapi, evaluation | Leave blank; local service only |
| traffic-rl-twin | Local SUMO traffic-simulation workbench with FastAPI/WebSockets, a React dashboard, DQN/PPO training paths and rule-based emergency preemption. | reinforcement-learning, sumo, fastapi, simulation, react | Leave blank; local prototype |
| UNSUPERVISED_ASTRONOMY | Exploratory FITS disk-image workflow using a PyTorch autoencoder, UMAP and HDBSCAN. Synthetic test data; scientific validation pending. | astronomy, unsupervised-learning, pytorch, autoencoder, clustering | Leave blank; notebook/local workflow |
| portfolio | Next.js presentation site for project dossiers and research notes. Technical claims should be checked against the linked source repositories. | portfolio, nextjs, typescript, react | https://portfolio-five-alpha-65.vercel.app/ |
| WeCode — proposed for maintainer | Collaborative AI/ML practice platform with a Monaco Python workspace, Wandbox execution and Gemini-assisted learning. Execution only; no correctness judge. | nextjs, typescript, prisma, postgresql, coding-practice | https://wecode-two.vercel.app/problems |

## Visual system and assets

The profile uses navy, teal and neutral text, with light/dark SVG banners. A small committed GIF plays once; a PNG, alt text and readable Markdown provide static access. No external stats widgets, typing services or JavaScript are required. The banner's line motif is decorative, not measured data.

Each owned project includes a 1280 × 640 editorial social card at `docs/assets/social-preview.png`. The profile card is at `assets/social-preview.png`. These are title cards, not invented product screenshots. Actual public screenshots are identified separately in StemLab and the WeCode proposal.

To assign a social card manually: repository **Settings → General → Social preview → Edit → Upload an image**, choose the matching PNG and save. Merely committing the PNG does not assign it as GitHub's preview. Existing preview state must be inspected in settings before replacing it. No license is added to any repository.

## WeCode handoff

This connection has read-only access to AmanGound2237/Wecode. The proposed replacement README is [here](proposals/wecode/README.md), with its actual [catalog screenshot](proposals/wecode/problems.jpg). Copy the README to the project root and place the screenshot at `docs/assets/problems.jpg`; change the proposal image target from `problems.jpg` to `docs/assets/problems.jpg`. A local `wecode-readme.patch` accompanies the proposal for direct application from the WeCode repository root.

The proposal fixes the execution-versus-judging distinction, the `/sing-in` link, obsolete Docker runner instructions, `SESSION_SECRET` versus `SESSION_PASSWORD`, separate Gemini keys, and the production seed caveat. It credits source-history-supported team contributions. It does not alter application code or send a message to the maintainer.

## Remaining work outside this documentation change

- Run a signed-in production StemLab smoke test: separation, play/solo/loop, effect rendering, export, save/reopen and optional composer/coach. Record input duration and browser, and separate synthetic mixer checks from real separation.
- Package Mini-R1's missing Task 20 initialization for reproduction, qualify H inference and update the old demo registry in a separate behavior-changing change.
- Complete Nullius's real annotation/adjudication/provider prerequisites; do not report fixture metrics as scientific results.
- Reconcile the portfolio's page copy with Mini-R1 dimensions, replay controls, single-seed limits and publicly accessible evidence. This task changes its README, not the application's content.
- Publish matched-seed traffic evaluation artifacts and a real demo recording; correct evaluator environment/metric definitions first.
- Qualify the astronomy split, augmentation, checkpoint and metric paths before claiming real-data performance.
- WeCode maintainer should review the README proposal and address seeded admin credentials, actual correctness judging and AI-route configuration separately.
