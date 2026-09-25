# Resultados arquivados e limites

[English](RESULTS.md) · [Estudo](../README.pt-BR.md) · [Protocolo futuro](PROTOCOL.pt-BR.md)

Os números vêm de artefatos versionados de **26/02/2026**, sem nova execução do
experimento em setembro. A [tabela antiga](../evidencias/05-comparativos/tabela-comparativa-resultados.md)
informa 20/02 e mistura outra cópia do PIT; permanece como rascunho histórico.
O [PDF/DOCX original](../evidencias/06-relatorio/) também é histórico. O
[JSON da auditoria](archive-audit.json) registra totais e hashes.

| Medida | EvoSuite | LLM com refinamento por PIT | Fonte |
|---|---:|---:|---|
| Casos JUnit, todos aprovados | 10 | 15 | [Surefire EvoSuite](../evidencias/03-evosuite/03-surefire/TEST-com.example.TriangleClassifier_ESTest.xml), [Surefire LLM](../evidencias/04-llm/04-surefire/TEST-com.example.TriangleClassifierTest.xml) |
| Instruções JaCoCo | 122/124 | 121/124 | [EvoSuite](../evidencias/03-evosuite/04-jacoco/jacoco.xml), [LLM](../evidencias/04-llm/05-jacoco/jacoco.xml) |
| Branches JaCoCo | 17/18 | 17/18 | Mesmos XMLs JaCoCo |
| Linhas JaCoCo | 23/24 | 23/24 | Mesmos XMLs JaCoCo |
| Mutantes mortos PIT | 16/25 (64%) | 22/25 (88%) | [EvoSuite](../evidencias/03-evosuite/05-pit/mutations.xml), [LLM](../evidencias/04-llm/06-pit/mutations.xml) |
| Sobreviventes / sem cobertura PIT | 8 / 1 | 3 / 0 | Mesmos XMLs PIT |
| Test strength PIT | 16/24 ≈67% | 22/25 =88% | [Definição do PIT](https://pitest.org/quickstart/commandline/) |
| Execuções de testes somadas no XML PIT | 128 | **75** | Mesmos XMLs PIT e [log EvoSuite](../evidencias/03-evosuite/02-logs/02-mvn-pitest-mutationCoverage.txt), [log LLM](../evidencias/04-llm/03-logs/02-mvn-pitest-mutationCoverage.txt) |

**Divergência do acervo.** `reports/llm/pit/mutations.xml` registra 83
execuções, enquanto `evidencias/04-llm/06-pit/mutations.xml` e o log histórico
correspondente registram 75. Ambos os XMLs têm 22 mutantes mortos e 3
sobreviventes. A tabela usa a cópia vinculada ao log. Nenhuma dessas contagens
mede redundância ou produtividade: o PIT escolhe testes por mutante e as suítes
têm tamanhos diferentes. Veja os [conceitos do PIT](https://pitest.org/quickstart/basic_concepts/).

O hash da classe alvo (SHA256 após normalizar CRLF para LF) é idêntico nos dois projetos e na cópia de evidências:
`ad290ecca146e3910258998e460e60d270f4442423b5b313698f94b1e8ad2726`.
As suítes atuais também são idênticas, byte a byte, às cópias do acervo.
`statistics.csv` do EvoSuite registra 19/19 objetivos BRANCH na geração;
JaCoCo registra separadamente 17/18 branches. São medidas distintas.

Os três sobreviventes da suíte LLM são mutações de fronteira na guarda dos lados
não positivos. A equivalência parece plausível pela desigualdade do triângulo
que vem depois, mas **não foi demonstrada formalmente para os mutantes PIT**.
Eles continuam no denominador. A pontuação de mutação mede detecção desse
conjunto de alterações sintéticas, não defeitos reais em produção. O [relatório DOCX](../evidencias/06-relatorio/Relatorio.docx) identifica
ChatGPT 5.2 Thinking como LLM, mas não preserva configuração completa da
sessão, registro de acesso ao modelo ou tempo de edição humana. Os seis
mutantes adicionais mortos não podem ser atribuídos somente ao LLM: sua suíte
recebeu feedback do PIT, os orçamentos de geração não foram pareados, há uma
classe e nenhuma repetição por semente. Legibilidade e manutenibilidade não
foram avaliadas às cegas com rubrica definida. Não há medida de produtividade
ou custo.
