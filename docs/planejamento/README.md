# Planilha em formato versionável

Os nove CSVs desta pasta são extraídos de
`Plano_PoC_StuStaPay_Cashless_OpenSource(1).xlsx`, preservada na raiz.
Execute `make export-plan` para regenerar; `make check` compara a exportação
com os arquivos versionados.

Formato: UTF-8, vírgula como separador e valores de células na ordem original.
Células vazias intermediárias são preservadas. Estilos, imagens, comentários,
validações e fórmulas não são transportados; fórmulas usam o último resultado
armazenado no XLSX, sem recálculo. Datas e percentuais permanecem nos valores
brutos da planilha. Linhas de apresentação não viram automaticamente cabeçalhos
ou tarefas. Consulte as divergências técnicas em [arquitetura](../arquitetura.md)
e o resumo de custos em [plano da PoC](../plano-poc.md).
