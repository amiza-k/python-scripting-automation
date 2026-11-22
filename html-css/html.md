# **جزوه جامع HTML — خلاصه برای مرور و یادگیری**

HTML Fundamentals | Quick Revision Notes

این جزوه شامل مباحثی است که تا اینجا مطالعه کردیم؛ از ساختار اولیه HTML تا Forms، Attributes و مفاهیم مهم برای Web Security و Bug Bounty.

# **1. Introduction to HTML**

**HTML (HyperText Markup Language)** زبان نشانه‌گذاری برای ساختاردهی محتوای صفحات وب است.

- HTML: ساختار صفحه
- CSS: ظاهر و طراحی صفحه
- JavaScript: رفتار و تعامل صفحه

### **مفاهیم پایه**

- **Tag:** نام تگ مانند `p` یا `div`.
- **Element:** تگ باز، محتوا و تگ بسته.
- **Attribute:** ویژگی اضافی یک عنصر.
- **Nesting:** قرار گرفتن یک عنصر داخل عنصر دیگر.

مثال:

```
<p class="text">Hello World</p>
```

- `p`: Tag
- کل عبارت: Element
- `class`: Attribute
- `text`: مقدار Attribute

# **2. HTML Document Structure**

ساختار استاندارد یک سند HTML:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>
</head>

<body>
    <h1>Hello World</h1>
    <p>Welcome to my website.</p>
</body>

</html>
```

| عنصر              | کاربرد                        |
| ----------------- | ----------------------------- |
| `<!DOCTYPE html>` | اعلام استاندارد HTML5         |
| `html`            | عنصر ریشه صفحه                |
| `head`            | اطلاعات و Metadata صفحه       |
| `body`            | محتوای قابل نمایش             |
| `title`           | عنوان تب مرورگر               |
| `meta`            | اطلاعات توصیفی و تنظیمات صفحه |

### **Metaهای مهم**

```
<meta charset="UTF-8">
```

تعیین Character Encoding.

```
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

تنظیم نمایش صفحه برای دستگاه‌های مختلف.

```
<meta name="description" content="HTML Tutorial">
```

توضیحات صفحه برای موتورهای جستجو.

### **Nesting**

قرار گرفتن یک عنصر داخل عنصر دیگر:

```
<div>
    <p>Hello <strong>World</strong></p>
</div>
```

- Parent: عنصر والد
- Child: عنصر فرزند
- تگ‌ها باید با ترتیب صحیح بسته شوند.

### **Comment**

برای توضیحات داخل سورس کد:

```
<!-- This is a comment -->
```

Comment در محتوای عادی صفحه نمایش داده نمی‌شود، اما در View Source قابل مشاهده است؛ پس اطلاعات حساس را داخل آن قرار ندهید.

# **3. Text Elements**

تگ‌های مربوط به متن و قالب‌بندی محتوا.

| Tag          | کاربرد                     |
| ------------ | -------------------------- |
| `h1` تا `h6` | عنوان‌ها و زیرعنوان‌ها     |
| `p`          | پاراگراف                   |
| `br`         | رفتن به خط بعد             |
| `hr`         | جداکننده موضوعی            |
| `pre`        | حفظ فاصله‌ها و خطوط متن    |
| `blockquote` | نقل‌قول طولانی             |
| `strong`     | اهمیت معنایی زیاد          |
| `em`         | تأکید معنایی               |
| `b`          | Bold ظاهری                 |
| `i`          | متن با حالت نوشتاری متفاوت |
| `small`      | متن جانبی کوچک‌تر          |
| `mark`       | هایلایت متن                |
| `del`        | متن حذف‌شده                |
| `ins`        | متن اضافه‌شده              |
| `sub`        | زیرنویس                    |
| `sup`        | بالانویس                   |

### **مثال‌ها**

```
<h1>Main Title</h1>
<h2>Sub Title</h2>

<p>This is a paragraph.</p>

Hello<br>World

<hr>

<pre>
Line 1
    Line 2
</pre>

<blockquote>Knowledge is power.</blockquote>

<strong>Important</strong>
<em>Emphasized</em>

<b>Bold</b>
<i>Italic</i>

<small>Disclaimer</small>
<mark>Highlighted</mark>

<del>100$</del>
<ins>80$</ins>

H<sub>2</sub>O
2<sup>3</sup>
```

