const lightbox = document.querySelector(".project-lightbox");
const lightboxImage = lightbox.querySelector(".project-lightbox-image");
const closeButton = lightbox.querySelector(".project-lightbox-close");
const body = document.body;

let triggeringLink;
let scrollPosition;
let bodyStyles;

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
        triggeringLink = link;
        lightboxImage.src = link.href;
        lockBackgroundScroll();
        lightbox.showModal();
        closeButton.focus();
    });
});

closeButton.addEventListener("click", closeLightbox);

lightbox.addEventListener("click", (event) => {
    if (event.target !== lightboxImage && event.target !== closeButton) {
        closeLightbox();
    }
});

lightbox.addEventListener("keydown", (event) => {
    if (event.key === "Tab") {
        event.preventDefault();
        closeButton.focus();
    }
});

lightbox.addEventListener("close", () => {
    restoreBackgroundScroll();
    lightboxImage.removeAttribute("src");
    triggeringLink.focus();
});
