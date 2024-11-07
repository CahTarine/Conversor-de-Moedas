# Lendo arquivos xml
import xmltodict

# Ler o arquivo xml
# with open: funçao para abrir arquivo; rb: modo de leitura; parse: faz o cod decodificar o arquivo que foi aberto
def nomes_moedas():
    with open ("moedas.xml", "rb") as arquivo_moedas:
        dic_moedas = xmltodict.parse(arquivo_moedas)

    moedas = dic_moedas["xml"]
    return moedas


def combinacoes_disponiveis():
    with open ("combinacoes.xml", "rb") as arquivo_combinacoes:
        dic_combinacoes = xmltodict.parse(arquivo_combinacoes)

    combinacoes = dic_combinacoes["xml"]
    dic_combinacoes_disponiveis = {}
    for par_combinacoes in combinacoes:
        moeda_origem, moeda_destino = par_combinacoes.split("-")
# Split: retira o elemento do texto separando o que resta, o primeiro valor vai para a primeira variavel e o segundo valor para a segunda variavel
        if moeda_origem in dic_combinacoes_disponiveis:
            dic_combinacoes_disponiveis[moeda_origem].append(moeda_destino)
        else:
            dic_combinacoes_disponiveis[moeda_origem] = [moeda_destino]
# Leitura: se a moeda_origem ja existe na dic_comb_disp, entao vou adicionar o outro valor como moeda_destino. Caso contrário, eu crio ela na dic_comb_disp.

    return dic_combinacoes_disponiveis
