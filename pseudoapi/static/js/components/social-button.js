Vue.component("social-button", {
    props: ["logo", "goto", "bg"],
    data(){
        return {
            styles: {
                bg:{
                    borderRadius: "100%",
                    backgroundColor: this.bg,
                    padding: "0.5em",
                    width: "2.5em",
                    height: "2.5em",
                    display: "flex",
                    justifyContent: "center",
                    alignContent: "center"
                },
                a: {
                    display: "flex",
                    justifyContent: "center",
                    alignContent: "center"
                }
            }
        }
    },
    template:`
        <div v-bind:style="styles.bg">
            <a v-bind:href="goto" v-bind:style="styles.a">
                <img v-bind:src="logo"/>
            </a>
        </div>
    `
})