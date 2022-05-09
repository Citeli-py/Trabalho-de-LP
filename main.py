# função: tipo nome(args,...)
# atrib: tipo nome=valor;
import os
def format(lines):
    while '' in lines:
        lines.remove('')
    return lines

def union(lines):
    code=''
    for line in lines:
        code += line
    return code

def format_spaces(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].replace(' ','')
    return lines

def get_lib(line): # Considerando um código sem erros
    try:
        lib = line.split('<')[1][:-1]
    except:
        try:
            lib = line.split('\"')[1]
        except:
            pass
    return lib

def format_define(line):
    aux = format(line.split(' '))
    if len(aux)>3:
        for i in range(len(aux[3:])):
            aux[2] += ' ' + aux[i+3]
    return (aux[1], aux[2])

def format_macros(line):
    #define SOMA(a,b) (a+b)
    aux = line.split(' ')
    if '(' in aux[1]:
        func = aux[1].split('(')[0]
        param = aux[1].split('(')[1][:-1]
        inst = ''
        for i in range(len(aux[2:])):
            inst += aux[i+2]+' '

        return (func, param, inst[:-1])
    return ''

def get_defines(lines):
    defines=list()
    define =''
    for line in lines:
        if "#define" in line:
            define = format_define(line)
            defines.append(define)
    return defines

def get_macros(lines):
    macros=list()
    macro =''
    for line in lines:
        if "#define" in line:
            macro = format_macros(line)
            macros.append(macro)
    return format(macros)

def get_libs(lines):
    libs=list()
    lib =''
    for line in lines:
        if "#include" in line:
            lib = get_lib(line)
            libs.append(lib)
    return format_spaces(libs)

def include_libs(code, libs):
    for lib in libs:
        code = code.replace(lib, '')

    for lib in libs:
        f = union(read("include/"+lib))
        code = f + code
    return code

def rmv_comments(lines):
    for i in range(len(lines)):
        aux = lines[i].find('//')
        if aux>=0:
            lines[i] = lines[i][:aux]
    return lines

def rmv_larger_comments(code):
    codes = code.split('/*')
    code = ''
    for word in codes:
        aux = word.find('*/')
        if aux > 0:
            code+= word[aux+2:] # aux+2 pois a posição do */ é index-2
        else:
            code += word
    return code

def rmv_spaces(code):
    markers = [';', ',', '{', '}', '(', ')', '[', ']', '=']
    code_aux = ''
    for i in range(len(code)):
        if not(code[i] == ' ' and (code[i-1] in markers or code[i+1] in markers)):
            code_aux += code[i]

    return code_aux

def rmv_libs(lines):
    for i in range(len(lines)):
        if '#include' in lines[i]:
            lines[i] = ''
    return format(lines)

def rmv_defines(lines):
    for i in range(len(lines)):
        if '#define' in lines[i]:
            lines[i] = ''
    return format(lines)

def rmv_tab(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].replace('  ','')
    return lines

def rmv_enter(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
    return format(lines)

def rmv_enter_code(code):
    while code.find('\n')>=0:
        code = code.replace('\n', '')
    return code

def put_macros(lines, macros):
    #(func, param, inst)
    for i in range(len(lines)):
        inst = ''
        for macro in macros:
            if macro[0] in lines[i]:
                aux = lines[i].split('(')[1][:lines[i].index(')')]
                param = '('+aux

                aux = aux.split(',')
                aux[-1] = aux[-1][:-2]

                params = macro[1].split(',')
                inst = macro[2]
                for j in range(len(params)):
                    inst = inst.replace(aux[j], params[j])

                lines[i] = lines[i].replace(macro[0]+param, inst+';')
    return lines

def put_defines(lines, defines):
    for i in range(len(lines)):
        for define in defines:
            lines[i] = lines[i].replace(define[0], define[1])
    return lines

def read(file):
    try: #Necessário pois há incompatibilidade entre o interpretador do windows com o que eu uso no VScode
        os.chdir(os.path.dirname(__file__))
    except Exception:
        pass
    with open(file) as f:
        lines = f.readlines()
    return lines

lines = read(input('Digite o arquivo .c: '))
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
code = include_libs(code, libs)
code = rmv_larger_comments(code)
code = rmv_spaces(code)
code = rmv_enter_code(code)
print(code)
