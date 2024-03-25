import streamlit as st
import pandas as pd
import plotly.express as px


st.write('''
## Introdução:
Esse conteúdo tem como objetivo complementar as diversas formas de explorar o dash board construído.
Ao longo das últimas duas décadas, os Estados brasileiros testemunharam uma série de eventos marcantes que moldaram profundamente suas economias. Nesta análise, exploramos a evolução do Produto Interno Bruto (PIB) industrial e total (PIB) de 2002 a 2021, destacando marcos cruciais e tendências que refletem as nuances da política e da economia do país.

## PIB Industrial: Impulsionando o Crescimento Econômico:
O primeiro gráfico apresenta a trajetória do Valor Adicionado Bruto (VAB) da indústria em milhões de reais ao longo dos anos, destacando o desempenho dos estados brasileiros. Observa-se uma montanha-russa econômica, com picos de crescimento e vales de desafios. Ao navegar pelos dados interativos, percebe-se que o PIB industrial é uma peça crucial do quebra-cabeça econômico do Brasil, refletindo não apenas o desenvolvimento econômico, mas também a estabilidade política e eventos globais impactantes.

## Principais Marcos Econômicos e Políticos:
- **Início do Governo Lula (2002):** O Brasil testemunha a posse do presidente Luiz Inácio Lula da Silva, marcando o início de uma nova era na política e na economia brasileira.
- **Crise Econômica Global (2008):** O mundo é abalado pela crise financeira global, e o Brasil enfrenta desafios econômicos significativos.
- **Crescimento Econômico (2010):** O país experimenta um período de crescimento econômico robusto, impulsionado por políticas expansionistas.
- **Início da Crise Política da Dilma (2014):** O início de uma crise política tumultuada no governo Dilma Rousseff gera incertezas no cenário econômico.
- **Impeachment da Dilma (2016):** A turbulência política atinge o ápice com o impeachment da presidente Dilma Rousseff, gerando repercussões econômicas significativas.
- **Pandemia de COVID-19 (2020):** O mundo enfrenta uma crise de saúde sem precedentes, impactando severamente as economias globais, incluindo a do Brasil.
- **Início do Governo Bolsonaro (2018):** O presidente Jair Bolsonaro assume o cargo, trazendo consigo uma nova agenda política e econômica.

## Conclusão:
Os gráficos fornecem uma perspectiva da história econômica do Brasil, destacando os altos e baixos de sua jornada. À medida que navegamos pelos eventos marcantes que influenciaram o PIB industrial e total, compreendemos melhor a complexidade e a resiliência da economia brasileira diante dos desafios. Este é apenas um capítulo na rica tapeçaria da economia global, mas oferece insights valiosos para compreendermos as dinâmicas econômicas em jogo.
''')


# Carregar dados
df = pd.read_csv('data/pibmun.csv', low_memory=False)
PIBindust_df =df.groupby(['Estado', 'Ano','Região'])['VAB Indústria'].sum().reset_index().round(2)

st.title('Evolução do PIB Industrial dos Estados Brasileiros Entre 2002 e 2021')
st.write('Selecione as regiões que deseja visualizar:')

# Criar widget de seleção de regiões
regioes_selecionadas = st.multiselect('Regiões', PIBindust_df['Região'].unique(), default=['Sudeste', 'Sul'])

# Filtrar dados com base nas regiões selecionadas
mask = PIBindust_df['Região'].isin(regioes_selecionadas)
filtered_df = PIBindust_df[mask]

# Criar gráfico de linha interativo
fig = px.line(filtered_df, x='Ano', y='VAB Indústria', color='Estado',
              labels={'VAB Indústria': 'VAB Indústria (Em Milhões)', 'Ano': 'Ano'},
              title='Evolução do PIB Industrial dos Estados Brasileiros Entre 2002 e 2021')

# Adicionar controle deslizante de tamanho
fig.update_layout(width=int(1700), height=int(600))

# Adicionar anotação
fig.add_annotation(x=2018, y=40000, text='Início do governo Bolsonaro', showarrow=True, arrowhead=1, ax=100, ay=100, font=dict(size=16))
fig.add_annotation(x=2020, y=40000, text='Pandemia de COVID-19', showarrow=True, arrowhead=1, ax=50, ay=50, font=dict(size=16))
fig.add_annotation(x=2016, y=40000, text='Impeachment da Dilma', showarrow=True, arrowhead=1, ax=50, ay=50, font=dict(size=16))
fig.add_annotation(x=2014, y=40000, text='Início da crise política da Dilma', showarrow=True, arrowhead=1, ax=100, ay=100, font=dict(size=16))
fig.add_annotation(x=2010, y=40000, text='Crescimento Econômico', showarrow=True, arrowhead=1, ax=50, ay=50, font=dict(size=16))
fig.add_annotation(x=2008, y=40000, text='Início da crise econômica global', showarrow=True, arrowhead=1, ax=100, ay=100, font=dict(size=16))
fig.add_annotation(x=2002, y=40000, text='Início do governo Lula', showarrow=True, arrowhead=1, ax=100, ay=100, font=dict(size=16))



st.plotly_chart(fig)

