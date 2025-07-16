const toggle = document.querySelector('#toggle_header')
const header = document.querySelector('header')
const hclasslist = header.classList

if (hclasslist.contains('green') == false && hclasslist.contains('red') == false){
    hclasslist.add('green')
}

toggle.addEventListener('click', function() {
    if (hclasslist.contains('green')){
        hclasslist.remove('green')
        hclasslist.add('red')
    }
    else{
        hclasslist.remove('red')
        hclasslist.add('green')
    }
})