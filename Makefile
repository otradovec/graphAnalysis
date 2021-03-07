main:
	make clean
	chmod 774 src/information.py
	cp src/information.py information
	chmod 774 src/fusion.py
	cp src/fusion.py fusion
	chmod 774 src/distribution.py
	cp src/distribution.py distribution
clean:
	rm -f information
	rm -f fusion
	rm -f distribution
	rm -f xotradov.zip
	rm -rf src/__pycache__
zip:
	unoconv -f pdf report.odt
	zip xotradov.zip Makefile src/* report.pdf
