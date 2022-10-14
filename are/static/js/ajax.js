$(document).ready(function() {
    $("#submit-comment").click(function(event) {
        debugger
        event.preventDefault();
        var id = `{{data}}`
        console.log(data)
        var url = "/application/";
        var dataPosted = $("#mainSubmit").serialize();
        $.ajax({
            type: 'POST',
            url: url,
            data: dataPosted,
            success: function(data) {
                debugger
                console.log(data)
                $('#comments-' + data.post).prepend(`<div class="col-lg-6 offset-lg-3">
                                                        <div class="card p-2">
                                                            <div class="row">
                                                                <div class="col-12">
                                                                    <strong>${data.user}</strong>
                                                                </div>
                                                                <div class="col-12">
                                                                    <p class="m-1 mt-3">${data.content}</p>
                                                                    <p class="text-right text-muted"><small>${data.created}</small></p>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>`)
            $(`#comment-count-${data.post}`).html(data.count)
            },
            error: function(rs, e) {
                alert("!error...")
            },
        });
    });