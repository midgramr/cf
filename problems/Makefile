SHELL = /bin/sh
.SUFFIXES:

.PHONY: all makebuild clean

CXX = g++-15
CXXFLAGS = -std=c++23 -Wall -Wextra -Wno-psabi
BUILDDIR = build
TARGETS := $(basename $(wildcard *.cpp))

all: $(TARGETS)

%: %.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

clean:
	-rm -f $(TARGETS)
