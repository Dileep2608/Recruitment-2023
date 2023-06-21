section .data
    num1    dd 120
    num2    dd 48
    result  dd 0

section .text
    global _start

_start:
    ; Multiply the numbers
    mov eax, dword [num1]
    mov ebx, dword [num2]
    imul eax, ebx
    mov dword [result], eax

    ; Exit the program
    mov eax, 1
    xor ebx, ebx
    int 0x80
