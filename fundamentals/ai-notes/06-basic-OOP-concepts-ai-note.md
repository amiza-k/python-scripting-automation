# ۶. مفاهیم پایه OOP در پایتون

OOP یا برنامه‌نویسی شی‌گرا روشی برای سازمان‌دهی کد با استفاده از کلاس‌ها و اشیاء است. در اتوماسیون، وقتی اسکریپت‌ها بزرگ‌تر می‌شوند، OOP به مرتب‌سازی و مدیریت کد کمک می‌کند.

## ۱. Class و Object

- Class (کلاس): قالبی برای ساخت اشیاء.
- Object (شیء): نمونه‌ای ساخته‌شده از یک کلاس.

```
class Robot:    passbot1 = Robot()bot2 = Robot()
```

اینجا `Robot` کلاس و `bot1` و `bot2` دو شیء مستقل هستند.

## ۲. Attributes و Methods

- Attribute: ویژگی یا دادهٔ یک شیء.
- Method: تابعی که داخل کلاس تعریف شده است.

```
class Robot:    def __init__(self, name):        self.name = name    def greet(self):        print(f"Hello, I'm {self.name}")bot = Robot("Alex")bot.greet()
```

خروجی:

```
Hello, I'm Alex
```

### متد سازنده `__init__()`

وقتی شیء ساخته می‌شود، `__init__()` برای مقداردهی اولیه اجرا می‌شود.

### مفهوم `self`

`self` به همان شیئی اشاره می‌کند که متد روی آن اجرا شده است. با `self.name` ویژگی مخصوص همان شیء را تعریف یا استفاده می‌کنیم.

## ۳. Instance Attributes و Class Attributes

- Instance Attribute: مخصوص هر شیء؛ مثل نام هر ربات.
- Class Attribute: بین نمونه‌های کلاس مشترک است.

```
class Robot:    category = "Automation"    def __init__(self, name):        self.name = namebot1 = Robot("Alex")bot2 = Robot("Sara")
```

- `bot1.name` برابر `"Alex"` است.
- `bot2.name` برابر `"Sara"` است.
- هر دو به `category` با مقدار `"Automation"` دسترسی دارند.

## ۴. Instance Method، Class Method و Static Method

| نوع متد         | کاربرد                                                                          |
| --------------- | ------------------------------------------------------------------------------- |
| Instance Method | کار با اطلاعات یک شیء؛ پارامتر اول `self`                                       |
| Class Method    | کار با خود کلاس؛ پارامتر اول `cls` و استفاده از `@classmethod`                  |
| Static Method   | تابع مرتبط با کلاس که به `self` یا `cls` نیاز ندارد؛ استفاده از `@staticmethod` |

```
class Converter:    factor = 2    def double(self, number):        return number * self.factor    @classmethod    def get_factor(cls):        return cls.factor    @staticmethod    def add(a, b):        return a + b
```

مثال استفاده:

```
converter = Converter()print(converter.double(5))print(Converter.get_factor())print(Converter.add(3, 4))
```

خروجی:

```
10
2
7
```

## ۵. Encapsulation — کپسوله‌سازی

یعنی داده‌ها و عملیات مرتبط را در یک کلاس جمع کنیم و دسترسی به جزئیات داخلی را مدیریت کنیم.

در پایتون، یک زیرخط مثل `_balance` معمولاً یعنی «این ویژگی داخلی است؛ مستقیم از بیرون دست‌کاری نکن». این بیشتر یک قرارداد است، نه محدودیت سخت‌گیرانه.

```
class Account:    def __init__(self, balance):        self._balance = balance    def get_balance(self):        return self._balance
```

## ۶. Inheritance — وراثت

یک کلاس می‌تواند ویژگی‌ها و متدهای کلاس دیگری را به ارث ببرد.

```
class Worker:    def run(self):        print("Working")class FileWorker(Worker):    passworker = FileWorker()worker.run()
```

خروجی:

```
Working
```

`FileWorker` متد `run()` را از `Worker` به ارث برده است.

## ۷. Composition — ترکیب اشیاء

یعنی یک کلاس، شیئی از کلاس دیگری را درون خودش داشته باشد؛ مثلاً یک سیستم اتوماسیون از یک شیء برای خواندن فایل و شیء دیگری برای ارسال ایمیل استفاده کند.

```
class FileReader:    def read(self):        return "Report data"class Automation:    def __init__(self):        self.reader = FileReader()    def run(self):        return self.reader.read()
```

اینجا `Automation` از یک شیء `FileReader` استفاده می‌کند، بدون اینکه از آن ارث‌بری کند.

## ۸. استفاده از کلاس‌های آماده پایتون

در کتابخانه‌های پایتون، کلاس‌های آماده زیادی وجود دارند. برای مثال، `Path` از ماژول `pathlib` یک کلاس است:

```
from pathlib import Pathfile = Path("report.txt")print(file.name)print(file.suffix)
```

خروجی:

```
report.txt
.txt
```

در اتوماسیون، استفاده از کلاس‌های آماده معمولاً از ساختن همه‌چیز از صفر بهتر است.

## ۹. آشنایی با `dataclass`

وقتی کلاسی عمدتاً برای نگهداری داده‌هاست، `dataclass` می‌تواند کد را کوتاه‌تر کند.

```
from dataclasses import dataclass@dataclassclass Task:    name: str    priority: inttask = Task("Backup", 1)print(task.name)print(task.priority)
```

خروجی:

```
Backup
1
```

پایتون به‌صورت خودکار سازنده و چند قابلیت مفید دیگر را ایجاد می‌کند.

## تمرین‌ها

تمرین‌ها را خودت کدنویسی کن؛ فعلاً راه‌حل کامل را نمی‌نویسم.

### تمرین ۱ — کلاس ساده

کلاس `FileTask` بساز که ویژگی‌های `filename` و `status` داشته باشد. با یک متد، نام فایل و وضعیت آن را نمایش بده. دو شیء با اطلاعات متفاوت بساز.

### تمرین ۲ — مدیریت وظایف اتوماسیون

کلاس `TaskManager` بساز که یک لیست از وظایف داشته باشد. متدهایی برای افزودن وظیفه و نمایش همهٔ وظایف تعریف کن. هر وظیفه می‌تواند یک شیء از کلاس `Task` باشد.

### تمرین ۳ — طراحی یک سیستم کوچک

با استفاده از `dataclass`، کلاسی به نام `FileJob` با ویژگی‌های `filename`، `action` و `priority` بساز. سپس کلاس `Automation` را طراحی کن که یک `FileJob` دریافت کند و اطلاعات آن را نمایش دهد. در این تمرین از Composition استفاده کن.

نکته: برای هدف اتوماسیون، فعلاً تسلط روی کلاس، شیء، `__init__`، `self` و متدها از حفظ‌کردن تمام جزئیات OOP مهم‌تر است.