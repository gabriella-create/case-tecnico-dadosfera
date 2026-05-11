# Case Técnico: Plataforma Dadosfera 🚀
**Candidata:** [Gabriella Dias Fidelis Rosa]
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
