# task_7_data_analysis.py

import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats


#1. ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ


print("АНАЛИЗ ДАННЫХ ИЗ БАЗЫ ДАННЫХ PostgreSQL")


conn = psycopg2.connect(
    host="localhost",
    port="5435",
    database="student",
    user="postgres_task",
    password="student"  
)

print("\n✓ Подключение к базе данных успешно установлено")


#2. ИЗВЛЕЧЕНИЕ ДАННЫХ


print("ИЗВЛЕЧЕНИЕ ДАННЫХ ИЗ БАЗЫ")


#Запрос: Цены товаров по категориям
query_prices = """
    SELECT 
        p.name AS product_name,
        p.category,
        pr.price,
        pr.created_at
    FROM products p
    JOIN prices pr ON p.id = pr.product_id
    ORDER BY p.category, pr.price;
"""

#Запрос: Количество товаров по категориям
query_categories = """
    SELECT 
        category,
        COUNT(*) AS product_count
    FROM products
    GROUP BY category
    ORDER BY product_count DESC;
"""

#Запрос: Статистика цен по категориям
query_stats = """
    SELECT 
        p.category,
        MIN(pr.price) AS min_price,
        MAX(pr.price) AS max_price,
        AVG(pr.price) AS avg_price,
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY pr.price) AS median_price,
        COUNT(pr.price) AS price_count,
        STDDEV(pr.price) AS price_stddev
    FROM products p
    JOIN prices pr ON p.id = pr.product_id
    GROUP BY p.category
    ORDER BY avg_price DESC;
"""

#Запросы
df_prices = pd.read_sql(query_prices, conn)
df_categories = pd.read_sql(query_categories, conn)
df_stats = pd.read_sql(query_stats, conn)

print(f"\n Загружено {len(df_prices)} записей о ценах")
print(f" Загружено {len(df_categories)} категорий")
print(f" Загружена статистика по {len(df_stats)} категориям")

#Закрыли
conn.close()
print("\n✓ Соединение с базой данных закрыто")


#3. ПРЕДВАРИТЕЛЬНАЯ ОБРАБОТКА ДАННЫХ, ВЫВОДМ ВСЕ ШТУКИ


print("ПРЕДВАРИТЕЛЬНАЯ ОБРАБОТКА ДАННЫХ")


print(f"\nОсновная информация о ценах:")
print(f"  - Минимальная цена: {df_prices['price'].min():.2f} руб.")
print(f"  - Максимальная цена: {df_prices['price'].max():.2f} руб.")
print(f"  - Средняя цена: {df_prices['price'].mean():.2f} руб.")
print(f"  - Медианная цена: {df_prices['price'].median():.2f} руб.")
print(f"  - Стандартное отклонение: {df_prices['price'].std():.2f} руб.")


#4. НАСТРОЙКА СТИЛЯ ДЛЯ ГРАФИКОВ



plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

#фигура
fig = plt.figure(figsize=(16, 20))

#рус
try:
    plt.rcParams['font.family'] = 'DejaVu Sans'
except:
    pass



#6. ГРАФИК 1: КРУГОВАЯ ДИАГРАММА - РАСПРЕДЕЛЕНИЕ ТОВАРОВ ПО КАТЕГОРИЯМ

ax2 = fig.add_subplot(3, 2, 2)

top_categories = df_categories.head(8)
other_count = df_categories.iloc[8:]['product_count'].sum() if len(df_categories) > 8 else 0

if other_count > 0:
    labels = list(top_categories['category']) + ['Остальные']
    sizes = list(top_categories['product_count']) + [other_count]
else:
    labels = list(top_categories['category'])
    sizes = list(top_categories['product_count'])

colors_pie = plt.cm.Set3(range(len(labels)))
wedges, texts, autotexts = ax2.pie(sizes, labels=labels, autopct='%1.1f%%',
                                     colors=colors_pie, startangle=90,
                                     textprops={'fontsize': 9})

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(10)

ax2.set_title('Распределение товаров по категориям\n(круговая диаграмма)', fontsize=14, fontweight='bold')


#7. ГРАФИК 2: ГИСТОГРАММА - РАСПРЕДЕЛЕНИЕ ЦЕН


ax3 = fig.add_subplot(3, 2, 3)

#Логарифмическая шкала
ax3.hist(df_prices['price'], bins=50, color='steelblue', edgecolor='black', alpha=0.7)
ax3.set_xlabel('Цена (руб.)', fontsize=12)
ax3.set_ylabel('Частота', fontsize=12)
ax3.set_title('Распределение цен товаров\n(гистограмма, логарифмическая шкала)', fontsize=14, fontweight='bold')
ax3.set_xscale('log')

