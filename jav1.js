// Exemplo básico de gerenciamento do carrinho
const cart = [];

function addToCart(product) {
    cart.push(product);
    updateCart();
}

function updateCart() {
    const cartDiv = document.getElementById('cart');
    cartDiv.innerHTML = '';
    cart.forEach(item => {
        cartDiv.innerHTML += `<p>${item.name} - R$${item.price}</p>`;
    });
    // Adicione cálculo do total aqui
}

function checkout() {
    const message = cart.map(item => `${item.name} - R$${item.price}`).join('\n');
    const total = cart.reduce((sum, item) => sum + item.price, 0);
    const whatsappMessage = `Pedido:\n${message}\nTotal: R$${total}\nEntre em contato para mais detalhes.`;
    const encodedMessage = encodeURIComponent(whatsappMessage);
    const phoneNumber = '5551997165784'; // Substitua pelo número do WhatsApp
    window.location.href = `https://wa.me/${phoneNumber}?text=${encodedMessage}`;
}
