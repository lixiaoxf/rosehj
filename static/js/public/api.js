define("js/public/api",[
    "jquery"
],function ($) {
    var api = {
        "queryArticle":function (params) {
            return $.ajax({
                "url":"../static/db/ar.json",
                "type":"get",
                "error":function () {
                    console.log("queryArticle error")
                }
            })
        }
    }
    return api
})
