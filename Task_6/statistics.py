import psycopg2
import pandas as pd
import numpy as np
from scipy import stats


#Step_1_Подключение

print("ЗАДАНИЕ 1: АНАЛИЗ ДАННЫХ ИЗ БАЗЫ ДАННЫХ")
connection = psycopg2.connect

print("\n Шаг 1: Подключение к PostgreSQL-контейнеру УСПЕШНО!")
print(f"   - Хост: localhost:5432")
print(f"   - База данных: testdb")
print(f"   - Пользователь: postgres")
#Step_2_sql_resp

print("ШАГ 2: ВЫПОЛНЕНИЕ SQL-ЗАПРОСА С JOIN")


query = """
    SELECT 
        pr.id AS price_id,
        pr.product_id,
        pr.price,
        pr.created_at,
        p.name AS product_name,
        p.category
    FROM prices pr
    JOIN products p ON pr.product_id = p.id
    ORDER BY pr.price DESC;
"""

#Download_in_pandas
df = pd.read_sql(query, connection)

print(f"\n SQL-запрос выполнен успешно!")
print(f"   - Загружено записей: {len(df)}")
print(f"   - Колонки: {', '.join(df.columns)}")

#Close_connection_with_DB
conn.close()
print(f"\n Соединение с базой данных закрыто")

#Show_5_steps
print(f"\n Первые 5 записей из загруженных данных:")
print(df.head().to_string(index=False))

#Step_3_things
print("\n" + "=" * 70)
print("ШАГ 3: ОСНОВНЫЕ СТАТИСТИЧЕСКИЕ ПОКАЗАТЕЛИ ЦЕН")
print("=" * 70)

mean_price = df['price'].mean()
median_price = df['price'].median()
std_price = df['price'].std()
min_price = df['price'].min()
max_price = df['price'].max()

print(f"\n Статистика цен на товары (в рублях):")
print(f"   {'Среднее значение:':<25} {mean_price:>15,.2f} руб.")
print(f"   {'Медиана:':<25} {median_price:>15,.2f} руб.")
print(f"   {'Стандартное отклонение:':<25} {std_price:>15,.2f} руб.")
print(f"   {'Минимальная цена:':<25} {min_price:>15,.2f} руб.")
print(f"   {'Максимальная цена:':<25} {max_price:>15,.2f} руб.")

#Step_4_rayoni_kvartalyi
print("\n" + "=" * 70)
print("ШАГ 4: КВАРТИЛИ, МЕЖКВАРТИЛЬНЫЙ РАЗМАХ И ВЫБРОСЫ")
print("=" * 70)

Q1 = df['price'].quantile(0.25)  
Q2 = df['price'].quantile(0.50)   
Q3 = df['price'].quantile(0.75)   
IQR = Q3 - Q1                      

print(f"\n Квартили распределения цен:")
print(f"   {'Первый квартиль (Q1, 25%):':<35} {Q1:>12,.2f} руб.")
print(f"   {'Второй квартиль (Q2, 50% = медиана):':<35} {Q2:>12,.2f} руб.")
print(f"   {'Третий квартиль (Q3, 75%):':<35} {Q3:>12,.2f} руб.")
print(f"   {'Межквартильный размах (IQR = Q3 - Q1):':<35} {IQR:>12,.2f} руб.")

#Items_higher_than_Q3
high_price_products = df[df['price'] > Q3].copy()
high_price_products = high_price_products.sort_values('price', ascending=False)

print(f"\n Товары с ценой ВЫШЕ третьего квартиля (price > {Q3:.2f} руб.):")
print(f"   Всего таких товаров: {len(high_price_products)}")
print(f"\n   {'Название товара':<45} {'Категория':<25} {'Цена, руб.':>12}")
print(f"   {'-'*45} {'-'*25} {'-'*12}")

for _, row in high_price_products.head(15).iterrows():
    print(f"   {row['product_name']:<45} {row['category']:<25} {row['price']:>12,.2f}")

if len(high_price_products) > 15:
    print(f"\n   ... и так далее {len(high_price_products) - 15} товаров")


#Step_5_Groups

print("\n" + "=" * 70)
print("ШАГ 5: СТАТИСТИКА ПО КАТЕГОРИЯМ ТОВАРОВ")
print("=" * 70)

# Группировка по категориям
category_stats = df.groupby('category').agg(
    price_count=('price', 'count'),
    mean_price=('price', 'mean'),
    median_price=('price', 'median'),
    std_price=('price', 'std')
).round(2)

# Сортировка по убыванию средней цены
category_stats = category_stats.sort_values('mean_price', ascending=False)

print(f"\n Статистика цен по категориям (отсортировано по убыванию средней цены):")
print(f"\n   {'Категория':<25} {'Кол-во':>8} {'Средняя, руб.':>15} {'Медиана, руб.':>15} {'Стд. откл., руб.':>18}")
print(f"   {'-'*25} {'-'*8} {'-'*15} {'-'*15} {'-'*18}")

for category, row in category_stats.iterrows():
    print(f"   {category:<25} {row['price_count']:>8} {row['mean_price']:>15,.2f} {row['median_price']:>15,.2f} {row['std_price']:>18,.2f}")

#Step_6_Prices_For_every_Items_5_Best

print("\n" + "=" * 70)
print("ШАГ 6: ТОВАРЫ С НАИБОЛЬШИМ РАЗБРОСОМ ЦЕН")
print("=" * 70)

#Min_an_Max_price_for_every_thing
price_span = df.groupby(['product_id', 'product_name', 'category']).agg(
    min_price=('price', 'min'),
    max_price=('price', 'max')
).reset_index()

#Razmah
price_span['price_diff'] = price_span['max_price'] - price_span['min_price']

#Into_DESC_po_ubivaniyu
top_5_span = price_span.sort_values('price_diff', ascending=False).head(5)

print(f"\n Топ-5 товаров с наибольшим разбросом цен:")
print(f"\n   {'Название товара':<45} {'Категория':<20} {'Мин. цена, руб.':>15} {'Макс. цена, руб.':>18} {'Разброс, руб.':>15}")
print(f"   {'-'*45} {'-'*20} {'-'*15} {'-'*18} {'-'*15}")

for _, row in top_5_span.iterrows():
    print(f"   {row['product_name']:<45} {row['category']:<20} {row['min_price']:>15,.2f} {row['max_price']:>18,.2f} {row['price_diff']:>15,.2f}")