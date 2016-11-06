define("js/common/page",[
    "jquery"
],function ($) {
    function Page(params) {
        this.option = $.extend({},Page.defaultParams,params);
    }
    Page.defaultParams = {
        "page":$(".page"),
        "current":1,
        "totalPage":1,
        "total":0,
        "pageSize":6
    }
    Page.prototype.init = function () {
        this.__init();
        this.render();
        this.initEvent();
    }
    Page.prototype.__init = function () {
        if(this.option.page.size()<=0||!this.option.page){
            this.createView();
        }
        this.option.nextbtn = this.option.page.find("[page-next]");
        this.option.prevbtn = this.option.page.find("[page-prev]")
    }
    Page.prototype.render = function (params) {
        $.extend(this.option,params);
        this.__countTotalPage();
        this.__render()
    }
    Page.prototype.createView = function () {
         var html = '<div class="page"><a class="prev" page-prev><span>←</span>Older posts</a><a class="next" page-next>Newer posts <span>→</span></a></div>',
             parent =this.option.page.parent;
        this.option.page = $(html);
        parent&&parent.append(this.option.page)
    }
    Page.prototype.go = function (page) {
        if(!this.validate(page)){
            return false;
        }
        this.option.current = page;
        this.__render()
        this.option.callback&&this.option.callback(this)
    }
    Page.prototype.__countTotalPage = function () {
        this.option.totalPage = this.option.total/this.option.pageSize;
    }
    Page.prototype.validate = function (page) {
        if(page > this.option.totalPage){
            return false
        }
        if(page < 1){
            return false
        }
        return true;
    }
    Page.prototype.__render = function () {
        if(this.option.total<this.option.pageSize){
            this.option.page.hide();
            return false;
        }else{
            this.option.page.show();
        }
        var current = this.option.current,
            totalPage = this.option.totalPage,
            minPage = 1;
        if(current >=totalPage){
            this.option.nextbtn.hide()
        }else{
            this.option.nextbtn.show()
        }
        if(current <=minPage){
            this.option.prevbtn.hide()
        }else{
            this.option.prevbtn.show()
        }
    }
    Page.prototype.next = function () {
        var toPage = this.option.current+1>this.option.totalPage
            ?this.option.totalPage:this.option.current+1
        this.go(toPage)
    }
    Page.prototype.prev = function () {
        var toPage= this.option.current-1<1?1:this.option.current-1;
        this.go(toPage)
    }
    Page.prototype.initEvent = function () {
        var self = this;
        this.option.nextbtn.on("click",function () {
            self.next()
        })
        this.option.prevbtn.on("click",function () {
            self.prev()
        })
    }
    function createPage(option) {
        var page = new Page(option)
        page.init();
        return page
    }
    return createPage
})
