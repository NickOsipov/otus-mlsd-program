# Материалы для подготовки к курсу ML System Design

Для прохождения курса не требуется заранее читать все материалы целиком. Достаточно ознакомиться с основными концепциями: жизненным циклом ML-системы, требованиями к production ML, работой с данными, serving, monitoring и техническим долгом.

## Книги

### 1. Chip Huyen — Designing Machine Learning Systems

Одна из основных книг по проектированию production ML-систем.

Рассматриваются:

- постановка задачи и выбор ML-метрик;
- сбор и подготовка данных;
- training и inference pipelines;
- batch и online inference;
- data distribution shifts;
- monitoring;
- continual learning;
- инфраструктура ML-платформ.

Книга строится вокруг требований **reliability, scalability, maintainability и adaptability**.

Ссылка:
[https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/)

---

### 2. Valerii Babushkin, Arseny Kravchenko — Machine Learning System Design

Практическая книга, непосредственно посвящённая процессу ML System Design: от анализа задачи и требований до deployment и дальнейшей эксплуатации системы. Рассматриваются метрики, работа с датасетами, error analysis, архитектурные решения и типичные ошибки при проектировании ML-систем.

Ссылка:
[https://www.manning.com/books/machine-learning-system-design](https://www.manning.com/books/machine-learning-system-design)

Хорошо подходит как дополнительная книга к Designing Machine Learning Systems.

---

### 3. Valliappa Lakshmanan, Sara Robinson, Michael Munn — Machine Learning Design Patterns

Каталог архитектурных и инженерных паттернов, встречающихся при создании ML-систем. Авторы систематизируют практики, накопленные при работе с большим количеством production ML-команд.

Полезна для понимания того, какие решения регулярно повторяются в реальных ML-проектах.

Ссылка:
[https://www.oreilly.com/library/view/machine-learning-design/9781098115777/](https://www.oreilly.com/library/view/machine-learning-design/9781098115777/)

---

### 4. Martin Kleppmann, Chris Riccomini — Designing Data-Intensive Applications, 2nd Edition

Книга не непосредственно про Machine Learning, но даёт важную базу по System Design: reliability, scalability, distributed systems, storage, replication, stream processing, event-driven architectures и выбору архитектурных компромиссов.

Вторая редакция вышла в 2026 году и существенно обновляет материал по современным data systems.

Ссылка:
[https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/)

---

### 5. Andriy Burkov — Machine Learning Engineering

Книга про инженерную сторону ML-проекта: что происходит до и после обучения модели.

Рассматриваются:

- определение задачи и достижимость целей;
- сбор, разметка и валидация данных;
- feature engineering и утечки данных;
- обучение, оценка и тестирование модели;
- deployment, версионирование и поддержка модели в продакшене;
- типичные ошибки и антипаттерны ML-проектов.

Полезна тем, что даёт чеклисты и практические правила для каждого этапа жизненного цикла.

Главы доступны бесплатно (принцип «read first, buy later»).

Ссылка:
[https://www.mlebook.com/](https://www.mlebook.com/)

Бесплатные главы:
[http://www.mlebook.com/wiki/doku.php](http://www.mlebook.com/wiki/doku.php)

---

# Статьи и бесплатные материалы

### 1. Google — Rules of Machine Learning

Классический материал Google о том, как строить ML-системы в production.

Особенно полезны идеи:

- сначала строить простую систему;
- отделять ML-задачу от продуктовой задачи;
- правильно проектировать features и pipelines;
- учитывать изменение данных со временем;
- контролировать training-serving skew.

В материале собрано 43 практических правила разработки ML-систем.

Ссылка:
[https://developers.google.com/machine-learning/guides/rules-of-ml](https://developers.google.com/machine-learning/guides/rules-of-ml)

---

### 2. Hidden Technical Debt in Machine Learning Systems

David Sculley et al., Google.

Одна из наиболее известных работ по ML Engineering. Показывает, почему production ML-система значительно сложнее самой модели.

Авторы рассматривают такие проблемы, как:

- data dependencies;
- feedback loops;
- configuration debt;
- entanglement;
- undeclared consumers;
- изменение внешнего мира;
- технический долг ML-систем.

Ссылка:
[https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html](https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)

---

### 3. The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction

Eric Breck et al., Google.

Работа посвящена вопросу: **как определить, действительно ли ML-система готова к production?**

Авторы предлагают набор из 28 проверок, связанных с:

- данными;
- моделями;
- инфраструктурой;
- monitoring;
- production reliability.

Ссылка:
[http://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/](http://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/)

---

### 4. Made With ML — Machine Learning Systems Design

Практический бесплатный материал Goku Mohandas по проектированию ML-систем.

Автор рассматривает последовательность:

**Product Design → System Design → Development → Deployment → Iteration**

и показывает, как перейти от бизнес-задачи к архитектуре ML-системы. ([madewithml.com][10])

ML System Design:
[https://madewithml.com/courses/mlops/systems-design/](https://madewithml.com/courses/mlops/systems-design/)

Полный курс:
[https://madewithml.com/courses/mlops/](https://madewithml.com/courses/mlops/)

---

### 5. Google Cloud — MLOps: Continuous delivery and automation pipelines in machine learning

Гайд Google Cloud об автоматизации ML-систем: CI, CD и continuous training.

Авторы описывают три уровня зрелости MLOps:

- level 0 — полностью ручной процесс, модель передаётся в продакшен «руками»;
- level 1 — автоматизированный ML-pipeline с continuous training, валидацией данных и модели, триггерами и metadata management;
- level 2 — автоматизированный CI/CD для самих пайплайнов: сборка, тесты и деплой компонентов, model registry, serving, monitoring.

Удобно использовать как общий язык при обсуждении того, на каком уровне находится проектируемая система и какой следующий шаг оправдан по стоимости.

Ссылка:
[https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)

---

