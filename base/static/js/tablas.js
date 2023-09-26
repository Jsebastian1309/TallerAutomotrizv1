const table = $('#example').DataTable({
    
    scrollY: '200px'
}); 
document.querySelectorAll('a.toggle-vis').forEach((el) => {
    el.addEventListener('click', function (e) {
        e.preventDefault();
 
        let columnIdx = e.target.getAttribute('data-column');
        let column = table.column(columnIdx);

        column.visible(!column.visible());
    });
});