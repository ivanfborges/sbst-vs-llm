# Prospective comparison protocol — draft, no new runs

[Português](PROTOCOL.pt-BR.md) · [Archived results](RESULTS.md)

**Status:** design for a future experiment. The February one-class exercise is
historical evidence, not a pilot used to choose winning settings. Freeze a
versioned protocol and a run manifest **before** generating new suites. Any
post hoc change must be labeled and kept separate from confirmatory results.

## Questions and arms

1. Under recorded generation budgets, how do *unrefined* EvoSuite and LLM suites
   compare on the same Java targets and fixed mutation set?
2. How much does a prespecified, equal PIT-feedback allowance change each
   approach? Analyze refined arms separately from the unrefined comparison.

Do not collapse "LLM + PIT + manual edits" into "LLM". Specify who makes each
change. If EvoSuite cannot receive a comparable refinement intervention, keep
the second question descriptive rather than calling its difference causal.

| Before-run item | Rule to record and freeze |
|---|---|
| Targets | TriangleClassifier plus at least two additional small Java classes chosen for varied control flow **before seeing new results**; commit exact source hashes, tests/specification and exclusion criteria. Do not pick targets based on which arm wins. |
| Replicates | Plan five independent generations per arm and target if feasible; record all seeds and failures. If resources limit this, reduce scope in the frozen protocol before running. Do not treat five within one target as five independent systems. |
| EvoSuite | Pin Java, JAR, runtime, Maven, criterion, search budget, stopping condition and seed. Capture full command, stdout, generated suite and elapsed generation time. The old README's 60-second command is an example, not verified historical configuration. |
| LLM | Identify provider/model/version, access mode, prompt text, temperature/top-p/seed when exposed, token limits, response, token/cost logs, generation time and all manual edits. Use the same target specification and output contract for every replicate. If the service cannot be fixed or priced, report that limit before execution. |
| Refinement | Predefine at most one PIT feedback round per arm, allowed information, intervention time limit and who may edit. Store both initial and final suites and mutation reports. Never present final-only scores as raw generator quality. |
| Build and scoring | Identical target bytecode/source and JUnit/JaCoCo/PIT versions, target classes, mutator set, compiler/runtime and test timeout across arms. Preserve all failures, flaky or uncompilable suites, rather than dropping them from the denominator. |
| Mutants | Record generated, killed, survived, uncovered, timed out and excluded for each run. Report mutation coverage and test strength with denominators. Review suspected equivalent mutants independently and report raw and adjudicated scores separately; do not remove them ad hoc. |
| Human assessment | If claiming readability/maintenance, define a rubric, use blinded raters and agreement reporting. Otherwise omit that claim. |

## Analysis and reporting

The unit of analysis is a **target**, with repeated generation runs nested
within it. Present every target and replicate; summarize paired per-target
mutant-kill differences and their spread, alongside JaCoCo branch coverage,
compilation success, test count, generation/refinement time and recorded cost.
Do not treat PIT's number of selected test invocations as productivity or
independent samples. With only a few targets, use descriptive ranges and do
not claim general superiority or precision from a row-level bootstrap.

Use the same target snapshot for all arms. A mutation set may change when
bytecode, PIT version or configuration changes, making raw percentages
non-comparable; verify equality before interpreting differences. Avoid using
PIT feedback to tune a supposedly unrefined arm. Keep run manifests, prompts,
model responses, Java suites, tool logs and aggregate reports with hashes.
Check whether any prompts or code contain data that should remain private
before publishing them.

## Start gate

A comparative run cannot be called fully reproducible yet because the
historical report names ChatGPT 5.2 Thinking, but full session
settings, sampling seeds and human edit time are absent. For
a future run, first select and freeze targets, model/configuration, budget and
available tools; then record a baseline command and execute the protocol.
This document authorizes no paid API use and makes no claim that the proposed
additional targets or repetitions have happened.
