const isnone = (value) => (value === null || value === undefined);

Vue.component("key-value", {
    props: ["type", "value", "id"],
    methods: {},
    data(){
        return {
            // value: {
            //     key: null,
            //     value: null
            // }
        };
    },
    template: `
        <div class="key-value">

            <div>

                <input v-model="value.key" type="text" placeholder="key...">
                
                <input v-model="value.value" v-if="type === 'string'" type="text" placeholder="text">
                <input v-model="value.value" v-else-if="type === 'integer'" type="number" placeholder="number">
                <input v-model="value.value" v-else-if="type === 'boolean'" type="checkbox">
                <template v-else>
                    <select v-model="value.value" id="input-method" class="form-control custom-select">
                        <option>int</option>
                        <option>str</option>
                        <option>bool</option>
                    </select>
                </template>
                
            </div>

            <button @click="$emit('del-pair', id)" type="button" class="btn btn-outline-danger">x</button>

        </div>
    `
});


Vue.component("dict-widget", {
    props: {
        label: String,
        id: String,
        value: Array,
        select: {
            type: Boolean,
            default: false
        }
    },
    methods: {
        deletePair(id){
            this.$emit("del-row", id);
            // this.value = this.value.filter(todo => todo.id !== id);
        },
        addvalue(){
            if (this.currenttype.length || this.select){
                let id = Number(this.usedids.slice(-1))+1;
                this.usedids.push(id);

                let newkeyvalue = {
                    id: id, 
                    type: (this.select) ? "type" : this.currenttype,
                    value: {
                        key: null,
                        value: null
                    }
                };
                // this.value = [...this.value, newkeyvalue];
                this.$emit("add-row", newkeyvalue);
            };
        }
    },
    data(){
        return {
            usedids: [-1],
            currenttype: ""
        };
    },
    template: `
    <div class="request-widget">
        
        <button v-if="select" type="button" class="btn btn-primary" @click="addvalue">add</button>
        <button v-else type="button" class="btn btn-primary" data-toggle="modal" v-bind:data-target="'#'+id+'-modal'">add</button>

        <div v-bind:id="id+'-key-values'">
            <key-value v-on:del-pair="deletePair" v-bind:id="item.id" v-bind:key="item.id" v-for="item in value" v-bind:type="item.type" v-model="item.value"></key-value>
        </div>

        <!-- Modal -->
        <div class="modal fade" v-bind:id="id+'-modal'" data-backdrop="static" tabindex="-1" role="dialog" v-bind:aria-labelledby="id+'-modal'" aria-hidden="true">
            
            <div class="modal-dialog modal-dialog-centered" role="document">
                
                <div class="modal-content">

                    <div class="modal-header">
                        <h5 class="modal-title" id="staticBackdropLabel">Row Type</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                        </button>
                    </div>

                    <div class="modal-body">
                        <select v-model="currenttype" id="input-method" class="form-control custom-select">
                            <option>integer</option>
                            <option>string</option>
                            <option>boolean</option>
                        </select>
                    </div>
        
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">close</button>
                        <button type="button" class="btn btn-primary" data-dismiss="modal" v-on:click="addvalue">create</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    `
});

Vue.component("modal-alert", {
    props: {
        label: String,
        message: String
    },
    template: `
    <!-- Modal -->
    <div class="modal fade" tabindex="-1" role="dialog" aria-hidden="true">
        
        <div class="modal-dialog modal-dialog-centered" role="document">
            
            <div class="modal-content">

                <div class="modal-header">
                    <h5 class="modal-title" id="staticBackdropLabel">{{label}}</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                    </button>
                </div>

                <div class="modal-body">
                    <p>{{message}}</p>
                </div>
    
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">close</button>
                </div>
            </div>
        </div>
    </div>
    `
});


const app = new Vue({
    el: "#app",
    data(){
        return {
            formdata: {
                method: "get",
                many: false,
                request: [],
                response: []
            },
            modalalert: {
                id: "modalx",
                message: "",
                label: ""
            }
        };
    },
    methods: {
        addResponseRow(data){
            this.formdata.response = [...this.formdata.response, data];
        },

        delResponseRow(id){
            this.formdata.response = this.formdata.response.filter(row => row.id !== id);
        },

        addRequestRow(data){
            this.formdata.request = [...this.formdata.request, data];
        },

        delRequestRow(id){
            this.formdata.request = this.formdata.request.filter(row => row.id !== id);
        },

        createapi(){
            let request = {};
            let response = {};
            let newapi = {
                many: this.formdata.many,
                method: this.formdata.method
            };

            this.formdata.request.forEach(element => {
                if (!isnone(element.value.key) && !isnone(element.value.value)){
                    request[element.value.key] = element.value.value;
                }
            });

            this.formdata.response.forEach(element => {
                if (!isnone(element.value.key) && !isnone(element.value.value)){
                    response[element.value.key] = element.value.value;
                }
            });

            newapi["response"] = JSON.stringify(response);
            newapi["request"] = JSON.stringify(request);
            
            axios.post("/workspace/apis/", newapi)
            .then((response) => {
                let route = window.location.origin+"/"+response.data.route;
                this.modalalert.label = "API Created";
                this.modalalert.message = "Your api is live at "+route;
                $("#"+this.modalalert.id).modal("show");
            })
            .catch((error) => {
                console.clear();
                console.error(error);

                this.modalalert.label = "Error";
                this.modalalert.message = "Sorry, there was an error. please check the console";
                $("#"+this.modalalert.id).modal("show");
            });
                
        }
    }
});