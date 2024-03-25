import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium
from streamlit_folium import folium_static
import json
import math
import plotly.graph_objects as go


# Aqui onde configuramos o título da página e o logo que aparecerá no Browser!!!
st.set_page_config(
    page_title="RAIO X DO PIB BRASILEIRO",
    page_icon='assets/logo.png',
    layout="wide",
    initial_sidebar_state="expanded",
)


df = pd.read_csv('data/pibmun.csv', low_memory=False)

df['PIB'] = df['PIB']/1000000

# Object notation
with st.sidebar:
    # Inserir imagem fixa
    st.write('Desenvolvido por:')
    st.write('Allan Bispo')
    st.write('Rogério Tiúma')

    st.image('assets/raiox_pib.png',use_column_width = True)
    values = st.slider('Escolha o ano', df['Ano'].min(), df['Ano'].max())
    estados_selecionados = st.multiselect(
        'Selecione os estados',
        df['Estado'].unique(),
        df['Estado'].unique()
    )

    todos_os_estados_selecionados = 'Todos os estados' in estados_selecionados

    if todos_os_estados_selecionados:
        chart_data_estado = df[df['Ano'] == values].groupby('Estado')['PIB'].sum().reset_index().round(2)
    else:
        chart_data_estado = df[(df['Ano'] == values) & (df['Estado'].isin(estados_selecionados))].groupby('Estado')['PIB'].sum().reset_index().round(2)

    if todos_os_estados_selecionados:
        chart_data_municipio = df[df['Ano'] == values].groupby(['UF', 'Município'])['PIB'].sum().reset_index().round(2)
    else:
        chart_data_municipio = df[(df['Ano'] == values) & (df['Estado'].isin(estados_selecionados))].groupby(['UF', 'Município'])['PIB'].sum().reset_index().round(2)

col1, col2 = st.columns(2)

with col1:
    st.markdown("<h1 style='text-align: center;'>PIB dos Estados</h1>", unsafe_allow_html=True)
    chart_data_estado_ordem = chart_data_estado.sort_values('PIB', ascending=True)   
    soma_pib_estado = chart_data_estado_ordem['PIB'].sum().round(2)
    st.write(f'Soma do PIB para os estados selecionados: {soma_pib_estado}')

    fig_estado = px.bar(chart_data_estado_ordem, x='PIB', y='Estado', orientation='h', text='PIB',
                labels={'PIB': 'PIB Total (Em Milhões)', 'Estado': 'Estado'},
                title=f'PIB por Estado no Ano {values} (Ordenado)',
                color_discrete_sequence=['#2E7D32'])
    fig_estado.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig_estado.update_layout(coloraxis_showscale=False)
    fig_estado.update_layout(height=800, width=900)
    
    # Definindo o fundo cinza
    fig_estado.update_layout(plot_bgcolor='#f2f2f2', paper_bgcolor='#f2f2f2')
   
    
    st.plotly_chart(fig_estado)

with col2:
    st.markdown("<h1 style='text-align: center;'>PIB dos Municípios</h1>", unsafe_allow_html=True)
    chart_data_municipio_ordem = chart_data_municipio.sort_values('PIB', ascending=False)  
    soma_pib_municipio = chart_data_municipio_ordem['PIB'].sum().round(2)
    st.write(f'Soma do PIB para os municípios selecionados: {soma_pib_municipio}')

    top_10_municipios = chart_data_municipio_ordem.head(20)

    fig_municipio = px.bar(top_10_municipios, x='PIB', y='Município', orientation='h', text='PIB',
                labels={'PIB': 'PIB Total (Em milhões)', 'UF': 'UF'},
                title=f'PIB por Município no Ano {values} (Top 20)',
                color_discrete_sequence=['#2E7D32'])
    
    fig_municipio.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig_municipio.update_layout(coloraxis_showscale=False)
    fig_municipio.update_layout(plot_bgcolor='#f2f2f2', paper_bgcolor='#f2f2f2')
    fig_municipio.update_layout(height=800, width=920)
    st.plotly_chart(fig_municipio)

