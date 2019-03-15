$(function () {
    // +
    $('.plus').click(function () {
        let that = this;
        let cartid = $(this).parent().parent('.menuList').attr('cartid');

        $.get('/app/addnum/', {cartid:cartid}, function (data) {
            if (data.status === 1) {
                $(that).prev().html(data.num)
            } else {
                console.log(data.msg)
            }

            // calculate();
        })
    });


    // -
    $('.reduce').click(function () {
        let that = this;
        let cartid = $(this).parent().parent('.menuList').attr('cartid');

        $.get('/app/reducenum/', {cartid: cartid}, function (data) {
            if (data.status === 1) {
                $(that).next().html(data.num)
            } else {
                console.log(data.msg)
            }

            // calculate();
        })
    });

    // 删除
    $('.delbtn').click(function () {
        let that = this;
        let cartid = $(this).parent('.menuList').attr('cartid');

        $.get('/app/delcart/', {cartid:cartid}, function (data) {
            if (data.status === 1){
                // location.reload() // 刷新整个页面
                $(that).parent().remove() // 删除节点
            }else {
                console.log(data)
            }
        })
    });

    // 计算总价
    function calculate() {
        total = 0;

        $('.menuList').each(function () {
        });
    }
});