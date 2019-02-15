$(function () {

    // 轮播
    new Swiper('#topSwiper', {
        loop: true,
        pagination: '.swiper-pagination',
        autoplay: 5000,
    });

    // 必购
    new Swiper('#swiperMenu', {
        slidesPerView: 3,
    });

});