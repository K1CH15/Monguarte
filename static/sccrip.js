(function($) {
    $(document).ready(function() {
        const open_btn_menu = document.querySelector('.open-btn')
        const close_btn = document.querySelector('.close-btn')
        const nav = document.querySelectorAll('.nav')
        
        open_btn_menu.addEventListener('click', () => {
            nav.forEach(nav_el => nav_el.classList.add('visible'))
        })
        
        close_btn.addEventListener('click', () => {
            nav.forEach(nav_el => nav_el.classList.remove('visible'))
        })
        
    });
})(jQuery);