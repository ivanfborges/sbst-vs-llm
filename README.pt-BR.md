# EvoSuite × testes com apoio de LLM: um estudo de caso Java

[English](README.md) · [README acadêmico original](docs/ACADEMIC-ORIGINAL.pt-BR.md)

Estudo prático de uma disciplina da pós-graduação em Engenharia de Software.
Duas suítes testam a **mesma** classe `TriangleClassifier`: uma gerada pelo
EvoSuite e outra criada com apoio de LLM e depois refinada com feedback de
mutações do PIT. A classe alvo tem os mesmos bytes nos dois projetos Maven.

**Resultado arquivado:** ambas cobriram 17/18 branches no JaCoCo. A suíte
EvoSuite matou 16/25 mutantes PIT; a suíte final com LLM matou 22/25. Esses
números descrevem **uma classe e uma execução registrada por abordagem**.
A suíte com LLM recebeu refinamento adicional após observar o PIT. O relatório acadêmico identifica **ChatGPT 5.2 Thinking**, mas faltam
configurações da sessão, detalhes de acesso e esforço humano suficientes
para reproduzir a geração ou comparar custos.

| Comece por | Conteúdo |
|---|---|
| [Resultados auditados e limites](docs/RESULTS.pt-BR.md) | Números ligados a Surefire, JaCoCo e PIT; divergência entre cópias explicada |
| [Protocolo para um estudo futuro](docs/PROTOCOL.pt-BR.md) | Desenho prévio, metadados necessários e limites de comparação; sem alegar novos experimentos |
| [Auditoria estruturada](docs/archive-audit.json) | Agregados extraídos por um [script da biblioteca padrão](scripts/audit_archive.py) |
| [Atividade e relatório originais](evidencias/README.md) | Enunciado, prompts, código, logs, capturas, PDF e DOCX preservados |

## Conferir as evidências existentes

Python 3.11 ou posterior; apenas biblioteca padrão:

```sh
python scripts/audit_archive.py
```

O script lê os arquivos versionados. Confere hash da classe alvo, contagens
Surefire, JaCoCo e PIT, e confronta as execuções do log PIT com o XML
correspondente. Não executa Java, EvoSuite, LLM ou experimento novo. Compare a
saída com `docs/archive-audit.json`.

Há dois projetos Maven e logs históricos. Para verificar localmente se os
testes **atuais** compilam e passam, use Java 11 e Maven:

```sh
cd evosuite && mvn test
cd ../llm && mvn test
```

Esses comandos criam artefatos locais; não recriam a busca original do EvoSuite
nem a geração pelos prompts. Leia os [limites](docs/RESULTS.pt-BR.md) antes de
interpretar novas execuções de cobertura ou mutação. Dependências originais
estão nos `pom.xml`; nenhum lock novo foi introduzido.

## Escopo e autoria

O [enunciado](evidencias/01-enunciado/enunciado.txt), os
[prompts e respostas](evidencias/04-llm/01-prompts/), os
[projetos Java](evosuite/) e a [suíte LLM](llm/) continuam disponíveis. O
relatório acadêmico é preservado como histórico. Esta revisão do portfólio
audita evidências e restringe conclusões, sem atribuir configurações da sessão,
esforço de revisão ou superioridade causal não registrados. A próxima fase
experimental depende de modelo/configuração documentados e protocolo prospectivo.
