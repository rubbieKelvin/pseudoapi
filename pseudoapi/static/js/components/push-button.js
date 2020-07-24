Vue.component("push-button", {
    props: ["text", "goto", "fg", "bg"],
    data(){
        return {
            styleObject: {
                textDecoration: "none",
                borderRadius: "5px",
                backgroundColor: this.bg,
                color: this.fg,
                padding: "0.9em",
                fontStyle: "normal",
                fontSize: "1.8em",
                lineHeight: "27px",
                marginRight: "0.4em"
            }
        };
    },
    template: `
        <a v-bind:href="goto" v-bind:style="styleObject" class="push-button">
            {{ text }}
        </a>
    `
});