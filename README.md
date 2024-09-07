# 專案說明 <br>
公車API資源於 https://pto.gov.taipei/News_Content.aspx?n=A1DF07A86105B6BB&s=55E8ADD164E4F579 <br>
google應用程式專用密碼申請於 https://www.shin-her.com.tw/R/07583ed,  如無法使用請先到 google帳戶>安全性>登入google的方式>兩步驟驗證 (這個要有啟用才可以申請) <br>
Table name為 bus_notify_information ; column 為 id(BIGINT), bus_number(character varying), bus_id(character varying), destination_stop(character varying), notify_flag(integer), email(character varying) <br>

設計的樣式為 使用者給定 公車號(672, 214...), 公車id(於台北等公車app查看, e.g. 282-U3, FAA-161), 目的地站(博仁醫院, 長壽公園...), email(被通知的使用者 email) <br>

搭配簡單的post API與本Script用同一張Table進行比較完善 <br>
