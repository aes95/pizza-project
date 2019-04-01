window.onload = function() {

    // update price as selections are made
    document.querySelectorAll('input').forEach(function(input) {
        input.addEventListener('change', getPizzaPrice)
    })
    document.querySelectorAll('.food').forEach(function(row) {
        row.addEventListener('click', itemInfo)
    })

}

function itemInfo() {
    const index = this.dataset.id
    fetch('/details', {
            method: 'POST',
            body: JSON.stringify({
                'id': index.toString()
            }),
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
        .then(function(data) { Swal.fire({
                    title: `${data.name}`,
                    type: 'info',
                    html: `Order a ${data.size} ${data.name} for ${data.price}`,
                    showCloseButton: true,
                    showCancelButton: true,
                    focusConfirm: false,
                    confirmButtonText: 'Add to Cart!',
                    cancelButtonText: 'Cancel',
                }).then((isConfirm) => {
                  if (isConfirm){
                  fetch('/cart-item', {
                        method: 'POST',
                        body: JSON.stringify(data),
                        credentials: "same-origin",
                        headers: {
                            "X-CSRFToken": getCookie("csrftoken"),
                            "Accept": "application/json",
                            'Content-Type': 'application/json'
                        },
                        redirect: "follow", // manual, *follow, error
                        referrer: "no-referrer", // no-referrer, *client
                    }).then((response) => {
                      if (response.ok){
                      addItemToCart(data)};
                    })
                      .catch((error) => console.log(error))
                }})
                })
    }

function getPizzaPrice() {
    const order_form = document.getElementById("pizza-order");
    const modal_price = document.querySelector('.modal-price');
    let form = new FormData(order_form)
    fetch('/get-pizza-price', {
            method: 'POST',
            body: form
        })
        .then(response => response.json())
        .then(response => modal_price.innerHTML = response['price'])
}

function addToCart() {
    const order_form = document.getElementById("pizza-order");
    let form = new FormData(order_form)
    order_form.reset()
    $('#pizzaModal').modal('hide')
    fetch('/cart', {
            method: 'POST',
            body: form
        })
        .then(response => response.json())
        .then(function(response) {
            const badge = document.querySelector('.badge')
            badge.innerHTML = response.items.length
        }).then(removeCart)
        .then(buildCart)
}

function addItemToCart(){
  removeCart();
  buildCart();
}
