if(window.addEventListener) {
    window.addEventListener('load',
        () => {
            window.dispatchEvent(new Event('resize'));
        });
}
