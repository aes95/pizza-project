window.addEventListener('load', function() {

    const checkout = document.querySelector('.checkout-btn');

    checkout.addEventListener('click', function() {
        return fetch('/checkout', {
                method: 'POST',
                credentials: "same-origin",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                    "Accept": "application/json",
                    'Content-Type': 'application/json'
                },
                redirect: "follow", // manual, *follow, error
                referrer: "no-referrer", // no-referrer, *client

            })
            .then((response) => response.json())
            .then((msg) => Swal.fire(
                'Order Placed Successfuly',
                `Order #${msg.id} will be out shortly`,
                'success'
            )).then(removeCart)
    })

})
