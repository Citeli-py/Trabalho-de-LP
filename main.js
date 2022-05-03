var fs = require('fs');

function read(file){
    const fileContents = fs.readFileSync(file).toString();
    return fileContents;
}

function rmv_enter(content){
    content = content.replace(/(\r\n|\n|\r)/gm, "");
    return content;
}

function rmv_space(content){
    content = content.replace(/(\t| )/gm, "");
    return content;
}

function add_space(content){
    content = content.replace(/(int)/gm, "int ");
    return content;
}

var str = read('teste.c');
str = rmv_enter(str);
//str = rmv_space(str);
console.log(str);

// função: tipo nome(args,...)
// atrib: tipo nome=valor;
// 