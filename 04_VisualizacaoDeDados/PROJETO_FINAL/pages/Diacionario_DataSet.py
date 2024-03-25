import streamlit as st
import pandas as pd

# Aqui onde configuramos o título da página e o logo que aparecerá no Browser!!!
st.set_page_config(
    page_title="Dicionário do Dashboard",
    page_icon='assets/logo.png',
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title('PIB dos Municípios Brasileiros')

st.subheader('Descrição do Dataset', divider='gray')

st.text('O dataset base do dashboard apresentado é o produto interno bruto (PIB) dos municípios brasileiros')
st.text(' de 2002 a 2021, obtido no website do IBGE, conforme endereço a seguir:')
st.markdown(':blue[https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9088-produto-interno-bruto-dos-municipios.html?=&t=downloads]')

st.text('Esse dataset apresenta o PIB dos municípios brasileiros com detalhamentos de vários níveis de regionalização,')
st.text('apresenta também o PIB per capita, impostos e a estratificação dos valores adicionados por ramo de negócios.')


st.subheader('Informações dos Campos do Dataset', divider='gray')

st.text('O dashboard explorou as principais features do dataset, buscando um foco em informações financeiras,')
st.text('geográficas, temporais e populacionais.')
st.text('A seguir os campos explorados nesse dashboard:')

dicio = {
    'Campo':['Ano (int)','Estado (str)','Município (str)','PIB (float)','PIB per Capita (float)','Impostos (float)','VAB Agropecuária (float)','VAB Indústria (float)','VAB Serviços (float)','VAB Administração, Defesa, Educação e Saúde (float)'],
    'Significado':['referência temporal do dashboard, abrange os anos de 2002 a 2021.','engloba todos os 26 estados brasileiros mais o distrito federal (DF).','abrange todos os municípios do Brasil, pondendo haver variação quantitativa ao longo dos anos devido a emancipação de novos municípios.','o produto interno bruto (PIB) é o fluxo de novos bens e serviços finais produzidos durante um período. Na base trabalhada a menor granularidade é em nível de município por ano.','o PIB per capita de cada município foi estimado pelo quociente entre o valor do PIB do município e a sua população residente no período.','totaliza os impostos incidentes nas valores adicionados brutos para cada município no período avaliado.','riqueza gerada pela produção de alimentos, fibras e outros produtos do campo, incluindo agricultura, pecuária, pesca, silvicultura e extrativismo vegetal.','valor adicionado pela transformação de matérias-primas e bens intermediários em produtos finais, abrangendo a indústria de transformação, mineração e construção civil.','riqueza criada por atividades que não produzem bens físicos, como comércio, transporte, turismo, serviços financeiros, comunicação, informação, educação, saúde e outros.','valor adicionado por serviços públicos essenciais que garantem o funcionamento do Estado e o bem-estar social, como administração pública, defesa nacional, educação pública e saúde pública.']
    }

df = pd.DataFrame.from_dict(dicio)

st.table(df)