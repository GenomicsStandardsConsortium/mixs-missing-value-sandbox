RUN=poetry run

src/data/valid/MixsCompliantData-001-report.txt: src/data/valid/MixsCompliantData-001.yaml \
src/mixs_missing_value_sandbox/schema/mixs_missing_value_sandbox.yaml
	$(RUN) linkml-validate \
		--schema $(word 2,$^) \
		--target-class $(shell echo $(basename $(notdir $(word 1,$^))) | cut -d'-' -f1) \
		$(word 1,$^) > $@

src/data/valid/MixsCompliantData-001.tsv: src/data/valid/MixsCompliantData-001.yaml \
src/mixs_missing_value_sandbox/schema/mixs_missing_value_sandbox.yaml
	$(RUN) linkml-convert --schema $(word 2,$^) \
		--output $@ \
		--index-slot mims_soil_data $(word 1,$^)
