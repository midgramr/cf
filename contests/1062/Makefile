SHELL = /bin/sh
.SUFFIXES:

CXX = g++-15
CXXFLAGS = -std=c++23 -Wall -Wextra -Wno-psabi -Wno-sign-compare
BUILDDIR = build

.PHONY: all makebuild clean

all:
	echo 'No default target. Please provide a file to compile'

%: %.cpp | makebuild
	$(CXX) $(CXXFLAGS) $< -o $(BUILDDIR)/$@

makebuild:
	mkdir -p $(BUILDDIR)

clean:
	-rm -rf $(BUILDDIR)/*