st.write('''Evolução da Indústria Brasileira e Estagnação do Crescimento em Alguns Estados (2002-2021)
Durante as últimas duas décadas, a indústria brasileira passou por uma série de transformações, refletindo tanto os momentos de crescimento vigoroso quanto os períodos de desafios e estagnação em determinadas regiões do país.

2002-2010: Crescimento e Expansão
No início do período analisado, a indústria brasileira experimentou um crescimento significativo, impulsionado pelo aumento da demanda interna e externa. Estados como São Paulo, Minas Gerais, Rio de Janeiro e Paraná foram líderes nesse crescimento, beneficiando-se de uma infraestrutura estabelecida, mão de obra qualificada e investimentos em tecnologia e inovação.

2010-2016: Desaceleração e Estagnação
Durante esse período, a indústria enfrentou desafios, incluindo a crise econômica global de 2008 e a desaceleração da economia brasileira. Alguns estados, como aqueles localizados nas regiões Norte e Nordeste, enfrentaram dificuldades adicionais devido à falta de diversificação econômica, infraestrutura inadequada e questões relacionadas à logística e transporte.

2016-2021: Recuperação Desigual e Impacto da Pandemia
Embora a indústria tenha mostrado sinais de recuperação após a recessão, a recuperação foi desigual entre os estados. Enquanto algumas regiões continuaram a crescer, outras enfrentaram desafios persistentes, como baixo investimento em infraestrutura, burocracia e falta de incentivos fiscais. O Paraná, por exemplo, destacou-se pelo crescimento constante de sua indústria, impulsionado por investimentos em setores estratégicos e políticas voltadas para o desenvolvimento econômico regional.

 ''')



# Carregar dados
df = pd.read_csv('data/pibmun.csv', low_memory=False)
PIB_df = df.groupby(['Estado', 'Ano','Região'])['PIB'].sum().reset_index().round(2)

st.title('Evolução do PIB nos Estados Brasileiros Entre 2002 e 2021')

# Filtrar dados com base nas regiões selecionadas
mask = PIB_df['Região'].isin(regioes_selecionadas)
filtered_df = PIB_df[mask]

# Criar gráfico de linha interativo
fig = px.line(filtered_df, x='Ano', y='PIB', color='Estado',
              labels={'PIB': 'VAB Indústria (Em Milhões)', 'Ano': 'Ano'},
              title='Evolução do PIB nos Estados Brasileiros Entre 2002 e 2021')

# Adicionar controle deslizante de tamanho
fig.update_layout(width=int(1700), height=int(600))

# Adicionar anotação
fig.add_annotation(x=2018, y=40000, text='Início do governo Bolsonaro', showarrow=True, arrowhead=1, ax=100, ay=100, font=dict(size=16))
fig.add_annotation(x=2020, y=40000, text='Pandemia de COVID-19', showarrow=True, arrowhead=1, ax=50, ay=50, font=dict(size=16))
fig.add_annotation(x=2016, y=40000, text='Impeachment da Dilma', showarrow=True, arrowhead=1, ax=50, ay=50, font=dict(size=16))
fig.add_annotation(x=2014, y=40000, text='Início da crise política da Dilma', showarrow=True, arrowhead=1, ax=100, ay=100, font=dict(size=16))
fig.add_annotation(x=2010, y=40000, text='Crescimento Econômico', showarrow=True, arrowhead=1, ax=50, ay=50, font=dict(size=16))
fig.add_annotation(x=2008, y=40000, text='Início da crise econômica global', showarrow=True, arrowhead=1, ax=100, ay=100, font=dict(size=16))
fig.add_annotation(x=2002, y=40000, text='Início do governo Lula', showarrow=True, arrowhead=1, ax=100, ay=100, font=dict(size=16))



st.plotly_chart(fig)

st.write('''Evolução da Indústria Brasileira e Estagnação do Crescimento em Alguns Estados (2002-2021)
Durante as últimas duas décadas, a indústria brasileira passou por uma série de transformações, refletindo tanto os momentos de crescimento vigoroso quanto os períodos de desafios e estagnação em determinadas regiões do país.

2002-2010: Crescimento e Expansão
No início do período analisado, a indústria brasileira experimentou um crescimento significativo, impulsionado pelo aumento da demanda interna e externa. Estados como São Paulo, Minas Gerais, Rio de Janeiro e Paraná foram líderes nesse crescimento, beneficiando-se de uma infraestrutura estabelecida, mão de obra qualificada e investimentos em tecnologia e inovação. Programas como o Programa de Aceleração do Crescimento (PAC) e o Programa de Desenvolvimento da Indústria Nacional (PAC) foram implementados para impulsionar investimentos em infraestrutura e fortalecer a competitividade da indústria nacional.

2010-2016: Desaceleração e Estagnação
Durante esse período, a indústria enfrentou desafios, incluindo a crise econômica global de 2008 e a desaceleração da economia brasileira. Alguns estados, como aqueles localizados nas regiões Norte e Nordeste, enfrentaram dificuldades adicionais devido à falta de diversificação econômica, infraestrutura inadequada e questões relacionadas à logística e transporte. Programas como o Plano Brasil Maior foram lançados para fortalecer a indústria nacional, promovendo a inovação, a competitividade e o acesso ao crédito para empresas.

2016-2021: Recuperação Desigual e Impacto da Pandemia
Embora a indústria tenha mostrado sinais de recuperação após a recessão, a recuperação foi desigual entre os estados. Enquanto algumas regiões continuaram a crescer, outras enfrentaram desafios persistentes, como baixo investimento em infraestrutura, burocracia e falta de incentivos fiscais. O Paraná, por exemplo, destacou-se pelo crescimento constante de sua indústria, impulsionado por programas como o Paraná Competitivo, que ofereceu incentivos fiscais e facilitou o ambiente de negócios para atrair investimentos e promover o desenvolvimento econômico regional.
 ''',)
