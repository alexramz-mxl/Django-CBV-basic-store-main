let slideIndex = 0;
        const slides = document.querySelector('.slides');
        const slideCount = document.querySelectorAll('.slide').length;

        function showSlide(index) {
            if (index >= slideCount) slideIndex = 0;
            if (index < 0) slideIndex = slideCount - 1;
            slides.style.transform = `translateX(-${slideIndex * 100}%)`;
        }

        function nextSlide() {
            slideIndex++;
            showSlide(slideIndex);
        }

        function prevSlide() {
            slideIndex--;
            showSlide(slideIndex);
        }

        setInterval(nextSlide, 5000);