کامپوننت‌های مهم در بوت‌استرپ
=======================================

فریم‌ورک بوت‌استرپ مجهز به تعداد زیادی «کامپوننت» است.
**کامپوننت** 
یک قطعه آماده رابط کاربری،
مثل دکمه، کارت، نوار ناوبری، مودال و ... است
که فقط با نوشتن چند کلاس
می‌توان از آن استفاده کرد.

در این متن با چند کامپوننت مهم آشنا می‌شویم.

۱. دکمه‌ها (Buttons)
---------------------

دکمه‌ها برای انجام کارها استفاده می‌شوند: مثل «ثبت نام»، «ورود»، «دانلود» و … .
کلاس دکمه یا
``btn``
بر روی عناصر
``button``
و
``<input type="button">``
و 
``a``
قابل اعمال است.

در بوت‌استرپ،
دکمه‌ها نیز مانند برخی عناصر دیگر طبق
:doc:`رنگ‌بندی معنایی </contents/j.bootstrap/j.03.colors>` 
که پیش‌تر درباره آن صحبت کردیم، قابل سفارشی‌سازی هستند.
به طور مثال می‌توان از کلاس‌های زیر برای رنگ‌بندی دکمه‌ها استفاده کرد.

- ``btn-primary``
- ``btn-secondary``
- ``btn-success`` 
- و ...

**مثال:**

.. code-block:: html
  
  <button type="button" class="btn btn-primary">دکمه اصلی</button>
  <button type="button" class="btn btn-secondary">دکمه ساده</button>
  <button type="button" class="btn btn-danger">دکمه خطر!</button>

.. figure:: /images/bootstrap/bootstrap-buttons.jpg
  :alt: کامپوننت دکمه در بوت‌استرپ
  :align: center

  کامپوننت دکمه در بوت‌استرپ

۲. کارت‌ها (Cards)
-------------------

کارت‌ها، باکس‌های شیک و منظم هستند که می‌توان درون آن‌ها عنوان، متن، عکس، دکمه
و … گذاشت.
بیشترین کاربرد کارت‌ها در محصولات سایت‌های فروشگاهی،
اطلاعات پروفایل افراد، کارت‌های خبرها در سایت‌های خبری است.

**مثال:**

.. figure:: /images/bootstrap/bootstrap-components-cards.jpg
  :alt: کامپوننت کارت در بوت‌استرپ
  :align: center

  کامپوننت کارت در بوت‌استرپ

.. code-block:: html

  <div class="card" style="width: 18rem;">
    <img src="image.jpg" class="card-img-top" alt="عکس نمونه">
    <div class="card-body">
      <h5 class="card-title">عنوان کارت</h5>
      <p class="card-text">
        این یک متن نمونه برای داخل کارت است.
      </p>
      <a href="#" class="btn btn-primary">بیشتر بخوانید</a>
    </div>
  </div>


۳. نوار پیمایش (Navbar)
------------------------

``Navbar`` همان نوار بالای سایت است که معمولاً لوگو، منو، دکمه‌ی ورود/ثبت‌نام
و … در آن قرار دارد و در تمام صفحات تکرار شده است.
این عنصر در صورت استفاده صحیح ریسپانسیو بوده و در صفحات بزرگ و کوچک
به درستی نمایش داده می‌شود؛
به گونه‌ای که در صفحات موبایل نوار به صورت جمع شونده نمایش داده می‌شود.

**مثال:**

.. figure:: /images/bootstrap/bootstrap-navbar-lg.jpg
  :alt: کامپوننت نوار پیمایش در بوت‌استرپ در حالت صفحه بزرگ
  :align: center

  کامپوننت نوار پیمایش در بوت‌استرپ در حالت صفحه بزرگ

.. figure:: /images/bootstrap/bootstrap-navbar-sm.jpg
  :alt: کامپوننت نوار پیمایش در بوت‌استرپ در حالت صفحه کوچک
  :align: center

  کامپوننت نوار پیمایش در بوت‌استرپ در حالت صفحه کوچک

.. code-block:: html

  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">لوگو</a>
      <button class="navbar-toggler" type="button"
              data-bs-toggle="collapse"
              data-bs-target="#mainNavbar">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="mainNavbar">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">خانه</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">درباره ما</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">تماس با ما</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>


۴. پیام‌ها / هشدارها (Alerts)
---------------------------------

Alert‌ها پیام‌های رنگی هستند که برای نمایش اطلاع‌رسانی، خطا، موفقیت و …
استفاده می‌شوند.

**مثال:**

.. figure:: /images/bootstrap/bootstrap-alerts.jpg
  :alt: کامپوننت Alert در بوت‌استرپ
  :align: center

  کامپوننت Alert در بوت‌استرپ

.. code-block:: html

  <div class="alert alert-success" role="alert">
    عملیات با موفقیت انجام شد!
  </div>

  <div class="alert alert-danger" role="alert">
    خطا! مشکلی پیش آمده است.
  </div>

  <div class="alert alert-info" role="alert">
    این یک پیام اطلاع‌رسانی است.
  </div>


۵. مودال‌ها (Modals)
--------------------

مودال‌ها پنجره‌های کوچکی هستند که روی صفحه باز می‌شوند و معمولاً برای
فرم ورود، نمایش جزئیات، تأیید حذف و … استفاده می‌شوند.

**کاربرد مودال:**

- نمایش یک پیام مهم بدون رفتن به صفحه‌ی دیگر
- گرفتن ورودی از کاربر (مثل نام، ایمیل و …) در یک پنجره کوچک

**مثال:**

.. figure:: /images/bootstrap/bootstrap-modal.jpg
  :alt: کامپوننت مودال در بوت‌استرپ
  :align: center

  کامپوننت مودال در بوت‌استرپ

.. admonition:: بیشتر بدانید
  :class: tip

  کد مودال بالا برای آشنایی شما در زیر قرار گرفته است:

  .. code-block:: html

    <!-- دکمه باز کردن مودال -->
    <button type="button" class="btn btn-primary"
            data-bs-toggle="modal" data-bs-target="#myModal">
      باز کردن مودال
    </button>

    <!-- خود مودال -->
    <div class="modal fade" id="myModal" tabindex="-1"
          aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="myModalLabel">عنوان مودال</h5>
          </div>
          <div class="modal-body">
            این متن داخل مودال است.
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary"
                    data-bs-dismiss="modal">بستن</button>
            <button type="button" class="btn btn-primary">
              ذخیره تغییرات
            </button>
          </div>
        </div>
      </div>
    </div>

سایر کامپوننت‌ها
-------------------------

کامپوننت‌های بسیاری در بوت‌استرپ وجود دارد
که برخی از آن‌ها را به اختصار توضیح دادیم.
برخی دیگر از کامپوننت‌ها نیز کاربرد زیادی در بوت‌استرپ دارند
که فقط به آن‌ها اشاره خواهیم کرد و در صورت تمایل خودتان
می توانید در
`سایت رسمی بوت‌استرپ <https://getbootstrap.com/>`_ 
یا در سایر سایت‌های آموزشی به یادگیری
کامل آن‌ها بپردازید.

برخی از این کامپوننت‌ها عبارتند از:

- اسلایدر تصاویر (Carousel)
- کامپوننت‌های مربوط به فرم‌ها (forms) مانند منوی کشویی (dropdown) و ...
- زبانه‌ها (Tabs)
- دکمه‌های صفحه‌بندی (Pagination)
- نوار پیشرفت (Progress Bar)
- گردونه بارگزاری یا لود شدن (Spinner)
- و ....
