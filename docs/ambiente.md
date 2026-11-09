# Ambiente local

Esta base segue o fluxo de desenvolvimento original: PostgreSQL em container,
APIs Python e interfaces web executadas no host. Não provisiona o evento completo.
Use apenas dados fictícios até concluir a homologação.

## Preparação

Na raiz, com Git, Bash, Make, Python 3.11+, Docker/Compose, uv e Node.js 22+:

```sh
make prepare
make db-up
```

`prepare` obtém o commit de `upstream.ref` via HTTPS em `.local/stustapay`, em
HEAD destacado. A primeira execução exige rede. A execução seguinte preserva o
checkout e as configurações; não faz pull nem descarta alterações.

Os arquivos `.local/config.yaml` e `.local/postgres.env` contêm segredos aleatórios
com permissão 0600. Não os publique. Não regenere a senha de uma instalação com
volume existente sem também planejar sua alteração no PostgreSQL.

O PostgreSQL 14 acompanha o Compose de desenvolvimento da revisão consultada.
O banco é publicado apenas em `127.0.0.1:5433` e persiste em volume Docker.
Se essa porta estiver ocupada, pare e ajuste a configuração e o Compose em conjunto.

## Backend

```sh
cd .local/stustapay
uv sync
uv run stustapay -c ../config.yaml db migrate
uv run stustapay -c ../config.yaml administration-api
```

Em outros terminais, a partir da mesma pasta:

```sh
uv run stustapay -c ../config.yaml terminalserver-api
uv run stustapay -c ../config.yaml customerportal-api
```

As portas configuradas são 8081 (administração), 8082 (portal) e 8083 (terminais).
Verifique as opções com `uv run stustapay --help`. Dependências nativas do sistema
podem ser necessárias; consulte a documentação do upstream e suas instruções
para Debian. Não use `db reset` ou `db rebuild` para iniciar um banco com dados.

## Interfaces web e configuração inicial

```sh
cd .local/stustapay/web
npm ci
npx nx serve administration
```

Para o portal, execute `npx nx serve customerportal` em outro terminal na mesma
pasta. Use os endereços exibidos pelo Nx; as portas da API não são as portas das
interfaces web. Siga as instruções originais para configurar administrador,
evento, produtos, caixas e terminais. O simulador do upstream é uma opção para
gerar dados de teste; revise suas operações antes de usá-lo.

## Android e acesso pela rede do piloto

Abra `.local/stustapay/app` no Android Studio, conforme o guia original.
Valide primeiro NFC integrado e tags suportadas. O leitor USB proposto ainda
precisa ser homologado. Não há uma flag `--without-tse` implementada nesta base.

O modelo inicial vincula APIs a localhost. Para testes no tablet, revise o campo
`host` do terminalserver, seu `base_url` e os endereços do frontend para o IP do
servidor na LAN. Restrinja o acesso à rede dedicada e configure TLS/proxy antes
de qualquer exposição externa. O PostgreSQL deve continuar restrito ao host.

## Parar e verificar

Na raiz:

```sh
make db-status
make db-stop
make check
docker compose config --quiet
```

`db-stop` preserva os dados. A remoção de volumes não faz parte dos comandos
automatizados. Backup e restauração em banco separado são requisitos do piloto
descritos em [validação](validacao.md); não estão automatizados nesta etapa.
