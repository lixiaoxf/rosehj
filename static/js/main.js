requirejs.config({
    baseUrl: "/static/",
    paths: {
        jquery:"lib/jquery/1.12.4/jquery",
        // pageRouter:"lib/page/page",
        director:"lib/director/director"
    },
    shim:{
        director:{
            exports:'Router',
            deps:["jquery"]
        }
    }
})
require([
        "jquery",
        "js/router/router",
        "js/common/header",
    ],
    function ($,router,header,page,index) {
        header.init();
        router.init();
    }
)