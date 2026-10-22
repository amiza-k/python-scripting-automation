# ۳. خطاها و `try/except` در پایتون

## ۱. تفاوت Syntax Error و Runtime Error

- Syntax Error: ساختار کد اشتباه است و پایتون نمی‌تواند آن را درست تفسیر کند.
- Runtime Error: کد از نظر ساختار قابل اجراست، اما هنگام اجرا مشکلی رخ می‌دهد.

مثال Syntax Error:

```
if True    print("Hello")
```

در این کد، `:` فراموش شده است.

مثال Runtime Error:

```
number = int("hello")
```

ساختار کد درست است، اما تبدیل متن `"hello"` به عدد باعث `ValueError` می‌شود.

## ۲. مفهوم Exception

`Exception` به خطاهایی گفته می‌شود که هنگام اجرای برنامه رخ می‌دهند و می‌توان آن‌ها را مدیریت کرد.

مثلاً ورودی نامعتبر، فایل پیدا‌نشده یا تقسیم بر صفر.

اگر خطا مدیریت نشود، ممکن است اجرای برنامه متوقف شود.

## ۳. ساختار `try` و `except`

کدهایی که احتمال خطا دارند داخل `try` قرار می‌گیرند؛ اگر خطای مشخص‌شده رخ دهد، بخش `except` اجرا می‌شود.

```
try:    number = int(input("Enter a number: "))    result = 100 / numberexcept ValueError:    print("Invalid number")except ZeroDivisionError:    print("Cannot divide by zero")
```

در این مثال:

- اگر ورودی عدد نباشد، `ValueError` مدیریت می‌شود.
- اگر عدد صفر باشد، `ZeroDivisionError` مدیریت می‌شود.
- اگر خطای دیگری رخ دهد، این دو `except` آن را مدیریت نمی‌کنند.

نکته: بهتر است فقط خطاهایی را بگیری که انتظار وقوعشان را داری.

## ۴. استفاده از چند `except`

هر `except` می‌تواند یک نوع خطا را مدیریت کند.

```
try:    items = [10, 20]    value = items[5]except IndexError:    print("Index does not exist")except TypeError:    print("Invalid data type")
```

می‌توان چند خطای مرتبط را نیز در یک `except` گرفت:

```
try:    number = int("abc")except (ValueError, TypeError):    print("Input conversion failed")
```

## ۵. استفاده از `else`

بخش `else` زمانی اجرا می‌شود که بخش `try` بدون خطا تمام شده باشد.

```
try:    number = int("25")except ValueError:    print("Invalid input")else:    print(number * 2)
```

خروجی:

```
50
```

از `else` برای جداکردن عملیات موفق از کد مدیریت خطا استفاده می‌کنیم.

## ۶. استفاده از `finally`

بخش `finally` چه خطا رخ دهد و چه رخ ندهد، در جریان عادی مدیریت خطا اجرا می‌شود. برای کارهایی مثل آزادسازی منابع کاربرد دارد.

```
try:    number = int("abc")except ValueError:    print("Conversion failed")finally:    print("Operation finished")
```

خروجی:

```
Conversion failed
Operation finished
```

ترتیب کلی ساختار:

```
try:    ...except SomeError:    ...else:    ...finally:    ...
```

`else` و `finally` اختیاری هستند.

## ۷. خطاهای رایج

| خطا                 | دلیل                    | مثال                             |
| ------------------- | ----------------------- | -------------------------------- |
| `ValueError`        | مقدار نامعتبر           | `int("abc")`                     |
| `TypeError`         | نوع داده نامناسب        | `"Age" + 20`                     |
| `NameError`         | نام تعریف‌نشده          | استفاده از `total` بدون تعریف آن |
| `IndexError`        | ایندکس نامعتبر          | `[1, 2][5]`                      |
| `KeyError`          | کلید ناموجود در دیکشنری | `{"a": 1}["b"]`                  |
| `FileNotFoundError` | فایل پیدا نمی‌شود       | بازکردن فایل ناموجود             |
| `PermissionError`   | دسترسی کافی وجود ندارد  | خواندن فایل بدون مجوز لازم       |

شناخت نوع خطا کمک می‌کند به‌جای پنهان‌کردن مشکل، راه‌حل مناسبی بنویسی.

## ۸. دریافت اطلاعات خطا

با `as` می‌توان اطلاعات خطا را در یک متغیر دریافت کرد.

```
try:    number = int("hello")except ValueError as error:    print(error)
```

خروجی:

