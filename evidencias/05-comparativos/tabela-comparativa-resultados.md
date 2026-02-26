# Tabela comparativa de resultados — EvoSuite vs LLM

## Contexto
Este arquivo resume os resultados do experimento de geração de testes unitários para a classe `TriangleClassifier`, comparando:

- **EvoSuite** — geração automática baseada em busca (*Search-Based Software Testing - SBST*)
- **LLM** — geração assistida por modelo de linguagem com refinamento orientado por mutation testing

Ferramentas de avaliação utilizadas:

- **JaCoCo** — cobertura estrutural
- **PIT / PITest** — cobertura de mutação e *test strength*

Data de consolidação dos resultados: **20/02/2026**

---

## Tabela comparativa

| Métrica | EvoSuite (SBST) | LLM (com refinamento por mutação) |
|---|---:|---:|
| Classe de teste principal | `TriangleClassifier_ESTest` | `TriangleClassifierTest` |
| Nº de testes executados (Surefire) | 10 | 15 |
| Tempo dos testes (Surefire) | ~1,64 s | ~0,17 s |
| JaCoCo – Instruções | 98% (122/124) | 97% (121/124) |
| JaCoCo – Branches | 94% (17/18) | 94% (17/18) |
| JaCoCo – Linhas | ~96% | 23/24 (~96%) |
| JaCoCo – Métodos | 100% (3/3) | 67% (2/3) |
| PIT – Line Coverage (classes mutadas) | 94% (17/18) | 94% (17/18) |
| PIT – Mutation Coverage | 64% (16/25) | 88% (22/25) |
| PIT – Test Strength | 67% | 88% |
| PIT – Mutations sem cobertura | 1 | 0 |
| PIT – Mutantes sobreviventes | 8 | 3 |
| PIT – Testes executados na análise de mutação | 128 | 83 |

---

## Principais achados

### 1. Cobertura estrutural semelhante
As duas abordagens obtiveram resultados muito próximos em cobertura estrutural:

- **JaCoCo Branches:** 94% em ambos os cenários
- **JaCoCo Instruções:** ligeira vantagem para o EvoSuite (98% vs 97%)

### 2. Melhor efetividade prática da suíte gerada com LLM
Apesar da cobertura estrutural semelhante, a abordagem com LLM apresentou melhor desempenho em mutation testing:

- **Mutation Coverage:** 88% vs 64%
- **Test Strength:** 88% vs 67%
- **Mutações sem cobertura:** 0 vs 1

### 3. Suíte LLM mais direcionada
O LLM executou menos testes durante a análise do PIT:

- **LLM:** 83 execuções
- **EvoSuite:** 128 execuções

Isso sugere menor redundância e maior direcionamento semântico para os cenários relevantes.

### 4. Mutantes sobreviventes no cenário LLM
No cenário LLM, permaneceram **3 mutantes sobreviventes**, todos do tipo:

- `ConditionalsBoundaryMutator`
- linha **17**
- condição: `a <= 0 || b <= 0 || c <= 0`

Há fortes indícios de que esses mutantes sejam **equivalentes** (ou quase equivalentes do ponto de vista comportamental), pois, mesmo com alteração da fronteira da condição, a lógica posterior tende a continuar classificando o caso como `INVALID`.

---

## Ganhos observados com o LLM em relação ao EvoSuite

- **Cobertura de mutação:** 64% → 88%
- **Aumento absoluto:** +24 pontos percentuais
- **Mutantes mortos:** 16 → 22
- **Aumento absoluto:** +6 mutantes mortos
- **Test strength:** 67% → 88%
- **Redução de execuções no PIT:** 128 → 83
- **Redução absoluta:** 45 execuções
- **Redução percentual aproximada:** 35,2%

---

## Interpretação geral

Os resultados indicam que:

1. **Cobertura estrutural, isoladamente, não foi suficiente para diferenciar a qualidade das suítes**;
2. **Mutation testing foi a métrica mais relevante para evidenciar a superioridade da abordagem com LLM**;
3. **EvoSuite funcionou bem como baseline automatizado**, com alta cobertura estrutural;
4. **LLM + PIT (refinamento iterativo)** produziu uma suíte mais efetiva, legível e com melhor capacidade de matar mutantes.

---

## Conclusão resumida

No estudo de caso com a classe `TriangleClassifier`, a abordagem com **LLM refinada com feedback do PIT** apresentou melhor equilíbrio entre:

- efetividade dos testes;
- legibilidade;
- manutenibilidade;
- capacidade de detectar mutações.

O **EvoSuite** foi útil como ponto de partida automatizado, mas o **LLM** mostrou desempenho superior na qualidade prática da suíte final.