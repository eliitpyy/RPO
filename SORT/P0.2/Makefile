all:exit

exit:exit.s
	as --32 -o exit.o exit.s
	ld -m elf_i386 exit.o -o exit 
clean:
	rm -vf exit *.o

run:exit
	./exit
	$(echo $?)
	ls
