# Checklist da PoC mínima

Escopo: **uma barraca, um PDV Android e dez pulseiras**, começando com valores
fictícios. Marque os itens somente após executá-los e registrar as evidências.

## Preparação e equipamentos

- [ ] Definir responsável técnico, operador e data do teste.
- [ ] Disponibilizar um computador para servidor e um roteador com rede local dedicada.
- [ ] Disponibilizar um Android com NFC compatível e carregador.
- [ ] Confirmar as tags antes da compra: a proposta cita NTAG213, mas o guia oficial consultado lista MIFARE Ultralight AES; consultar [arquitetura e evidências](arquitetura.md).
- [ ] Validar uma tag no Android antes de adquirir as dez pulseiras. Se mantiver leitor USB, testar sua compatibilidade.

## Ambiente e configuração

- [ ] Preparar o ambiente com `make prepare` e iniciar o banco com `make db-up`.
- [ ] Instalar dependências, aplicar migrações e iniciar APIs e painel conforme [o guia do ambiente](ambiente.md).
- [ ] Instalar e conectar o app Android ao servidor pela rede local.
- [ ] Confirmar como executar a PoC sem equipamento fiscal TSE alemão.
- [ ] Configurar administrador, operador, evento, caixa e três produtos de teste.
- [ ] Confirmar suporte a BRL e valores com centavos.

## Execução e aceite

- [ ] Cadastrar dez pulseiras e demonstrar recarga, consulta de saldo, venda e reembolso.
- [ ] Testar saldo insuficiente e duplo toque/reenvio, verificando que não há cobrança duplicada.
- [ ] Testar separadamente queda da internet e perda da conexão com o servidor; registrar o comportamento real.
- [ ] Fazer backup e comprovar restauração em banco separado.
- [ ] Conciliar os lançamentos e registrar resultados, limitações e decisão de continuidade.

**Aceite mínimo:** as dez pulseiras funcionam, o ciclo financeiro fecha sem
diferença de centavos e não há perda ou duplicação de transações. Vendas sem
conexão ao servidor precisam ser demonstradas antes de serem prometidas.
Use o [roteiro de validação](validacao.md) para os cenários e o registro de evidências.

PIX automático, tradução completa, quiosques e expansão para várias barracas
podem ficar para uma etapa posterior. Esta checklist reduz o primeiro ensaio;
o [plano da PoC](plano-poc.md) mantém o escopo mais amplo do piloto.
