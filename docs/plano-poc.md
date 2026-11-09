# Plano da prova de conceito

Objetivo: avaliar StuStaPay para uma feira com um posto de venda Android,
uma barraca e dez participantes/pulseiras. Duração proposta: quatro semanas
(20 dias úteis), precedidas de preparação. Todas as tarefas seguem planejadas;
criar esta base não equivale a concluir a implantação.

## Sequência

| Etapa | Entregas | Condição de avanço |
| --- | --- | --- |
| Semana 0 | Evento e equipe definidos, orçamento reconciliado, hardware escolhido, revisão upstream fixada | Resolver as divergências de NFC e modo de operação |
| Semana 1 — T1.1–T1.5 | Ambiente, banco, APIs, painel, build Android e smoke test | Login e cadastro de produto demonstrados |
| Semana 2 — T2.1–T2.6 | Evento/produtos, dez tags, configuração do terminal, vocabulário e tradução essencial | Fluxo NFC → conta → consulta de saldo validado |
| Semana 3 — T3.1–T3.6 | Recarga/venda/reembolso, quedas, reinício, carga e triagem | Evidências de integridade e limitações documentadas |
| Semana 4 — T4.1–T4.6 | Treinamento, piloto de quatro horas, coleta e relatório | Decisão go/no-go baseada nos critérios de aceite |

Os IDs, responsáveis, durações, dependências e status originais estão nos
[CSVs exportados](planejamento). São documentação local; nenhuma issue ou epic
foi criada no GitHub. A planilha original permanece a fonte para reexportação.

## Escopo e decisões

O fluxo principal é cadastrar a pulseira/conta, recarregar, consultar saldo,
vender e devolver o restante. Tradução essencial PT-BR, treinamento, auditoria
e validação de falhas fazem parte do plano. Fiscal brasileiro, PIX automático,
quiosque self-service e expansão para centenas de bancas ficam para outra etapa.

Antes do piloto:

- Confirmar tags suportadas e funcionamento no dispositivo escolhido; validar o leitor USB se mantido.
- Confirmar suporte a moeda BRL, precisão dos valores e formato monetário.
- Demonstrar a configuração sem TSE ou registrar o impedimento.
- Testar operação sem WAN e sem LAN/API; ajustar o escopo se venda offline não for suportada.
- Definir meio de recarga/reembolso simulado e responsável pela conciliação.
- Registrar versão do app, backend, firmware/tag e configuração em cada ensaio.

## Custos e riscos

O resumo da planilha fala em R$ 8–12 mil, mas a aba de custos totaliza
**R$ 48.739,50**, incluindo R$ 34.840 de mão de obra, R$ 8.755 de hardware,
R$ 135 de software/hospedagem, R$ 650 operacionais e R$ 4.359,50 de reserva.
São valores do documento, não cotações atualizadas. A referência de leitores
também diverge: duas unidades no custo e menção a sobressalente. Reconciliar
escopo, quantidades e orçamento antes de adquirir equipamentos.

Prioridades: compatibilidade NFC; dependência da rede local; integridade de saldo;
backup/restauração; configuração TSE; treinamento e tradução; bateria e energia.
A aba de riscos original inclui hipóteses técnicas que ainda precisam da
validação em [arquitetura](arquitetura.md). Use [o roteiro de aceite](validacao.md)
para registrar o que foi demonstrado, falhou ou foi bloqueado.
