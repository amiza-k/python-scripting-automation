# ۴. آموزش `pathlib` در پایتون

`pathlib` ماژولی داخلی برای ساخت مسیرها و مدیریت فایل‌ها و پوشه‌هاست؛ یکی از ابزارهای پرکاربرد در اسکریپت‌نویسی و اتوماسیون.

## ۱. مفهوم `Path` و تفاوت آن با `String`

`String` مسیر را صرفاً به‌شکل متن نگه می‌دارد، اما `Path` امکاناتی برای کار با مسیر فایل و پوشه فراهم می‌کند.

```
from pathlib import Pathtext_path = "data/report.txt"file_path = Path("data/report.txt")
```

با `Path` می‌توانی وجود فایل را بررسی کنی، مسیر بسازی، فایل بخوانی و عملیات مختلف انجام بدهی.

## ۲. ساخت مسیر و اتصال مسیرها

با `Path()` مسیر می‌سازیم و با عملگر `/` اجزای مسیر را به هم متصل می‌کنیم.

```
from pathlib import Pathfolder = Path("data")file_path = folder / "report.txt"
```

مسیر نسبی (`Relative`) نسبت به محل اجرای برنامه تفسیر می‌شود؛ مسیر مطلق (`Absolute`) از نقطه شروع مشخصی در سیستم فایل آغاز می‌شود.

```
path = Path("data/report.txt")print(path.is_absolute())print(Path.cwd())
```

خروجی خط اول برای این مسیر نسبی `False` است. خط دوم مسیر پوشه کاری فعلی را نمایش می‌دهد.

## ۳. اجزای مسیر

```
from pathlib import Pathpath = Path("documents/report.pdf")print(path.name)print(path.stem)print(path.suffix)print(path.parent)
```

خروجی:

```
report.pdf
report
.pdf
documents
```

- `name`: نام فایل همراه پسوند
- `stem`: نام فایل بدون پسوند نهایی
- `suffix`: پسوند نهایی
- `parent`: پوشه والد

## ۴. بررسی وجود فایل و پوشه

با این متدها وضعیت مسیر را بررسی می‌کنیم:

```
from pathlib import Pathpath = Path("data/report.txt")print(path.exists())print(path.is_file())print(path.is_dir())
```

- `exists()`: آیا مسیر وجود دارد؟
- `is_file()`: آیا مسیر به فایل اشاره می‌کند؟
- `is_dir()`: آیا مسیر به پوشه اشاره می‌کند؟

## ۵. ساخت پوشه با `mkdir()`

```
from pathlib import Pathfolder = Path("data/reports")folder.mkdir(parents=True, exist_ok=True)
```

- `parents=True`: پوشه‌های والدِ لازم را نیز می‌سازد.
- `exist_ok=True`: اگر پوشه از قبل وجود داشته باشد، خطا نمی‌دهد.

## ۶. فهرست‌کردن و جست‌وجوی فایل‌ها

### `iterdir()`

محتویات مستقیم یک پوشه را پیمایش می‌کند:

```
from pathlib import Pathfolder = Path("data")for item in folder.iterdir():    print(item.name)
```

### `glob()` و `rglob()`

`glob()` برای جست‌وجو بر اساس الگو در پوشه مشخص‌شده و `rglob()` برای جست‌وجوی بازگشتی در زیرپوشه‌هاست.

```
from pathlib import Pathfolder = Path("data")for file in folder.glob("*.txt"):    print(file)for file in folder.rglob("*.pdf"):    print(file)
```

`*.txt` یعنی فایل‌هایی با پسوند `.txt`. در جست‌وجوی بازگشتی، فایل‌های زیرپوشه‌ها نیز بررسی می‌شوند.

## ۷. تغییر نام و حذف فایل یا پوشه

```
from pathlib import Pathfile = Path("data/old.txt")file.rename("data/new.txt")
```

`rename()` نام یا مسیر فایل را تغییر می‌دهد؛ رفتار آن در مقصد موجود و بین فایل‌سیستم‌های مختلف می‌تواند متفاوت باشد.

`replace()` نیز فایل مقصد را جایگزین می‌کند؛ بنابراین در استفاده از آن مراقب فایل مقصد باش.

```
from pathlib import Pathfile = Path("data/old.txt")file.replace("data/new.txt")
```

برای حذف فایل:

```
from pathlib import PathPath("data/old.txt").unlink()
```

برای حذف پوشه خالی:

```
from pathlib import PathPath("data/empty").rmdir()
```

