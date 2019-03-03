$(function () {
    let flag_1 = false;
    let flag_2 = false;
    let flag_3 = false;
    let flag_4 = false;

    $('#username').change(function () {
        const value = $(this).val();
        flag_1 = !!/^[a-zA-Z]\w{5,7}$/.test(value);
    });

    $('#password').change(function () {

    });

    $('#again').change(function () {

    });
    
    $('#email').change(function () {

    });

    if (flag_1 && flag_2 && flag_3 && flag_4) {
        return true
    }else {
        alert("输入不合法");
        // 提示不让用户提交表单
        return false
    }
});