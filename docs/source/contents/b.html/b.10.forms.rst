فرم‌ها در HTML
======================

فرم‌ها در HTML
----------------------

فرم‌ها برای گرفتن اطلاعات از کاربر استفاده می‌شوند؛
مثل نام، ایمیل، رمز عبور یا نظر (کامنت).
وقتی در سایتی چیزی وارد می‌کنیم، در واقع داریم از فرم‌ها استفاده می‌کنیم.
یک فرم با تگ `<form>`
ساخته می‌شود و داخل آن می‌توان ورودی‌های مختلف قرار داد.

برای مثال، قطعه‌کد زیر یک فرم ساده برای دریافت نام و ایمیل کاربر است:

.. code-block:: html

    <form>
        <label for="name">نام:</label>
        <input type="text" id="name" name="name"><br><br>

        <label for="email">ایمیل:</label>
        <input type="email" id="email" name="email"><br><br>

        <input type="submit" value="ارسال">
    </form>

.. admonition:: خروجی
    :class: hint

    .. raw:: html

        <form>
            <label for="name">نام:</label>
            <input type="text" id="name" name="name" style="background-color: #ffffff; border: 0.5px solid black;"><br><br>

            <label for="email">ایمیل:</label>
            <input type="email" id="email" name="email" style="background-color: #ffffff; border: 0.5px solid black;"><br><br>

            <button style="background-color: #ffffff; border: 0.5px solid black;">ارسال</button>
        </form>

در این فرم، تگ ``<input>``
برای ساخت فیلدهای ورودی استفاده می‌شود.
نوع فیلد را با ویژگی ``type``
مشخص می‌کنیم؛
مثل ``text``
برای نوشتن متن معمولی یا ``email``
برای ورود آدرس ایمیل.
دکمه‌ی ارسال با نوع ``submit``
باعث می‌شود اطلاعات فرم برای پردازش فرستاده شود.

برچسب‌های ``<label>``
نیز عنوان هر فیلد ورودی را مشخص می‌کنند.

کاربر مقدارها را وارد می‌کند و سپس روی دکمه‌ی ارسال می‌زند. با این روش می‌توان فرم‌های ثبت‌نام، ورود، نظرسنجی یا تماس با ما را طراحی کرد. فرم‌ها یکی از مهم‌ترین بخش‌های HTML هستند چون ارتباط میان کاربر و وب‌سایت را برقرار می‌کنند.

از سایر برچسب‌هایی که در فرم برای ورود اطلاعات کاربرد دارد می‌توان به 
``<textarea>``
برای نوشتن متن بلندتر،
``<select>`` و ``<option>``
برای ساخت منوی کشویی و انتخاب یک گزینه از بین تعدادی گزینه‌ی موجود
و ``<button>``
اشاره کرد که در ادامه به توضیح آن‌ها خواهیم پرداخت.

انواع ورودی‌های اصلی در فرم‌های HTML
--------------------------------------

تگ ``<input>`` با استفاده از ویژگی ``type``، انواع مختلفی از فیلدهای ورودی را در فرم‌های HTML ایجاد می‌کند. در زیر به تفکیک هر نوع، مثال‌های کد و نمایش خروجی مربوطه آورده شده است.

1. نوع ``text``
^^^^^^^^^^^^^^^^^^^^

برای دریافت متن معمولی و کوتاه استفاده می‌شود.

.. code-block:: html

    <input type="text" id="fullname" name="fullname" placeholder="نام و نام خانوادگی">

.. raw:: html

   <div>
       <label for="fullname">نام و نام خانوادگی:</label>
       <input type="text" id="fullname" name="fullname" style="width: 150px; background-color: #ffffff; border: 0.5px solid black; padding: 5px; margin-bottom: 10px;">
   </div>

1. نوع ``password``
^^^^^^^^^^^^^^^^^^^^^^

برای ورودی‌هایی که باید مخفی بمانند (مانند رمز عبور) استفاده می‌شود.

.. code-block:: html

    <input type="password">

.. raw:: html

   <div>
       <label for="password">رمز عبور:</label>
       <input type="password" id="password" name="password" maxlength="10" value="******" style="width: 150px;background-color: #ffffff; border: 0.5px solid black; padding: 5px; margin-bottom: 10px;">
   </div>

1. نوع ``email``
^^^^^^^^^^^^^^^^^^^^

برای دریافت آدرس ایمیل که مرورگر می‌تواند ساختار آن را اعتبارسنجی کند.

.. code-block:: html

    <input type="email">

.. raw:: html

   <div>
       <label for="user_email">ایمیل:</label>
       <input type="email" id="user_email" name="user_email" required value="user@example.com" style="width: 200px;background-color: #ffffff; border: 0.5px solid black; padding: 5px; margin-bottom: 10px;">
   </div>

1. نوع ``number``

برای ورود اعداد صحیح یا اعشاری، به همراه کنترل‌های بالا/پایین.