# Criando um contêiner
with st.container():
    col3, col4 = st.columns(2)
    with col3:
        def load_municipios_json(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                municipios_data = json.load(f)
            return municipios_data

        municipios_data = load_municipios_json('data/BR.json')
        df_ano = df[(df['Ano'] == int(values)) & (df['Estado'].isin(estados_selecionados))]
        df_ano['IBGE'] = df_ano['IBGE'].astype(str)

        # Lista das colunas a serem mantidas
        colunas_mantidas = ['Ano', 'Município', 'PIB', 'IBGE','Estado','VAB Agropecuária', 'VAB Indústria','VAB Serviços','VAB AdmDefEduSaude','Impostos']

        # Exclui as colunas que não estão na lista de colunas mantidas
        df_ano = df_ano.drop(columns=[col for col in df.columns if col not in colunas_mantidas])
        df_ano.loc[:, 'PIB'] = (df_ano['PIB'].astype(float)).round(2)
        df_ano.loc[:, 'VAB Agropecuária'] = (df_ano['VAB Agropecuária'].astype(float)/1000000).round(2)
        df_ano.loc[:, 'VAB Indústria'] = (df_ano['VAB Indústria'].astype(float)/1000000).round(2)
        df_ano.loc[:, 'VAB Serviços'] = (df_ano['VAB Serviços'].astype(float)/1000000).round(2)
        df_ano.loc[:, 'VAB AdmDefEduSaude'] = (df_ano['VAB AdmDefEduSaude'].astype(float)/1000000).round(2)
        df_ano.loc[:, 'Impostos'] = (df_ano['Impostos'].astype(float)/1000000).round(2)
        
        # Definindo o tamanho do mapa diretamente com HTML/CSS
        st.markdown('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        st.markdown('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        st.markdown('<style>div.Widget.row-widget.stRadio > div > label{padding:2px 10px;}</style>', unsafe_allow_html=True)
        st.markdown('<style>div.row-widget.stRadio > div > label{padding:2px 10px;}</style>', unsafe_allow_html=True)

        st.markdown("<h1 style='text-align: center;'>Mapa do PIB por Município</h1>", unsafe_allow_html=True)
        #st.write("## Mapa do PIB por Município")
        #st.write(f'Ano selecionado: {values}')

        #Tratando arquivo json
        df_index = df_ano
        df_index.set_index('IBGE',inplace=True)
        
        PIB_max = df_ano['PIB'].round(2).max()

        # Criando um intervalo de cores personalizado
        threshold_scale = [0, PIB_max*0.01, PIB_max*0.05, PIB_max*0.1, PIB_max*0.25, PIB_max*0.5, PIB_max]
        
        # Conjunto para armazenar os índices (ou chaves) de municípios já processados
        indices_processados = set()

        # Itera sobre os recursos (features) em municipios_data
        for state in municipios_data['features']:
            codarea = state['properties']['codarea']  # Obtém o valor de 'codarea'
            
            # Verifica se 'codarea' está presente no índice de pibmun
            if codarea in df_index.index:
                # Verifica se o índice já foi processado
                if codarea not in indices_processados:
                    # Adiciona o índice ao conjunto de índices processados
                    indices_processados.add(codarea)
                    
                    # Copia as propriedades para 'state' em municipios_data
                    state['properties']['PIB'] = df_index.loc[codarea, 'PIB']
                    state['properties']['VAB Agropecuária'] = df_index.loc[codarea, 'VAB Agropecuária']
                    state['properties']['VAB Indústria'] = df_index.loc[codarea, 'VAB Indústria']
                    state['properties']['VAB Serviços'] = df_index.loc[codarea, 'VAB Serviços']
                    state['properties']['VAB AdmDefEduSaude'] = df_index.loc[codarea, 'VAB AdmDefEduSaude']
                    state['properties']['Impostos'] = df_index.loc[codarea, 'Impostos']
                    state['properties']['Município'] = df_index.loc[codarea, 'Município']
                    state['properties']['Estado'] = df_index.loc[codarea, 'Estado']
                else:
                    # Se o índice não foi encontrado, remova as propriedades do estado
                    state['properties']['PIB'] = 0.00
                    state['properties']['VAB Agropecuária'] = 0.00
                    state['properties']['VAB Indústria'] = 0.00
                    state['properties']['VAB Serviços'] = 0.00
                    state['properties']['VAB AdmDefEduSaude'] = 0.00
                    state['properties']['Impostos'] = 0.00
                    state['properties']['Município'] = "Não encontrado"
                    state['properties']['Estado'] = "Não encontrado"
            else:
                    # Se o índice não foi encontrado, remova as propriedades do estado
                    state['properties']['PIB'] = 0.00
                    state['properties']['VAB Agropecuária'] = 0.00
                    state['properties']['VAB Indústria'] = 0.00
                    state['properties']['VAB Serviços'] = 0.00
                    state['properties']['VAB AdmDefEduSaude'] = 0.00
                    state['properties']['Impostos'] = 0.00
                    state['properties']['Município'] = "Não encontrado"
                    state['properties']['Estado'] = "Não encontrado"


        # Certifique-se de que o caminho do arquivo está correto
        caminho_arquivo_json = 'data/municipios_data_final.json'

        # Salva o arquivo JSON
        with open(caminho_arquivo_json, 'w') as f:
            json.dump(municipios_data, f)

        # Carrega o arquivo JSON de volta para a variável municipios_data_final
        with open(caminho_arquivo_json, 'r') as f:
            municipios_data_final = json.load(f)
            

            # Carrega o arquivo JSON
            with open('data/municipios_data_final.json', 'r') as f:
                municipios_data_final = json.load(f)

            #st.write(df_ano)
            #print(type(df_ano))
            

            # Criando o mapa coroplético com Streamlit Folium
            mapa_PIB = folium.Map(location=[-13.4008012,-46.4565518], tiles = "cartodbpositron", zoom_start = 4)

            folium.Choropleth(geo_data = municipios_data_final, data = df_ano, columns = [df_ano.index,"PIB"], key_on = "feature.properties.codarea", fill_color = "YlGnBu", fill_opacity = 0.8, line_opacity = 0.5, legend_name = "PIB", nan_fill_color = "black", name = "cloropleth", threshold_scale=threshold_scale).add_to(mapa_PIB)

            
            #Adicionando a função de destaque
            estilo = lambda x: {"fillColor": "white", "color": "black", "fillOpacity": 0.01, "weight": 0.001}
            estilo_destaque = lambda x: {"fillColor": "#2E7D32", "color": "black", "fillOpacity": 0.5, "weight": 1}
            highlight = folium.features.GeoJson(data = municipios_data_final, style_function = estilo, highlight_function = estilo_destaque, name = "Destaque")

            # Adicionando caixa de texto
            folium.features.GeoJsonTooltip(fields=['Município', 'PIB','VAB Agropecuária', 'VAB Indústria','VAB Serviços','VAB AdmDefEduSaude','Impostos','Estado'], 
                                        aliases=["Município:", "PIB (R$ em Milhões):",'VAB Agropecuária (R$ em Milhões):', 'VAB Indústria (R$ em Milhões):','VAB Serviços (R$ em Milhões):','VAB AdmDefEduSaude (R$ em Milhões):','Impostos (R$ em Milhões):',"Estado"], 
                                        labels=True, style=("background-color: white; color: black; font-family: arial; font-size: 16px; padding: 10px;")).add_to(highlight)

            #Adicionando o destaque ao mapa
            mapa_PIB.add_child(highlight) 

            #Adicionando o controle de camadas
            folium.LayerControl().add_to(mapa_PIB)

            # Exibindo o mapa com Streamlit
            folium_static(mapa_PIB, width=900, height=990)


    with col4:
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        #st.write("## Mapa do PIB por Setor")
        st.markdown("<h1 style='text-align: center;'>Mapa do PIB por Setor</h1>", unsafe_allow_html=True)

        # Filtre o DataFrame com base no ano e estados escolhidos
        if todos_os_estados_selecionados:
            chart_data_col4 = df[df['Ano'] == values].groupby('Estado').sum()[['VAB Agropecuária', 'VAB Indústria', 'VAB Serviços', 'VAB AdmDefEduSaude']].reset_index()
            chart_data_col4[['VAB Agropecuária', 'VAB Indústria', 'VAB Serviços', 'VAB AdmDefEduSaude']] = chart_data_col4[['VAB Agropecuária', 'VAB Indústria', 'VAB Serviços', 'VAB AdmDefEduSaude']].round(2)
        else:
            chart_data_col4 = df[(df['Ano'] == values) & (df['Estado'].isin(estados_selecionados))].groupby('Estado').sum()[['VAB Agropecuária', 'VAB Indústria', 'VAB Serviços', 'VAB AdmDefEduSaude']].reset_index()
            chart_data_col4[['VAB Agropecuária', 'VAB Indústria', 'VAB Serviços', 'VAB AdmDefEduSaude']] = chart_data_col4[['VAB Agropecuária', 'VAB Indústria', 'VAB Serviços', 'VAB AdmDefEduSaude']].round(2)                                                                    
        # Ordene os dados pelo PIB
        chart_data_ordem = chart_data_col4.sort_values('VAB Serviços', ascending=True) 

        # Definindo cores personalizadas
        colors_custom = ['#FF5722', '#1565C0', '#2E7D32','#FFEB3B']


        def grafico_barras_horizontal(df):

            # Transforma o DataFrame para o formato "longo" usando melt
            df_long = df.melt(id_vars=['Estado'], var_name='Setor', value_name='VAB')

            # Cria o gráfico de barras horizontais
            fig = px.bar(df_long, 
                        x='VAB', 
                        y='Estado', 
                        color='Setor', 
                        orientation='h', 
                        title='VAB por Estado e Setor',
                        height=1000, color_discrete_sequence=colors_custom)
            
            # Define o estilo da fonte
            #fig.update_layout(title_font=dict(size=30), font=dict(size=20))
            #fig.update_layout(title=dict(text="GDP-per-capita", font=dict(size=50), 
                                        # automargin=True, yref='paper'))
            
            fig.update_layout(barmode='stack', yaxis={'categoryorder':'total ascending'})            
            fig.update_layout(plot_bgcolor='#f2f2f2', paper_bgcolor='#f2f2f2')
            
            # Exibe o gráfico
            st.plotly_chart(fig, use_container_width=True, height=500)
            
        
        grafico_barras_horizontal(chart_data_ordem)