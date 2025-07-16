const additem_elem = document.querySelector('#add_item');
const my_list = document.querySelector('.my_list');

additem_elem.addEventListener('click', function() {
    const list = document.createElement('li');
    const text = document.createTextNode('Item');
    list.appendChild(text);
    my_list.appendChild(list);
});