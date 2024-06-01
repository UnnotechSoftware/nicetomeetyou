document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/news/')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('news-container');
            data.forEach(news => {
                const newsElement = document.createElement('div');
                newsElement.innerHTML = `
                    <h2><a href="/api/news-page/${news.pid}">${news.headline}</a></h2>
                    <p>${news.author}</p>
                    <p><small>${news.date_published}</small></p>
                `;
                container.appendChild(newsElement);
            });
        })
        .catch(error => console.error('Error fetching news:', error));
});
