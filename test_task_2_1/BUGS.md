# BUGS.md  

## Баг-репорты по API микросервиса объявлений  

---

### Баг 1 – API создаёт объявления с некорректным значением цены

**ID:** BUG_001  

**Краткое описание:**  
API позволяет создать объявление с отрицательной ценой.

**Шаги для воспроизведения:**  
1. Отправить POST-запрос на /api/1/item с полем price = -100.
2. Проверить статус-код и тело ответа.

**Фактический результат:**  
 - Ответ: 200 OK
 - Объявление создаётся.

**Ожидаемый результат:**
 - Ответ: 400 Bad Request
 - Сообщение об ошибке: "Цена не может быть отрицательной".

**Приоритет:** High

---

### Баг 2 – API создаёт объявления с пустым именем

**ID:** BUG_002  

**Краткое описание:**  
API создаёт объявления с пустым именем

**Шаги для воспроизведения:**  
1. Отправить POST-запрос на /api/1/item с name = "".
2. Проверить статус-код и тело ответа.

**Фактический результат:**  
 - Ответ: 200 OK
 - Объявление создаётся.

**Ожидаемый результат:**
 - Ответ: 400 Bad Request
 - Сообщение об ошибке: "Поле name не может быть пустым".

**Приоритет:** Medium

---

### Баг 3 – API создаёт объявления с чрезмерно большой ценой

**ID:** BUG_003

**Краткое описание:**  
API позволяет создать объявление с нереалистично большой ценой (10^10).

**Шаги для воспроизведения:**  
1. Отправить POST-запрос на /api/1/item с price = 10000000000.
2. Проверить статус-код и тело ответа.

**Фактический результат:**  
 - Ответ: 200 OK
 - Объявление создаётся.

**Ожидаемый результат:**
 - Ответ: 400 Bad Request
 - Сообщение об ошибке: "Цена превышает допустимый диапазон".

**Приоритет:** Low

---

### Баг 4 – API создаёт объявления с null-значениями в полях

**ID:** BUG_004

**Краткое описание:**  
API позволяет создать объявление с null-значениями в полях sellerID, name, price.

**Шаги для воспроизведения:**  
1. Отправить POST-запрос на /api/1/item с полями sellerID = null, name = null, price = null.
2. Проверить статус-код и тело ответа.

**Фактический результат:**  
 - Ответ: 200 OK
 - Объявление создаётся.

**Ожидаемый результат:**
 - Ответ: 400 Bad Request
 - Сообщение об ошибке: "Обязательные поля не могут быть null".

**Приоритет:** Low

---

### Баг 5 – Некорректный формат успешного ответа при создании объявления  

**ID:** BUG_005

**Краткое описание:**  
При создании объявления API возвращает сообщение вида `Сохранили объявление - <ID>`, вместо ожидаемого `{"status": "ok"}`.  

**Шаги для воспроизведения:**  
1. Отправить POST-запрос на `/api/1/item` с валидными данными.  
2. Проверить тело ответа.

**Фактический результат:**  

```json
{
  "status": "Сохранили объявление - 866fea4f-d91a-41a9-86c6-996963064730"
}
```

**Ожидаемый результат:**
```json
{
  "status": "Ok"
}
```

**Приоритет:** Medium

---

### Баг 6 – Ошибки при создании объявления с отсутствующими обязательными полями

**ID:** BUG_006

**Краткое описание:**  
API позволяет создать объявление без обязательного поля sellerID.

**Шаги для воспроизведения:**  
1. Отправить POST-запрос на `/api/1/item` без `sellerID`
2. Проверить статус-код и тело ответа.

**Фактический результат:**  
 - Ответ: 200 OK
 - Объявление создаётся.

**Ожидаемый результат:**
 - Ответ: 400 Bad Request
 - Сервер возвращает корректную ошибку с описанием отсутствующих полей.

**Приоритет:** High