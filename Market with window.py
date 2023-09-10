import tkinter as tk
from tkinter import messagebox

# Função para exibir o inventário atual
def mostrar_inventario():
    inventario_text.delete(1.0, tk.END)  # Limpa o texto atual
    for produto, quantidade in inventario.items():
        inventario_text.insert(tk.END, f"{produto}: {quantidade} unidades\n")

# Função para realizar uma compra
def comprar_produto():
    produto = produto_entry.get().lower()
    quantidade = int(quantidade_entry.get())

    if produto in inventario and inventario[produto] >= quantidade:
        total = precos[produto] * quantidade
        inventario[produto] -= quantidade
        mostrar_inventario()
        messagebox.showinfo("Compra Realizada", f"Você comprou {quantidade} unidades de {produto} por R$ {total:.2f}")
    else:
        messagebox.showerror("Erro na Compra", "Desculpe, produto não disponível ou quantidade insuficiente em estoque.")

# Dicionário para armazenar o inventário do mercado
inventario = {
    'banana': 50,
    'maçã': 100,
    'arroz': 2000,
    'feijão': 1500,
    'carne': 300,
}

# Dicionário para armazenar os preços dos produtos
precos = {
    'banana': 2.0,
    'maçã': 3.0,
    'arroz': 5.0,
    'feijão': 4.0,
    'carne': 10.0,
}

# Criar a janela principal
janela = tk.Tk()
janela.title("Mercado XYZ")

# Rótulos e campos de entrada
produto_label = tk.Label(janela, text="Produto:")
produto_label.pack()
produto_entry = tk.Entry(janela)
produto_entry.pack()

quantidade_label = tk.Label(janela, text="Quantidade:")
quantidade_label.pack()
quantidade_entry = tk.Entry(janela)
quantidade_entry.pack()

# Botões
mostrar_inventario_button = tk.Button(janela, text="Mostrar Inventário", command=mostrar_inventario)
mostrar_inventario_button.pack()

comprar_button = tk.Button(janela, text="Comprar", command=comprar_produto)
comprar_button.pack()

# Área de texto para mostrar o inventário
inventario_text = tk.Text(janela, height=10, width=40)
inventario_text.pack()

# Iniciar a interface gráfica
janela.mainloop()