document.addEventListener('DOMContentLoaded', function() {
    const incrementButtons = document.querySelectorAll('.control-btn.increment');
    const decrementButtons = document.querySelectorAll('.control-btn.decrement');
    const removeButtons = document.querySelectorAll('.remove-btn');

    incrementButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.getAttribute('data-product-id');
            changeQuantity(productId, 1);
        });
    });

    decrementButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.getAttribute('data-product-id');
            changeQuantity(productId, -1);
        });
    });

    removeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.getAttribute('data-product.id');
            removeItem(productId);
        });
    });
});

function changeQuantity(productId, change) {
    var input = document.querySelector(`input[data-product-id="${productId}"]`);
    var currentQuantity = parseInt(input.value);
    var newQuantity = Math.max(1, currentQuantity + change);

    if (newQuantity !== currentQuantity) {
        input.value = newQuantity;
        console.log(`Updated product ${productId} to quantity ${newQuantity}`);
    }
}
function removeItem(productId) {
    console.log(`Removing product ${productId}`);
        }