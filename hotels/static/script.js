function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

$("document").ready(
    function () {
        $(".star-rating__input").on("click", function () {
            let r = $(this).attr("id").split('_');
            let rating = r[2];
            let tipe_id = r[3];
            let hotel_id = r[0];
            let name_hotel = r[1];
            $.ajax({
                "url":"/hotels/rating-ajax/",
                "data": {"tipe_id": tipe_id,
                    "ratk": rating,
                    "hotel_id": hotel_id,
                    "name_hotel": name_hotel,
                    "csrfmiddlewaretoken": csrftoken},
                "method": "post",
                success: function (data) {
                   console.log(data);
                    $(`.${tipe_id}`).html(`<h5>${data}</h5>`);
                },
                error: function (data) {
                    console.log('hello error', data)
                }
            });
        })
    }   
);

