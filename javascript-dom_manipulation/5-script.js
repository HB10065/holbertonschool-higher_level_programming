const new_button = document.querySelector('#update_header');
const header = document.querySelector('header');

new_button.addEventListener('click', function() {
    header.textContent = 'New Header!!!';
});