**نکته:** `strong` و `em` معنای محتوایی دارند، اما `b` و `i` بیشتر برای نمایش یا لحن متفاوت هستند.

# **4. Links and Navigation**

برای ایجاد لینک و انتقال کاربر به صفحات یا منابع دیگر.

### **تگ&#x20;**`a`**&#x20;و Attribute&#x20;**`href`

```
<a href="https://google.com">Google</a>
```

- `a`: Anchor Element
- `href`: آدرس مقصد لینک

### **انواع URL**

| نوع               | توضیح                   | مثال                        |
| ----------------- | ----------------------- | --------------------------- |
| Absolute URL      | آدرس کامل               | `https://example.com/about` |
| Relative URL      | مسیر نسبی               | `about.html`                |
| Root-relative URL | مسیر نسبت به ریشه دامنه | `/login`                    |

### **لینک داخلی و خارجی**

```
<!-- External -->
<a href="https://google.com">Google</a>

<!-- Internal -->
<a href="/login">Login</a>
```

### **لینک به بخش مشخصی از صفحه**

با `id` و `#`:

```
<a href="#contact">Contact</a>

<h2 id="contact">Contact Section</h2>
```

### **Attribute&#x20;**`target`

تعیین محل باز شدن لینک:

| مقدار     | کاربرد                    |
| --------- | ------------------------- |
| `_self`   | همان Tab                  |
| `_blank`  | Tab یا Window جدید        |
| `_parent` | Parent Context            |
| `_top`    | بالاترین Browsing Context |

```
<a href="https://example.com" target="_blank">
    Open Website
</a>
```

### **Attribute&#x20;**`rel`

مشخص کردن رابطه بین صفحه فعلی و مقصد:

```
<a href="https://example.com"
   target="_blank"
   rel="noopener noreferrer">
   Open
</a>
```

- `noopener`: جلوگیری از دسترسی صفحه مقصد به `window.opener`.
- `noreferrer`: عدم ارسال Referer به مقصد و اعمال رفتار noopener در مرورگرهای مدرن.

### **لینک ایمیل و تلفن**

```
<a href="mailto:test@example.com">Email</a>

<a href="tel:+989123456789">Call</a>
```

**نکته Web Security:** بررسی URLها، پارامترها، لینک‌های Redirect و Attributeهای لینک در تحلیل امنیت وب کاربرد دارد.

# **5. Images and Media**

### **تصویر با&#x20;**`img`

```
<img src="photo.jpg" alt="My Photo">
```

| Attribute | کاربرد            |
| --------- | ----------------- |
| `src`     | مسیر تصویر        |
| `alt`     | متن جایگزین تصویر |
| `width`   | عرض               |
| `height`  | ارتفاع            |

`img` یک Void Element است و تگ بسته ندارد.

```
<img src="cat.jpg" alt="Cat" width="300" height="200">
```

### `figure`**&#x20;و&#x20;**`figcaption`

برای نمایش محتوا همراه با توضیحات:

```
<figure>
    <img src="cat.jpg" alt="Cat">
    <figcaption>A cute cat</figcaption>
</figure>
```

### **Audio**

```
<audio controls>
    <source src="music.mp3" type="audio/mpeg">
</audio>
```

### **Video**

```
<video controls width="400">
    <source src="video.mp4" type="video/mp4">
</video>
```

Attributeهای مهم:

- `controls`: نمایش کنترل پخش
- `autoplay`: پخش خودکار
- `muted`: بی‌صدا
- `loop`: تکرار
- `poster`: تصویر پیش‌نمایش ویدئو

### **Source**

برای معرفی منابع جایگزین Media:

```
<video controls>
    <source src="video.mp4" type="video/mp4">
    <source src="video.webm" type="video/webm">
</video>
```

### **iframe**

برای Embed کردن صفحه یا محتوای خارجی:

```
<iframe src="https://example.com"
        width="500"
        height="300">
</iframe>
```

**نکته امنیتی:** Attribute مهم `sandbox` برای محدود کردن قابلیت‌های محتوای داخل iframe است.

```
<iframe src="https://example.com" sandbox></iframe>
```

# **6. Lists**

برای نمایش مجموعه‌ای از اطلاعات.

### **Unordered List —&#x20;**`ul`

