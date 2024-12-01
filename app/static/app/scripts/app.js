$(document).ready(function () {
    $('.carousel').carousel({
        interval: 5000 // Интервал в миллисекундах между автоматическими переключениями слайдов
    });

    // Вызов функции для изменения размеров изображений
    resizeImages();
});

function resizeImages() {
    var carouselImages = document.querySelectorAll('.carousel-image');
    carouselImages.forEach(function (image) {
        image.style.height = '500px'; // Установите высоту изображений
    });
}

function toggleIframe() {
    var iframeContainer = document.getElementById('iframe-container');
    if (iframeContainer.style.display === 'none') {
        iframeContainer.style.display = 'block';
    } else {
        iframeContainer.style.display = 'none';
    }
}
