CC = gcc
outfile = karatsuba
CFlags = -c
karatsuba: compile
	$(CC) karatsuba.o main.o -o $(outfile)
compile: main.c karatsuba.c karatsuba.h
	$(CC) $(CFlags) karatsuba.c main.c
clean: karatsuba.o main.o
	rm *.o