لیست بدون ترتیب، معمولاً با Bullet:

```
<ul>
    <li>Python</li>
    <li>HTML</li>
    <li>JavaScript</li>
</ul>
```

### **Ordered List —&#x20;**`ol`

لیست شماره‌گذاری‌شده:

```
<ol>
    <li>Install</li>
    <li>Configure</li>
    <li>Run</li>
</ol>
```

### **List Item —&#x20;**`li`

هر آیتم داخل لیست.

### **Description List —&#x20;**`dl`

لیست شامل عنوان و توضیحات:

```
<dl>
    <dt>HTML</dt>
    <dd>Markup language for web pages.</dd>
</dl>
```

- `dl`: کل لیست
- `dt`: عنوان یا Term
- `dd`: توضیحات

### **Nested Lists**

لیست تو در تو:

```
<ul>
    <li>Security
        <ul>
            <li>XSS</li>
            <li>SQL Injection</li>
        </ul>
    </li>
</ul>
```

# **7. Tables**

برای نمایش داده‌ها در قالب سطر و ستون.

### **تگ‌های جدول**

| Tag       | کاربرد           |
| --------- | ---------------- |
| `table`   | کل جدول          |
| `tr`      | سطر              |
| `td`      | سلول داده        |
| `th`      | سلول عنوان       |
| `thead`   | بخش Header       |
| `tbody`   | بخش اصلی داده‌ها |
| `tfoot`   | بخش پایانی       |
| `caption` | عنوان جدول       |

### **مثال کامل**

```
<table>
    <caption>Users</caption>

    <thead>
        <tr>
            <th>Name</th>
            <th>Age</th>
        </tr>
    </thead>

    <tbody>
        <tr>
            <td>Amir</td>
            <td>21</td>
        </tr>
    </tbody>

    <tfoot>
        <tr>
            <td>Total</td>
            <td>1 User</td>
        </tr>
    </tfoot>
</table>
```

### `colspan`

ادغام چند ستون:

```
<td colspan="2">Full Width</td>
```

### `rowspan`

ادغام چند سطر:

```
<td rowspan="2">Security</td>
```

# **8. HTML Forms**

بسیار مهم برای Web Security

Form برای دریافت اطلاعات کاربر و ارسال آن به سرور استفاده می‌شود.

### **Form، Action و Method**

```
<form action="/login" method="POST">

    <input type="text" name="username">
    <input type="password" name="password">

    <button type="submit">Login</button>

</form>
```

| مفهوم    | کاربرد             |
| -------- | ------------------ |
| `form`   | تعریف فرم          |
| `action` | مقصد ارسال اطلاعات |
| `method` | روش ارسال اطلاعات  |

### **تفاوت GET و POST**

| GET                                  | POST                                          |
| ------------------------------------ | --------------------------------------------- |
| داده‌ها معمولاً در URL ارسال می‌شوند | داده‌ها معمولاً در Request Body ارسال می‌شوند |
| مناسب جستجو و دریافت اطلاعات         | مناسب ارسال داده و عملیات                     |
| Query String دارد                    | معمولاً Body دارد                             |
| داده‌ها در URL قابل مشاهده‌اند       | داده‌ها در URL نمایش داده نمی‌شوند            |

مثال GET:

```
GET /search?q=html HTTP/1.1
```

مثال POST:

```
POST /login HTTP/1.1
Content-Type: application/x-www-form-urlencoded

username=amir&password=123
```

**نکته امنیتی:** POST به‌تنهایی امنیت ایجاد نمی‌کند. برای محافظت از اطلاعات به HTTPS و کنترل‌های امنیتی مناسب نیاز داریم.

### **Input و انواع آن**

| Type       | کاربرد                    |
| ---------- | ------------------------- |
| `text`     | متن                       |
| `password` | رمز عبور                  |
| `email`    | ایمیل                     |
| `number`   | عدد                       |
| `hidden`   | مقدار غیرقابل نمایش در UI |
| `checkbox` | انتخاب چند گزینه          |
| `radio`    | انتخاب یک گزینه           |
| `file`     | انتخاب فایل               |
| `submit`   | ارسال فرم                 |
| `button`   | دکمه معمولی               |
| `search`   | جستجو                     |
| `url`      | دریافت URL                |

مثال:

