const toggle = document.querySelector('#toggle_header')
const header = document.querySelector('header')

if (header.getAttribute('class') != 'green' && header.getAttribute('class') !='red'){
        header.setAttribute('class', 'green')
}

toggle.addEventListener('click', function() {
    if (header.getAttribute('class') == 'green'){
        header.setAttribute('class', 'red')
    }
    else{
        header.setAttribute('class', 'green')
    }
})