# Contribuição

Documentação e discussões desta PoC usam português brasileiro. Preserve os
documentos originais na raiz. Para atualizar os CSVs após uma mudança na planilha,
execute `make export-plan` e revise o diff; não edite CSVs gerados à mão.

Execute `make check` antes de propor alterações. Se alterar o Compose, gere a
configuração com `make config` e valide com `docker compose config --quiet`.
Não versione `.local/`, credenciais, dados de participantes ou dumps do banco.

Para modificar backend, web ou Android, crie uma branch/fork de trabalho do
StuStaPay a partir do SHA em `upstream.ref`, fora do checkout de referência.
Siga as instruções e testes daquele projeto. Registre aqui o fork, a revisão,
a motivação e as evidências antes de atualizar a referência de integração.

Ao atualizar `upstream.ref`, revise a documentação e o ambiente: versões, schema,
CLI, hardware NFC e integrações podem mudar. A preparação recusa trocar
automaticamente um checkout existente de outra revisão, preservando trabalho local.

Use commits focados, como `docs: documentar teste de recarga`. Descreva nas
propostas o resultado esperado, a verificação executada e as limitações.
