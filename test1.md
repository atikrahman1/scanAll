# FFUF Report

  Command line : `ffuf -u https://faculty.daffodilvarsity.edu.bd/FUZZ -w E:\PENTEST-POCS\master_wordlist.txt -ac -mc 200,403 -o test.md -of md`
  Time: 2023-02-16T15:18:04&#43;06:00

  | FUZZ | URL | Redirectlocation | Position | Status Code | Content Length | Content Words | Content Lines | Content Type | Duration | ResultFile | ScraperData
  | :- | :-- | :--------------- | :---- | :------- | :---------- | :------------- | :------------ | :--------- | :----------- | :------------ |
  | 6ed2b1d | .admin | https://faculty.daffodilvarsity.edu.bd/.admin |  | 29 | 200 | 0 | 1 | 1 | text/html; charset=UTF-8 | 52.9988ms |  |  |
  | 6ed2b261 | .html | https://faculty.daffodilvarsity.edu.bd/.html |  | 609 | 200 | 14527 | 4156 | 266 | text/html; charset=UTF-8 | 60.6323ms |  |  |
  | 6ed2b505 | .users | https://faculty.daffodilvarsity.edu.bd/.users |  | 1285 | 200 | 0 | 1 | 1 | text/html; charset=UTF-8 | 61.785ms |  |  |
  | 6ed2b528 | .well-known/ | https://faculty.daffodilvarsity.edu.bd/.well-known/ |  | 1320 | 200 | 978 | 85 | 17 | text/html;charset=ISO-8859-1 | 63.6367ms |  |  |
  | 6ed2b857 | Admin | https://faculty.daffodilvarsity.edu.bd/Admin |  | 2135 | 200 | 0 | 1 | 1 | text/html; charset=UTF-8 | 60.0102ms |  |  |
  | 6ed2b858 | admin | https://faculty.daffodilvarsity.edu.bd/admin |  | 2136 | 200 | 0 | 1 | 1 | text/html; charset=UTF-8 | 60.0085ms |  |  |
  | 6ed2b887 | admin. | https://faculty.daffodilvarsity.edu.bd/admin. |  | 2183 | 200 | 0 | 1 | 1 | text/html; charset=UTF-8 | 57.8454ms |  |  |
  | 6ed2b89b | admin.html | https://faculty.daffodilvarsity.edu.bd/admin.html |  | 2203 | 200 | 0 | 1 | 1 | text/html; charset=UTF-8 | 57.0498ms |  |  |
  | 6ed2b89c | Admin.html | https://faculty.daffodilvarsity.edu.bd/Admin.html |  | 2204 | 200 | 0 | 1 | 1 | text/html; charset=UTF-8 | 57.5553ms |  |  |
  | 6ed2b8b3 | admin/ | https://faculty.daffodilvarsity.edu.bd/admin/ |  | 2227 | 200 | 0 | 1 | 1 | text/html; charset=UTF-8 | 56.7534ms |  |  |
  | 6ed2b8b6 | admin/?/login | https://faculty.daffodilvarsity.edu.bd/admin/?/login |  | 2230 | 200 | 0 | 1 | 1 | text/html; charset=UTF-8 | 58.525ms |  |  |
  | 6ed2b913 | admin/index | https://faculty.daffodilvarsity.edu.bd/admin/index |  | 2323 | 200 | 0 | 1 | 1 | text/html; charset=UTF-8 | 51.5138ms |  |  |
  | 6ed2b916 | admin/index.html | https://faculty.daffodilvarsity.edu.bd/admin/index.html |  | 2326 | 200 | 0 | 1 | 1 | text/html; charset=UTF-8 | 52.9385ms |  |  |
  | 6ed2b921 | admin/login | https://faculty.daffodilvarsity.edu.bd/admin/login |  | 2337 | 200 | 6512 | 1848 | 112 | text/html; charset=UTF-8 | 64.1565ms |  |  |
  | 6ed2b927 | admin/login.html | https://faculty.daffodilvarsity.edu.bd/admin/login.html |  | 2343 | 200 | 6512 | 1848 | 112 | text/html; charset=UTF-8 | 62.1171ms |  |  |
  | 6ed2b92c | Admin/login/ | https://faculty.daffodilvarsity.edu.bd/Admin/login/ |  | 2348 | 200 | 6512 | 1848 | 112 | text/html; charset=UTF-8 | 206.8191ms |  |  |
  | 6ed2b10cb | contact | https://faculty.daffodilvarsity.edu.bd/contact |  | 4299 | 200 | 0 | 1 | 1 | text/html; charset=UTF-8 | 50.8482ms |  |  |
  | 6ed2b10e4 | controlpanel | https://faculty.daffodilvarsity.edu.bd/controlpanel |  | 4324 | 200 | 34066 | 1364 | 330 | text/html | 121.2076ms |  |  |
  | 6ed2b10ea | controlpanel/ | https://faculty.daffodilvarsity.edu.bd/controlpanel/ |  | 4330 | 200 | 34091 | 1364 | 330 | text/html | 121.1966ms |  |  |
  | 6ed2b110c | cpanel | https://faculty.daffodilvarsity.edu.bd/cpanel |  | 4364 | 200 | 34066 | 1364 | 330 | text/html | 121.7307ms |  |  |
  | 6ed2b110f | cpanel/ | https://faculty.daffodilvarsity.edu.bd/cpanel/ |  | 4367 | 200 | 34091 | 1364 | 330 | text/html | 121.9006ms |  |  |
  | 6ed2b1237 | dist/ | https://faculty.daffodilvarsity.edu.bd/dist/ |  | 4663 | 200 | 1115 | 135 | 18 | text/html;charset=ISO-8859-1 | 51.1231ms |  |  |
  | 6ed2b13b4 | faculty | https://faculty.daffodilvarsity.edu.bd/faculty |  | 5044 | 200 | 0 | 1 | 1 | text/html; charset=UTF-8 | 50.356ms |  |  |
  | 6ed2b15c1 | images/ | https://faculty.daffodilvarsity.edu.bd/images/ |  | 5569 | 200 | 4061 | 393 | 34 | text/html;charset=ISO-8859-1 | 50.8235ms |  |  |
  | 6ed2b1620 | index.php | https://faculty.daffodilvarsity.edu.bd/index.php |  | 5664 | 200 | 14527 | 4156 | 266 | text/html; charset=UTF-8 | 60.5588ms |  |  |
  | 6ed2b1704 | js/ | https://faculty.daffodilvarsity.edu.bd/js/ |  | 5892 | 200 | 1131 | 113 | 18 | text/html;charset=ISO-8859-1 | 50.3227ms |  |  |
  | 6ed2b1745 | kpanel/ | https://faculty.daffodilvarsity.edu.bd/kpanel/ |  | 5957 | 200 | 34091 | 1364 | 330 | text/html | 131.0299ms |  |  |
  | 6ed2b18b4 | mailman/ | https://faculty.daffodilvarsity.edu.bd/mailman/ |  | 6324 | 403 | 318 | 29 | 10 | text/html; charset=iso-8859-1 | 50.3377ms |  |  |
  | 6ed2b18b5 | mailman/listinfo | https://faculty.daffodilvarsity.edu.bd/mailman/listinfo |  | 6325 | 200 | 1657 | 228 | 45 | text/html; charset=us-ascii | 172.8983ms |  |  |
  | 6ed2b1f2d | search | https://faculty.daffodilvarsity.edu.bd/search |  | 7981 | 200 | 0 | 1 | 1 | text/html; charset=UTF-8 | 50.6611ms |  |  |
  | 6ed2b2290 | test/ | https://faculty.daffodilvarsity.edu.bd/test/ |  | 8848 | 200 | 1498 | 143 | 20 | text/html;charset=ISO-8859-1 | 50.4154ms |  |  |
  | 6ed2b22df | tinymce/ | https://faculty.daffodilvarsity.edu.bd/tinymce/ |  | 8927 | 200 | 2017 | 233 | 23 | text/html;charset=ISO-8859-1 | 60.3603ms |  |  |
  | 6ed2b2387 | upload/ | https://faculty.daffodilvarsity.edu.bd/upload/ |  | 9095 | 200 | 961 | 92 | 17 | text/html;charset=ISO-8859-1 | 50.4524ms |  |  |
  | 6ed2b23d0 | users | https://faculty.daffodilvarsity.edu.bd/users |  | 9168 | 200 | 0 | 1 | 1 | text/html; charset=UTF-8 | 50.5064ms |  |  |
  | 6ed2b23de | users/ | https://faculty.daffodilvarsity.edu.bd/users/ |  | 9182 | 200 | 0 | 1 | 1 | text/html; charset=UTF-8 | 50.3906ms |  |  |
  | 6ed2b255d | webmail/ | https://faculty.daffodilvarsity.edu.bd/webmail/ |  | 9565 | 200 | 34096 | 1364 | 330 | text/html | 152.9483ms |  |  |
  | 6ed2b255f | webmail/src/configtest.phpv1.1.0-git&#34; | https://faculty.daffodilvarsity.edu.bd/webmail/src/configtest.phpv1.1.0-git&#34; |  | 9567 | 200 | 34461 | 1364 | 330 | text/html | 163.0188ms |  |  |
  | 6ed2b255e | webmail/src/configtest.php | https://faculty.daffodilvarsity.edu.bd/webmail/src/configtest.php |  | 9566 | 200 | 34308 | 1364 | 330 | text/html | 173.2292ms |  |  |
  