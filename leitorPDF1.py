import PyPDF2, camelot, PyPDF4, pdfreader, re, pdfquery, json ,pandas as pd
from pdfreader import PDFDocument, SimplePDFViewer
from tabula import read_pdf
class CompraAtaRegistroPreco:
    ''' Classe respresentativa de objetos ou serviços comprados dentro de um ambiente de ata de registro de preço
        com informações retiradas do PDF'''
    def __init__(self, objeto, numProcesso, modalidade, empresa, item, cnpj, itemDesc, valorUnitario, quantidade, totalAdjudicado):
        self.objeto = objeto
        self.numProcesso = numProcesso
        self.modalidade = modalidade
        self.empresa = empresa
        self.item = item
        self.cnpj = cnpj
        self.itemDesc = itemDesc
        self.valorUnitario = valorUnitario
        self.quantidade = quantidade
        self.totalAdjudicado = totalAdjudicado
        self.total_itens = quantidade*valorUnitario


def recuperaListaTabelaPdf(data_frame_merged, codigo):
    data_frame_single = data_frame_merged.loc[data_frame_merged.iloc[:,1] ==  codigo]
    return data_frame_single.values.tolist()

#defseparaValores(data_frame_single):


def leituraTabelasPdf(pdfPath):

    # java_options="-Dfile.encoding=UTF8"
    #pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #pageObj = pdfReader.getPage(0)
    #print(pageObj.extractText())
    df2 = read_pdf(pdfPath, encoding='utf-8', pages = 'all')
    teste = []
    #print (df2)
    merge = pd.concat(df2)
    index = merge.index
    columns = merge.columns
    values = merge.values
    print(merge)
    
    df4 = merge.loc[merge.iloc[:,1] ==  '6515.68.264-07']
    listaTeste = df4.values.tolist()
    print(type(listaTeste))
    print(listaTeste)
    print(len(listaTeste[0]))
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    print(listaTeste[0][4])
    #print(merge.iloc[:,1])
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    #print(df4)
    
    #item 0 - cabeçalho
    #item 1 - código
    #item 2 - descricao
    #item 3 - quantidade
    #item 4 - preço
    #item 5 - empresa
    #item 6 - empenho

    #teste2 = merge.loc[df4.iloc[:,0]]
    #print(teste2.to_string)

    #print (index)
    #print(columns)
    #print(values)
    #print(merge)
    #print(merge.iloc[1])
    merge.to_csv('output.csv', encoding='utf-8', index=False)
    return merge
    #for df in df2:
    #    teste.append(df)
    #print(df2)

##########################NÃO DELETAR, SOMENTE APÓS DOCUMENTAR NO TCC############################################

#a = len(df2)
#for i in range (a -3):
#    df2[i].rename( columns={'Unnamed: 2':'desc'}, inplace=True)
#    print(df2[i]['desc'])

#df = read_pdf('/Users/mathe/Downloads/rio_de_janeiro_2020-09-02_pag_36.pdf', format="csv")

#print(df)
#teste = re.compile("text':\s'.{36,}[A-Z]+\.?'}")
#k = 0
#listNovoObjeto = []

#for i in range (len(df)):
#    texto = df[i]
#    texto = str(texto)
#    listTexto = (texto.split('{'))
#    for j in range (len(listTexto)):
#        leituraAtual = listTexto[j]
#        match = teste.search(leituraAtual)
#        if match:
#            start = match.start()
#            end = match.end()
#            hfound = leituraAtual[start:end]
#            print ('**************'+hfound+'**************')
#            novoObjeto = df2[k]
#            listNovoObjeto.append(novoObjeto)
#            listNovoObjeto[k].append(hfound)
#            print(listNovoObjeto[k])
#            k += 1

#tables = camelot.read_pdf('/Users/mathe/Downloads/rio_de_janeiro_2020-09-02_pag_36.pdf', pages ="1-end")
#for i in range (len(tables)):
#    print (tables[i].df)

#pdf = pdfquery.PDFQuery('/Users/mathe/Downloads/rio_de_janeiro_2020-09-02_pag_36.pdf')
#pdf.load()
#print(pdf.tree.write('/Users/mathe/Downloads/rio_de_janeiro_2020-09-02_pag_36.xml', pretty_print=True))

#pdfFileObj = open('/Users/mathe/Downloads/rio_de_janeiro_2020-09-02_pag_36.pdf', mode="rb")

##########################NÃO DELETAR, SOMENTE APÓS DOCUMENTAR NO TCC############################################

#viewer = SimplePDFViewer(pdfFileObj)
#viewer.render()
#texto = "".join(viewer.canvas.strings)

#print(texto)


##########################NÃO DELETAR, SOMENTE APÓS DOCUMENTAR NO TCC############################################

