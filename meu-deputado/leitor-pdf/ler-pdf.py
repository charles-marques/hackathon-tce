# import PyPDF2
# import pandas as pd
# import re
#
# pdf_file = open('PDFs/Demonstrativo de Gastos.pdf', 'rb')
# read_pdf = PyPDF2.PdfFileReader(pdf_file)
# number_of_pages = read_pdf.getNumPages()
# page = read_pdf.getPage(0)
#
#
# page_content = page.extractText()
# page_content
# print(page_content)
#
#
# parsed = ''.join(page_content)
# #parsed = re.sub('\n', '', parsed)
# #parsed = re.sub('Fonte', '', parsed)
# novastring = parsed[0:20]
# print(parsed)
#
# arquivo = open('teste.txt', 'r+')
# texto = arquivo.readlines()
# texto.append(parsed)
# arquivo.writelines(texto)
# arquivo.close()
from tabula import read_pdf
import pandas as pd

deputados_mes = [
    ['Janeiro', '01',
        ['ADERLANIA NORONHA', 'AGENOR NETO', 'ANTONIO GRANJA', 'AUDIC MOTA', 'AUGUSTA BRITO', 'BETHROSE',
         'BRUNO GONCALVES', 'BRUNO PEDROSA', 'CAPITAO WAGNER', 'CARLOS FELIPE', 'CARLOS MATOS', 'DANNIEL OLIVEIRA',
         'DAVID DURAND', 'DEDE TEIXEIRA', 'DR. SARTO', 'DRA SILVANA', 'ELMANO', 'ELY AGUIAR', 'EVANDRO LEITAO',
         'FERNANDA PESSOA', 'FERNANDO HUGO', 'FERREIRA ARAGAO', 'GONY ARRUDA', 'HEITOR FERRER', 'JEOVA MOTA',
         'JOAO JAIME', 'JOAQUIM NORONHA', 'JOSE ALBUQUERQUE', 'JULINHO', 'LEONARDO ARAUJO', 'LEONARDO PINHEIRO',
         'LUCILVIO GIRAO', 'MANOEL DUCA', 'MARIO HELIO', 'MIRIAN SOBREIRA', 'MOISES BRAZ', 'ODILON AGUIAR',
         'OSMAR BAQUIT', 'RACHEL MARQUES', 'RENATO ROSENO', 'ROBERIO MONTEIRO', 'ROBERTO MESQUITA', 'SERGIO AGUIAR',
         'TIN GOMES', 'TOMAZ HOLANDA', 'WALTER CAVALCANTE'], '2019'],
    ['Fevereiro', '02',
        ['ACRÍSIO SENA', 'ADERLANIA NORONHA', 'AGENOR NETO', 'ANDRE FERNANDES', 'ANTONIO GRANJA', 'AP. LUIZ HENRIQUE',
         'AUDIC MOTA', 'AUGUSTA BRITO', 'BETHROSE', 'BRUNO GONCALVES',
          'BRUNO PEDROSA', 'CAPITAO WAGNER', 'CARLOS FELIPE', 'CARLOS MATOS', 'DANNIEL OLIVEIRA',
          'DAVID DURAND', 'DEDE TEIXEIRA', 'DELEGADO CAVALCANTE', 'DR. SARTO', 'DRA SILVANA', 'ELMANO',
          'ELY AGUIAR', 'ERIKA AMORIM', 'EVANDRO LEITAO', 'FERNANDA PESSOA', 'FERNANDO HUGO',
          'FERNANDO SANTANA', 'FERREIRA ARAGAO', 'GONY ARRUDA', 'GUILHERME LANDIM', 'HEITOR FERRER',
          'JEOVA MOTA', 'JOAO JAIME', 'JOSE ALBUQUERQUE', 'JULINHO', 'LEONARDO ARAUJO', 'LEONARDO PINHEIRO',
          'LUCILVIO GIRAO', 'MANOEL DUCA', 'MARCOS SOBREIRA', 'MARIO HELIO', 'MIRIAN SOBREIRA',
          'MOISES BRAZ', 'NELINHO', 'NEZINHO FARIAS', 'NIZO COSTA', 'ODILON AGUIAR', 'OSMAR BAQUIT',
          'PATRICIA AGUIAR', 'QUEIROZ FILHO', 'RACHEL MARQUES', 'RENATO ROSENO', 'ROBERIO MONTEIRO',
          'ROMEU ALDIGUERI', 'SERGIO AGUIAR', 'SOLDADO NOELIO', 'TIN GOMES', 'TOMAZ HOLANDA', 'VITOR VALIM',
          'WALTER CAVALCANTE'], '2019'],
    ['Março', '03',
         ['ACRÍSIO SENA', 'ADERLANIA NORONHA', 'AGENOR NETO', 'ANDRE FERNANDES', 'ANTONIO GRANJA', 'AP. LUIZ HENRIQUE',
          'AUDIC MOTA', 'AUGUSTA BRITO', 'BRUNO GONCALVES', 'BRUNO PEDROSA', 'CARLOS FELIPE', 'DANNIEL OLIVEIRA',
          'DAVID DURAND', 'DELEGADO CAVALCANTE', 'DR. SARTO', 'DRA SILVANA', 'ELMANO', 'ERIKA AMORIM', 'EVANDRO LEITAO',
          'FERNANDA PESSOA', 'FERNANDO HUGO', 'FERNANDO SANTANA', 'GONY ARRUDA', 'GUILHERME LANDIM', 'HEITOR FERRER',
          'JEOVA MOTA', 'JOAO JAIME', 'JOSE ALBUQUERQUE', 'JULINHO', 'LEONARDO ARAUJO', 'LEONARDO PINHEIRO',
          'LUCILVIO GIRAO', 'MANOEL DUCA', 'MARCOS SOBREIRA', 'MIRIAN SOBREIRA', 'MOISES BRAZ', 'NELINHO', 'NEZINHO FARIAS',
          'NIZO COSTA', 'ODILON AGUIAR', 'OSMAR BAQUIT', 'PATRICIA AGUIAR', 'QUEIROZ FILHO', 'RENATO ROSENO',
          'ROBERIO MONTEIRO', 'ROMEU ALDIGUERI', 'SERGIO AGUIAR', 'SOLDADO NOELIO', 'TIN GOMES', 'VITOR VALIM',
          'WALTER CAVALCANTE'], '2019'],
    ['Abril', '04',
        ['ACRÍSIO SENA', 'ADERLANIA NORONHA', 'AGENOR NETO', 'ANDRE FERNANDES', 'ANTONIO GRANJA', 'AP. LUIZ HENRIQUE',
         'AUDIC MOTA', 'AUGUSTA BRITO', 'BRUNO GONCALVES', 'BRUNO PEDROSA', 'CARLOS FELIPE', 'DANNIEL OLIVEIRA',
         'DAVID DURAND', 'DELEGADO CAVALCANTE', 'DR. SARTO', 'DRA SILVANA', 'ELMANO', 'ERIKA AMORIM', 'EVANDRO LEITAO',
         'FERNANDA PESSOA', 'FERNANDO HUGO', 'FERNANDO SANTANA', 'GUILHERME LANDIM', 'HEITOR FERRER', 'JEOVA MOTA',
         'JOAO JAIME', 'JÚLIOCÉSAR FILHO', 'LEONARDO ARAUJO', 'LEONARDO PINHEIRO', 'LUCILVIO GIRAO', 'MANOEL DUCA',
         'MARCOS SOBREIRA', 'MOISES BRAZ', 'NELINHO', 'NEZINHO FARIAS', 'NIZO COSTA', 'OSMAR BAQUIT', 'PATRICIA AGUIAR',
         'QUEIROZ FILHO', 'RENATO ROSENO', 'ROBERIO MONTEIRO', 'ROMEU ALDIGUERI', 'SALMITO', 'SERGIO AGUIAR',
         'SOLDADO NOELIO', 'TIN GOMES', 'VITOR VALIM', 'WALTER CAVALCANTE'], '2019'],
    ['Maio', '05',
        ['ACRÍSIO SENA', 'ADERLANIA NORONHA', 'AGENOR NETO', 'ANDRE FERNANDES', 'ANTONIO GRANJA', 'AP. LUIZ HENRIQUE',
         'AUDIC MOTA', 'AUGUSTA BRITO', 'BRUNO GONCALVES', 'BRUNO PEDROSA', 'CARLOS FELIPE', 'DANNIEL OLIVEIRA',
         'DAVID DURAND', 'DELEGADO CAVALCANTE', 'DR. SARTO', 'DRA SILVANA', 'ELMANO', 'ERIKA AMORIM', 'EVANDRO LEITAO',
         'FERNANDA PESSOA', 'FERNANDO HUGO', 'FERNANDO SANTANA', 'GUILHERME LANDIM', 'HEITOR FERRER', 'JEOVA MOTA',
         'JOAO JAIME', 'JÚLIOCÉSAR FILHO', 'LEONARDO ARAUJO', 'LEONARDO PINHEIRO', 'LUCILVIO GIRAO', 'MANOEL DUCA',
         'MARCOS SOBREIRA', 'MOISES BRAZ', 'NELINHO', 'NEZINHO FARIAS', 'NIZO COSTA', 'OSMAR BAQUIT', 'PATRICIA AGUIAR',
         'QUEIROZ FILHO', 'RENATO ROSENO', 'ROMEU ALDIGUERI', 'SALMITO', 'SERGIO AGUIAR', 'SOLDADO NOELIO',
         'VITOR VALIM', 'WALTER CAVALCANTE'], '2019'],
    ['Junho', '06',
        ['ACRÍSIO SENA', 'ADERLANIA NORONHA', 'AGENOR NETO', 'ANDRE FERNANDES', 'ANTONIO GRANJA', 'AP. LUIZ HENRIQUE',
          'AUDIC MOTA', 'AUGUSTA BRITO', 'BRUNO GONCALVES', 'BRUNO PEDROSA', 'CARLOS FELIPE', 'DANNIEL OLIVEIRA',
          'DAVID DURAND', 'DELEGADO CAVALCANTE', 'DR. SARTO', 'DRA SILVANA', 'ELMANO', 'ERIKA AMORIM', 'EVANDRO LEITAO',
          'FERNANDA PESSOA', 'FERNANDO HUGO', 'FERNANDO SANTANA', 'GUILHERME LANDIM', 'HEITOR FERRER', 'JEOVA MOTA',
          'JOAO JAIME', 'JÚLIOCÉSAR FILHO', 'LEONARDO ARAUJO', 'LEONARDO PINHEIRO', 'LUCILVIO GIRAO', 'MANOEL DUCA',
          'MARCOS SOBREIRA', 'MOISES BRAZ', 'NELINHO', 'NEZINHO FARIAS', 'NIZO COSTA', 'OSMAR BAQUIT', 'PATRICIA AGUIAR',
          'QUEIROZ FILHO', 'RENATO ROSENO', 'ROMEU ALDIGUERI', 'SALMITO', 'SERGIO AGUIAR', 'SOLDADO NOELIO', 'TIN GOMES',
          'VITOR VALIM', 'WALTER CAVALCANTE'], '2019'],
    ['Julho', '07',
        ['ACRÍSIO SENA', 'ADERLANIA NORONHA', 'AGENOR NETO', 'ANDRE FERNANDES', 'ANTONIO GRANJA', 'AP. LUIZ HENRIQUE',
         'AUDIC MOTA', 'AUGUSTA BRITO', 'BRUNO GONCALVES', 'BRUNO PEDROSA', 'CARLOS FELIPE', 'DANNIEL OLIVEIRA',
         'DAVID DURAND', 'DELEGADO CAVALCANTE', 'DR. SARTO', 'ELMANO', 'ERIKA AMORIM', 'EVANDRO LEITAO',
         'FERNANDA PESSOA', 'FERNANDO HUGO', 'FERNANDO SANTANA', 'GUILHERME LANDIM', 'HEITOR FERRER', 'JEOVA MOTA',
         'JOAO JAIME', 'JÚLIOCÉSAR FILHO', 'LEONARDO ARAUJO', 'LEONARDO PINHEIRO', 'LUCILVIO GIRAO', 'MANOEL DUCA',
         'MARCOS SOBREIRA', 'MOISES BRAZ', 'NELINHO', 'NEZINHO FARIAS', 'NIZO COSTA', 'OSMAR BAQUIT', 'PATRICIA AGUIAR',
         'QUEIROZ FILHO', 'RENATO ROSENO', 'ROMEU ALDIGUERI', 'SALMITO', 'SERGIO AGUIAR', 'SOLDADO NOELIO', 'TIN GOMES',
         'TONY BRITO', 'VITOR VALIM', 'WALTER CAVALCANTE'],
        '2019'],
    ['Agosto', '08',
        ['ACRÍSIO SENA', 'ADERLANIA NORONHA', 'AGENOR NETO', 'ANDRE FERNANDES', 'ANTONIO GRANJA', 'AP. LUIZ HENRIQUE',
         'AUDIC MOTA', 'AUGUSTA BRITO', 'BRUNO GONCALVES', 'BRUNO PEDROSA', 'CARLOS FELIPE', 'DANNIEL OLIVEIRA',
         'DAVI DE RAIMUNDÃO', 'DAVID DURAND', 'DELEGADO CAVALCANTE', 'DR. SARTO', 'DRA SILVANA', 'ELMANO',
         'ERIKA AMORIM', 'EVANDRO LEITAO', 'FERNANDA PESSOA', 'FERNANDO HUGO', 'FERNANDO SANTANA', 'GORDIM ARAÚJO',
         'GUILHERME LANDIM', 'HEITOR FERRER', 'JEOVA MOTA', 'JOAO JAIME', 'JÚLIOCÉSAR FILHO', 'LEONARDO ARAUJO',
         'LEONARDO PINHEIRO', 'LUCILVIO GIRAO', 'MANOEL DUCA', 'MARCOS SOBREIRA', 'MOISES BRAZ', 'NELINHO',
         'NEZINHO FARIAS', 'NIZO COSTA', 'OSMAR BAQUIT', 'PATRICIA AGUIAR', 'QUEIROZ FILHO', 'RENATO ROSENO',
         'ROMEU ALDIGUERI', 'SALMITO', 'SERGIO AGUIAR', 'TIN GOMES', 'TONY BRITO', 'VITOR VALIM',
         'WALTER CAVALCANTE'], '2019'],
    ['Setembro', '09',
        ['ACRÍSIO SENA', 'ADERLANIA NORONHA', 'ANDRE FERNANDES', 'ANTONIO GRANJA', 'AP. LUIZ HENRIQUE', 'AUDIC MOTA',
         'AUGUSTA BRITO', 'CARLOS FELIPE', 'DANNIEL OLIVEIRA', 'DAVI DE RAIMUNDÃO', 'DAVID DURAND',
         'DELEGADO CAVALCANTE', 'DR. SARTO', 'DRA SILVANA', 'EDILARDO EUFRASIO', 'ELMANO', 'ERIKA AMORIM',
         'EVANDRO LEITAO', 'FERNANDA PESSOA', 'FERNANDO HUGO', 'FERNANDO SANTANA', 'GORDIM ARAÚJO', 'GUILHERME LANDIM',
         'HEITOR FERRER', 'JEOVA MOTA', 'JOAO JAIME', 'JÚLIOCÉSAR FILHO', 'LEONARDO PINHEIRO', 'LUCILVIO GIRAO',
         'MANOEL DUCA', 'MARCOS SOBREIRA', 'MOISES BRAZ', 'NELINHO', 'NEZINHO FARIAS', 'NIZO COSTA', 'ORIEL NUNES FILHO',
         'OSMAR BAQUIT', 'PATRICIA AGUIAR', 'QUEIROZ FILHO', 'RENATO ROSENO', 'ROMEU ALDIGUERI', 'SALMITO',
         'SERGIO AGUIAR', 'TIN GOMES', 'TONY BRITO', 'VITOR VALIM', 'WALTER CAVALCANTE'], '2019'],
    ['Outubro', '10',
        ['ACRÍSIO SENA', 'ADERLANIA NORONHA', 'ANDRE FERNANDES', 'ANTONIO GRANJA', 'AP. LUIZ HENRIQUE', 'AUDIC MOTA',
         'AUGUSTA BRITO', 'CARLOS FELIPE', 'DANNIEL OLIVEIRA', 'DAVI DE RAIMUNDÃO', 'DAVID DURAND',
         'DELEGADO CAVALCANTE', 'DR. SARTO', 'DRA SILVANA', 'EDILARDO EUFRASIO', 'ELMANO', 'ERIKA AMORIM',
         'EVANDRO LEITAO', 'FERNANDA PESSOA', 'FERNANDO HUGO', 'FERNANDO SANTANA', 'GORDIM ARAÚJO', 'GUILHERME LANDIM',
         'HEITOR FERRER', 'JEOVA MOTA', 'JOAO JAIME', 'JÚLIOCÉSAR FILHO', 'LEONARDO PINHEIRO', 'LUCILVIO GIRAO',
         'MANOEL DUCA', 'MARCOS SOBREIRA', 'MOISES BRAZ', 'NELINHO', 'NEZINHO FARIAS', 'NIZO COSTA',
         'ORIEL NUNES FILHO', 'OSMAR BAQUIT', 'PATRICIA AGUIAR', 'QUEIROZ FILHO', 'RENATO ROSENO', 'ROMEU ALDIGUERI',
         'SALMITO', 'SERGIO AGUIAR', 'TIN GOMES', 'TONY BRITO', 'VITOR VALIM', 'WALTER CAVALCANTE'], '2019'],
    ['Novembro', '11',
        ['ACRÍSIO SENA', 'ADERLANIA NORONHA', 'ANDRE FERNANDES', 'ANTONIO GRANJA', 'AP. LUIZ HENRIQUE', 'AUDIC MOTA',
         'AUGUSTA BRITO', 'CARLOS FELIPE', 'DANNIEL OLIVEIRA', 'DAVI DE RAIMUNDÃO', 'DAVID DURAND',
         'DELEGADO CAVALCANTE', 'DR. SARTO', 'DRA SILVANA', 'EDILARDO EUFRASIO', 'ELMANO', 'ERIKA AMORIM',
         'EVANDRO LEITAO', 'FERNANDA PESSOA', 'FERNANDO HUGO', 'FERNANDO SANTANA', 'GORDIM ARAÚJO', 'GUILHERME LANDIM',
         'HEITOR FERRER', 'JEOVA MOTA', 'JOAO JAIME', 'JÚLIOCÉSAR FILHO', 'LEONARDO PINHEIRO', 'LUCILVIO GIRAO',
         'MANOEL DUCA', 'MARCOS SOBREIRA', 'MOISES BRAZ', 'NELINHO', 'NEZINHO FARIAS', 'NIZO COSTA',
         'ORIEL NUNES FILHO', 'PATRICIA AGUIAR', 'QUEIROZ FILHO', 'RENATO ROSENO', 'ROMEU ALDIGUERI', 'SALMITO',
         'SERGIO AGUIAR', 'SOLDADO NOELIO', 'TIN GOMES', 'TONY BRITO', 'VITOR VALIM', 'WALTER CAVALCANTE'], '2019'],
    ['Dezembro', '12',
        ['ACRÍSIO SENA', 'ADERLANIA NORONHA', 'AGENOR NETO', 'ANDRE FERNANDES', 'ANTONIO GRANJA', 'AP. LUIZ HENRIQUE',
         'AUDIC MOTA', 'AUGUSTA BRITO', 'BRUNO GONCALVES', 'BRUNO PEDROSA', 'CARLOS FELIPE', 'DANNIEL OLIVEIRA',
         'DAVI DE RAIMUNDÃO', 'DAVID DURAND', 'DELEGADO CAVALCANTE', 'DR. SARTO', 'DRA SILVANA', 'EDILARDO EUFRASIO',
         'ELMANO', 'ERIKA AMORIM', 'EVANDRO LEITAO', 'FERNANDA PESSOA', 'FERNANDO HUGO', 'FERNANDO SANTANA',
         'GORDIM ARAÚJO', 'GUILHERME LANDIM', 'HEITOR FERRER', 'JEOVA MOTA', 'JOAO JAIME', 'JÚLIOCÉSAR FILHO',
         'LEONARDO ARAUJO', 'LEONARDO PINHEIRO', 'LUCILVIO GIRAO', 'MANOEL DUCA', 'MARCOS SOBREIRA', 'MOISES BRAZ',
         'NELINHO', 'NEZINHO FARIAS', 'NIZO COSTA', 'ORIEL NUNES FILHO', 'PATRICIA AGUIAR', 'QUEIROZ FILHO',
         'RENATO ROSENO', 'ROMEU ALDIGUERI', 'SALMITO', 'SERGIO AGUIAR', 'SOLDADO NOELIO', 'TIN GOMES',
         'TONY BRITO', 'VITOR VALIM', 'WALTER CAVALCANTE'], '2019'],

]

erros = []
df_geral = pd.DataFrame()
for mes in deputados_mes:
    str_mes = mes[0]
    num_mes = mes[1]
    deputados = mes[2]
    for deputado in deputados:
        deputado_rep = deputado.replace(' ', '+')
        tabela = read_pdf(f"PDFs/2019/{deputado}/{deputado_rep+'_2019'+str_mes}.pdf", pages='all')
        if len(tabela) != 0:
            print(f'extraindo: {str_mes} do deputado {deputado}')
            df = pd.DataFrame(tabela[0])
            df = df.drop(df.index[-1])
            df['Deputado'] = deputado
            df['Data'] = f'01/{num_mes}/2019'

            df_geral = pd.concat([df_geral, df])
        else:
            erros.append([str_mes, deputado])

df_geral.reset_index(inplace = True)
df_geral.drop('index', axis=1, inplace=True)
df_geral.to_json('gastos_candidatos.json', orient='index')
df_geral.to_csv('gastos_candidatos.csv')