نکات مهم:

- `unlink()` فایل را حذف می‌کند؛ برای حذف فایل ناموجود می‌توان از `missing_ok=True` استفاده کرد.
- `rmdir()` فقط پوشه خالی را حذف می‌کند.
- برای عملیات حذف و جایگزینی، مسیر را قبل از اجرا بررسی کن.

## ۸. خواندن و نوشتن متن

```
from pathlib import Pathfile = Path("data/report.txt")file.write_text("Hello Python", encoding="utf-8")content = file.read_text(encoding="utf-8")
```

`write_text()` محتوای قبلی فایل را جایگزین می‌کند. `read_text()` کل محتوای فایل را به‌صورت رشته می‌خواند.

## ۹. خواندن و نوشتن بایت

برای فایل‌های باینری مثل تصویر و PDF از متدهای بایتی استفاده می‌کنیم.

```
from pathlib import Pathsource = Path("image.png")destination = Path("image-copy.png")data = source.read_bytes()destination.write_bytes(data)
```

- `read_bytes()`: محتوا را به‌صورت `bytes` می‌خواند.
- `write_bytes()`: داده باینری را می‌نویسد و محتوای قبلی را جایگزین می‌کند.

برای فایل متنی از متدهای متنی و برای فایل باینری از متدهای بایتی استفاده کن.

## ۱۰. کار با پسوندها

برای تغییر پسوند نهایی فایل از `with_suffix()` استفاده می‌کنیم:

```
from pathlib import Pathfile = Path("report.txt")new_file = file.with_suffix(".csv")
```

مقدار `file` همچنان `report.txt` است؛ مقدار جدید در `new_file` ذخیره می‌شود. این متد مسیر جدید می‌سازد و خودش فایل را تغییر نام نمی‌دهد.

برای تغییر نام واقعی فایل:

```
file.rename(new_file)
```

## ۱۱. سازگاری با سیستم‌عامل‌های مختلف

`pathlib` جداکننده مسیر را با سیستم‌عامل هماهنگ می‌کند. بنابراین به‌جای ساخت مسیر با چسباندن رشته‌ها، از `/` استفاده کن.

```
from pathlib import Pathfile = Path("data") / "reports" / "report.txt"
```

این روش در ویندوز، لینوکس و macOS قابل استفاده است.

## ۱۲. تفاوت `resolve()` و `absolute()`

- `absolute()`: مسیر را به‌شکل مطلق تبدیل می‌کند.
- `resolve()`: مسیر را به‌شکل استانداردشده حل می‌کند و معمولاً بخش‌هایی مثل `..` و پیوندهای نمادین را نیز در نظر می‌گیرد.

```
from pathlib import Pathpath = Path("data/../report.txt")print(path.absolute())print(path.resolve())
```

خروجی دقیق به سیستم و محل اجرای برنامه بستگی دارد.

# سه تمرین جامع

### تمرین ۱ — بررسی پوشه

مسیر یک پوشه را از کاربر دریافت کن؛ وجود آن را بررسی کن، فایل‌ها و پوشه‌های داخلش را فهرست کن و تعداد فایل‌های `.txt` را بشمار. اگر پوشه وجود نداشت، پیام مناسب نمایش بده.

مفاهیم: Path، exists، is_dir، iterdir، suffix

### تمرین ۲ — مرتب‌سازی فایل‌ها

برنامه‌ای بنویس که در یک پوشه، فایل‌های متنی را پیدا کند و با توجه به پسوندشان به پوشه‌های جداگانه منتقل کند. پوشه‌های مقصد در صورت نیاز ساخته شوند و فایل‌های هم‌نام بدون بررسی حذف یا جایگزین نشوند.

مفاهیم: glob، mkdir، rename یا replace، name، suffix

### تمرین ۳ — ابزار پشتیبان‌گیری

مسیر یک پوشه را دریافت کن، تمام فایل‌های آن و زیرپوشه‌هایش را با `rglob()` پیدا کن و نسخه‌ای از فایل‌ها را در پوشه پشتیبان بساز. ساختار پوشه‌ها حفظ شود، مسیرها با `pathlib` ساخته شوند و خطاهای فایل و دسترسی مدیریت شوند.

مفاهیم: rglob، read_bytes، write_bytes، parent، resolve و مدیریت خطا

پیشنهاد: تمرین اول را بنویس و کدت را بفرست تا بررسی کنیم؛ بعد به سراغ اتوماسیون فایل‌ها در تمرین‌های دوم و سوم برویم.