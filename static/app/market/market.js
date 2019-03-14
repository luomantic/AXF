$(function () {

    // 点击全部类型JS
    $('#child_type').click(function () {
        $('#child_type_container').toggle(); // 切换显示
        $('#child_type_icon').toggleClass('glyphicon-menu-down glyphicon-menu-up');

        if ($('#sort_rule_container').is(':visible')) {
            $('#sort_rule_container').triggerHandler('click');
        }
    });

    $('#child_type_container').click(function () {
        $(this).hide();
        $('#child_type_icon').toggleClass('glyphicon-menu-down glyphicon-menu-up');
    });

    // 点击综合类型JS
    $('#sort_rule').click(function () {
        $('#sort_rule_container').toggle(); // 切换显示
        $('#sort_rule_icon').toggleClass('glyphicon-menu-down glyphicon-menu-up');

        if ($('#child_type_container').is(':visible')) {
            $('#child_type_container').triggerHandler('click');
        }
    });

    $('#sort_rule_container').click(function () {
        $(this).hide();
        $('#sort_rule_icon').toggleClass('glyphicon-menu-down glyphicon-menu-up');
    });


    // 加入购物车
    // 数量 -
    $('.reduce').click(function () {
        let $number = $(this).parent().find('.goods_num');
        num = parseInt($number.html())- 1;
        if (num < 1) {
            num = 1;
        }
        $number.html( num );
    });

    // 数量 +
    $('.plus').click(function () {
        let $number = $(this).parent().find('.goods_num');
        $number.html( parseInt($number.html()) + 1);
    });

    // 点击加入购物车
    $('.addtocart').click(function () {
        // 获取当前要加入购物车的商品的id
        goods_id = $(this).attr('goods_id');
        // 获取商品数量
        goods_num = parseInt($(this).prev().find('.goods_num').html());

        // ajax提交给后台
        $.get('/app/addtocart/', {goods_id:goods_id, goods_num:goods_num}, function (data) {
            console.log(data);
        });
    });
});