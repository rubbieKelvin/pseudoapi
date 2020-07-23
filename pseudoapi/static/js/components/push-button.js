Vue.component("push-button", {
    props: ["text", "goto", "accent"],
    data(){
        return {
            styleObject: {
                textDecoration: "none",
                borderRadius: "5px",
                backgroundColor: this.accent,
                color: "#ffffff",
                padding: {
                    top: "1em"
                }
            }
        };
    },
    template: `
        <a v-bind:href="goto" v-bind:style="styleObject" v-on:click="markC">
            {{ text }}
        </a>
    `,
    methods: {
        markC(){
            alert(this.accent);
        }
    }
});