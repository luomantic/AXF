$(function(){

    //支付
    $('#pay').click(function () {
        $.get('/app/order_change_status/', {'orderid':$(this).attr('orderid'), 'status':'1'}, function (data) {
            if (data.status === 1) {
                alert('支付成功');
                location.href = '/app/mine/';
            } else {
                console.log(data.msg)
            }
        });
    })

});