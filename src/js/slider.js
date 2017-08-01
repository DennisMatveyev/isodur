import {LEFT_ARROW_PARTNER, RIGHT_ARROW_PRODUCT, RIGTH_ARROW_PARTNER, LEFT_ARROW_PRODUCT} from './carousel_images';

$(document).ready(function () {

    /**
     * Added Owl carousel hook
     */
    $('.owl-carousel').owlCarousel({
        loop: true,
        margin: 10,
        items: 1,
        pullDrag: false,
        touchDrag: false,
        mouseDrag: false,
        center: true,
        dots: true,
        dotsData: true,
        autoplay: true,
        autoplayTimeout: 4000
    });

    /**
     * Added Owl carousel hook
     */
    $('.partner-carousel').owlCarousel({
        nav: true,
        loop: true,
        smartSpeed: 400,
        lazyContent: true,
        autoplayTimeout: 4000,
        lazyLoad: true,
        autoplay: true,
        navText: [`<img class="partner_nav" src=${LEFT_ARROW_PARTNER}>`, `<img class="partner_nav" src=${RIGTH_ARROW_PARTNER}>`],
        items: 3,
    });

    /**
     * Added Owl carousel hook
     */
    $('.product-carousel').owlCarousel({
        nav: true,
        smartSpeed: 400,
        dots: true,
        loop: true,
        lazyContent: true,
        autoplayTimeout: 4000,
        lazyLoad: true,
        navText: [`<img width="20px" src=${LEFT_ARROW_PRODUCT}>`, `<img width="20px" class="partner_nav" src=${RIGHT_ARROW_PRODUCT}>`],
        items: 3,
    });
    /**
     * Added Owl carousel hook
     */
    $('.video-carousel').owlCarousel({
        smartSpeed: 400,
        dots: true,
        loop: true,
        dotsData: true,
        autoplay: true,
        center: true,
        pullDrag: false,
        touchDrag: false,
        mouseDrag: false,
        autoplayTimeout: 4000,
        lazyContent: true,
        navText: [`<img class="partner_nav" src=${LEFT_ARROW_PARTNER}>`, `<img class="partner_nav" src=${RIGHT_ARROW_PRODUCT}>`],
        lazyLoad: true,
        items: 1,
    });
});
