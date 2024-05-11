document.getElementById('getNews').addEventListener('click', getNews);

function getNews() {
    fetch('http://localhost:8000/api/v1/')
        .then(response => response.json())
        .then(data => displayNews(data))
        .catch(error => console.error('Error:', error));
}

function displayNews(news) {
    const newsContainer = document.getElementById('newsContainer');
    newsContainer.innerHTML = '';
    news.forEach(item => {
        const newsItem = document.createElement('div');
        newsItem.textContent = item.title;
        newsContainer.appendChild(newsItem);
    });
}
