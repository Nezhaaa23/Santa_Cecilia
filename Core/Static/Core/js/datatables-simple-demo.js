$(document).ready(function() {
    $('#aseoTable, #computacionTable, #profesoresTable,#inteescolarTable,extraescolarTable').DataTable({
        paging: true,
        searching: true,
        ordering: true,
        lengthChange: true,
        language: {
            url: "//cdn.datatables.net/plug-ins/1.11.5/i18n/Spanish.json"
        }
    });
});



//window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    //const datatablesSimple = document.getElementById('datatablesSimple');
    //if (datatablesSimple) {
   //     new simpleDatatables.DataTable(datatablesSimple);
    //}
//});
