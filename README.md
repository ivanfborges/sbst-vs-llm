# SBST vs LLM — EvoSuite x LLM (JaCoCo + PIT)

Este repositório contém uma atividade prática de **Software-Based Software Testing (SBST)** comparando duas abordagens de criação de testes automatizados para um projeto Java:

- **EvoSuite** (geração automática baseada em busca — foco em *branch coverage*)
- **LLM** (testes escritos a partir de um prompt e revisão incremental)

A avaliação é feita com:
- **JaCoCo** (cobertura de código)
- **PIT** (mutation testing: mutation coverage e test strength)

---

## Objetivo

Comparar **quantidade/qualidade** de testes gerados por EvoSuite vs LLM, usando métricas objetivas:

- Cobertura (linhas / branches) — *JaCoCo*
- Efetividade dos testes em matar mutantes — *PIT*

---

## Estrutura do projeto

- `evosuite/`  
  Projeto Maven com a classe alvo e testes gerados pelo **EvoSuite**.

- `llm/`  
  Projeto Maven com a mesma classe alvo e testes gerados por **LLM** (prompt + ajustes).

- `reports/`  
  Relatórios gerados (JaCoCo e PIT) para cada abordagem.
  - `reports/evosuite/...` (se aplicável)
  - `reports/llm/jacoco/...`
  - `reports/llm/pit/...`

- `tools/`  
  Ferramentas locais usadas no processo (ex.: JAR do EvoSuite).

---

## Pré-requisitos

- **Java**
  - Para rodar EvoSuite: **Java 11**
  - Para build/test do projeto: Java 11 ou 17 (dependendo do seu setup)
- **Maven**
- **Git**

> Observação: EvoSuite 1.2.0 costuma ser mais estável com **Java 8/11**.

---

## Como executar

### 1) Build e testes (Maven)

#### EvoSuite
cd evosuite
mvn -q test

#### LLM
cd llm
mvn -q test

### 2) Gerar relatórios de cobertura (JaCoCo)
(Se o pom.xml já estiver configurado com JaCoCo)

#### EvoSuite
cd evosuite
mvn -q test jacoco:report

#### LLM
cd llm
mvn -q test jacoco:report

Relatório HTML:
target/site/jacoco/index.html

### 3) Rodar mutation testing (PIT)

#### EvoSuite
cd evosuite
mvn -q pitest:mutationCoverage

#### LLM
cd llm
mvn -q pitest:mutationCoverage

Relatório HTML:
target/pit-reports/<timestamp>/index.html

## Geração de testes com EvoSuite (branch coverage)
Exemplo de comando (com classpath do Maven build):

java -jar ..\tools\evosuite-1.2.0.jar ^
  -class com.example.TriangleClassifier ^
  -projectCP target\classes ^
  -criterion BRANCH ^
  -Dsearch_budget=60

Os testes gerados ficam em evosuite-tests/ e depois podem ser copiados para:

src/test/java/

## Resultados (resumo)
### LLM
#### JaCoCo
Line coverage: ~94%
Branch coverage: ~94% (varia conforme o relatório)

#### PIT
Mutation coverage: 88% (22/25)
Test strength: 88%

Os números exatos podem ser verificados nos relatórios em reports/ ou em target/....

### Loop de melhoria (LLM + PIT)
Processo recomendado:

Rodar PIT (mvn pitest:mutationCoverage)

Identificar mutantes SURVIVED

Criar testes direcionados para matar esses mutantes

Repetir até estabilizar (ou atingir o objetivo do trabalho)

### Observações importantes
Avisos de SLF4J e “illegal reflective access” podem aparecer ao usar EvoSuite runtime.
Em geral não impedem a execução, mas podem variar conforme versão do Java.

Evite commitar arquivos temporários do Maven (target/) se não forem necessários.

## Referências
EvoSuite: geração automática de testes com busca (DynaMOSA etc.)
JaCoCo: cobertura de código para Java
PIT: mutation testing para avaliar qualidade de testes

## Autor
Ivan Borges