.. code-block:: html

    <input type="number">

.. raw:: html

   <div>
       <label for="quantity">تعداد (۱ تا ۱۰):</label>
       <input type="number" id="quantity" name="quantity" value="3" style="width: 150px;background-color: #ffffff; border: 0.5px solid black; padding: 5px; margin-bottom: 10px;">
   </div>

1. نوع ``date``
^^^^^^^^^^^^^^^^^^

نمایش یک انتخابگر تاریخ (تقویم).

.. code-block:: html

    <input type="date" id="dob" name="dob" value="2025-11-06">

.. raw:: html

   <div>
       <label for="dob">تاریخ تولد:</label>
       <input type="date" id="dob" name="dob" value="2025-11-06" style="width: 150px;">
   </div>

6. نوع ``checkbox``
^^^^^^^^^^^^^^^^^^^^^^^^^

اجازه می‌دهد کاربر چندین گزینه را همزمان انتخاب کند. تمام گزینه‌های مرتبط باید یک ``name`` مشترک داشته باشند.

.. code-block:: html

    <input type="checkbox" id="opt1" name="options" value="A">
    <label for="opt1">گزینه الف</label>
    <input type="checkbox" id="opt2" name="options" value="B" checked>
    <label for="opt2">گزینه ب</label>

.. raw:: html

   <div>
       <label>انتخاب‌ها:</label><br>
       <input type="checkbox" id="opt1" name="options" value="A">
       <label for="opt1">گزینه الف</label>
       <input type="checkbox" id="opt2" name="options" value="B" checked>
       <label for="opt2">گزینه ب</label>
   </div>

7. نوع ``radio``
^^^^^^^^^^^^^^^^^^^^^^^

اجازه می‌دهد کاربر دقیقاً یکی از گزینه‌ها را از یک گروه انتخاب کند. تمام رادیو باتن‌های یک گروه باید دارای ``name`` یکسان باشند.

.. code-block:: html

    <input type="radio" id="male" name="gender" value="male">
    <label for="male">مرد</label>
    <input type="radio" id="female" name="gender" value="female" checked>
    <label for="female">زن</label>

.. raw:: html

   <div>
       <label>جنسیت:</label><br>
       <input type="radio" id="male" name="gender" value="male">
       <label for="male">مرد</label>
       <input type="radio" id="female" name="gender" value="female" checked>
       <label for="female">زن</label>
   </div>

8. نوع ``submit``
^^^^^^^^^^^^^^^^^^

دکمه‌ای که با کلیک شدن، داده‌های فرم را به سرور ارسال می‌کند.

.. code-block:: html

    <input type="submit" value="ثبت و ادامه">

.. raw:: html

   <div>
       <input type="submit" value="ثبت و ادامه" style="width: 150px;background-color: #ffffff; border: 0.5px solid black; padding: 5px; margin-bottom: 10px;">
   </div>

ویژگی‌ها (Attributes) در فرم‌ها
----------------------------------------------
فرم‌ها و ورودی‌های داخل آن می‌توانند ویژگی‌های مختلفی داشته باشند که رفتار و ظاهر آن‌ها را کنترل می‌کند. در زیر به برخی از مهم‌ترین ویژگی‌ها اشاره می‌کنیم:

مهم‌ترین ویژگی‌های تگ ``<form>``
عبارتند از:

* ``action``: مشخص می‌کند که داده‌های فرم به کدام آدرس در سرور (URL) ارسال شود.
* ``method``: تعیین می‌کند که داده‌ها با کدام روش HTTP ارسال شوند (مثل GET یا POST).

.. note::

    تفاوت متد GET و POST
    در نحوه ارسال داده‌هاست.
    در متد GET اطلاعات در نوار آدرس گنجانده می‌شوند. این روش امنیت بالایی ندارد.
    
    اما برای داده‌های حساس مثل رمز عبور از متد POST
    استفاده می‌شود که اطلاعات را در بدنه درخواست و خارج از URL
    ارسال می‌کند و امنیت بیشتری دارد.

مهم‌ترین ویژگی‌های تگ ``<input>``
عبارتند از:

* ``name``: نام فیلد ورودی که هنگام ارسال فرم استفاده می‌شود.
* ``value``: مقدار پیش‌فرض یا مقدار فعلی فیلد ورودی.
* ``placeholder``: متنی که در فیلد ورودی نمایش داده می‌شود تا کاربر بداند چه چیزی باید وارد کند.
* ``required``: اگر این ویژگی وجود داشته باشد، کاربر باید حتماً این فیلد را پر کند تا فرم ارسال شود.
* ``maxlength``: حداکثر تعداد کاراکتری که کاربر می‌تواند وارد کند.
* ``checked``: برای فیلدهای چک‌باکس و رادیو باتن، مشخص می‌کند که آیا به صورت پیش‌فرض انتخاب شده‌اند یا خیر.
