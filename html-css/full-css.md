# **سطح ۱ — مبانی CSS**

# **1. Introduction to CSS**

## **CSS چیست؟**

**CSS (Cascading Style Sheets)** زبان استایل‌دهی صفحات وب است. با CSS ظاهر، رنگ، اندازه، فاصله، موقعیت و نحوه نمایش عناصر HTML را کنترل می‌کنیم.

HTML اسکلت است، CSS ظاهر آن و JavaScript رفتار آن را کنترل می‌کند.

**بدون CSS**

Hello World

**Login**

Username:

Enter username

Submit

**با CSS**

# **Welcome Back**

Login to your account

Username

Password

Login

CSS ظاهر عناصر HTML را تغییر می‌دهد، نه لزوماً ساختار یا منطق آن‌ها را.

### **تفاوت HTML، CSS و JavaScript**

| زبان       | وظیفه       | مثال                       |
| ---------- | ----------- | -------------------------- |
| HTML       | ساختار صفحه | ساخت Button                |
| CSS        | ظاهر صفحه   | رنگ و اندازه Button        |
| JavaScript | رفتار صفحه  | کلیک Button و اجرای عملیات |

مثال:

```
<button id="btn">Click me</button>
```

- HTML دکمه را ایجاد می‌کند.
- CSS دکمه را رنگی و زیبا می‌کند.
- JavaScript می‌تواند با کلیک روی آن یک پیام نمایش دهد.

## **روش‌های اتصال CSS به HTML**

### **1. Inline CSS**

CSS مستقیماً داخل Attribute یک عنصر HTML نوشته می‌شود.

```
<p style="color: red; font-size: 20px;">
  Hello
</p>
```

- `style` محل نوشتن CSS است.
- `color` رنگ متن را تعیین می‌کند.
- `font-size` اندازه متن را تعیین می‌کند.

در Inline CSS، استایل مستقیماً روی همان عنصر اعمال می‌شود.

### **2. Internal CSS**

CSS داخل تگ `<style>` و معمولاً در بخش `<head>` نوشته می‌شود.

```
<head>
  <style>
    p {
      color: blue;
    }
  </style>
</head>
```

تمام تگ‌های `p` در این صفحه، در صورت نبود قوانین متعارض، آبی می‌شوند.

### **3. External CSS**

CSS در یک فایل جداگانه نوشته می‌شود.

index.html

```
<head>
  <link rel="stylesheet" href="style.css">
</head>
```

style.css

```
p {
  color: green;
}
```

- `rel="stylesheet"` مشخص می‌کند فایل لینک‌شده یک stylesheet است.
- `href` مسیر فایل CSS را مشخص می‌کند.

External CSS روش رایج در پروژه‌های واقعی است.

## **ساختار CSS Rule**

```
p {
  color: red;
  font-size: 20px;
}
```

اجزای این Rule

p

Selector

color

Property

red

Value

| اصطلاح      | معنی                                   |
| ----------- | -------------------------------------- |
| Selector    | انتخاب عنصر موردنظر                    |
| Property    | ویژگی‌ای که می‌خواهیم تغییر دهیم       |
| Value       | مقدار آن ویژگی                         |
| Declaration | یک Property و Value همراه با `;`       |
| Rule        | Selector به همراه مجموعه Declarationها |

# **2. CSS Syntax & Selectors**

**Selector مشخص می‌کند CSS روی کدام عنصر یا عناصر HTML اعمال شود.**

## **1. Element Selector**

انتخاب عناصر بر اساس نام تگ HTML.

```
p {
  color: red;
}

h1 {
  font-size: 30px;
}
```

تمام `p`ها قرمز و تمام `h1`ها با اندازه 30 پیکسل نمایش داده می‌شوند.

## **2. Class Selector**

انتخاب عناصر بر اساس Class. با `.` شروع می‌شود.

```
<p class="warning">Danger!</p>
<p class="warning">Alert!</p>
```

```
.warning {
  color: red;
}
```

تمام عناصر دارای کلاس `warning` استایل می‌گیرند.

یک Class می‌تواند روی چندین عنصر استفاده شود و یک عنصر نیز می‌تواند چند Class داشته باشد.

```
<p class="warning bold">Danger!</p>
```

## **3. ID Selector**

انتخاب عنصر بر اساس ID. با `#` شروع می‌شود.

```
<div id="header">Header</div>
```

```
#header {
  background-color: black;
  color: white;
}
```

