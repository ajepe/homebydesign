$(document).ready(function() {

    var html = '';
    $.get('api-tasks-status', function(data) {
        $.each(data, function(index, element) {
            $.each(element, function(name, values) {
                html += `<li class='accordion '><h3>${name}</h3><div><ol>`;
                $.each(values, function(index, value) {
                    html += `<li class="divider"><p><span><b>${value.project}:- </b>\u0020 Open: <span class="badge"> ${value.open_tasks}</span>\u0020 Delay: <span class="badge">${value.delay_tasks}</span> \u0020 <b>Finish Month: <span class="badge">${value.finish_month}</span> \u0020 Finish Week: <span class="badge">${value.finish_week}</span></p></li>`;

                });
                html += `</ol></div></li>`

            });
        });
        console.log(html);

        $(".sub").html(html)
        $(".sub").accordion()
    });


});