define("js/public/article",[
    "jquery"
],function ($) {
    function Article(params) {
        this.params = $.extend({},params)
    }
    Article.prototype.init = function () {
        
    }
    Article.prototype.getHtml = function () {
        var html = '<article class="site-content-card">'+
                        '<header>'+
                            '<h2>Valentino Spring Summer 2017 Fashion Show</h2>'+
                            '<p class="site-content-card-author">Published by bryanboy</p>'+
                        '</header>'+
                        '<div class="site-content-card-detail">'+
                            '<p>Pierpaolo Piccioli will present his solo, spring summer 2017 womenswear debut at Valentino this afternoon in Paris. Don’t forget to tune in and watch the fashion show livestream at 3:00PM Paris time (that’s 9:00AM New York time).</p>'+
                            '<img src="../img/photo/1.png">'+
                            '<p>See you at the show!</p>'+
                        '</div>'+
                        '<footer>'+
                            '<div>September 14, 2016 — <a>comments 2</a></div>'+
                            '<div>Fashion, Shows</div>'+
                            '<div><a>Permalink</a></div>'+
                        '</footer>'+
                '</article>'
        return html;
    }
    return Article
})
