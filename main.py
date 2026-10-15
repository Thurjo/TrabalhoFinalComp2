import tkinter as tk

class ListaDeComprasApp:
  def __init__(self,root):
    self.root = root
    self.root.title("Lista de Compras")

    self.itens_lista = []
    #self.checkbuttons = []

    #Configuracao da entrada de texto
    self.entrada_item = tk.Entry(root, width=30)
    self.entrada_item.grid(row=0, column=0, padx=10, pady=10)

    #Botao para adicionar item na lista
    botao_adicionar = tk.Button(root, text="Adicionar Item", command=self.adicionar_item)
    botao_adicionar.grid(row=0, column=1, padx=10, pady=10)

    #Scrollbar para exibir a lista de compras
    self.scrollbar = tk.Scrollbar(root)
    self.scrollbar.grid(row=1, column=1, sticky="ns")
    
    #Lista de compras
    self.lista_compras = tk.Listbox(root, yscrollcommand=self.scrollbar.set)
    self.lista_compras.grid(row=1, column=0, padx=10, pady=10)
    self.scrollbar.config(command=self.lista_compras.yview)
    
    #Botao para remover item da lista
    botao_remover = tk.Button(root, text="Remover Item", command=self.remover_item)
    botao_remover.grid(row=2, column=0, padx=10, pady=10)
    
    #Botao para marcar item como comprado
    botao_comprado = tk.Button(root, text="Marcar como Comprado", command=self.marcar_comprado)
    botao_comprado.grid(row=2, column=1, padx=10, pady=10)

    #Exibe a lista de compras
    self.exibir_lista()

  def adicionar_item(self):
    item = self.entrada_item.get()
    if item:
      self.itens_lista.append(item)
      
      #limpa a entrada de texto depois de adicionar o item
      self.entrada_item.delete(0, tk.END)
      #Com isso a exibicao da lista vai atualizar
      self.exibir_lista()

  def remover_item(self):
    selecionado = self.lista_compras.curselection()
    if selecionado:
      indice = selecionado[0]
      self.itens_lista.pop(indice)
      self.exibir_lista()

  def marcar_comprado(self):
    selecionado = self.lista_compras.curselection()
    if selecionado:
      indice = selecionado[0]
      self.itens_lista[indice] = f"[Comprado] {self.itens_lista[indice]}"
      self.exibir_lista()

  def exibir_lista(self):
    self.lista_compras.delete(0, tk.END)
    for item in self.itens_lista:
      self.lista_compras.insert(tk.END, item)

    #Checagem para marcar item como comprado
    for i in range(self.lista_compras.size()):
      self.lista_compras.itemconfig(i, bg= "lightgreen" if self.itens_lista[i].startswith("[Comprado]") else "white")


if __name__ == "__main__":
  root = tk.Tk()
  root.geometry("450x360")
  app = ListaDeComprasApp(root)
  root.mainloop()