define("js/router/router",[
    "jquery",
    "director",
    "js/page/controller"
],function ($,director,controller) {
    var routes = {
        "/":function () {
            controller.index.init();
        },
        //world
        "/w":function () {
            controller.world.init();
        },
        //fashtion
        '/f':function () {
            controller.fashion.init();
        },
        //detail
        '/d':function () {
            
        },
        //admin
        '/a':function () {
            
        }
    },
     router = director(routes);
    router.configure({
        "notfound":function () {
            alert(1)
        }
    })
    return router
})
