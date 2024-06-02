# Unnotech Backend Engineer 徵才小專案

[//]: # (1. 抓取 http://tw-nba.udn.com/nba/index 中的焦點新聞。)

[//]: # (2. 使用 [Django]&#40;https://www.djangoproject.com/&#41; 設計恰當的 Model，並將所抓取新聞存儲至 DB。)

[//]: # (3. 使用 [Django REST Framework]&#40;http://www.django-rest-framework.org/&#41; 配合 AJAX 實現以下頁面：)

[//]: # (	 * 焦點新聞列表)

[//]: # (	 * 新聞詳情頁面)

[//]: # (4. 以 Pull-Request 的方式將代碼提交。)

[//]: # (	)
[//]: # (## 進階要求)

[//]: # (1. 實現爬蟲自動定時抓取。)

[//]: # (2. 使用 Websocket 服務，抓取到新的新聞時立即通知前端頁面。)

[//]: # (3. 將本 demo 部署到伺服器並可正確運行。)

[//]: # (4. 所實現新聞列表 API 可承受 100 QPS 的壓力測試。)

## How to use

1. 讀取新聞列表頁面: http://52.194.224.176/api/news-page/
   - 每15分鐘Celery work執行一次爬蟲，若有新資料會去更新cache
   - 若沒有新資料回傳status_code=400
   - 若cache內無資料會從db撈取，並存進cache
2. 讀取新聞詳情頁面: http://52.194.224.176/api/news-page/1
   - id根據新聞列表api那回傳的pid決定
3. 若有新資料存進資料庫，Notifications會顯示`You got a new news!!` 
4. 服務預計2024-06-07禮拜五terminate EC2 instance，可再隨時開啟，但ip會變

## app說明

1. backend使用Django，負責api views, models and db communication
2. cache使用redis，負責儲存新聞列表以及Celery的broker
3. Celery提供爬蟲的worker以及trigger爬蟲的 functions
4. nginx提供反向代理
5. 服務部署在AWS，直接git clone並用docker-compose.yaml啟動服務
6. Backend, celery及nginx有提供image在dockerhub: https://hub.docker.com/r/hunghsianghuang/nice_to_meet_you (非最新版本)
