# 📦 Restful-booker API Tests

[![Build Status](https://github.com/marinagrieg/AcademITSAutoPython/actions/workflows/run-tests.yml/badge.svg)](https://github.com/marinagrieg/AcademITSAutoPython/actions)
[![Allure Report](https://img.shields.io/badge/Allure-Report-blueviolet?logo=allure&style=flat-square)](https://marinagrieg.github.io/AcademITSAutoPython/)

API-тесты для [Restful-booker](https://restful-booker.herokuapp.com) — домашнее задание №7 по теме CI/CD (папка `6. Restful booker`).

## Технологии

- Python 3.14
- pytest
- requests
- pydantic
- Allure Report (allure-pytest)
- GitHub Actions
- GitHub Pages

## Запуск тестов из консоли

```bash
pip install -r requirements.txt
pytest "6. Restful booker" -v --alluredir=allure-results
```

## ⚙️ CI/CD Pipeline Overview

```mermaid
graph TD;
    Code[🧠 Push Code] --> Test[🧪 Run API Tests];
    Test --> Allure[📊 Generate Allure Report];
    Allure --> Pages[🌐 Publish to GitHub Pages];
    Test --> GH[🔁 Save History to Artifact];
    GH --> Allure;
```