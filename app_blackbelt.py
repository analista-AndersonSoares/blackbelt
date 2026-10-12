import streamlit as st

# Configuração da página (deve ser a primeira chamada do Streamlit)
st.set_page_config(
    page_title="Portfólio Black Belt | Anderson Soares",
    page_icon="🥋",
    layout="wide"
)

def main():
    # Menu lateral para futura navegação entre as fases do DMAIC
    st.sidebar.title("Navegação")
    page = st.sidebar.radio("Ir para:", ["Apresentação", "Projetos DMAIC", "Contato"])

    if page == "Apresentação":
        show_presentation()
    elif page == "Projetos DMAIC":
        st.info("Em breve: Registro dos projetos práticos aplicando Define, Measure, Analyze, Improve e Control.")
    elif page == "Contato":
        st.info("Em breve: Links para o seu GitHub e LinkedIn.")

def show_presentation():
    # Título principal
    st.title("Portfólio de Certificação Black Belt 🥋")
    st.markdown("---")

    # Divisão da tela em duas colunas
    col1, col2 = st.columns([1, 1.2])

    with col1:
        st.header("Sobre Mim")
        st.subheader("Anderson Pereira Miranda Soares")
        st.write("""
        Sou um profissional com uma base analítica sólida e foco em melhoria contínua. 
        Tenho formação técnica em Química (CRQ ativo) e atuei por mais de uma década na 
        indústria química, passando por toda a cadeia de valor: desde a operação fabril 
        e estações de tratamento de água/efluentes até a rotina minuciosa de laboratório 
        e controle de qualidade.
        
        Atualmente, curso Gestão Empresarial na FATEC e atuo no suporte técnico de ERP 
        para gestão pública, utilizando diariamente SQL e estruturando dados. Uno minha 
        bagagem industrial com programação em Python (Pandas, SciPy, Streamlit) para 
        otimizar processos, validar documentos e extrair inteligência de dados.
        """)
        
        st.write("**Certificações e Ferramentas:**")
        st.write("- Lean Six Sigma: Green Belt (Rumo ao Black Belt!)")
        st.write("- Linguagens: Python, SQL")
        st.write("- Ferramentas: Streamlit, Plotly, Power BI, Excel, DBeaver, Git/GitHub")
        st.write("- Sistema Operacional: Linux (Zorin OS) e Windows")

    with col2:
        st.header("O que é o Black Belt?")
        st.write("""
        A certificação **Lean Six Sigma Black Belt** atesta a capacidade de um profissional 
        em liderar projetos complexos de melhoria contínua, reduzindo variabilidades, 
        eliminando desperdícios e gerando impacto financeiro real para o negócio.
        """)
        
        st.info("""
        **Metodologia DMAIC:**
        - **D (Define):** Definição clara do problema, escopo, métricas (SIPOC, VOC, Árvore CTC).
        - **M (Measure):** Coleta de dados, avaliação de estabilidade e capabilidade do processo.
        - **A (Analyze):** Análise estatística profunda (Testes de Hipótese, ANOVA, Regressão) para encontrar as causas-raiz.
        - **I (Improve):** Planejamento de Experimentos (DoE) e implementação de melhorias.
        - **C (Control):** Padronização, CEP (Controle Estatístico de Processo) e garantia de resultados a longo prazo.
        """)

        st.write("""
        **Objetivo deste Portfólio:**
        Este espaço foi desenvolvido em Python/Streamlit para documentar minha jornada de 
        estudos e projetos práticos. Aqui, registrarei a aplicação de ferramentas estatísticas e 
        de gestão da qualidade, consolidando meu aprendizado e demonstrando minhas habilidades 
        na resolução de problemas complexos.
        """)

if __name__ == "__main__":
    main()