$(function () {
    $('#child_type').click(function () {
        $('#child_type_container').toggle(); // 切换显示
        $('#child_type_icon').toggleClass('glyphicon-menu-down glyphicon-menu-up');
    });

    $('#child_type_container').click(function () {
        $(this).hide();
        $('#child_type_icon').toggleClass('glyphicon-menu-down glyphicon-menu-up');
    });
});