ID معمولاً برای شناسایی یک عنصر مشخص استفاده می‌شود و در یک صفحه باید یکتا باشد.

## **4. Universal Selector**

انتخاب تمام عناصر HTML با `*`.

```
* {
  box-sizing: border-box;
}
```

این قانون روی تمام عناصر صفحه اعمال می‌شود.

یکی از کاربردهای رایج آن تنظیم Box Model برای تمام عناصر است.

## **5. Grouping Selector**

چند Selector را با کاما ترکیب می‌کنیم تا یک استایل مشترک به آن‌ها اعمال شود.

```
h1, h2, p {
  color: blue;
}
```

تمام `h1`، `h2` و `p`ها آبی می‌شوند.

کاما به معنی انتخاب چند Selector مستقل است.

## **6. Attribute Selector**

انتخاب عناصر بر اساس Attribute یا مقدار Attribute.

```
<input type="text">
<input type="password">
<input type="email">
```

```
input[type="password"] {
  border: 2px solid red;
}
```

فقط Inputهایی که Attribute `type` آن‌ها `password` است انتخاب می‌شوند.

### **انواع مهم Attribute Selector**

| Selector           | کاربرد                                  |
| ------------------ | --------------------------------------- |
| `[type]`           | عناصر دارای Attribute نوع type          |
| `[type="text"]`    | مقدار دقیق text                         |
| `[href^="https"]`  | مقدار شروع‌شونده با https               |
| `[href$=".pdf"]`   | مقدار پایان‌یافته با pdf                |
| `[class*="admin"]` | مقداری که شامل admin باشد               |
| `[type~="text"]`   | شامل کلمه text در مقدار space-separated |
| `[lang\\|="en"]`   | مقدار en یا شروع‌شده با en-             |

مثال:

```
a[href^="https"] {
  color: green;
}
```

تمام لینک‌هایی که `href` آن‌ها با `https` شروع می‌شود انتخاب می‌شوند.

Attribute Selector در بررسی ساختار HTML، فرم‌ها و سناریوهای CSS Injection اهمیت زیادی دارد.

## **7. Descendant Selector**

انتخاب عناصر داخل یک عنصر دیگر، در هر عمقی.

```
<div class="container">
  <p>Hello</p>

  <section>
    <p>Nested Hello</p>
  </section>
</div>
```

```
.container p {
  color: red;
}
```

هر دو `p` انتخاب می‌شوند؛ چون در داخل `.container` قرار دارند.

فاصله بین Selectorها یعنی انتخاب Descendant.

## **8. Child Selector**

انتخاب فقط فرزندان مستقیم یک عنصر با `>`.

```
<div class="container">
  <p>Direct Child</p>

  <section>
    <p>Nested Child</p>
  </section>
</div>
```

```
.container > p {
  color: blue;
}
```

انتخاب می‌شود:

Direct Child

انتخاب نمی‌شود:

Nested Child

چون `p` دوم فرزند مستقیم `.container` نیست.

## **9. Adjacent Sibling Selector**

انتخاب عنصر بلافاصله بعد از عنصر دیگر با `+`.

```
<h2>Title</h2>
<p>First paragraph</p>
<p>Second paragraph</p>
```

```
h2 + p {
  color: red;
}
```

فقط `First paragraph` انتخاب می‌شود؛ چون بلافاصله بعد از `h2` قرار دارد.

## **10. General Sibling Selector**

انتخاب تمام عناصر هم‌سطح بعد از عنصر موردنظر با `~`.

```
<h2>Title</h2>
<p>First paragraph</p>
<div>Other Element</div>
<p>Second paragraph</p>
```

```
h2 ~ p {
  color: blue;
}
```

هر دو `p` انتخاب می‌شوند؛ چون هر دو بعد از `h2` و در سطح یکسان هستند.

تفاوت `+` و `~`

`+` Adjacent

فقط اولین عنصر هم‌سطح بلافاصله بعدی.

`~` General

تمام عناصر هم‌سطح بعدی، حتی با وجود عناصر دیگر.

## **11. Pseudo-classes**

Pseudo-class وضعیت یا شرایط خاص یک عنصر را مشخص می‌کند.

با `:` نوشته می‌شود.

### **مثال‌های مهم**

