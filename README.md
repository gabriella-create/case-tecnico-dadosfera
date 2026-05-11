# Case Técnico: Plataforma Dadosfera 🚀
**Candidata:** [Seu Nome Completo]
**Objetivo:** Demonstrar o ciclo de vida completo do dado, da concepção ao valor de negócio.

---

## 📅 Item 0 - Agilidade e Planejamento (PMBOK)
Para este projeto, utilizei uma abordagem baseada nas melhores práticas do **PMBOK**. O planejamento foi dividido em fases para garantir que a solução técnica atendesse aos requisitos de negócio da Dadosfera.

### Fluxograma do Processo (Pipeline de Dados)
Este fluxograma representa o caminho que o dado percorre: desde o nascimento (script) até a entrega final (dashboard).

```mermaid
graph TD
    classDef bronze fill:#cd7f32,stroke:#333,stroke-width:2px,color:#fff;
    classDef silver fill:#c0c0c0,stroke:#333,stroke-width:2px;
    classDef gold fill:#ffd700,stroke:#333,stroke-width:2px;
    classDef tech fill:#f9f,stroke:#333,stroke-width:2px;
    classDef delivery fill:#bbf,stroke:#333,stroke-width:2px;

    START[Início: Script Python 100k registros] --> BRONZE(Camada Bronze: Dados Brutos / Raw)
    BRONZE --> QUALITY{Data Quality: Limpeza}
    QUALITY --> SILVER(Camada Silver: Dados Padronizados)
    SILVER --> AI[Processamento GenAI: Extração de Atributos]
    AI --> GOLD(Camada Gold: Dados Refinados / Business)
    GOLD --> DASH[Dashboard: Metabase / Visualização]
    DASH --> APP[Data App: Streamlit]

    class START tech;
    class BRONZE bronze;
    class SILVER silver;
    class GOLD gold;
    class DASH,APP delivery;

## 📊 Item 1: Base de Dados (+100.000 registros)
Desenvolvi um script robusto em Python (localizado na pasta /scripts) para gerar **100.000 registros sintéticos** de E-commerce.
 * **Objetivo:** Simular o volume real de uma operação de grande porte e testar a escalabilidade da Dadosfera.
 * **Campos:** IDs únicos, carimbos de data/hora, categorias, preços unitários e descrições qualitativas.
## 📂 Item 2: Catalogação de Dados
Utilizei a governança da Dadosfera para catalogar cada ativo de dado gerado.
 * **Metadados:** Definição de tipos de dados e tags de sensibilidade (LGPD).
 * **Linhagem:** Rastreamento completo para garantir que o usuário final saiba a origem de cada informação.
## 🔍 Item 3: Exploração de Dados (EDA)
Realizei a análise exploratória via SQL e ferramentas visuais. Esta fase foi essencial para validar padrões de compra e identificar sazonalidades, garantindo que o modelo de negócio fosse baseado em tendências reais observadas na base.
## 🧼 Item 4: Qualidade de Dados (Data Quality)
Para garantir a confiabilidade das decisões, apliquei rotinas de limpeza:
 * **Null Check:** Remoção de registros sem identificação essencial.
 * **Range Check:** Garantia de que preços e quantidades sejam positivos e lógicos.
 * **Deduplicação:** Limpeza de transações repetidas geradas por simulação de falhas.
## 🤖 Item 5: Inteligência Artificial (GenAI / LLM)
Utilizei modelos de IA Generativa para o enriquecimento da base:
 * **Extração de Atributos:** A IA lê a descrição textual e extrai automaticamente "Cor", "Material" e "Marca".
 * **Valor Gerado:** Transformação de dados não estruturados (textos) em colunas prontas para análise de BI.
## 🏗️ Item 6: Modelagem de Dados (Kimball)
Apliquei a arquitetura **Star Schema (Esquema Estrela)**:
 * **Tabela Fato:** Métricas de performance de vendas (Preços, Qtd).
 * **Tabelas Dimensão:** Produtos (enriquecidos pela IA), Clientes, Tempo e Localidade.
 * **Vantagem:** Otimização máxima para consultas rápidas em dashboards.
## 📈 Item 7: Visualização de Dados (Dashboards)
Desenvolvi painéis no **Metabase** focados em KPIs de alto nível para a gestão:
 * Evolução do faturamento mensal.
 * Ticket médio por categoria de produto.
 * Ranking de produtos mais vendidos.
## ⚙️ Item 8: Pipelines de Dados
Os pipelines foram automatizados para realizar o movimento entre as camadas **Medalhão (Bronze -> Silver -> Gold)**. Cada etapa possui logs de execução e monitoramento de integridade.
## 🚀 Item 9: Data App (Streamlit)
Desenvolvi uma interface interativa que permite ao usuário final explorar a base de 100k registros utilizando os filtros gerados pela IA, demonstrando a agilidade da Dadosfera na entrega de produtos de dados.
## 💡 Item 10: Apresentação e Viabilidade Técnica
A Dadosfera se prova a melhor solução técnica para o cliente pois:
 * **All-in-One:** Centraliza Engenharia, Governança e BI em uma única interface amigável.
 * **TCO Reduzido:** Diminui drasticamente o gasto com licenciamento e integração de ferramentas fragmentadas.
 * **Time-to-Value:** Acelera a entrega de insights estratégicos, transformando meses de desenvolvimento em dias de configuração.
**Nota:** Este projeto foi desenvolvido como demonstração técnica para o processo seletivo da Dadosfera.
