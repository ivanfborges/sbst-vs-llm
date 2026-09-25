# Archived results and limits

[Português](RESULTS.pt-BR.md) · [Study](../README.md) · [Future protocol](PROTOCOL.md)

These figures come from committed February **26**, 2026 artifacts, not from a
September rerun. The old [comparison table](../evidencias/05-comparativos/tabela-comparativa-resultados.md)
says February 20 and mixes a second PIT copy; treat it as a historical draft.
The [original PDF/DOCX](../evidencias/06-relatorio/) are also historical.
[Audit JSON](archive-audit.json) records the extracted totals and file hashes.

| Measure | EvoSuite | LLM drafted, then PIT refined | Source |
|---|---:|---:|---|
| JUnit cases, all passing | 10 | 15 | [EvoSuite Surefire](../evidencias/03-evosuite/03-surefire/TEST-com.example.TriangleClassifier_ESTest.xml), [LLM Surefire](../evidencias/04-llm/04-surefire/TEST-com.example.TriangleClassifierTest.xml) |
| JaCoCo instructions | 122/124 | 121/124 | [EvoSuite](../evidencias/03-evosuite/04-jacoco/jacoco.xml), [LLM](../evidencias/04-llm/05-jacoco/jacoco.xml) |
| JaCoCo branches | 17/18 | 17/18 | Same JaCoCo XMLs |
| JaCoCo lines | 23/24 | 23/24 | Same JaCoCo XMLs |
| PIT mutations killed | 16/25 (64%) | 22/25 (88%) | [EvoSuite](../evidencias/03-evosuite/05-pit/mutations.xml), [LLM](../evidencias/04-llm/06-pit/mutations.xml) |
| PIT survived / no coverage | 8 / 1 | 3 / 0 | Same PIT XMLs |
| PIT test strength | 16/24 ≈67% | 22/25 =88% | [PIT definition](https://pitest.org/quickstart/commandline/) |
| PIT test invocations summed from XML | 128 | **75** | Same PIT XMLs and [EvoSuite log](../evidencias/03-evosuite/02-logs/02-mvn-pitest-mutationCoverage.txt), [LLM log](../evidencias/04-llm/03-logs/02-mvn-pitest-mutationCoverage.txt) |

**Archive discrepancy.** `reports/llm/pit/mutations.xml` has 83 test
invocations, while `evidencias/04-llm/06-pit/mutations.xml` and its archived log
both have 75. Both XML copies have 22 killed and 3 survived mutants. We use the
copy paired with the archived run log for the table. Neither count is a measure
of test redundancy or productivity: PIT selects tests per mutant, and the
suites have different numbers of JUnit cases. See PIT's
[basic concepts](https://pitest.org/quickstart/basic_concepts/).

The target source hash (SHA256 after normalizing CRLF to LF) matches in both arms and the preserved source copy:
`ad290ecca146e3910258998e460e60d270f4442423b5b313698f94b1e8ad2726`.
The current suite files also match their evidence copies byte for byte.
EvoSuite's own `statistics.csv` records 19/19 BRANCH goals for its generation
criterion; JaCoCo separately records 17/18 branches. These are different tool
measures and should not be equated.

The three LLM-suite survivors are boundary mutations at the nonpositive-side
guard. Their equivalence is plausible from the source's downstream triangle
inequality, but has **not been formally established for the PIT mutants**.
We retain them in the denominator. Mutation score measures detection of this
set of synthetic code changes, not production defect detection. The academic [DOCX report](../evidencias/06-relatorio/Relatorio.docx) names
ChatGPT 5.2 Thinking as the LLM, but does not preserve a full run configuration,
model-access record or human-editing time. The observed
six extra killed mutants cannot be attributed to the LLM alone: the LLM arm
used PIT feedback, the generation budgets are not matched, and there is one
target and no repeated seeds. Readability and maintainability were not scored
blindly or with a defined rubric. There is no productivity or cost measurement.
