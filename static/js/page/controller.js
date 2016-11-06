define("js/page/controller",[
        "jquery",
        "js/page/index/app",
        "js/page/fashion/app",
        "js/page/world/app"
    ],
    function ($,index,fashion,world) {
        var app = {
            "index":index,
            "fashion":fashion,
            "world":world
        }
        return app
    }
)