| Pseudo-class    | کاربرد                              |
| --------------- | ----------------------------------- |
| `:hover`        | وقتی Mouse روی عنصر قرار می‌گیرد    |
| `:active`       | هنگام فعال شدن یا فشردن عنصر        |
| `:focus`        | وقتی عنصر Focus دارد                |
| `:visited`      | لینک بازدیدشده                      |
| `:checked`      | Input انتخاب‌شده                    |
| `:disabled`     | عنصر غیرفعال                        |
| `:first-child`  | اولین فرزند                         |
| `:last-child`   | آخرین فرزند                         |
| `:nth-child(n)` | انتخاب بر اساس موقعیت فرزند         |
| `:not()`        | انتخاب عناصر به‌جز موارد مشخص       |
| `:is()`         | ترکیب Selectorها                    |
| `:where()`      | ترکیب Selectorها با Specificity صفر |

مثال:

```
button:hover {
  background-color: green;
}

input:focus {
  border-color: blue;
}

li:first-child {
  color: red;
}
```

- وقتی Mouse روی Button باشد، رنگ آن سبز می‌شود.
- وقتی Input Focus داشته باشد، Border آن آبی می‌شود.
- اولین `li` قرمز می‌شود.

### `:nth-child()`

```
li:nth-child(2) {
  color: red;
}
```

فرزند دوم انتخاب می‌شود.

```
li:nth-child(odd) {
  background-color: gray;
}
```

فرزندان با موقعیت فرد انتخاب می‌شوند.

```
li:nth-child(even) {
  background-color: white;
}
```

فرزندان با موقعیت زوج انتخاب می‌شوند.

## **12. Pseudo-elements**

Pseudo-element به ما اجازه می‌دهد بخش خاصی از یک عنصر را استایل دهی کنیم یا محتوای تزئینی ایجاد کنیم.

با `::` نوشته می‌شود.

| Pseudo-element   | کاربرد                          |
| ---------------- | ------------------------------- |
| `::before`       | ایجاد محتوای قبل از محتوای عنصر |
| `::after`        | ایجاد محتوای بعد از محتوای عنصر |
| `::first-letter` | استایل اولین حرف                |
| `::first-line`   | استایل اولین خط                 |
| `::selection`    | استایل متن انتخاب‌شده           |
| `::placeholder`  | استایل Placeholder Input        |

مثال:

```
h1::before {
  content: "🔥 ";
}

h1::after {
  content: "!";
}
```

اگر HTML این باشد:

```
<h1>Hello World</h1>
```

در ظاهر این متن را می‌بینیم:

# **🔥 Hello World!**

محتوای ایجادشده با `::before` و `::after` لزوماً جزئی از DOM واقعی HTML نیست و به‌تنهایی جایگزین HTML نمی‌شود.

# **خلاصه Selectorها برای مرور سریع**

| Selector        | نمونه           | مفهوم                      |
| --------------- | --------------- | -------------------------- |
| Element         | `p`             | تمام تگ‌های p              |
| Class           | `.box`          | تمام عناصر دارای box       |
| ID              | `#main`         | عنصر دارای ID main         |
| Universal       | `*`             | تمام عناصر                 |
| Grouping        | `h1, p`         | چند Selector               |
| Attribute       | `[type="text"]` | عناصر با Attribute مشخص    |
| Descendant      | `.box p`        | p در هر عمق داخل box       |
| Child           | `.box > p`      | p فرزند مستقیم box         |
| Adjacent        | `h2 + p`        | p بلافاصله بعد از h2       |
| General Sibling | `h2 ~ p`        | تمام pهای هم‌سطح بعد از h2 |
| Pseudo-class    | `input:focus`   | عنصر در وضعیت مشخص         |
| Pseudo-element  | `p::first-line` | بخشی از عنصر               |

**تمرین سریع**

یک فایل HTML بساز و سعی کن بدون نگاه کردن به جواب، با Selectorها عناصر زیر را انتخاب کنی:

- تمام `p`ها را قرمز کن.
- فقط عناصر دارای کلاس `info` را آبی کن.
- عنصر دارای ID `header` را خاکستری کن.
- Inputهای `password` را Border قرمز بده.
- فقط `p`های داخل `.container` را انتخاب کن.
- فقط فرزندان مستقیم `.container` را انتخاب کن.
- اولین `p` بعد از `h2` را سبز کن.
- وقتی Mouse روی Button رفت، رنگش تغییر کند.
- قبل از هر `h2` یک `★` نمایش بده.

اگر این سطح را فهمیدی، آماده‌ای برویم سراغ **Box Model، Units، Typography و Background**.
