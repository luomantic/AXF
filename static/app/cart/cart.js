$(function () {
    // +
    $('.plus').click(function () {
        let that = this;
        let cartid = $(this).parent().parent('.menuList').attr('cartid');

        $.get('/app/addnum/', {cartid: cartid}, function (data) {
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

        $.get('/app/delcart/', {cartid: cartid}, function (data) {
            if (data.status === 1) {
                // location.reload() // 刷新整个页面
                $(that).parent().remove() // 删除节点
            } else {
                console.log(data.msg)
            }

            isAllSelected();
        })
    });

    // 勾选/取消勾选
    $('.select').click(function () {
        let that = this;
        let cartid = $(this).parents('.menuList').attr('cartid');


        $.get('/app/cartselect/', {cartid: cartid}, function (data) {
            if (data.status === 1) {
                if (data.is_select) {
                    $(that).find('span').html('√')
                } else {
                    $(that).find('span').html('')
                }
            } else {
                console.log(data.msg)
            }
            isAllSelected();
        });
    });

    // 全选
    $('#allselect').click(function () {
        // 1,如果当前全部勾选了，则全不选,将所有的都不勾选
        // 2,如果有未勾选的，则全选，将未勾选的勾选
        selects = [];
        unselects = [];

        // 遍历所有的li
        $('.menuList').each(function () {
            var select = $(this).find('.select').children('span').html();
            if (select) {
                //如果是勾选的，则添加到selects中
                selects.push($(this).attr('cartid'))
            }
            else {
                //如果未勾选，则添加到unselects中
                unselects.push($(this).attr('cartid'))
            }
        });

        // 如果当前全部都勾选了，则执行全不选
        if (unselects.length === 0) {
            //ajax
            $.get('/app/cartselectall/', {'action': 'cancelselect', 'selects': selects.join('#')}, function (data) {
                // console.log(data)
                if (data.status === 1) {
                    $('.select').find('span').html('')
                }
                else {
                    console.log(data.msg)
                }

                // 重新判断是否全选
                isAllSelected()
            });
        }
        // 如果当前未全部勾选，则执行全选
        else {
            //ajax
            $.get('/app/cartselectall/', {'action': 'select', 'selects': unselects.join('#')}, function (data) {
                // console.log(data)
                if (data.status === 1) {
                    $('.select').find('span').html('√')
                }
                else {
                    console.log(data.msg)
                }

                // 重新判断是否全选
                isAllSelected()
            });
        }
    });

    // 检测是否全选了
    isAllSelected();

    function isAllSelected() {
        var count = 0;
        $('.select').each(function () {
            if ($(this).find('span').html()) {
                count++;
            }
        });

        //如果全选了
        if (count === $('.select').length) {
            $('#allselect').find('span').html('√')
        }
        //否则不打勾
        else {
            $('#allselect').find('span').html('')
        }

        //重新计算总价
        //calculate();

    }

    // 计算总价
    function calculate() {
        total = 0;

        $('.menuList').each(function () {
        });
    }
});