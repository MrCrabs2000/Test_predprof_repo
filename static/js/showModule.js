const itemsInItemsList = document.querySelectorAll('.itemsList__item');

itemsInItemsList.forEach(item => {
    let itemButton = item.querySelector('button');

    itemButton.addEventListener('click', function() {
        const content = this.innerHTML;

        const url = new URL(window.location.href);
        url.searchParams.set('module', content);
    
        window.location.href = url.href;

    });
});