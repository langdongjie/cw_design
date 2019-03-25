var $go_login;

$(function () {
    $(".header").remove();
    $(".footer").remove();
})

$(function () {

    $(".register-in-button").click(function () {

        registerName = $("#register-name").val();
        registerEmail = $("#register-email").val();
        registerPasswd = $("#register-passwd").val();

        // 0.注册成功
        if(registerName.length >= 2 && registerEmail.length >=3 && registerPasswd.length >= 3){

            promptInfo(1, "注册成功！即将跳转至登录页面！");

            // 注册成功，跳转到登录页面
            clearInterval($go_login);
            $go_login = setInterval(function () {
                $(location).attr("href", "login.html");
                window.location='login.html?userName='+encodeURI(encodeURI(registerName))+'&&'+'userPasswd='
                    +encodeURI(encodeURI(registerPasswd))+'&&'+'userAccount='+encodeURI(encodeURI(registerEmail));

            }, 3000);

        }

        // 1、用户名不能为空
        else if(!registerName.trim()){
            promptInfo(0, "用户名不能为空！");
        }
        // 2、邮箱不能为空
        else if(!registerEmail.trim()){
            promptInfo(0, "邮箱不能为空！");
        }
        // 3、密码不能为空
        else if(!registerPasswd.trim()){
            promptInfo(0, "密码不能为空");
        }
        else if(registerName.length < 2){
            promptInfo(0, "用户名至少为2个字符！");
        }
        else if(registerEmail.length < 3){
            promptInfo(0, "邮箱至少为3个字符！");
        }
        else if(registerPasswd.length < 3){
            promptInfo(0, "密码至少为3个字符！");
        }

        // return ;

    })

})