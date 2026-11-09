.PHONY: help prepare config upstream db-up db-stop db-status export-plan check
help:
	@printf '%s\n' 'prepare: gerar configuração e obter upstream fixado' 'config: gerar segredos locais (não sobrescreve)' 'upstream: obter StuStaPay em .local/stustapay' 'db-up: iniciar banco local' 'db-stop: parar banco, preservando volume' 'db-status: consultar banco' 'export-plan: exportar XLSX para CSV' 'check: verificar sintaxe, links e exportação'
prepare: config upstream
config:
	python3 scripts/init_config.py
upstream:
	bash scripts/prepare-upstream.sh
db-up: config
	docker compose up -d --wait postgres
db-stop:
	docker compose stop postgres
db-status:
	docker compose ps
export-plan:
	python3 scripts/export_plan.py
check:
	bash -n scripts/prepare-upstream.sh
	python3 scripts/check.py
