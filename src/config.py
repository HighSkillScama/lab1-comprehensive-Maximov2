"""
Конфигурационный файл микросервиса «Расчет корзины и скидок».
Содержит настройки подключения к БД и бизнес-константы.
"""

import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "loyalty_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "secret")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


BASE_DISCOUNT_THRESHOLD = 15000.0  # Порог суммы корзины для базовой скидки
BASE_DISCOUNT_RATE = 0.85          # Базовая скидка 15%

# Промокоды
PROMO_SUMMER_VALUE = 500.0         # Скидка по промокоду SUMMER (в рублях)
PROMO_VIP_RATE = 0.90              # Множитель цены по промокоду VIP

# Уровни лояльности (Tier)
TIER_1_RATE = 0.97                 # Скидка для 1-го уровня лояльности (3%)
TIER_2_RATE = 0.93                 # Скидка для 2-го уровня лояльности (7%)

# Ограничения
MAX_DISCOUNT_RATE = 0.70           # Максимально возможная скидка (цена не может упасть ниже 70% от исходной)
