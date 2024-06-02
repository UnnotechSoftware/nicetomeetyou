document.addEventListener('DOMContentLoaded', function () {
    const newsId = document.getElementById('news-detail').getAttribute('data-id');
    fetch(`/api/news/${newsId}`)
        .then(response => response.json())
        .then(news => {
            const container = document.getElementById('news-detail');
            container.innerHTML = `
                <h2>${news.headline}</h2>
                <p>${news.context}</p>
                <p>${news.author}</p>
                <p>${news.publisher}</p>
                <p><small>${news.date_published}</small></p>
            `;
        })
        .catch(error => console.error('Error fetching news:', error));

    document.getElementById('back-button').addEventListener('click', function () {
        window.location.href = '/api/news-page/';
    });
});
