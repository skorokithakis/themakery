document.querySelectorAll("[data-subscription-form]").forEach((form) => {
    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const submitButton = form.querySelector("button[type=submit]");
        const status = form.querySelector("[data-subscription-status]");

        submitButton.disabled = true;
        submitButton.textContent = "Subscribing…";
        status.textContent = "";
        status.dataset.state = "";

        try {
            const response = await fetch(form.action, {
                method: form.method,
                body: new FormData(form),
            });

            if (!response.ok) {
                throw new Error("Subscription failed");
            }

            form.reset();
            status.dataset.state = "success";
            status.textContent = "Successfully subscribed!";
        } catch (error) {
            status.dataset.state = "error";
            status.textContent = "Something went wrong. Please try again later.";
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = "Subscribe";
        }
    });
});
