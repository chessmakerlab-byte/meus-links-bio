import os

# 1. Dados simulados (Nossa futura conexão com o Notion)
clientes = [
    {
        "slug": "sapataria",
        "nome": "Sapataria São João",
        "cor_fundo": "#f4f4f9",
        "logo": "https://api.dicebear.com/7.x/initials/svg?seed=SJ&backgroundColor=333333",
        "links": [
            {"titulo": "Falar no WhatsApp", "url": "#"},
            {"titulo": "Catálogo", "url": "#"}
        ]
    },
    {
        "slug": "pizzaria",
        "nome": "Pizzaria do Mario",
        "cor_fundo": "#ffe8e8",
        "logo": "https://api.dicebear.com/7.x/initials/svg?seed=PM&backgroundColor=d32f2f",
        "links": [
            {"titulo": "Fazer Pedido", "url": "#"},
            {"titulo": "Cardápio PDF", "url": "#"},
            {"titulo": "Instagram", "url": "#"}
        ]
    }
]

# 2. Template Base
html_template = """


    
    
    {nome} | Links
    


    
    {nome}
    {botoes_html}

"""

# 3. Lógica de Geração
pasta_saida = "public"

# Garante que a pasta public existe
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

for cliente in clientes:
    botoes_html = ""
    for link in cliente["links"]:
        botoes_html += f'{link["titulo"]}\n        '
    
    # Preenche o molde
    html_final = html_template.format(
        nome=cliente["nome"],
        cor_fundo=cliente["cor_fundo"],
        logo=cliente["logo"],
        botoes_html=botoes_html
    )
    
    # Salva o arquivo dentro da pasta 'public'
    caminho_arquivo = os.path.join(pasta_saida, f"{cliente['slug']}.html")
    
    # O encoding='utf-8' garante que os acentos fiquem perfeitos
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(html_final)
        
    print(f"Página gerada: {caminho_arquivo}")

print("Todas as páginas foram geradas com sucesso!")
