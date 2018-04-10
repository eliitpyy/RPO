all:maximum

maximum:maximum.s
	as --32 maximum.s -o maximum.o
	ld -m elf_i386 maximum.o -o maximum 
clean:
	rm -vf maximum *.o

run:maximum
	./maximum



