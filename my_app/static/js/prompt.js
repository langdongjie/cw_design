// -----------------警告条---------------------

var $prompt_timer;

function promptInfo(flag, texts) {

    clearInterval($prompt_timer);

    // flag > 0 为提示信息
    if(flag > 0){
        $(".prompt").css("background-color","#00ae00");
    }else {
        $(".prompt").css("background-color","#e70000");
    }

    $(".prompt_text").text(texts);

    // 警告条出现
    $(".prompt").fadeIn(300)

    // 4秒之后，警告条消失
    $prompt_timer = setInterval(function () {
        promptRemove();
    }, 3000);

}

function promptRemove(){
    $(".prompt").stop().fadeOut(300);
}

// 输出提示条的 HTML 代码
$(function () {
    var prompt = $("<div class=\"prompt\" >\n" +
        "    <p class=\"prompt_text\">该网页开发未完成！</p>\n" +
        "    <div class=\"prompt_close\">×</div>\n" +
        "</div>");

    $("body").append(prompt);
})

//点击提示条，消失
$(function () {
    $(".prompt").click(function () {
        console.log("fffff")
        promptRemove();
    })
})

