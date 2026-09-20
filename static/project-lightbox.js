const lightbox = document.querySelector(".project-lightbox");
const lightboxImage = lightbox.querySelector(".project-lightbox-image");
const closeButton = lightbox.querySelector(".project-lightbox-close");
const previousButton = lightbox.querySelector(".project-lightbox-previous");
const nextButton = lightbox.querySelector(".project-lightbox-next");
const lightboxStage = lightbox.querySelector(".project-lightbox-stage");
const body = document.body;

let group = [];
let currentIndex = 0;
let triggeringLink;
let scrollPosition;
let bodyStyles;
let touchStartX;
let touchStartY;

function lockBackgroundScroll() {
    scrollPosition = { left: window.scrollX, top: window.scrollY };
    bodyStyles = {
        left: body.style.left,
        overflow: body.style.overflow,
        position: body.style.position,
        right: body.style.right,
        top: body.style.top,
        width: body.style.width,
    };

    Object.assign(body.style, {
        left: "0",
        overflow: "hidden",
        position: "fixed",
        right: "0",
        top: `-${scrollPosition.top}px`,
        width: "100%",
    });
}

function restoreBackgroundScroll() {
    Object.assign(body.style, bodyStyles);
    window.scrollTo(scrollPosition.left, scrollPosition.top);
}

function closeLightbox() {
    lightbox.close();
}

function showImage(index) {
    currentIndex = (index + group.length) % group.length;
    lightboxImage.src = group[currentIndex].href;
}

function openLightbox(link) {
    group = Array.from(
        link.closest("[data-lightbox-group]").querySelectorAll(".project-image-link")
    );

    const hasMultiple = group.length > 1;
    previousButton.hidden = !hasMultiple;
    nextButton.hidden = !hasMultiple;

    triggeringLink = link;
    lockBackgroundScroll();
    lightbox.showModal();
    closeButton.focus();
    showImage(group.indexOf(link));
}

document.querySelectorAll(".project-image-link").forEach((link) => {
    link.addEventListener("click", (event) => {
        if (
            event.button !== 0 ||
            event.metaKey ||
            event.ctrlKey ||
            event.shiftKey ||
            event.altKey
        ) {
            return;
        }

        event.preventDefault();
        openLightbox(link);
    });
});

closeButton.addEventListener("click", closeLightbox);

previousButton.addEventListener("click", () => {
    showImage(currentIndex - 1);
});

nextButton.addEventListener("click", () => {
    showImage(currentIndex + 1);
});

lightbox.addEventListener("click", (event) => {
    if (!event.target.closest("button") && event.target !== lightboxImage) {
        closeLightbox();
    }
});

lightbox.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft") {
        showImage(currentIndex - 1);
    } else if (event.key === "ArrowRight") {
        showImage(currentIndex + 1);
    }
});

lightboxStage.addEventListener(
    "touchstart",
    (event) => {
        if (event.touches.length !== 1) {
            touchStartX = undefined;
            return;
        }

        touchStartX = event.touches[0].clientX;
        touchStartY = event.touches[0].clientY;
    },
    { passive: true }
);

lightboxStage.addEventListener("touchend", (event) => {
    if (touchStartX === undefined || event.changedTouches.length !== 1) {
        return;
    }

    const deltaX = event.changedTouches[0].clientX - touchStartX;
    const deltaY = event.changedTouches[0].clientY - touchStartY;
    touchStartX = undefined;

    if (Math.abs(deltaX) < 50 || Math.abs(deltaX) <= Math.abs(deltaY)) {
        return;
    }

    if (deltaX < 0) {
        showImage(currentIndex + 1);
    } else {
        showImage(currentIndex - 1);
    }
});

lightbox.addEventListener("close", () => {
    restoreBackgroundScroll();
    lightboxImage.removeAttribute("src");
    triggeringLink.focus();
});
