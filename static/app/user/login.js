// 验证用户名是否合法等操作
$(function () {
    $('#login').click(function () {
       if ($('#username').val() == null){
            alert('用户名不能为空');
       }else if ($('#password').val() == null) {
           alert("密码不能为空")
       }
    });
});