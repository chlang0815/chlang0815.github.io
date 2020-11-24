

var $table = $('#table')
$('#dl-button').click(function () {
    $.ajax({
        type: "POST",
        contentType: "application/json;charset=utf-8",
        url: "/downloads/",
        data: JSON.stringify($table.bootstrapTable('getSelections')),
        dataType: "json"
    });
});

