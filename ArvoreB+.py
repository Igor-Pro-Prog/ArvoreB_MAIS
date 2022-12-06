#algumas funções da arvore B+ 
#inserir e remover e buscar 

class No:
    def __init__(self, folha = False):#inicializa o no
        self.chaves = []#lista de chaves
        self.filhos = []#lista de filhos
        self.folha = folha#se for folha ou nao

    def busca(self, k):#busca a chave k na arvore
        i = 0
        while i < len(self.chaves) and k > self.chaves[i]:#enquanto a chave for maior que a chave atual
            i += 1
        if i < len(self.chaves) and k == self.chaves[i]:#se a chave for igual a chave atual
            return (self, i)#retorna o no e a posicao da chave
        elif self.folha:#se for folha e nao encontrar a chave
            return (None, None)
        else:#se nao for folha e nao encontrar a chave
            return self.filhos[i].busca(k)
    
    def insere(self, k):# insere a chave k na arvore    
        if self.folha:#se for folha
            i = 0
            while i < len(self.chaves) and k > self.chaves[i]:#enquanto a chave for maior que a chave atual
                i += 1
            self.chaves.insert(i, k)#insere a chave na posicao i
        else:#se nao for folha
            i = 0
            while i < len(self.chaves) and k > self.chaves[i]:#enquanto a chave for maior que a chave atual
                i += 1
            if len(self.filhos[i].chaves) == 2*t - 1: #se o no filho estiver cheio
                self.filhos[i].dividir() #divide o no filho
                if k > self.chaves[i]:#se a chave for maior que a chave atual
                    i += 1
            self.filhos[i].insere(k)#insere a chave na posicao i

    def dividir(self):#divide o no
        meio = self.chaves[t-1]#pega a chave do meio
        direita = No(self.folha)#cria um no a direita
        direita.chaves = self.chaves[t:]#pega as chaves a direita do meio
        if not self.folha:#se nao for folha
            direita.filhos = self.filhos[t:]#pega os filhos a direita do meio
        self.chaves = self.chaves[:t-1]#pega as chaves a esquerda do meio
        self.filhos = self.filhos[:t]#pega os filhos a esquerda do meio
        return (meio, direita)#retorna a chave do meio e o no a direita

    def remove(self, k):#remove a chave k da arvore
        i = 0
        while i < len(self.chaves) and k > self.chaves[i]:#enquanto a chave for maior que a chave atual
            i += 1
        if i < len(self.chaves) and k == self.chaves[i]:#se a chave for igual a chave atual
            if self.folha:
                del self.chaves[i]#remove a chave
            else:
                if len(self.filhos[i].chaves) >= t:#se o no filho tiver mais que t chaves
                    pred = self.filhos[i].pred(i)
                    self.chaves[i] = pred
                    self.filhos[i].remove(pred)
                elif len(self.filhos[i+1].chaves) >= t:#se o no filho tiver mais que t chaves
                    succ = self.filhos[i+1].succ(i)
                    self.chaves[i] = succ
                    self.filhos[i+1].remove(succ)
                else:#se o no filho tiver menos que t chaves
                    self.filhos[i].chaves.append(self.chaves[i])#adiciona a chave no no filho
                    self.filhos[i].chaves.extend(self.filhos[i+1].chaves)#adiciona as chaves do no filho a direita
                    if not self.filhos[i].folha:#se nao for folha
                        self.filhos[i].filhos.extend(self.filhos[i+1].filhos)#adiciona os filhos do no filho a direita
                    del self.chaves[i]#remove a chave
                    del self.filhos[i+1]#remove o no filho a direita
                    self.filhos[i].remove(k)#remove a chave
        elif self.folha:#  se for folha e nao encontrar a chave
            print("Chave não encontrada")
        else:
            if len(self.filhos[i].chaves) == t-1:#se o no filho tiver t-1 chaves
                if i > 0 and len(self.filhos[i-1].chaves) >= t:#se o no filho a esquerda tiver mais que t chaves
                    self.filhos[i].chaves.insert(0, self.chaves[i-1])#adiciona a chave no no filho
                    self.chaves[i-1] = self.filhos[i-1].chaves.pop()#remove a chave do no filho a esquerda
                    if not self.filhos[i].folha:#se nao for folha
                        self.filhos[i].filhos.insert(0, self.filhos[i-1].filhos.pop())#adiciona o filho do no filho a esquerda
                elif i < len(self.filhos)-1 and len(self.filhos[i+1].chaves) >= t:#se o no filho a direita tiver mais que t chaves
                    self.filhos[i].chaves.append(self.chaves[i])#adiciona a chave no no filho
                    self.chaves[i] = self.filhos[i+1].chaves.pop(0)#remove a chave do no filho a direita
                    if not self.filhos[i].folha:#se nao for folha
                        self.filhos[i].filhos.append(self.filhos[i+1].filhos.pop(0))#adiciona o filho do no filho a direita
                elif i > 0:#se o no filho a esquerda tiver menos que t chaves
                    self.filhos[i-1].chaves.append(self.chaves[i-1])#adiciona a chave no no filho a esquerda
                    self.filhos[i- 1].chaves.extend(self.filhos[i].chaves)#adiciona as chaves do no filho
                    if not self.filhos[i].folha:#se nao for folha
                        self.filhos[i-1].filhos.extend(self.filhos[i].filhos)#adiciona os filhos do no filho
                    del self.chaves[i-1]#remove a chave
                    del self.filhos[i]#remove o no filho
                    i -= 1
                else:#se o no filho a direita tiver menos que t chaves
                    self.filhos[i].chaves.append(self.chaves[i])#adiciona a chave no no filho
                    self.filhos[i].chaves.extend(self.filhos[i+1].chaves)#adiciona as chaves do no filho a direita
                    if not self.filhos[i].folha:#se nao for folha
                        self.filhos[i].filhos.extend(self.filhos[i+1].filhos)#adiciona os filhos do no filho a direita
                    del self.chaves[i]#remove a chave
                    del self.filhos[i+1]#remove o no filho a direita
            self.filhos[i].remove(k)#remove a chave

    
    