```
invalid literal for int() with base 10: 'hello'
```

متن دقیق خطا ممکن است با نسخه پایتون متفاوت باشد.

این روش برای گزارش خطا و اشکال‌زدایی مفید است؛ اما نمایش مستقیم جزئیات داخلی خطا به کاربران نهایی همیشه مناسب نیست.

## ۹. استفاده از `raise`

با `raise` می‌توانیم خودمان خطا ایجاد کنیم یا یک خطای گرفته‌شده را دوباره بالا بفرستیم.

### ایجاد خطای اختصاصی

```
age = -5if age < 0:    raise ValueError("Age cannot be negative")
```

وقتی سن منفی باشد، خطای `ValueError` ایجاد می‌شود.

### انتقال دوباره خطا

```
try:    number = int("abc")except ValueError:    print("Logging the error")    raise
```

`raise` بدون آرگومان، همان خطای فعلی را دوباره بالا می‌فرستد.

## ۱۰. مدیریت خطا هنگام کار با فایل

یکی از خطاهای رایج، بازکردن فایلی است که وجود ندارد.

```
try:    with open("data.txt", "r", encoding="utf-8") as file:        content = file.read()except FileNotFoundError:    print("File not found")except PermissionError:    print("Permission denied")
```

استفاده از `with` باعث می‌شود فایل پس از پایان کار به‌درستی بسته شود.

هنگام نوشتن فایل نیز ممکن است خطای دسترسی یا خطاهای ورودی/خروجی رخ دهد:

```
try:    with open("report.txt", "w", encoding="utf-8") as file:        file.write("Report")except PermissionError:    print("Cannot write to this file")except OSError as error:    print(f"File operation failed: {error}")
```

`OSError` دسته‌ای از خطاهای مربوط به عملیات سیستم‌عامل و فایل است.

## ۱۱. مدیریت خطا در API و کتابخانه‌های خارجی

هنگام کار با API ممکن است اینترنت قطع باشد، سرور پاسخ ندهد یا پاسخ نامعتبر دریافت شود.

مثال با کتابخانه `requests`:

```
import requeststry:    response = requests.get(        "https://api.github.com",        timeout=10    )    response.raise_for_status()    data = response.json()except requests.exceptions.Timeout:    print("Request timed out")except requests.exceptions.HTTPError as error:    print(f"HTTP error: {error}")except requests.exceptions.RequestException as error:    print(f"Request failed: {error}")except ValueError:    print("Invalid JSON response")
```

نکات مهم:

- `timeout` برای جلوگیری از انتظار نامحدود است.
- `raise_for_status()` پاسخ‌های HTTP ناموفق را به خطا تبدیل می‌کند.
- `RequestException` خطاهای مرتبط با درخواست را پوشش می‌دهد.
- `response.json()` ممکن است در صورت نامعتبر بودن JSON خطای `ValueError` ایجاد کند.

برای اجرای این مثال، کتابخانه `requests` باید نصب شده باشد.

## ۱۲. سه تمرین جامع

### تمرین ۱ — ماشین‌حساب مقاوم

برنامه‌ای بنویس که دو عدد و یک عملگر از کاربر بگیرد. ورودی نامعتبر، تقسیم بر صفر و عملگر ناشناخته را مدیریت کند. برای خطاهای مختلف پیام مناسب نمایش بده.

مفاهیم: try، چند except، ValueError، raise

### تمرین ۲ — خواندن و ذخیره فایل

نام یک فایل را از کاربر بگیر، محتوای آن را بخوان و تعداد کلماتش را در فایلی دیگر ذخیره کن. نبودن فایل، خطای دسترسی و خطاهای ورودی/خروجی را مدیریت کن. از `with` و `else` نیز استفاده کن.

مفاهیم: FileNotFoundError، PermissionError، OSError، else، finally

### تمرین ۳ — دریافت و اعتبارسنجی اطلاعات API

با `requests` اطلاعات یک API عمومی را دریافت کن. timeout، پاسخ HTTP ناموفق و JSON نامعتبر را مدیریت کن. سپس بررسی کن که داده دریافتی کلید موردنیاز را دارد؛ اگر نداشت، با `raise` خطای مناسبی ایجاد کن.

مفاهیم: Exception، raise، مدیریت خطای API و اعتبارسنجی داده

قاعده طلایی: خطاهای مشخص را مدیریت کن، محدوده `try` را بی‌دلیل بزرگ نکن و از `except:` عمومی برای پنهان‌کردن همه خطاها استفاده نکن.