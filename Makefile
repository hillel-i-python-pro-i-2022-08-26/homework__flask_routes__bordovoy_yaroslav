.PHONY: homework-i-run
# Run homework
homework-i-run:
	@python app.py

.PHONY: homework-i-purge
homework-i-purge:
	@echo The end

.PHONY: init-dev
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	pre-commit install
