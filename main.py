# função: tipo nome(args,...)
# atrib: tipo nome=valor;

def format(lines):
    while '' in lines:
        lines.remove('')
    return lines

def format_spaces(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].replace(' ','')
    return lines

def get_lib(line): # Considerando um código sem erros
    try:
        lib = line.split('<')[1][:-1]
    except:
        try:
            lib = line.split('\"')[1][:-1]
        except:
            pass
    return lib

def format_define(line):
    aux = format(line.split(' '))
    if len(aux)>3:
        for i in range(len(aux[3:])):
            aux[2] += ' ' + aux[i+3]
    return (aux[1], aux[2])

def get_defines(lines):
    defines=list()
    define =''
    for line in lines:
        if "#define" in line:
            define = format_define(line)
            defines.append(define)
    return defines

def get_libs(lines):
    libs=list()
    lib =''
    for line in lines:
        if "#include" in line:
            lib = get_lib(line)
            libs.append(lib)
    return format_spaces(libs)

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
            code+= word[aux+1:]
        else:
            code += word
    return code

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

def put_defines(lines, defines):
    for i in range(len(lines)):
        for define in defines:
            lines[i] = lines[i].replace(define[0], define[1])
    return lines

def read(file):
    import os
    os.chdir(os.path.dirname(__file__))
    with open(file) as f:
        lines = f.readlines()
    return lines

def union(lines):
    code=''
    for line in lines:
        code += line
    return code

lines = read('teste.c')
lines = rmv_enter(lines)
lines = rmv_comments(lines)
lines = rmv_tab(lines)
libs = get_libs(lines)
defines = get_defines(lines)
lines = put_defines(lines, defines)
lines = rmv_defines(lines)
code = union(lines)
code = rmv_larger_comments(code)
print(lines)
print(libs)
print(defines)
print(code)


