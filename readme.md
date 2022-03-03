<a id="anchor"></a> 
## [![alt text="Школа тестировщиков ПО"](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtTLGrH5SvrSpUQM4bgSjSIQsTaflT4EMohw&usqp=CAU)Online-образовательная "Школа тестировщиков ПО"]

### *Описание*
```
Практика по курсу "Автоматизация" (разработка авто-тестов в PyCharm с использованием Python и Selenium на основе тест-кейсов).
Проект выполнен в учебных целях для закрепления навыков по Git, Python, DevTools, HTML, CSS.
Эти задания были разработаны, чтобы улучшить мастерство автоматизации тестирования.
```
#### *Проект состоит из трех разделов: Home, Registration & login, Shop*

### ➣ Разделы проекта:
---
- [x] Home
- [x] Registration & login
- [x] Shop

### ➣ Разделы и спецификации: 
---
### ***Home*** (один тест)
 
[1] ▼ Home: добавление комментария
***"01_home__add_comment.py"***
```
    1. Откройте http://practice.automationtesting.in/
    2. Проскролльте страницу вниз на 600 пикселей
    3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
    4. Нажмите на вкладку "REVIEWS"
    5. Поставьте 5 звёзд
    6. Заполните поле "Review" сообщением: "Nice book!"
    7. Заполните поле "Name"
    8. Заполните "Email"
    9. Нажмите на кнопку "SUBMIT"
```
### ***Registration & login*** (два теста)

[1] ▼ Registration_login: регистрация аккаунта
***"02_registration_login__account_registration.py"***
```
  1. Откройте http://practice.automationtesting.in/
  2. Нажмите на вкладку "My Account Menu"
  3. В разделе "Register", введите email для регистрации
  4. В разделе "Register", введите пароль для регистрации (уровень сложности "Medium" или "Strong"), почту и пароль сохраните, потребуюутся в дальнейшем
  5. Нажмите на кнопку "Register" 
```

[2] ▼ Registration_login: логин в систему
***"03_registration_login__login_into_account.py"***
```
  1. Откройте http://practice.automationtesting.in/
  2. Нажмите на вкладку "My Account Menu"
  3. В разделе "Login", введите email для логина (данные можно взять из предыдущего теста)
  4. В разделе "Login", введите пароль для логина (данные можно взять из предыдущего теста)
  5. Нажмите на кнопку "Login"
  6. Добавьте проверку, что на странице есть элемент "Logout"
```

### ***Shop*** (семь тестов)

[1] ▼ Shop: отображение страницы товара
***"04_shop__display_product_page.py"***
```
	1. Откройте http://practice.automationtesting.in/
	2. Залогиньтесь
	3. Нажмите на вкладку "Shop"
	4. Откройте книгу "HTML 5 Forms"
	5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms" 
```

[2] ▼ Shop: количество товаров в категории
***"05_shop__products_quantity_in_category.py"***
```
	1. Откройте http://practice.automationtesting.in/
	2. Залогиньтесь
	3. Нажмите на вкладку "Shop"
	4. Откройте категорию "HTML"
	5. Добавьте тест, что отображается три товара
```

[3] ▼ Shop: сортировка товаров
***"06_shop__product_sorting.py"***
```
	1. Откройте http://practice.automationtesting.in/
	2. Залогиньтесь
	3. Нажмите на вкладку "Shop"
	4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию (используйте проверку по value)
	5. Отсортируйте товары по цене от большей к меньшей (в селекторах используйте класс Select)
	6. Снова объявите переменную с локатором основного селектора сортировки, т.к после сортировки страница обновится
	7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей (используйте проверку по value)
```

[4] ▼ Shop: отображение, скидка товара
***"07_shop__display_product_discount.py"***
```
	1. Откройте http://practice.automationtesting.in/
	2. Залогиньтесь
	3. Нажмите на вкладку "Shop"
	4. Откройте книгу "Android Quick Start Guide"
	5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
	6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
	7. Добавьте явное ожидание и нажмите на обложку книги (подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу))
	8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
```

[5] ▼ Shop: проверка цены в корзине
***"08_shop__checking_price_in_the_cart.py"***
```
	1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
	2. Нажмите на вкладку "Shop"
	3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
	4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00" (используйте для проверки assert)
	5. Перейдите в корзину
	6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
	7. Используя явное ожидание, проверьте что в Total отобразилась стоимость 
```

[6] ▼ Shop: работа в корзине
***"09_shop__ work_with_cart.py"***
```
	1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
	2. Нажмите на вкладку "Shop"
	3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm" (перед добавлением первой книги, проскролльте вниз на 300 пикселей)
	4. Перейдите в корзину
	5. Удалите первую книгу
	6. Нажмите на Undo (отмена удаления)
	7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“ (предварительно очистите поле с помощью локатор_поля.clear())
	8. Нажмите на кнопку "UPDATE BASKET"
	9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 (используйте assert)
	10. Нажмите на кнопку "APPLY COUPON"
	11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
```

[7] ▼ Shop: покупка товара
***"10_shop__buy_the_book.py"***
```
	1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
	2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
	3. Добавьте в корзину книгу "HTML5 WebApp Development"
	4. Перейдите в корзину
	5. Нажмите "PROCEED TO CHECKOUT" (перед нажатием, добавьте явное ожидание)
	6. Заполните все обязательные поля (перед заполнением first name, добавьте явное ожидание, для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - >" нажать на вариант который отобразится ниже ввода). Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
	7. Выберите способ оплаты "Check Payments" (перед выбором, проскролльте на 600 пикселей вниз)
	9. Нажмите PLACE ORDER
	10. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
	11. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
```
####     [Вверх](#anchor)