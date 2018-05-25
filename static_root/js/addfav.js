/**
 * Created by Administrator on 2018/5/26.
 */
//收藏分享
//取消收藏
function add_fav(current_elem, fav_id, fav_type) {
    $.ajax({
        cache: false,
        type: "POST",
        url: "{% url 'organization:add_fav' %}",
        data: {'fav_id': fav_id, 'fav_type': fav_type},
        async: true,
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
        },
        success: function (data) {
            if (data.status == 'fail') {
                if (data.msg == '用户未登录') {
                    window.location.href = "{% url 'login' %}";
                } else {
                    alert(data.msg)
                }

            } else if (data.status == 'success') {
                current_elem.text(data.msg)
            }
        },
    });
}

$('.collectionbtn').on('click', function () {
    var fav_id = $(this).attr('data-favid');
    var fav_type = $(this).attr('data-fav-type');
    add_fav($(this), fav_id, fav_type);
});

$(function () {
    var $precision = $('.precision'),
        score = $precision.attr('data-star-scope'),
        option = {
            half: true,
            path: '/static/images/',
            precision: true,
            size: 24,
            starOff: 'g_star.png',
            starOn: 'r_star.png',
            starHalf: 'h_star.png',
            hints: ['极差', '差', '一般', '好评', '非常满意'],
            noRatedMsg: '暂时还未获得评价！',
            readOnly: true,
            score: score
        };
    $precision.raty(option);

    $('.jsFavBtn').on('click', function () {
        var type = $(this).attr('data-fav-type');
        if (type == '1') {
            favPraise($(this), 'fav', 1, '收藏');

        } else if (type == '3') {
            favPraise($(this), 'fav', 3);

        } else if (type == '11') {
            favPraise($(this), 'pra', 1);

        } else if (type == '4') {
            favPraise($(this), 'fav', 4);

        }
    });
})

$(function () {
    $('.recordbtn1').click(function () {
        $('.recordbox1').show();
    });
    $('.recordbtn2').click(function () {
        $('.recordbox2').show();
    });

    $('.imgslide').unslider({
        speed: 500,               //  The speed to animate each slide (in milliseconds)
        delay: 3000,              //  The delay between slide animations (in milliseconds)
        complete: function () {
        },  //  A function that gets called after every slide animation
        keys: true,               //  Enable keyboard (left, right) arrow shortcuts
        dots: true,               //  Display dot navigation
        fluid: false              //  Support responsive design. May break non-responsive designs
    });
    var unslider = $('.imgslide').unslider();
    $('.unslider-arrow').click(function () {
        var fn = this.className.split(' ')[1];
        unslider.data('unslider')[fn]();
    });
});