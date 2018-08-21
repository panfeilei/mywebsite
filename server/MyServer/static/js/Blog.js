    const comment_html = '\
        <li class="media"> \
            <div class="media-left">\
                <a><img src="/media/head.jpg" class="img-circle comment-icon" /></a>\
            </div>\
            <div class="media-body">\
                <a class="comment-id" hidden>0</a>\
                <h4 class="comment-username">username</h4>\
                <p class="comment-content">comment-content</p>\
                <div class="comment-foot">\
                    <span class="comment-time">2018.01.22</span>\
                    <a class="reply_a" >reply</a>\
                </div>\
                <div>\
                    <ul id="comment-in" style="list-style:none;" class="reply-list">\
                    </ul>\
                </div>\
            </div>\
        </li> \
    ';
    
    const reply_form_html = '<div class="replay_block">\
            <form action="/uploadData/?action=uploadReply" method="post" class="replay_block_form">\
                <input type="hidden" name="toblogId" value=""></input>\
                <input type="hidden" name="toCommentId" value=""></input>\
                <input type="hidden" name="toUsername" value=""></input>\
                <textarea class="replay_block_form_text"  style="resize: none;width:100%;" name="content" required></textarea>\
                <button class="replay_block_submit" type="submit" style="float:right" >ok</button>\
            </form>\
        </div>';
    
    const reply_item_html = '<li class="media">\
                            <div class="media-left"><a><img class="img-circle replay-icon" src="/media/head.jpg" class="img-circle" style="width:30px"/></a></div>\
                            <div class="media-body">\
                                <h4 class="reply-username">username</h4>\
                                <a class="reply-toUsername"></a>\
                                <span class="reply-content">reply</span>\
                                <div class="reply-foot">\
                                    <span class="reply-time">2018.01.22</span>\
                                    <a class="reply_a">reply</a>\
                                </div>\
                            </div>\
                        </li>';
    var authorId = 0;
    function getUrlParam(name){
        var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
        var r = window.location.search.substr(1).match(reg); //匹配目标参数
        if (r != null) return unescape(r[2]); return null; //返回参数值 
    }
    
    function getBlogId(){
        var r = $('.blog-id').text()
        return r;
    }
    
    $(function(){

        initView();
        initComment();
    })
    
    function initView(){
        var blogId = getBlogId();
        
        $('.comment-form').append('<input type="hidden" name="to_blogId" value=\'' + blogId + '\'>');
        var commentForm = $('.comment-form')[0]
        FormSubmit(commentForm);
        $.get('/blogInfo/{id}/'.replace('{id}', blogId), function(data, status){
            
            blogInfo = data['blogInfo'];
            authorInfo = data['authorInfo'];
            authorId = authorInfo['UserInfo']['userId'];
            $('.pageActive-item-num').text(blogInfo['favorNum']);
            $('.author-name').text(authorInfo['UserInfo']['name']);
            $('.avatar_pic').attr('src', authorInfo['UserInfo']['iconUrl']);
            $('.icon-link').attr('href', '/users/PersonalZone/' + authorInfo['UserInfo']['userId']);
            isIntere = $('.inter-button');
            if(authorInfo['isIntere'] == true){
                isIntere.addClass('inter-gray-button');
                isIntere.text('已关注');
            }
            
            if(blogInfo['isFavou'] == true){
                $('.pageActive-item-text').text('取消收藏');
                $('.pageActive-item').addClass('alreadyFav');
            }
            // console.log(blogInfo['isFavou']);
            
        })
    }
    
    function initComment(){
        getComment_replay();
        BindEvent();
    }
    
    function getAuthorId()
    {
        return authorId;
    }
    
    function getComment_replay(){
        blog_id = getBlogId('id')
        $.get("/getcomment/{blogid}/".replace('{blogid}', blog_id),function(data, status){
            comment_div = $(".comment-list")
            //comment_json = JSON.parse(data);
            //comment_obj = $(comment_html);
            console.log(data);
            for(var comment_item of data){
                comment_obj = $(comment_html);
                comment_obj.find('.comment-username').text(comment_item['userInfo']['name']);
                comment_obj.find('.comment-time').text(comment_item['time']);
                comment_obj.find('.comment-id').text(comment_item['comment_id']);
                comment_obj.find('.comment-content').text(comment_item['content']);
                comment_obj.find('.comment-icon').attr('src',comment_item['userInfo']['iconUrl']);
                var reply_obj = null;
                for(var reply_item of comment_item.reply_list)
                {
                    reply_obj = $(reply_item_html);
                    reply_obj.find('.reply-toUsername').text('@'+reply_item['to_username']);
                    reply_obj.find('.reply-content').text(reply_item['content']);
                    reply_obj.find('.reply-username').text(reply_item['userInfo']['name']);
                    reply_obj.find('.reply-time').text(reply_item['time']);
                    reply_obj.find('.replay-icon').attr('src', reply_item['userInfo']['headlink']);
                    //console.log(reply_item.username);
                    comment_obj.find('.reply-list').append(reply_obj);
                }
                console.log(comment_obj.find('.reply-list').html());
                comment_div.append(comment_obj)
            }
            $('.reply_a').click(function(){
                $('.replay_block').remove();
                comment_id = $(this).parents('.media-body').find('.comment-id').text();
                var blogId = getBlogId('id');
                var toUsername = $(this).parents('.media-body').find('.comment-username').text();
                //console.log(comment_id);
                reply_form = $(reply_form_html);
                reply_form.find('input[name="toCommentId"]').val(comment_id);
                reply_form.find('input[name="toblogId"]').val(blogId);
                reply_form.find('input[name="toUsername"]').val(toUsername);
                $(this).parent().append(reply_form);
                var reply_form = $('.replay_block_form')[0]
                FormSubmit(reply_form);
            })
        })
    }
    
    function FormSubmit(form){
       $(form).ajaxForm(function(result) {
            console.log('post form ok');
        });
    }
    
    function BindEvent(){

    }

    
    