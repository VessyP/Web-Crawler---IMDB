IMDB Crawler

Task:

Да се извлекат филмите в "Most Popular Movies" класацията на IMDB, които са с IMDB рейтинг >= 8.

Линк към класацията: https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm

Данните, които трябва да се съхранят в база данни (MySQL или MongoDB) са:

 - жанр
 - име на филмите
 - имената на режисьорите
 - 
Да се състави потребителски интерфейс в който да се представят таблично получените данни.

Трябва да има поле за филтриране по жанр на филм и възможност за сортиране (в намаляващ/увеличаващ ред) по име на филм.



Install:

1. Create virtual environment:

open terminal in project root folder and write:

python -m venv .venv

2. Activate virtual environment:

in CMD:

.venv\Scripts\activate.bat

3. Install packages:

pip install -r requirements.txt

4. Change config.ini

In lib/config.ini set your MySQL username, password and DB name

5. Download MySQL Server

6. Run App:

python app.py