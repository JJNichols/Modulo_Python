meuDicionario = {
    'nome'     : 'Jason', 
    'sobrenome': 'Nichols', 
    'anos'     : 48
}

print(meuDicionario);

frutaDicionario = {
    'maça': 3,
    'banana': 6,
    'uva': 8,
    
};

print("Significado encontrado no dicionario: ", frutaDicionario["maça"]);
print();
frutaDicionario["maça"] = 5;
frutaDicionario["Maca"] = 7;

print("Nova quantidade de maçã: ", frutaDicionario["maça"]);
print();
print(frutaDicionario);

frutaDicionario["maça"]    = 5;
frutaDicionario["laranja"] = 10


print(frutaDicionario);
print(); 

animaisDicionario = {};
animaisDicionario["cacharro"] = "Melissa";
print(animaisDicionario);   

aluno = {
    'nome' : 'Jason',
    'idade' : 48,
    'hobbies' : ['Netflix séries', 'viagem' ] 
    
}

print(aluno);

frutaDicionario = {
    'maçã'       : 3, 
    'banana'     : 6,
    'uva'        : 8,
    'laranja'    : 10
};

print();
print("Quantidade de maçãs: ", frutaDicionario.get("maçã"));
print("Quantidade de bananas: ", frutaDicionario.get("banana"));

print("Quantidade de morangos: ", frutaDicionario.get("morangos",  "Não foi encontrado a definição de morango"));
print();

elementRemovido = frutaDicionario.pop("laranja");
print(elementRemovido);
print();
print("Dicionário atulizado: ", frutaDicionario);

print();
print("Chaves encontradas no dicionários: ", frutaDicionario.keys());
print("Valores encontrados no dicionário: ", frutaDicionario.values());
print(frutaDicionario.items());