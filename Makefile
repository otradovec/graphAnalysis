main:
	make clean
	chmod 774 `ls src/*.py`
	cp src/information.py information
	cp src/fusion.py fusion
	cp src/distribution.py distribution
	cp src/power.py power
	cp src/reset.py reset
	cp src/weakness.py weakness
	cp src/avltree.py avltree
clean:
	rm -f information fusion distribution power reset weakness avltree
	rm -f xotradov.zip
	rm -rf src/__pycache__
zip:
	unoconv -f pdf report.odt
	zip xotradov.zip Makefile src/* report.pdf
