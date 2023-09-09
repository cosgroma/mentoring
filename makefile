
# Create md files from json files
JSON_FILES := $(wildcard data/*.json)
MD_FILES := $(patsubst data/%.json, plans/%.md, $(JSON_FILES))
DOCX_FILES := $(patsubst plans/%.md, plans/%.docx, $(MD_FILES))

.PHONY: all clean info-json info-md

all: plans $(JSON_FILES) $(MD_FILES) $(DOCX_FILES)

plans/%.md: data/%.json
	@echo "Generating $@ from $<"
	python generate_plan.py $< $@

clean:
	rm -f plans/*.md
	rm -f plans/*.docx

# generate docx files from md files
plans/%.docx: plans/%.md
	@echo "Generating $@ from $<"
	pandoc $< -o $@ 

plans:
	mkdir -p plans

info-json:
	@echo "JSON Data to be run =>"
	@for s in $(JSON_FILES); do \
		echo $$s;\
	done;

info-md:
	@echo "MD Data to be generated =>"
	@for s in $(MD_FILES); do \
		echo $$s;\
	done;