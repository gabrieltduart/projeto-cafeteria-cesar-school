from app.utils.utilitarios_global import obter_texto

def gerar_proximo_id(cardapio: dict) -> int:
    return max(
        (item['id'] for categoria in cardapio.values()
                        for subcategoria in categoria.values()
                            for item in subcategoria),
        default=0
    ) + 1
    
def obter_categoria_e_subcategoria_valida():
    categorias_validas = {
        'bebidas': ['cafes', 'cafes_especiais', 'outras_bebidas'],
        'lanches': ['sanduiches', 'sobremesas']
    }
    
    categoria_geral = obter_texto('\n📂 Digite a Categoria Geral (ex: bebidas, lanches): ').lower()
    if categoria_geral not in categorias_validas:
        print('\n⚠️ Categoria geral inválida! Verifique e tente novamente. ')
        return
        
        
    categoria_especifica = obter_texto("🏷️  Digite a Categoria Específica (ex: cafes, cafes_especiais, sobremesas...): ").lower()
    if categoria_especifica not in categorias_validas[categoria_geral]:
        print('\n⚠️ Categoria específica inválida! Verifique e tente novamente.')
        return
    
    return categoria_geral, categoria_especifica    

def exibir_titulo_cardapio(emoji, categoria_formatada):
    print(f"\n{emoji} {categoria_formatada.upper()} {emoji}".ljust(45) + f"Preço".rjust(10))
    print(' ' + '-' * 58)