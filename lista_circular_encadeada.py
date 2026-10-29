class No:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None


class ListaCircular:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar(self, nome):
        novo_no = No(nome)

        ## Se a lista estiver vazia
        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no

            ## O primeiro aluno aponta para ele mesmo
            novo_no.proximo = self.inicio
        else:
            ## O último aluno aponta para o novo aluno
            self.fim.proximo = novo_no

            ## Atualiza o último aluno
            self.fim = novo_no

            ## O último aponta novamente para o primeiro
            self.fim.proximo = self.inicio

    def mostrar_alunos(self):
        if self.inicio is None:
            print("Nenhum aluno cadastrado.")
            return

        atual = self.inicio

        ## Percorre a lista uma única vez
        while True:
            print(atual.nome)
            atual = atual.proximo

            ## Para quando retornar ao primeiro aluno
            if atual == self.inicio:
                break

    def simular_apresentacoes(self, quantidade):
        if self.inicio is None:
            print("Não há alunos para apresentar.")
            return

        atual = self.inicio

        for i in range(1, quantidade + 1):
            print(f"Apresentação {i}: {atual.nome}")

            ## Avança para o próximo aluno
            atual = atual.proximo


## Programa principal
lista = ListaCircular()

## Cadastro dos alunos
lista.adicionar("Helena")
lista.adicionar("João")
lista.adicionar("José")
lista.adicionar("Bernado")
lista.adicionar("Federico")

## Exibe os alunos cadastrados
print("=== ALUNOS CADASTRADOS ===")
print()
lista.mostrar_alunos()

## Simula 10 apresentações
print()
print("=== ORDEM DAS APRESENTAÇÕES ===")
print()
lista.simular_apresentacoes(10)
