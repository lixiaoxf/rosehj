define("js/public/articleList",[
        "jquery",
        "js/common/page",
        "js/public/article",
        "js/public/api"
    ],
    function ($,page,Article,api) {
        function getList() {
            var app = {
                "init":function (params) {
                    this.articleList = params["parent"];
                    this.queryParms = params["query"];
                    // this.page = page({
                    //     "parent":this.articleList.parent(),
                    //     "callback":function () {
                    //         alert(1)
                    //     }
                    // })
                    this.render()
                },
                "render":function () {
                    var self = this;
                    api.queryArticle(this.queryParms).done(function (data) {
                        data = [1,2,3,4,5,6]
                        self.__render(data)
                        // self.page.reset({
                        //     "total":17,
                        //     "current":2
                        // })
                    })
                },
                "__render":function (data) {
                    var i = 0,length = data.length,html="";
                    for(;i<length;i++){
                        var article = new Article(data[i]);
                        html+=article.getHtml();
                    }
                    this.articleList.html(html)
                }
            }
            return app
        }
        return getList();
    }
)
