# ۵. کار با JSON در پایتون

## ۱. مفهوم JSON و ساختار داده‌ها

`JSON` فرمتی متنی برای ذخیره‌سازی و انتقال داده است؛ مثلاً ذخیره تنظیمات برنامه یا دریافت اطلاعات از API.

```
{
    name Ali,
    age 25,
    active true,
    skills [Python, SQL]
}
```

انواع داده در JSON

- String متن
- Number عدد صحیح یا اعشاری
- Boolean `true` و `false`
- Null مقدار `null`
- Object مجموعه‌ای از کلید و مقدار
- Array فهرستی از مقادیر

تفاوت‌های مهم با پایتون

 JSON              Python           
 ----------------  ---------------- 
 Object `{}`       معمولاً `dict`   
 Array `[]`        معمولاً `list`   
 `true`  `false`  `True`  `False` 
 `null`            `None`           

JSON و Dictionary یکسان نیستند؛ JSON قالب متنی است، اما Dictionary یک نوع داده پایتون است.

## ۲. تبدیل Python به JSON با `json.dumps()`

برای تبدیل داده پایتون به رشته JSON از `dumps()` استفاده می‌کنیم.

```
import jsondata = {    name Ali,    age 25,    active True}text = json.dumps(data)
```

مقدار `text` یک رشته (`str`) است که داده‌ها را با قالب JSON نگه می‌دارد.

## ۳. تبدیل JSON به Python با `json.loads()`

برای تبدیل رشته JSON به داده پایتون از `loads()` استفاده می‌کنیم.

```
import jsontext = '{name Ali, age 25}'data = json.loads(text)name = data[name]
```

خروجی متغیر `name`

```
Ali
```

تفاوت مهم `dumps` و `loads` برای رشته‌ها هستند؛ `dump` و `load` برای فایل‌ها استفاده می‌شوند.

## ۴. خواندن و نوشتن فایل JSON

### نوشتن با `json.dump()`

```
import jsondata = {name Sara, age 22}with open(user.json, w, encoding=utf-8) as file    json.dump(data, file, ensure_ascii=False, indent=4)
```

این کد اطلاعات را در فایل `user.json` ذخیره می‌کند.

### خواندن با `json.load()`

```
import jsonwith open(user.json, r, encoding=utf-8) as file    data = json.load(file)
```

اکنون `data` یک دیکشنری پایتون است.

## ۵. پارامترهای مهم JSON

 پارامتر               کاربرد                    
 --------------------  ------------------------- 
 `indent=4`            مرتب‌کردن و تورفتگی خروجی 
 `ensure_ascii=False`  نمایش مستقیم حروف فارسی   
 `sort_keys=True`      مرتب‌سازی کلیدها          

مثال

```
import jsondata = {name علی, age 25}text = json.dumps(    data,    ensure_ascii=False,    indent=4,    sort_keys=True)
```

استفاده از `ensure_ascii=False` برای فایل‌های JSON فارسی خواناتر است.

## ۶. کار با داده‌های تو‌در‌تو (Nested JSON)

ممکن است یک دیکشنری شامل دیکشنری یا لیست دیگری باشد.

```
data = {    user {        name Ali,        address {            city Tehran        }    },    skills [Python, SQL]}
```

دسترسی به مقادیر

```
name = data[user][name]city = data[user][address][city]first_skill = data[skills][0]
```

خروجی `city` برابر `Tehran` و خروجی `first_skill` برابر `Python` است.

## ۷. تغییر، اضافه‌کردن و حذف داده‌ها

چون داده JSON را به پایتون تبدیل کرده‌ایم، می‌توانیم آن را مثل دیکشنری و لیست تغییر دهیم.

```
data = {    name Ali,    age 25}data[age] = 26data[city] = Tehrandel data[name]
```

- تغییر مقدار انتساب به کلید موجود
- افزودن مقدار انتساب به کلید جدید
- حذف مقدار استفاده از `del`

