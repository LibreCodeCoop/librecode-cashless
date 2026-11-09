# Validação do piloto

Execute com dados fictícios e ambiente isolado. Nenhum cenário abaixo foi
executado pela criação deste repositório. Registre data, operador, SHA, app,
hardware, rede, entradas, resultado e evidência para cada teste.

| ID | Cenário | Critério de aceite proposto |
| --- | --- | --- |
| V01 | Ler e cadastrar dez tags no Android selecionado | Todas lidas e vinculadas à conta correta; tag desconhecida rejeitada |
| V02 | Recarregar R$ 80, vender R$ 22 + R$ 18 + R$ 25, reembolsar R$ 15 | Saldo final zero e lançamentos conciliados com os mesmos valores |
| V03 | Saldo insuficiente, duplo toque/reenvio e pedidos concorrentes em dois PDVs | Sem débito duplicado, saldo indevido ou venda aprovada além do permitido |
| V04 | Cortar somente WAN, mantendo servidor e Wi-Fi local | Fluxo local demonstrado; identificar o que depende de serviço externo |
| V05 | Perder conexão entre PDV e servidor e tentar cinco vendas | Observar suporte real; nenhuma confirmação falsa ou perda/duplicação; se não suportado, bloquear meta de venda offline |
| V06 | Reiniciar backend durante operação | Reconciliação entre operações confirmadas e banco sem perda/duplicação |
| V07 | Gerar 50 transações/minuto por dez minutos | Registrar sucesso/erro e p50/p95/p99; meta proposta p95 < 1 s, do toque à confirmação |
| V08 | Atualizar painel sob carga | Totais conciliados e atraso medido; meta proposta < 1 s, ainda a demonstrar |
| V09 | Perder/bloquear/substituir pulseira | Conta e saldo preservados; pulseira bloqueada não autoriza novas vendas |
| V10 | Fazer backup e restaurar em banco separado | Lançamentos e saldos conferidos; documentar tempo de restauração e janela de perda |
| V11 | Operador sem permissão e chamadas sem autenticação | Operações administrativas e financeiras protegidas; trilha de autoria |
| V12 | Piloto de quatro horas com dez participantes | Recarga/venda/reembolso conciliados, incidentes e feedback registrados |

As metas de tempo são critérios propostos para homologação, não medições já
obtidas. Divergência de centavos, duplicação ou perda de lançamento bloqueia
avanço. A meta offline só pode ser aceita com teste que cubra desconexão da API
e concorrência entre terminais.

O teste de reinício não substitui ensaio de queda de energia. Qualquer ensaio
destrutivo deve usar uma instalação descartável, fora do piloto com participantes.
Para backup, a planilha propõe intervalo de quinze minutos; definir destino,
retenção e responsáveis e comprovar restauração antes do evento.

## Registro de resultado

Copie para o relatório do ensaio e preencha:

```text
Cenário / data / responsável:
Revisão backend e versão app:
Hardware/tag/rede/configuração:
Entradas e passos:
Resultado esperado / resultado observado:
Lançamentos, métricas e evidências:
Status: aprovado / falhou / bloqueado / não executado
Pendências e decisão:
```

A decisão final deve indicar critérios atendidos, bloqueios e escopo autorizado
para a próxima etapa. Uma alteração de escopo (por exemplo, operar apenas com
LAN disponível) deve ficar explícita na decisão.
