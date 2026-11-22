# **CSS — سطح ۱ | خلاصه مرور و جزوه**

## **1. Introduction to CSS**

**CSS (Cascading Style Sheets):** زبان استایل‌دهی صفحات وب برای کنترل ظاهر، رنگ، اندازه، فاصله و موقعیت عناصر HTML.

| زبان       | کاربرد             |
| ---------- | ------------------ |
| HTML       | ساختار صفحه        |
| CSS        | ظاهر صفحه          |
| JavaScript | رفتار و تعامل صفحه |

### **روش‌های اتصال CSS به HTML**

**1. Inline:** داخل Attribute عنصر HTML

```
<p style="color: red;">Hello</p>
```

**2. Internal:** داخل تگ `<style>` در HTML

```
<style>
  p { color: blue; }
</style>
```

**3. External:** داخل فایل CSS جداگانه

```
<link rel="stylesheet" href="style.css">
```

### **ساختار CSS Rule**

```
p {
  color: red;
  font-size: 20px;
}
```

- Selector: انتخاب عنصر (`p`)
- Property: ویژگی (`color`)
- Value: مقدار (`red`)
- Declaration: ترکیب Property و Value
- Rule: مجموعه Selector و Declarationها

## **2. CSS Syntax & Selectors**

Selector مشخص می‌کند CSS روی کدام عنصر HTML اعمال شود.

| نوع       | Syntax          | کاربرد                      |
| --------- | --------------- | --------------------------- |
| Element   | `p`             | انتخاب تمام تگ‌های p        |
| Class     | `.box`          | انتخاب عناصر دارای کلاس box |
| ID        | `#header`       | انتخاب عنصر دارای ID مشخص   |
| Universal | `*`             | انتخاب تمام عناصر           |
| Grouping  | `h1, p`         | انتخاب چند گروه مستقل       |
| Attribute | `[type="text"]` | انتخاب بر اساس Attribute    |

### **Attribute Selectors**

| Syntax             | کاربرد                  |
| ------------------ | ----------------------- |
| `[type]`           | دارای Attribute موردنظر |
| `[type="text"]`    | مقدار دقیق              |
| `[href^="https"]`  | شروع با مقدار مشخص      |
| `[href$=".pdf"]`   | پایان با مقدار مشخص     |
| `[class*="admin"]` | شامل عبارت مشخص         |
| `[lang\\|="en"]`   | مقدار en یا شروع با en- |

مثال:

```
input[type="password"] {
  border: 2px solid red;
}
```

### **Combinators (ارتباط بین عناصر)**

| Syntax     | نام              | کاربرد                          |
| ---------- | ---------------- | ------------------------------- |
| `.box p`   | Descendant       | تمام pهای داخل box در هر عمقی   |
| `.box > p` | Child            | فقط pهای فرزند مستقیم           |
| `h2 + p`   | Adjacent Sibling | اولین عنصر هم‌سطح بلافاصله بعدی |
| `h2 ~ p`   | General Sibling  | تمام pهای هم‌سطح بعدی           |

مثال:

```
.container p {
  color: red;
}

.container > p {
  color: blue;
}

h2 + p {
  color: green;
}

h2 ~ p {
  font-size: 20px;
}
```

## **3. Pseudo-classes**

برای انتخاب عنصر بر اساس وضعیت یا شرایط خاص استفاده می‌شوند.

با `:` نوشته می‌شوند.

| Syntax          | کاربرد                              |
| --------------- | ----------------------------------- |
| `:hover`        | قرار گرفتن Mouse روی عنصر           |
| `:active`       | فعال یا فشرده بودن عنصر             |
| `:focus`        | دریافت Focus                        |
| `:visited`      | لینک بازدیدشده                      |
| `:checked`      | Input انتخاب‌شده                    |
| `:disabled`     | عنصر غیرفعال                        |
| `:enabled`      | عنصر فعال                           |
| `:first-child`  | اولین فرزند                         |
| `:last-child`   | آخرین فرزند                         |
| `:nth-child(n)` | فرزند با موقعیت مشخص                |
| `:not()`        | به‌جز Selector مشخص                 |
| `:is()`         | ترکیب Selectorها                    |
| `:where()`      | ترکیب Selectorها با Specificity صفر |

مثال:

```
button:hover {
  background: green;
}

input:focus {
  border-color: blue;
}

li:nth-child(2) {
  color: red;
}

li:nth-child(odd) {
  background: gray;
}
```

## **4. Pseudo-elements**

برای استایل‌دهی بخش خاصی از عنصر یا ایجاد محتوای تزئینی استفاده می‌شوند.

با `::` نوشته می‌شوند.

| Syntax           | کاربرد                  |
| ---------------- | ----------------------- |
| `::before`       | ایجاد محتوا قبل از عنصر |
| `::after`        | ایجاد محتوا بعد از عنصر |
| `::first-letter` | اولین حرف               |
| `::first-line`   | اولین خط                |
| `::selection`    | متن انتخاب‌شده          |
| `::placeholder`  | Placeholder ورودی       |

مثال:

```
h1::before {
  content: "★ ";
}

p::first-letter {
  font-size: 30px;
}

input::placeholder {
  color: gray;
}
```

نکته: `::before` و `::after` با `content` کار می‌کنند و محتوای تولیدشده لزوماً به DOM اضافه نمی‌شود.

## **5. نکات مهم برای Web Security**

- HTML ساختار عناصر را مشخص می‌کند.
- CSS می‌تواند ظاهر عناصر را تغییر دهد، اما به‌تنهایی کنترل دسترسی یا امنیت ایجاد نمی‌کند.
- Attribute Selector برای بررسی Attributeهای HTML کاربرد دارد.
- شناخت Class، ID و Selectorها برای تحلیل DOM ضروری است.
- `:checked`، `:focus` و `:disabled` در بررسی فرم‌ها کاربرد دارند.
- `display: none` و `visibility: hidden` در ظاهر صفحه تفاوت دارند.
- CSS Injection یکی از مباحث امنیتی مرتبط با CSS است.
- CSS می‌تواند در کنار HTML و DOM در بررسی رفتار غیرعادی صفحات کمک‌کننده باشد.

## **چک‌لیست تسلط سطح ۱**

0 از 10 مورد

0٪

تفاوت HTML، CSS و JavaScript را می‌دانم.

سه روش اتصال CSS را می‌شناسم.

ساختار CSS Rule را می‌فهمم.

Element، Class و ID Selector را می‌شناسم.

Attribute Selectorها را می‌توانم بنویسم.

تفاوت Descendant و Child را می‌دانم.

تفاوت + و \~ را می‌فهمم.

Pseudo-classها را می‌شناسم.

Pseudo-elementها را می‌شناسم.

می‌توانم Selectorهای مختلف را در یک صفحه واقعی تشخیص بدهم.

**نکته نهایی:** مهم‌ترین بخش این جلسه برای مسیر Bug Bounty، تسلط بر انواع Selectorها، Attribute Selectorها، Combinators و Pseudo-classes است. این‌ها را باید بتوانی بدون نگاه کردن به جزوه بنویسی و تحلیل کنی.
