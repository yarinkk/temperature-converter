# Temperature Converter

## Опис

Програма конвертує температуру з градусів Цельсія у градуси Фаренгейта.

---

## Формула конвертації

:contentReference[oaicite:0]{index=0}

---

## Встановлення

Створення віртуального середовища:

```bash
python -m venv venv
```

Активація:

### Windows

```bash
venv\Scripts\activate
```

### Linux / MacOS

```bash
source venv/bin/activate
```

Встановлення залежностей:

```bash
pip install -r requirements.txt
```

---

## Запуск програми

```bash
python main.py
```

Приклад роботи:

```text
Введіть температуру у Цельсіях: 25
Температура у Фаренгейтах: 77.0
```

---

## Тестування

### pytest

```bash
pytest
```

### doctest

```bash
python -m doctest app/converter.py -v
```

---

## Docker

### Збірка Docker-образу

```bash
docker build -t temperature-converter .
```

### Запуск контейнера

```bash
docker run -it temperature-converter
```



