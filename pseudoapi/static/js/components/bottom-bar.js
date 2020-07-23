Vue.component("bottom-bar", {
    props: ["links", "bg"],
    data(){
        return {
            styles: {
                footer: {
                    padding: "4em",
                    paddingTop: "0px",
                    paddingBottom: "0px",
                    display: "flex",
                    alignContent: "center"
                }
            }
        }
    },
    template: `
        <footer v-bind:style="styles.footer">
            <div v-bind:style="{width:'50%'}">
                <p>copyright stuffsbyrubbie 2020</p>
            </div>
            <div v-bind:style="{width:'50%', display:'flex', justifyContent:'end'}">
                <social-button v-bind:style="{marginLeft:'0.5em'}" v-bind:goto="link.url" v-bind:logo="link.src" v-bind:key="link.id" v-for="link in links" v-bind:bg="bg"></social-button>
            </div>
        </footer>
    `
});