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
    })
});