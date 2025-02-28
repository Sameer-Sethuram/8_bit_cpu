# General Things to Note for using the CPU

Make sure to load the image file into the instuction memory and the data memory before running the circuit. It doesn't really work otherwise because how else is it going to read instructions and pull data from memory?
The timing of this circuit is a little bit off because matching rising and falling edge instructions proved to be a little bit difficult, so if something isn't updating immediately, give it a few more iterations through the instruction memory and you should have your final result.
Any combination of hexadecimal instructions (from 00-FF) is an instruction. Because this is an 8-bit CPU, we intended to fit as many instructions in it as possible. As such, each instruction is a byte, the first two bits representing the OP code, the second two representing the destination register, the third two representing the first register to be used, and the last two reprenting the second register to be used.
This circuit relies on 4 registers.
For the STR instruction, the second two bits that are supposed to be representative of the destination register are actually representing what data you are going to store into memory. The other two registers we use are supposed to add up to the address that you want to store the data in memory.
Similarly, for the LDR instruction, the two registers used as the last 4 bits of the instruction add up to the address from memory that you want to load the data from. The destination register is the register that you will load that data into.
