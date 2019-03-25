
// 解析链接中的参数
function getUrlParam(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg);  //匹配目标参数
    if (r != null) return unescape(r[2]);
    return null; //返回参数值

}


// -----------------警告条---------------------

var $prompt_timer;

function promptInfo(flag, texts) {

    clearInterval($prompt_timer);

    // flag > 0 为提示信息
    if(flag > 0){
        $(".warn").css("background-color","#00ae00");
    }else {
        $(".warn").css("background-color","#e70000");
    }

    $(".warnText").text(texts);

    // 警告条出现
    $(".warn").fadeIn(300)

    // 4秒之后，警告条消失
    $prompt_timer = setInterval(function () {
        warnRemove();
    }, 4000);

}
//警告条消失
function warnRemove() {
    $(".warn").stop().fadeOut(300);
}

//点击未开发的功能会提示信息
$(function () {

    $(".noOpen").click(function () {
        promptInfo("0", "该功能尚未开发！");
    });

    // 点击警告条，警告条消失
    $(".warn").click(function () {
        warnRemove();
    });
})