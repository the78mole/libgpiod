# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: 2022 Bartosz Golaszewski <brgl@bgdev.pl>

EXTRA_DIST = \
	MANIFEST.in \
	setup.py

if WITH_TESTS

BUILD_TESTS = 1

endif

all-local:
	GPIOD_WITH_TESTS=$(BUILD_TESTS) \
	$(PYTHON) setup.py build_ext --inplace \
		--include-dirs=$(top_srcdir)/include/:$(top_srcdir)/tests/gpiosim/ \
		--library-dirs=$(top_builddir)/lib/.libs/:$(top_srcdir)/tests/gpiosim/.libs/

install-exec-local:
	GPIOD_WITH_TESTS= \
	$(PYTHON) setup.py install --prefix=$(DESTDIR)$(prefix)

SUBDIRS = gpiod

if WITH_TESTS

SUBDIRS += tests

endif

if WITH_EXAMPLES

SUBDIRS += examples

endif
