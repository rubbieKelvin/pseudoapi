Vue.component("nav-bar", {
    props: {},
    methods: {
        handleSelect(key, keyPath) {
            console.log(key, keyPath);
        }
    },
    data(){
        return {
            activeIndex: '1',
            activeIndex2: '1'
        };
    },
    template: `
        <el-row type="flex" class="row-bg" justify="center">
            <el-col :span="20">
                <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" active-text-color="#FF1744">
                    <el-menu-item index="1">&lt;PseudoAPI&gt;</el-menu-item>
                    <el-menu-item index="2">login</el-menu-item>
                    <el-menu-item index="3">about</el-menu-item>
                </el-menu>
            </el-col>
        </el-row>
    `
});