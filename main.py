from pre_processamento import *

#lines = read(input('Digite o arquivo .c: '))
lines = read("teste.c")
lines = rmv_enter(lines)
lines = rmv_comments(lines)
lines = rmv_tab(lines)

macros = get_macros(lines)
libs = get_libs(lines)
defines = get_defines(lines)

lines = put_macros(lines, macros)
lines = put_defines(lines, defines)
lines = rmv_defines(lines)
lines = rmv_libs(lines)

code = union(lines)
#code = include_libs(code, libs)
code = rmv_larger_comments(code)
code = rmv_spaces(code)
code = rmv_enter_code(code)
print(code)