regex_PDF = re.compile("Órgão(\s)*Gestor(\s)*:(\s)*(.*)\.|Objeto(\s)*:(\s)*(\s)([^\.](\s)?)*\.|Processo(\s)*:(\s)*(\s)\d{2}\/\d{3}\.\d{3}\/\d{4}|Modalidade(\s)*:(\s)*(\s)([^\.](\s)?)*\.|Empresa(\s)*Vencedora(\s)*\-(\s)*Ite(m|ns)([^\:](\s)?)*:(\s)*(.*?(\s)?)?CNPJ|CNPJ(\s)*:(\s)*(\d){2}\.(\d){3}\.(\d){3}\/(\d){4}\-(\d){2}|Valor(\s)*Total(\s)*Adjudicado(\s)*:(\s)*R\$(\s).*,(\d){2}|(\d){4}\.(\d){2}.(\d){3}\-(\d){2}")

#objetoBox = re.compile(r'(?P<objeto>Objeto(\s)*:(\s)*(\s)([^\.](\s)?)*\.)'
    #r'(?P<Orgao_gestor>Órgão(\s)*Gestor(\s)*:(\s)*(.*)\.)'
    #r'(?P<Num_Processo>Processo(\s)*:(\s)*(\s)\d{2}\/\d{3}\.\d{3}\/\d{4})', texo)
    #r'(?P<Modalidade>Modalidade(\s)*:(\s)*(\s)([^\.](\s)?)*\.)'
    #r'(?P<EmpresaVencedoraAndItens>Empresa(\s)*Vencedora(\s)*\-(\s)*Ite(m|ns)([^\:](\s)?)*:(\s)*(.*?(\s)?)?CNPJ)'
    #r'(?P<cnpj>CNPJ(\s)*:(\s)*(\d){2}\.(\d){3}\.(\d){3}\/(\d){4}\-(\d){2})'
    #r'(?P<ValorAdjudicado>Valor(\s)*Total(\s)*Adjudicado(\s)*:(\s)*R\$(\s).*,(\d){2})'
    #r'(?P<codigo>(\d){4}\.(\d){2}.(\d){3}\-(\d){2})')

#print('****************************************************************************')
pdfPath = '/Users/mathe/Downloads/rio_de_janeiro_2020-09-02_pag_36.pdf'
#pdfPath = '/Users/mathe/Downloads/rio_de_janeiro_2019-01-31_pag_53.pdf'
#pdfPath = '/Users/mathe/Downloads/rio_de_janeiro_2018-01-02_pag_105.pdf'
pdfFileObj = open(pdfPath, "rb")

data_frame_merged =  leituraTabelasPdf(pdfPath)
#TODO colocar em volta de um try catch

pdfReader = PyPDF4.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
texto = pageObj.extractText()

regexCNPJ = re.compile("CNPJ(\s)*:(\s)*(\d){2}\.(\d){3}\.(\d){3}\/(\d){4}\-(\d){2}")
regexCodigoItem = re.compile("(\d){4}\.(\d){2}.(\d){3}\-(\d){2}")

#print(texto)

validar_multiplos_itens = 0
estado = 0
for match in regex_PDF.finditer(texto):
    match_atual = match.group().rstrip()
    match_atual = match_atual.rstrip('\n')
    #print ('***************'+match_atual+'***************')
    if "Objeto" in match_atual:
        print(match_atual)
        objeto = match_atual
        estado = 1
        validar_multiplos_itens = 0
    elif "Processo" in match_atual:
        if (estado == 1):
            processo = match_atual
            print(processo)
            estado = 2
        else:
            estado = 0
            objeto = ""
            processo = ""
    elif "Modalidade" in match_atual:
        if (estado == 2):
            if ("pregão" in match_atual.lower() or "ata de registro" in match_atual.lower() or "licitação" in  match_atual.lower() or "compra direta" in match_atual.lower()):
               estado = 3 
               modalidade = match_atual
               print(modalidade)
            else:
                estado = 0
                objeto = ""
                processo = ""
        else:
            estado = 0
            objeto = ""
            processo = ""
    elif (estado == 3):
        if "Empresa" in match_atual and "vencedora" in match_atual.lower():
            empresaVencedora = match_atual
            verificar_se_multiplos_itens = 1
        elif "CNPJ" in match_atual:
            if regexCNPJ.match(match_atual):
                cnpj = match_atual
        elif "valor adjudicado" in match_atual.lower():
            valor_adjudicado = match_atual
        elif regexCodigoItem.match(match_atual):
            codigo_item = match_atual
            validar_multiplos_itens = 1
            list_tabela_itens = recuperaListaTabelaPdf(data_frame_merged, codigo_item)
            estado = 0
    elif validar_multiplos_itens == 1:
        if regexCodigoItem.match(match_atual):
            codigo_item = match_atual    
            list_tabela_itens = recuperaListaTabelaPdf(data_frame_merged, codigo_item)
        
            
