# Case Técnico: Plataforma Dadosfera 🚀
**Candidata:** Gabriella Dias 
**Objetivo:** Demonstrar o ciclo de vida completo do dado, da concepção ao valor de negócio.

---

## 📅 Item 0 - Agilidade e Planejamento (PMBOK)
Para este projeto, utilizei uma abordagem baseada nas melhores práticas do *PMBOK*. O planejamento foi dividido em fases para garantir que a solução técnica atendesse aos requisitos de negócio da Dadosfera.

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
    class DASH,APP delivery;'''
## 📊 Item 1: Base de Dados (+100k registros)
Foi desenvolvido um script em Python para gerar uma base sintética de 100.000 registros, garantindo volume para testes de performance e diversidade de categorias.
* *Domínio:* Varejo Digital.
* *Ativos:* Clientes, Produtos, Pedidos e Vendedores.

---

## 🧼 Item 4: Relatório de Qualidade de Dados
Utilizei práticas de Data Quality para identificar e tratar:
- *Nulos:* Remoção de registros sem ID de produto.
- *Inconsistências:* Ajuste de preços negativos ou zerados.
- *Padronização:* Normalização de estados e cidades brasileiros.
## 🤖 Item 5: Processamento com GenAI
Transformação de descrições textuais desestruturadas em atributos técnicos (JSON).
- *Input:* "Smartphone X, 128GB, cor Preto, acabamento em vidro."
- *Output:* {"memoria": "128GB", "cor": "Preto", "material": "Vidro"}

---

## 🏆 Item 10: Conclusão e Viabilidade
A Dadosfera se provou a melhor solução técnica por:
- *Redução de Custos:* Menos ferramentas para gerenciar.
- *Time-to-Value:* Implementação rápida de modelos de IA.
- *Integração:* Unifica engenharia, governança e análise em um só lugar.