اگر کلید وجود نداشته باشد، دسترسی مستقیم با `data[key]` خطای `KeyError` می‌دهد. برای دریافت امن‌تر می‌توان از `data.get(key)` استفاده کرد.

## ۸. مدیریت `JSONDecodeError`

اگر رشته یا فایل JSON ساختار معتبری نداشته باشد، معمولاً خطای `JSONDecodeError` رخ می‌دهد.

```
import jsontext = '{name Ali,}'try    data = json.loads(text)except json.JSONDecodeError as error    print(fInvalid JSON {error})
```

در این مثال، ویرگول اضافه باعث نامعتبرشدن JSON شده است.

هنگام خواندن فایل، ممکن است علاوه بر خطای JSON، خطای نبودن فایل یا دسترسی هم رخ دهد؛ این خطاها باید جداگانه مدیریت شوند.

## ۹. کار با JSON دریافتی از API

بسیاری از APIها داده‌ها را به شکل JSON برمی‌گردانند. با کتابخانه `requests` می‌توان پاسخ را پردازش کرد.

```
import requeststry    response = requests.get(        httpsapi.github.com,        timeout=10    )    response.raise_for_status()    data = response.json()except requests.exceptions.RequestException as error    print(fRequest failed {error})except ValueError    print(Invalid JSON response)
```

- `raise_for_status()` خطاهای HTTP را مدیریت‌پذیر می‌کند.
- `response.json()` پاسخ را به داده‌های پایتون تبدیل می‌کند.
- `timeout` از انتظار نامحدود جلوگیری می‌کند.

برای اجرای این مثال باید `requests` نصب شده باشد.

## ۱۰. ذخیره تنظیمات برنامه در JSON

JSON برای ذخیره تنظیماتی مثل زبان برنامه، مسیر فایل‌ها یا وضعیت گزینه‌ها کاربرد دارد.

```
import jsonfrom pathlib import Pathconfig_path = Path(config.json)config = {    language fa,    theme dark,    notifications True}config_path.write_text(    json.dumps(config, ensure_ascii=False, indent=4),    encoding=utf-8)
```

برای خواندن تنظیمات

```
config = json.loads(    config_path.read_text(encoding=utf-8))
```

در برنامه واقعی، هنگام خواندن تنظیمات باید نبودن فایل و نامعتبر بودن JSON را هم مدیریت کنی.

# سه تمرین جامع

### تمرین ۱ — مدیریت اطلاعات کاربران

یک دیکشنری شامل اطلاعات چند کاربر بساز، آن را به JSON تبدیل کن، در فایل ذخیره کن و دوباره بخوان. سپس نام یکی از کاربران را تغییر بده و سن یک کاربر جدید را اضافه کن.

مفاهیم dumps، loads، dump، load، دیکشنری و لیست

### تمرین ۲ — مدیریت تنظیمات برنامه

برنامه‌ای بساز که تنظیمات را از `config.json` بخواند. اگر فایل وجود نداشت، تنظیمات پیش‌فرض ایجاد کند. اگر JSON نامعتبر بود، خطا را مدیریت کند. کاربر بتواند مقدار زبان و تم را تغییر دهد و تنظیمات جدید ذخیره شوند.

مفاهیم pathlib، json.load، json.dump، JSONDecodeError

### تمرین ۳ — تحلیل داده‌های JSON

یک فایل JSON شامل فهرست محصولات، قیمت‌ها و دسته‌بندی‌ها بساز. برنامه باید داده‌ها را بخواند، محصولات یک دسته را پیدا کند، قیمت محصولی را تغییر دهد، یک محصول جدید اضافه کند و محصولی را حذف کند. در پایان، داده‌ها را با `indent=4` و `ensure_ascii=False` ذخیره کن.

مفاهیم Nested JSON، پیمایش لیست‌ها، تغییر داده و مدیریت خطا

پیشنهاد تمرین دوم برای مسیر یادگیری اتوماسیون بسیار کاربردی است؛ چون ذخیره تنظیمات و مدیریت فایل JSON در اسکریپت‌های واقعی زیاد استفاده می‌شود.