# para criar uma classe use "class" Nome da classe:
'''class MyClass:
    x = 10
c = MyClass()
print(c.x)
# já o objeto pode ter diversas caracteristicas, nesse caso seria o "c"
class Pessoa:
    def __init__(proprio, nome, idade):
        proprio.nome = nome
        proprio.idade = idade
eu = Pessoa('Mayco', 20)
print ('Eu me chamo',eu.nome,'e tenho ',eu.idade, 'anos de idade')'''
# também temos que entender a função __init__(), ela é usada para criar um objeto na classe
# A função é chamada automaticamente toda vez que a classe está sendo usada para criar um novo objeto.__init__() ou seja, todas as classes tem um __init__() imbutido.

'''class Pessoa: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}({self.age})'''
    
'''eu = Pessoa('Mayco', 20)
print(eu)'''
#A função __str__ controla o que deve ser retornado quando o objeto da classe é representado como uma string.
#Se a função __str__() não estiver definida, a representação em string do objeto será retornada.
# Começar uma classe com __init__ ajuda ainstanciação de objetos e __str__ é util pata depurar.

'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print('Hello brother, my name is ' + self.name)

eu = Person('Mayco', 20)
eu.myfunc()'''

# Objetos também podem ter metodos ou funções que o pertencem.

#O parâmetro é uma referência ao instância atual da classe e é usada para acessar variáveis que pertencem à classe.self
#Não precisa ser nomeado, você pode chame-o como quiser, mas tem que ser o primeiro parâmetro de qualquer função Na aula:self
'''class Person:
  def _init_(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)'''

#apenas troquei o self por mysillyobject, sendo que este deve estar sempre em primeiro nos objetos da classe.  '''
'''class Pessoa:
    def __init__(self, nome, idade, altura) :
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def apresentação(status):
        print('Hello man, my name is ' +status.nome)
        print('i have ' + status.idade + ' years old' )
        print('and ' + status.altura +' cm of hedge')
eu = Pessoa('Mayco', '20', '175')
p1 = Pessoa('Ana', '15', '170')
p2 = Pessoa('Marcos', '23', '180')
p3 = Pessoa('Vanderleisom', '1500', '200')
lista = [eu, p1, p2, p3]
lista.pop(1)
for c in lista: 
    c.apresentação()'''

#Se por algum motivo houver uma classe sem conteudo coloque-a na pass instrução para evitar erro.
'''class Teste:
    pass'''
