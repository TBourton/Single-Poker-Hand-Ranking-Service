requirements:
	rm requirements.txt | true
	pip-compile --no-emit-find-links --no-emit-index-url requirements.in -o requirements.txt
	rm dev-requirements.txt | true
	pip-compile --no-emit-find-links --no-emit-index-url dev-requirements.in -o dev-requirements.txt

.PHONY: requirements
