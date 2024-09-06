document.addEventListener('DOMContentLoaded', function () {
    const checkoutButton = document.getElementById('checkout-button');

    if (checkoutButton) {
        checkoutButton.addEventListener('click', function (event) {
            event.preventDefault();
            Swal.fire({
                text: "It´s almost yours!",
                icon: 'success',
                showConfirmButton: false,
                timer: 2500,
                timerProgressBar: true,
            }).then(() => { 
                    window.location.href = checkoutButton.href;
            });
        });
    }
});