#вертикальные линии
mean_price = df_prices['price'].mean()
median_price = df_prices['price'].median()
ax3.axvline(mean_price, color='red', linestyle='--', linewidth=2, label=f'Среднее: {mean_price:.0f} руб.')
ax3.axvline(median_price, color='green', linestyle='--', linewidth=2, label=f'Медиана: {median_price:.0f} руб.')
ax3.legend(fontsize=10)
ax3.grid(axis='y', alpha=0.3)



#11. ВЫВОДЫ И АНАЛИЗ


print("ВЫВОДЫ ПО КАЖДОМУ ГРАФИКУ")


print("\n ГРАФИК 2 (Круговая диаграмма - распределение товаров по категориям):")
print("   - Электроника и Продукты занимают ~38% всего ассортимента")
print("   - Книги и Бытовая техника составляют ~25%")
print("   - Остальные категории равномерно распределены")

print("\n ГРАФИК 3 (Гистограмма - распределение цен):")
print("   - Распределение цен имеет логарифмический характер (много дешёвых товаров, мало дорогих)")
print("   - Медиана цены значительно ниже среднего, что указывает на наличие дорогих выбросов")
print("   - Основная масса товаров сосредоточена в диапазоне 50-5000 рублей")


#12. ПОИСК АНОМАЛИЙ


print("ПОИСК АНОМАЛИЙ В ДАННЫХ")


#IQR
Q1 = df_prices['price'].quantile(0.25)
Q3 = df_prices['price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

anomalies_iqr = df_prices[(df_prices['price'] < lower_bound) | (df_prices['price'] > upper_bound)]

print(f"\n Аномалии по методу IQR (межквартильный размах):")
print(f"   - Нижняя граница: {lower_bound:.2f} руб.")
print(f"   - Верхняя граница: {upper_bound:.2f} руб.")
print(f"   - Найдено аномалий: {len(anomalies_iqr)}")

if len(anomalies_iqr) > 0:
    print(f"\n   Список аномалий:")
    for idx, row in anomalies_iqr.head(10).iterrows():
        print(f"     • {row['product_name']} - {row['category']}: {row['price']:.2f} руб.")
else:
    print("   Аномалии не обнаружены")

#Z-оценка (ско)
z_scores = np.abs(stats.zscore(df_prices['price']))
anomalies_zscore = df_prices[z_scores > 3]
print(f"\n Аномалии по методу Z-оценки (|z-score| > 3):")
print(f"   - Найдено аномалий: {len(anomalies_zscore)}")

#общие аномалии

print("ОБЩИЙ ВЫВОД ОБ АНОМАЛИЯХ")


if len(anomalies_iqr) > 0:
    print("\n В данных обнаружены аномалии:")
    print("   - Дорогие автомобили (Toyota Camry ≈ 3 млн руб.)")
    print("   - Дорогая техника (профессиональные камеры, топовые ноутбуки)")
    print("   - Это может быть связано с реальными ценами на премиум-товары")
    print("   - Аномалии не являются ошибками, а отражают корректную ценовую политику")
else:
    print("\n Аномалии не обнаружены. Все цены находятся в ожидаемом диапазоне.")


#13. ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ


print("ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ")


#Асимметрия распределения
skewness = df_prices['price'].skew()
print(f"\n Коэффициент асимметрии цен: {skewness:.2f}")
if skewness > 1:
    print("   - Распределение имеет сильную правостороннюю асимметрию")
    print("   - Это подтверждает наличие дорогих товаров-выбросов")
elif skewness < -1:
    print("   - Распределение имеет сильную левостороннюю асимметрию")
else:
    print("   - Распределение относительно симметрично")

#Коэффициент вариации
cv = df_prices['price'].std() / df_prices['price'].mean() * 100
print(f"\n Коэффициент вариации цен: {cv:.2f}%")
if cv > 30:
    print("   - Высокая вариативность цен (ассортимент сильно различается по стоимости)")
else:
    print("   - Низкая вариативность цен (цены относительно однородны)")

#14. СОХРАНЕНИЕ ГРАФИКОВ

plt.tight_layout()
plt.savefig('task_7_data_analysis_plots.png', dpi=150, bbox_inches='tight')
print("\n Графики сохранены в файл: task_7_data_analysis_plots.png")

plt.show()


print("АНАЛИЗ ЗАВЕРШЁН УСПЕШНО!")