```
<input type="text" name="username">

<input type="password" name="password">

<input type="email" name="email">

<input type="hidden" name="role" value="user">

<input type="checkbox" name="remember">

<input type="radio" name="gender" value="male">

<input type="file" name="avatar">
```

### **Input Attributes**

| Attribute      | کاربرد                             |
| -------------- | ---------------------------------- |
| `name`         | نام پارامتر ارسالی                 |
| `value`        | مقدار اولیه                        |
| `placeholder`  | متن راهنما                         |
| `required`     | الزامی بودن                        |
| `readonly`     | فقط خواندنی                        |
| `disabled`     | غیرفعال                            |
| `maxlength`    | حداکثر طول متن                     |
| `min`          | حداقل مقدار                        |
| `max`          | حداکثر مقدار                       |
| `pattern`      | الگوی Regex برای اعتبارسنجی مرورگر |
| `autocomplete` | تنظیم Autofill                     |
| `type`         | نوع ورودی                          |

مثال:

```
<input
    type="text"
    name="username"
    value="amir"
    placeholder="Enter username"
    maxlength="20"
    required
>
```

### **تفاوت readonly و disabled**

- `readonly`: کاربر نمی‌تواند مقدار را از طریق UI ویرایش کند، اما مقدار معمولاً ارسال می‌شود.
- `disabled`: عنصر غیرفعال است و مقدار آن در ارسال معمول فرم شرکت نمی‌کند.

### **Label**

ارتباط دادن عنوان به Input:

```
<label for="username">Username:</label>

<input type="text" id="username">
```

مقدار `for` باید با `id` عنصر موردنظر یکی باشد.

### **Textarea**

برای متن چندخطی:

```
<textarea name="message" rows="4"></textarea>
```

### **Select و Option**

برای ساخت Dropdown:

```
<select name="country">
    <option value="iran">Iran</option>
    <option value="italy">Italy</option>
</select>
```

### **Button**

```
<button type="submit">Submit</button>

<button type="button">Click</button>

<button type="reset">Reset</button>
```

| Type     | کاربرد                      |
| -------- | --------------------------- |
| `submit` | ارسال فرم                   |
| `button` | دکمه معمولی                 |
| `reset`  | بازگرداندن مقادیر اولیه فرم |

### **Fieldset و Legend**

برای گروه‌بندی ورودی‌های مرتبط:

```
<fieldset>
    <legend>Account Information</legend>

    <input type="text" name="username">
    <input type="password" name="password">

</fieldset>
```

# **9. HTML Attributes**

Attributeها ویژگی‌های اضافی عناصر HTML هستند.

### **Global Attributes**

در اکثر عناصر HTML قابل استفاده هستند.

| Attribute         | کاربرد              |
| ----------------- | ------------------- |
| `id`              | شناسه یکتا          |
| `class`           | گروه‌بندی عناصر     |
| `style`           | CSS مستقیم          |
| `title`           | توضیح اضافی         |
| `data-*`          | اطلاعات سفارشی      |
| `hidden`          | مخفی کردن عنصر      |
| `tabindex`        | کنترل Focus         |
| `contenteditable` | قابلیت ویرایش محتوا |
| `draggable`       | قابلیت Drag         |
| `dir`             | جهت متن             |
| `lang`            | زبان محتوا          |

### **مثال‌ها**

```
<h1 id="main-title">Welcome</h1>

<p class="info">Hello</p>

<p style="color:red;">Red Text</p>

<p title="Extra Information">Hover Me</p>

<div data-user-id="123" data-role="admin">
    User
</div>

<p hidden>Hidden Content</p>

<button tabindex="0">Focusable</button>

<p contenteditable="true">Edit Me</p>

<div draggable="true">Drag Me</div>

<p dir="rtl">سلام</p>

<p lang="fa">سلام</p>
```

### **نکات امنیتی مهم**

- `hidden`: محتوا را محرمانه نمی‌کند.
- `data-*`: داده‌های قابل دسترسی برای JavaScript را نگهداری می‌کند.
- `contenteditable`: امکان ویرایش محتوا را فراهم می‌کند.
- `id` و `class`: در انتخاب عناصر توسط JavaScript و DOM کاربرد دارند.
- `style`: می‌تواند روی ظاهر و برخی رفتارهای نمایشی اثر بگذارد.

# **10. HTML Entities**

