// window.onload = function(){
    // var bu = document.getElementById("testbu");
    // bu.onclick=function(e){
        // var bux = e.clientX;
        // var buy = e.clientY;
        // var old = this.getElementsByClassName("animate-ink")[0];
        // if(old != null)
        // {
            // this.removeChild(old);
        // }
        // var myspan = document.createElement("span");
        // myspan.className = "ink";
        // this.appendChild(myspan);
        
        // myspan.style.left = String(bux-myspan.offsetWidth/2)+'px';
        // myspan.style.top = String(buy-myspan.offsetHeight/2)+'px';
        // console.log(myspan.offsetHeight);
        // myspan.className = myspan.className+" animate-ink";
    // };
// }

$(function(){   
    $("#mainlist li a").click(function(e){
        $(".ink").remove();
        if($(this).children(".ink").length==0)
        {
            var myspan = "<span class='ink'></span>";
            $(this).prepend(myspan);
        }
        var ink = $(this).find(".ink");
        ink.removeClass("animate-ink");
        if (!ink.height() && !ink.width()) {
            var d = Math.max($(this).outerWidth(), $(this).outerHeight());
            ink.css({
            height:d+'px',
            width:d+'px'
            });
            
        }
        console.log(ink.width());
        x = e.pageX-$(this).offset().left-ink.width()/2;
        y = e.pageY-$(this).offset().top-ink.height()/2;
        ink.css({
            left: x + 'px',
            top: y + 'px',
            position:'absolute',

        }).addClass("animate-ink");
        
    })
});