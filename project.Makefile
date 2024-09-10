RUN=poetry run

src/data/valid/MixsCompliantData-001-report.txt: src/data/examples/valid \
src/mixs_missing_value_sandbox/schema/mixs_missing_value_sandbox.yaml
	$(RUN) linkml-validate \
		--schema $(word 2,$^) \
		--target-class $(shell echo $(basename $(notdir $(word 1,$^))) | cut -d'-' -f1) \
		$(word 1,$^) > $@

src/data/valid/MixsCompliantData-001.tsv: src/data/examples/valid \
src/mixs_missing_value_sandbox/schema/mixs_missing_value_sandbox.yaml
	$(RUN) linkml-convert --schema $(word 2,$^) \
		--output $@ \
		--index-slot mims_soil_data $(word 1,$^)

assets/compare_mims_and_soil_slots.txt:
	poetry run python src/scripts/compare_mims_and_soil_slots.py > $@

assets/ranges_of_requireds_of_combination.txt:
	poetry run python src/scripts/ranges_of_requireds_of_combination.py > $@