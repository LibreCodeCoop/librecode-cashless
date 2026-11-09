# LibreCode Cashless

Base de implantação e validação de uma prova de conceito (PoC) de pagamentos
com pulseiras NFC para feiras e eventos, baseada no **StuStaPay**.

O piloto proposto nos materiais é de **1 barraca, 1 PDV Android e 10 pulseiras**,
em quatro semanas. Este repositório reúne o planejamento, prepara um banco local
e obtém uma revisão fixa do sistema original. O backend, os painéis web e o app
Android são desenvolvidos no StuStaPay; ainda não foram adaptados ou homologados
para o piloto brasileiro.

## Começar

Requisitos: Git, Bash, Python 3.11+, Make, Docker com Compose v2+, `uv` e
Node.js 22+ (conferir também os requisitos da revisão do upstream).

```sh
make prepare    # gera segredos locais e baixa o StuStaPay na revisão fixada
make db-up      # inicia somente o PostgreSQL, em 127.0.0.1:5433
```

Depois siga [o guia do ambiente](docs/ambiente.md) para instalar dependências,
aplicar migrações e executar as APIs e interfaces originais.
`make help` lista os comandos. `make check` valida os arquivos desta base sem
iniciar serviços ou acessar a rede.

## Conteúdo

| Caminho | Conteúdo |
| --- | --- |
| [docs/arquitetura.md](docs/arquitetura.md) | Arquitetura conferida e divergências dos materiais |
| [docs/plano-poc.md](docs/plano-poc.md) | Escopo, cronograma e decisões pendentes |
| [docs/validacao.md](docs/validacao.md) | Cenários e critérios de aceite do piloto |
| [docs/glossario.md](docs/glossario.md) | Vocabulário inicial PT-BR/EN |
| [docs/planejamento](docs/planejamento) | Nove abas da planilha exportadas para CSV |
| [docs/fontes.md](docs/fontes.md) | Documentos originais e fontes técnicas |
| `compose.yaml` | Banco de desenvolvimento local; não é deploy completo |
| `scripts/` | Preparação, exportação e verificações locais |
| `upstream.ref` | Commit do StuStaPay usado como referência reproduzível |
| `.local/` | Checkout do upstream e configurações privadas, ignorados pelo Git |

## Estado da PoC

Os documentos de apresentação contêm premissas ainda não demonstradas. Em
particular, a documentação NFC da revisão consultada indica **MIFARE Ultralight
AES**, enquanto a proposta lista NTAG213. Compatibilidade do leitor ACR1222L,
venda sem conexão ao servidor, desativação de TSE, moeda BRL, PIX e localização
PT-BR precisam de validação. A perda da internet e a perda da rede local são
cenários distintos. Os detalhes e evidências estão em
[arquitetura](docs/arquitetura.md).

## Contribuir

Consulte [CONTRIBUTING.md](CONTRIBUTING.md). Alterações no sistema original devem
ser desenvolvidas em um fork/branch próprio do StuStaPay, preservando sua licença
e autoria; este repositório mantém a integração e a documentação do piloto.

Código novo desta base: AGPL-3.0-or-later, conforme [LICENSE](LICENSE).
Os materiais de referência são preservados com sua autoria original; sua inclusão
não altera os direitos de terceiros.
