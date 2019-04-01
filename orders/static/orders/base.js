const cart_detail = document.querySelector('.shopping-cart');
const cart_logo = document.querySelector('#cart');

//Add functionality to shopping cart. default does not show detail
window.addEventListener('load',function(){
  buildCart();
  cart_logo.addEventListener('click', function(){
    if (cart_detail.style.display === ''){
      cart_detail.style.display = 'none';
    }else{
      cart_detail.style.display = '';
    }
  })
  cart_detail.style.display='none'
})

function getCart(){
  return fetch('/cart', {
          method: 'GET',
      })
      .then(response => response.json())
}

function buildCart(){
  updateBadge();
  getCart()
  .then(function (response){
        items = response.items
        for (let i = 0; i < items.length; i++){
          addCartItem(items[i], i);
        }
    })
}

function updateBadge() {
  getCart()
  .then(function(response){
  const badge = document.querySelector('.badge')
  badge.innerHTML = response.items.length
  const subtotal = document.querySelector('.cart-subtotal')
  subtotal.innerHTML = `$${formatMoney(response.subtotal)}`
    })
  document.getElementById('clear-cart').addEventListener('click',removeCartItem)
}

function addCartItem(item, index){
  const li = document.createElement('li');
  li.classList.add('clearfix');
  li.dataset.index = index
  const name = document.createElement('span');
  name.classList.add('item-name');
  name.innerHTML = `${item.size} ${item.name}`;
  const price = document.createElement('span');
  price.classList.add('item-price');
  price.innerHTML = `$${formatMoney(item.price)}`;
  const quantity = document.createElement('span');
  quantity.classList.add('item-quantity');
  minus = document.createElement('i')
  minus.classList.add('fas', 'fa-minus-circle')
  minus.dataset.index = index
  quantity.innerHTML = `Quantity: 1  `;
  quantity.appendChild(minus)
  li.appendChild(name);
  li.appendChild(price);
  li.appendChild(quantity);
  minus.addEventListener('click', removeCartItem)
  document.querySelector('.shopping-cart-items').appendChild(li);
}

function removeCartItem(){
  const index = this.dataset.index
  number = index.toString()
  return fetch('/clear-cart', {
          method: 'POST',
          body: JSON.stringify({'num':number}),
          credentials: "same-origin",
          headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": "application/json",
            'Content-Type': 'application/json'
          },
          redirect: "follow", // manual, *follow, error
          referrer: "no-referrer", // no-referrer, *client
      })
      .then(removeCart)
      .then(buildCart)
}

function removeCart(){
  const ul = document.querySelector('.shopping-cart-items')
  while (ul.firstChild){
    ul.removeChild(ul.firstChild)
  }
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function formatMoney(amount, decimalCount = 2, decimal = ".", thousands = ",") {
  try {
    decimalCount = Math.abs(decimalCount);
    decimalCount = isNaN(decimalCount) ? 2 : decimalCount;

    const negativeSign = amount < 0 ? "-" : "";

    let i = parseInt(amount = Math.abs(Number(amount) || 0).toFixed(decimalCount)).toString();
    let j = (i.length > 3) ? i.length % 3 : 0;

    return negativeSign + (j ? i.substr(0, j) + thousands : '') + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + thousands) + (decimalCount ? decimal + Math.abs(amount - i).toFixed(decimalCount).slice(2) : "");
  } catch (e) {
    console.log(e)
  }
};
