# Пример диаграммы Mermaid

Синтаксис для раздела 4.1 design doc. В VS Code / Cursor откройте превью Markdown: блок ниже должен отрисоваться как схема.

Это **пример синтаксиса**, а не универсальная архитектура. В проекте замените компоненты на свои (иначе схема не пройдёт проверку на специфичность).

Альтернатива: тот же код в файле `diagrams/architecture.mmd` и ссылка из §4.1.

```mermaid
flowchart TB
  subgraph ingest ["Данные"]
    Events["События заказа<br/>Kafka"]
    Warehouse["Витрина признаков<br/>ClickHouse"]
    Labels["Разметка фрода<br/>Label Studio"]
  end

  subgraph training ["Training"]
    Features["Daily feature job"]
    Train["Обучение LightGBM"]
    Registry["Model Registry<br/>MLflow"]
  end

  subgraph serving ["Serving"]
    API["Fraud API<br/>p95 ≤ 80 мс"]
    Model["Модель v3 в памяти"]
    Rules["Правила: сумма, страна, velocity"]
    Queue["Очередь HITL<br/>если score ≥ 0.72"]
    Analyst["Антифрод-аналитик"]
  end

  Checkout["Checkout"] --> API
  API --> Model
  API --> Rules
  Model --> API
  API -->|"score < 0.72"| Checkout
  API -->|"score ≥ 0.72"| Queue
  Queue --> Analyst

  Events --> Warehouse
  Warehouse --> Features
  Labels --> Train
  Features --> Train
  Train --> Registry
  Registry -->|canary 5%| Model
```

## Как читать

- два потока на одной схеме: **serving** (онлайн-запрос) и **training** (батч до реестра);
- есть деталь кейса, которую нельзя перенести в чужой проект без правок: порог 0.72, HITL, LightGBM, Kafka → ClickHouse;
- подписи на стрелках — контракт или условие, не декорация.

Документация: [https://mermaid.js.org/syntax/flowchart.html](https://mermaid.js.org/syntax/flowchart.html)
