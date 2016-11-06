define("js/common/header",[
    "jquery"
],function ($) {
    var header = {
        "init":function () {
            this.header = $(".site-header");
            this.headerbtn = this.header.find(".menu-toggle")
            this.nav = this.header.find("[toggle-menu-content]")
            this.initEvent();
        },
        "initEvent":function () {
            var self = this;
            this.headerbtn.on("click",function () {
                self.nav.toggle("slow")
            })

        }
    }
    return header
})
