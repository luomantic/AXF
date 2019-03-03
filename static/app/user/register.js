$(function () {
    let flag_1 = false;
    let flag_2 = false;
    let flag_3 = false;
    let flag_4 = false;

    $('#username').blur(function () {
        const value = $(this).val();
        flag_1 = !!/^[a-zA-Z]\w{5,7}$/.test(value);
    });

    $('#password').blur(function () {
    // $('#password').change(function () {
        // change表示状态改变

    });

    $('#again').blur(function () {

    });

    $('#email').blur(function () {

    });

    if (flag_1 && flag_2 && flag_3 && flag_4) {
        return true
    } else {
        alert("输入不合法");
        // 提示不让用户提交表单
        return false
    }

    /**
     * 问题：
     *  在js中对密码进行加密，抓包能抓到post提交的，加密后的密码，
     *  也能抓到js中写的加密方式，那么js中加密还有作用么
     */
});