# Protocolo prospectivo de comparação — rascunho, sem novas execuções

[English](PROTOCOL.md) · [Resultados arquivados](RESULTS.pt-BR.md)

**Estado:** desenho de um experimento futuro. O exercício de fevereiro com uma
classe é evidência histórica; não foi usado para escolher configurações
vencedoras. Congelar protocolo versionado e manifesto de execução **antes** de
gerar novas suítes. Qualquer mudança posterior deve ser rotulada e separada
dos resultados confirmatórios.

## Perguntas e abordagens

1. Com orçamentos registrados, como EvoSuite e LLM *sem refinamento* se
   comparam nos mesmos alvos Java e conjunto fixo de mutantes?
2. Quanto uma rodada de feedback PIT previamente definida altera cada
   abordagem? Analisar as versões refinadas separadamente.

Não resumir "LLM + PIT + edições humanas" como "LLM". Registrar quem fez cada
ajuste. Se o EvoSuite não puder receber intervenção comparável, tratar a
segunda pergunta como descritiva, sem atribuição causal.

| Antes de executar | Regra a registrar e congelar |
|---|---|
| Alvos | `TriangleClassifier` e pelo menos duas classes Java pequenas adicionais, escolhidas por variedade de fluxo **antes dos novos resultados**; registrar hash da fonte, especificação/testes e exclusões. Não escolher pelo vencedor. |
| Repetições | Planejar cinco gerações independentes por abordagem e alvo, se viável; registrar sementes e falhas. Se faltar recurso, reduzir o escopo no protocolo congelado antes de rodar. Cinco execuções de uma classe não são cinco sistemas independentes. |
| EvoSuite | Fixar Java, JAR, runtime, Maven, critério, orçamento, parada e semente. Guardar comando completo, log, suíte e tempo de geração. Os 60 segundos no README antigo são um exemplo, não configuração histórica verificada. |
| LLM | Registrar provedor/modelo/versão, acesso, prompt, temperatura/top-p/semente quando expostos, limites de tokens, resposta, consumo/custo, tempo e edições humanas. Mesma especificação e contrato de saída em todas as repetições. Se serviço ou preço não forem fixáveis, relatar o limite antes da execução. |
| Refinamento | Definir previamente no máximo uma rodada de feedback PIT por abordagem, dados permitidos, tempo máximo e responsável pelos ajustes. Salvar suítes e relatórios inicial/final. Não chamar escore final de qualidade do gerador bruto. |
| Build e métricas | Mesmos bytes do alvo, versões JUnit/JaCoCo/PIT, classes mutadas, mutadores, compilador/runtime e timeout. Preservar falhas e suítes que não compilarem, sem descartá-las do denominador. |
| Mutantes | Registrar gerados, mortos, sobreviventes, sem cobertura, timeout e excluídos. Informar cobertura de mutação e test strength com denominadores. Revisar supostos equivalentes independentemente e separar valores brutos dos ajustados; não removê-los conforme conveniência. |
| Avaliação humana | Se alegar legibilidade/manutenção, definir rubrica, avaliadores cegos e concordância. Caso contrário, não alegar. |

## Análise e comunicação

A unidade de análise é a **classe alvo**; gerações repetidas ficam dentro dela.
Apresentar cada classe e repetição, diferenças pareadas de mutantes mortos por
alvo e sua dispersão, junto de branches JaCoCo, sucesso de compilação, número
de testes, tempo de geração/refinamento e custo registrado. Contagens de
execução selecionadas pelo PIT não medem produtividade nem amostras
independentes. Com poucas classes, relatar amplitudes descritivas, sem alegar
superioridade geral ou precisão artificial de bootstrap por linha.

Usar o mesmo snapshot de cada alvo em todas as abordagens. Alterações no
bytecode, versão/configuração do PIT podem mudar o conjunto de mutantes e
tornar percentuais incomparáveis; verificar igualdade antes de interpretar.
Não usar feedback PIT para ajustar uma abordagem apresentada como "sem
refinamento". Guardar manifestos, prompts, respostas, suítes Java, logs e
agregados com hashes. Revisar se prompts/código incluem informação privada
antes da publicação.

## Condições para começar

A geração histórica não pode ser plenamente reproduzida: o relatório histórico identifica ChatGPT 5.2 Thinking,
mas faltam configurações completas da sessão, sementes e tempo de edição humana. Em uma nova rodada, primeiro
selecionar e congelar alvos, modelo/configuração, orçamento e ferramentas;
depois executar o protocolo. Este texto não autoriza API paga nem afirma que
os novos alvos ou repetições já foram executados.
