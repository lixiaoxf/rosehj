define("js/page/world/app",[
        "jquery",
        "js/common/page",
        "js/public/articleList"
    ],
    function ($,page,articleList) {
        var app = {
            "init":function () {
                articleList.init({
                    "parent":$("#articleList"),
                    "query":{}
                })
            },
        }
        return app
    }
)
