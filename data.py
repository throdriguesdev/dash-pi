###v1.0
###data-filter.py
####17/05
###selecionar valores relevantes
import pandas as pd
file_path = 'basico.csv'  # Atualize o caminho do arquivo conforme necessário
data = pd.read_csv(file_path, delimiter=';', encoding='latin1')
data = data[data['NU_ANO_CENSO'] == 2023]
data = data[data['TP_SITUACAO_FUNCIONAMENTO'] == 1]
data['IN_BIBLIOTECA'] = data['IN_BIBLIOTECA'].astype(int)
escolas_publicas = data[(data['TP_DEPENDENCIA'] != 4) & (data['IN_BIBLIOTECA'] == 1)]
escolas_particulares = data[(data['TP_DEPENDENCIA'] == 4) & (data['IN_BIBLIOTECA'] == 1)]
pub_por_estado = escolas_publicas['NO_UF'].value_counts()
part_por_estado = escolas_particulares['NO_UF'].value_counts()
pub_por_estado.to_csv('dataset-1.csv', header=['Escolas_Publicas_Com_Biblioteca'])
part_por_estado.to_csv('dataset-2.csv', header=['Escolas_Particulares_Com_Biblioteca'])
pub_por_regiao = escolas_publicas['NO_REGIAO'].value_counts()
part_por_regiao = escolas_particulares['NO_REGIAO'].value_counts()
pub_por_regiao.to_csv('dataset-3.csv', header=['Escolas_Publicas_Com_Biblioteca'])
part_por_regiao.to_csv('dataset-4.csv', header=['Escolas_Particulares_Com_Biblioteca'])
total_escolas = len(data)
total_pub_com_bib = len(escolas_publicas)
total_part_com_bib = len(escolas_particulares)
total_com_biblioteca = pd.DataFrame({
    "Categoria": ["Publica", "Particular"],
    "Total": [total_pub_com_bib, total_part_com_bib],
    "Percentual": [round((total_pub_com_bib / total_escolas) * 100, 2), round((total_part_com_bib / total_escolas) * 100, 2)]
})
total_com_biblioteca.to_csv('dataset-5.csv', index=False)
