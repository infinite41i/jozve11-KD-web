چیدمان عناصر در صفحه به کمک CSS
========================================

در طراحی صفحات وب، برای مرتب‌سازی و کنار هم قرار دادن عناصر،
دو روش متداول وجود دارد: **Float** و **Flexbox**
که هرکدام مزایا و کاربردهای خاص خود را دارند.

چیدمان با Float
-----------------
در گذشته برای ساخت چیدمان‌های چندستونه از ویژگی `float`
استفاده می‌شد.  
این ویژگی به عناصر اجازه می‌دهد در جهت چپ یا راست حرکت کنند و سایر عناصر در کنار آن‌ها قرار بگیرند.

.. admonition:: مثال

    .. code-block:: html
    
        <img src="image.jpg" style="float:left;">
        <p>این متن در سمت راست تصویر قرار می‌گیرد.</p>

    .. در این مثال، تصویر به سمت چپ صفحه حرکت می‌کند و متن در سمت راست آن قرار می‌گیرد.


    .. .. raw:: html

    ..     <img src="../../_images/sample-img.jpg" alt="مثال Float"  style="float:left; width:150px; margin-right:10px;">
    ..     <p>یک پاراگراف متن ساختگی یک پاراگراف متن ساختگی یک پاراگراف متن ساختگی یک پاراگراف متن ساختگی یک پاراگراف متن ساختگی یک پاراگراف متن ساختگی یک پاراگراف متن ساختگی یک پاراگراف متن ساختگی </p>


چیدمان با Flexbox
--------------------

Flexbox یا **Flexible Box Layout** یکی از سیستم‌های قدرتمند چیدمان در CSS است که هدف آن تنظیم، توزیع و تراز عناصر در یک جهت (افقی یا عمودی) به شکل انعطاف‌پذیر است. این مدل چیدمان در طراحی‌های مدرن وب به‌صورت گسترده استفاده می‌شود؛ زیرا نسبت به روش‌های قدیمی مانند **float** کنترل بسیار بیشتری روی ساختار صفحه فراهم می‌کند.

ساختار کلی Flexbox
^^^^^^^^^^^^^^^^^^^^^^^^

Flexbox از دو بخش تشکیل می‌شود:

1. **Flex Container (جعبه مادر):** عنصری که خاصیت `display: flex;` دارد و شامل تمام آیتم‌های آن قابل انعطاف است.  
2. **Flex Items (آیتم‌های فرزند):** عناصری که داخل container قرار دارند و رفتارشان با ویژگی‌های Flexbox کنترل می‌شود.

.. image:: /images/flexbox/01-container.svg

.. image:: /images/flexbox/02-items.svg

.. admonition:: مثال

    .. code-block:: html

        <div style="display:flex; justify-content:space-around; align-items:center;">
            <div>آیتم ۱</div>
            <div>آیتم ۲</div>
            <div>آیتم ۳</div>
        </div>

    خروجی:

    .. raw:: html

        <div style="display:flex; justify-content:space-around; align-items:center;">
            <div style="background-color: #994400; color: #ffffff; padding: 15px;">آیتم ۱</div>
            <div style="background-color: #994400; color: #ffffff; padding: 15px;">آیتم ۲</div>
            <div style="background-color: #994400; color: #ffffff; padding: 15px;">آیتم ۳</div>
        </div>

ویژگی‌های مهم Flexbox
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **display: flex**
    فعال‌سازی حالت Flexbox

    **دقت کنید که این ویژگی را به والد عناصری می‌دهیم که می‌خواهیم چیدمان شوند.**

* **flex-direction**
    جهت چیدمان عناصر را مشخص می‌کند:

    * `row`: افقی از چپ به راست  
    * `row-reverse`: افقی از راست به چپ  
    * `column`: عمودی از بالا به پایین  
    * `column-reverse`: عمودی از پایین به بالا  

    .. image:: /images/flexbox/flex-direction.svg
    

* **justify-content**
    کنترل چیدمان افقی (محور اصلی):

    * `flex-start`، `center`، `flex-end`، `space-between`، `space-around`

    .. image:: /images/flexbox/justify-content.svg
    

* **align-items**
    تراز عناصر در محور عمودی (محور متقاطع):

    * `flex-start`، `center`، `flex-end`، `stretch`, `baseline`

    .. image:: /images/flexbox/align-items.svg

* **flex-wrap**
    مشخص می‌کند آیا آیتم‌ها در صورت کمبود فضا به خط بعدی بروند یا نه:

    * `nowrap` (پیش‌فرض): همه عناصر در یک خط  
    * `wrap`: عناصر به خطوط بعدی منتقل می‌شوند  

    .. image:: /images/flexbox/flex-wrap.svg
    

* **align-content**
    وقتی چند خط وجود دارد، فاصله بین آن‌ها را تنظیم می‌کند.

    * `flex-start`، `center`، `flex-end`، `space-between`، `space-around`، `stretch`

    .. image:: /images/flexbox/align-content.svg
    

* **gap**
    فاصله بین آیتم‌ها را به‌سادگی تنظیم می‌کند.

    .. image:: /images/flexbox/gap-1.svg


.. admonition:: منبع

    منبع تصاویر فوق:
    https://css-tricks.com/snippets/css/a-guide-to-flexbox/

    
