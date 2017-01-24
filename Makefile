
GIT_PATH := $(shell which git)
BIN_DIR  := $(shell dirname $(GIT_PATH))
BIN_DIR  := /usr/local/bin
PLUGIN   = ./git-annotator

all:
	@echo "Usage: sudo make [install|uninstall]"

install:
	test -w $(BIN_DIR)
	install -d -m 0755 $(BIN_DIR)
	install -m 0755 $(PLUGIN) $(BIN_DIR)

uninstall:
	test -d $(BIN_DIR) && \
	cd $(BIN_DIR) && \
	rm -f $(PLUGIN)
