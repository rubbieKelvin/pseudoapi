let app = new Vue({
    el: "#app",
    data: () => {
        return {
            links: [
                {text:"login", url:"/login"},
                {text:"about", url:"/about"}
            ],
            colors: {
                theme: "#EB5757",
                themeLight: "#FBDDDD"
            },
            footerLinks:[
                {url:"http://github.com/rubbiekelvin", src:"/static/images/github.svg"},
                {url:"https://www.linkedin.com/in/rubbie-kelvin-831400176", src:"/static/images/linkedin.svg"},
                {url:"http://twitter.com/kelvinrubbie", src:"/static/images/twitter.svg"}
            ]
        }
    }
})