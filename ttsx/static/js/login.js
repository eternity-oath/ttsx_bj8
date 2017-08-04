
$(function () {
    name_ok = true;
    pwd_ok = true;
    $('.name_input').blur(function () {
        uname = $(this).val();
        if(uname.length<5||uname.length>20){
            $('.user_error').html('请输入5-20个字符').show();
            name_ok = false;
        }
        else {
            $('.user_error').html().hide();
            name_ok = true;
        }
    });

    $('.pass_input').blur(function () {
        upwd = $(this).val();
        if(upwd.length<8||upwd.length>20){
            $('.pwd_error').html('请输入8-20个字符').show();
            pwd_ok = false;
        }
        else {
            $('.pwd_error').html().hide();
            pwd_ok = true
        }
    });

    $('form').submit(function () {
        $('.name_input').blur();
        $('.pass_input').blur();
        return name_ok && pwd_ok;
    });

    if('{{name_error}}' == '1'){
        $('.user_error').html('用户名错误').show();
        name_ok = false;
    }
    if('{{pwd_error}}' == '1'){
        $('.pwd_error').html('密码错误').show();
        pwd_ok = false;
    }

});