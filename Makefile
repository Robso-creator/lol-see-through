create_revisions:
	@echo "-------CREATE REVISIONS -------"
	@echo ""
	@python -m src.create_revisions

pc:
	@echo "[PRE-COMMIT] All files"
	pre-commit run --all-files
