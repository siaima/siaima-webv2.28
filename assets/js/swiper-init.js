document.addEventListener('DOMContentLoaded', function () {
  if (typeof Swiper === 'undefined') return;

  // Logo wall — continuous autoplay
  if (document.querySelector('.logo-wall-swiper')) {
    new Swiper('.logo-wall-swiper', {
      loop: true,
      speed: 4000,
      autoplay: { delay: 0, disableOnInteraction: false, pauseOnMouseEnter: false },
      slidesPerView: 'auto',
      spaceBetween: 48,
      allowTouchMove: false,
      freeMode: true
    });
  }

  // Case studies carousel
  if (document.querySelector('.cases-swiper')) {
    new Swiper('.cases-swiper', {
      slidesPerView: 1.1,
      spaceBetween: 16,
      grabCursor: true,
      breakpoints: {
        768: { slidesPerView: 2.1, spaceBetween: 20 },
        1024: { slidesPerView: 3, spaceBetween: 24 }
      },
      pagination: { el: '.cases-swiper .swiper-pagination', clickable: true },
      navigation: {
        nextEl: '.cases-swiper .swiper-button-next',
        prevEl: '.cases-swiper .swiper-button-prev'
      }
    });
  }
});