برای نمایش کاراکترهای خاص و کاراکترهایی که با Syntax HTML تداخل دارند.

| Entity   | خروجی              |
| -------- | ------------------ |
| `&lt;`   | `<`                |
| `&gt;`   | `>`                |
| `&amp;`  | `&`                |
| `&quot;` | `"`                |
| `&apos;` | `'`                |
| `&nbsp;` | فاصله Non-breaking |

### **مثال**

```
<p>&lt;h1&gt;Hello&lt;/h1&gt;</p>
```

خروجی:

`<h1>Hello</h1>`

مرورگر به‌جای تفسیر متن به‌عنوان تگ HTML، آن را به‌صورت متن نمایش می‌دهد.

**نکته امنیتی:** Encoding باید متناسب با Context باشد. HTML Entity Encoding برای تمام Contextهای JavaScript، URL یا CSS کافی نیست.

# **11. نکات مهم HTML برای Bug Bounty**

این بخش را جداگانه نگه دار؛ چون در بررسی صفحات وب و پیدا کردن آسیب‌پذیری‌ها کاربرد مستقیم دارد.

| مفهوم             | اهمیت امنیتی                           |
| ----------------- | -------------------------------------- |
| `form`            | شناخت محل ارسال اطلاعات                |
| `action`          | شناسایی Endpoint                       |
| `method`          | تشخیص GET و POST                       |
| `name`            | شناسایی پارامترهای درخواست             |
| `value`           | بررسی مقادیر قابل تغییر                |
| `hidden`          | بررسی داده‌های پنهان در UI             |
| `readonly`        | بررسی محدودیت‌های سمت کلاینت           |
| `disabled`        | بررسی وضعیت ورودی‌ها                   |
| `pattern`         | شناخت Client-side Validation           |
| `data-*`          | بررسی داده‌های مورد استفاده JavaScript |
| `contenteditable` | شناخت نقاط ورودی محتوای کاربر          |
| `iframe`          | بررسی Contextهای Embedded              |
| `href`            | بررسی مقصد لینک‌ها                     |
| `target` و `rel`  | شناخت رفتار لینک‌ها                    |
| HTML Entities     | شناخت Encoding و Decoding              |
| Comments          | بررسی اطلاعات افشاشده در Source        |

## **چند نکته کلیدی که نباید فراموش کنی**

1. هر چیزی که در سمت کلاینت قرار دارد، بالقوه قابل مشاهده و تغییر است.
2. Validation سمت مرورگر جایگزین Validation سمت سرور نیست.
3. `hidden` به معنی محرمانه بودن اطلاعات نیست.
4. `readonly` و `disabled` کنترل امنیتی سمت سرور نیستند.
5. GET و POST به‌تنهایی سطح امنیت را تعیین نمی‌کنند.
6. HTML Entities و Encoding در درک XSS اهمیت زیادی دارند.
7. HTML Source با DOM نهایی مرورگر همیشه یکسان نیست.

# **12. چک‌لیست مرور نهایی**

برای اینکه مطمئن شوی HTML را یاد گرفته‌ای، باید بتوانی این موارد را بدون مراجعه به جزوه انجام بدهی:

**پیشرفت یادگیری HTML**

# **0٪**

0 از 13 مورد تکمیل شده

ساختار استاندارد HTML5 را از حفظ بنویسم.

تفاوت Tag، Element و Attribute را توضیح بدهم.

تفاوت h1 تا h6 و تگ‌های متنی را بدانم.

لینک داخلی، خارجی، Absolute و Relative بسازم.

تصویر، Audio، Video و iframe ایجاد کنم.

تفاوت ul، ol و dl را بدانم.

یک جدول با colspan و rowspan بسازم.

یک فرم Login با GET و POST طراحی کنم.

انواع Input و Attributeهای آن را بشناسم.

تفاوت readonly و disabled را توضیح بدهم.

Global Attributes را بشناسم.

HTML Entities را درک کنم.

توضیح بدهم چرا hidden و Comment امنیت ایجاد نمی‌کنند.

**پیشنهاد برای ادامه مسیر:** بعد از این جزوه، سراغ Semantic HTML، DOM، JavaScript Integration و سپس HTML Contexts برو. این مباحث برای درک عمیق‌تر XSS و تحلیل رفتار مرورگر اهمیت زیادی دارند.
