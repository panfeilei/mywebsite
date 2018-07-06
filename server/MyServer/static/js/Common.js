function getcsrf(cookie){
    var r = $.cookie('csrftoken');
    return r;
}